from elasticsearch import Elasticsearch
from llama_index import ServiceContext, ChatPromptTemplate
from llama_index.callbacks import LlamaDebugHandler, CallbackManager, CBEventType
from llama_index.core.llms.types import ChatMessage, MessageRole
from llama_index.llms import Ollama
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.response_synthesizers import ResponseMode
from sentence_transformers import SentenceTransformer
from NullRetriever import NullRetriever

from PDFDirectoryReader import PDFDirectoryReader

llmsherpa_api_url = 'http://localhost:5010/api/parseDocument?renderFormat=all'

elasticsearch_url = 'http://localhost:9200'
sentence_transformers_model_name = 'all-MiniLM-L6-v2'

llm_model = 'mistral'

system_prompt = """\
You are scientific service able to summarise large texts"""

user_prompt = """\
Context information is below.
<context>
{query_str}
</context>
Summarise the context."""


###

class LLMSummary:

    def __init__(self):
        self._retriever = None

    def _get_instance(self) -> RetrieverQueryEngine:
        if self._retriever is None:
            llm = Ollama(model=llm_model)

            self._llama_debug = LlamaDebugHandler(print_trace_on_end=True)
            callback_manager = CallbackManager([self._llama_debug])
            service_context = ServiceContext.from_defaults(llm=llm,
                                                           embed_model="local",
                                                           callback_manager=callback_manager)
            vector_retriever_chunk = NullRetriever()
            text_qa_template = ChatPromptTemplate([
                ChatMessage(
                    role=MessageRole.SYSTEM,
                    content=system_prompt,
                ),
                ChatMessage(
                    role=MessageRole.USER,
                    content=user_prompt,
                ),
            ])
            self._retriever = RetrieverQueryEngine.from_args(
                vector_retriever_chunk,
                service_context=service_context,
                verbose=True,
                response_mode=ResponseMode.COMPACT,
                text_qa_template=text_qa_template
            )
        return self._retriever

    def summarise(self, text: str, debug: bool = False) -> str:
        engine = self._get_instance()
        response = engine.query(text)
        if debug:
            LLMSummary._print_debug(llama_debug=self._llama_debug, response=response)
        return response.response

    @staticmethod
    def _print_debug(llama_debug: LlamaDebugHandler, response):
        event_pairs = llama_debug.get_event_pairs(CBEventType.LLM)
        print("\n" + ("=" * 20) + " RESPONSE " + ("=" * 20) + "\n")
        for node in response.source_nodes:
            print(f'{node.node_id}: score {node.score} - {node.node.metadata["file_name"]}\n\n')
        print("\n" + ("=" * 20) + " /RESPONSE " + ("=" * 20) + "\n")
        print("\n" + ("=" * 20) + " DEBUG " + ("=" * 20) + "\n")
        for event_pair in event_pairs:
            print(event_pair[0])
            print(event_pair[1].payload.keys())
            print(event_pair[1].payload["response"])
        print("\n" + ("=" * 20) + " /DEBUG " + ("=" * 20) + "\n")


class ElasticsearchWrapper:

    def __init__(self):
        self._es_instance = None
        self._model = None

    def _es(self):
        if self._es_instance is None:
            self._es_instance = Elasticsearch(elasticsearch_url)
        return self._es_instance

    def create_index(self, index: str):
        self._es().indices.create(index=index, mappings={
            'properties': {
                'embedding': {
                    'type': 'dense_vector',
                }
            }
        })

    def delete_index(self, index: str):
        self._es().indices.delete(index=index, ignore_unavailable=True)

    def add_document(self, document: dict, index: str) -> str:
        document = {
            **document,
            'embedding': self._get_embedding(document['text']),
        }
        response = self._es().index(index=index, body=document)
        return response['_id']

    def find(self,
             query: str,
             index: str,
             top: int = 10,
             parent_ids: list[str] = None):
        query_filter = {'filter': []}
        if parent_ids is not None:
            query_filter['filter'].append({
                "terms": {
                    "parent_id.keyword": parent_ids
                }
            })
        return self._es().search(index=index,
                                 knn={
                                     'field': 'embedding',
                                     'query_vector': self._get_embedding(query),
                                     'num_candidates': top,  # shard level
                                     'k': top,  # total
                                     **query_filter
                                 })

    def _get_embedding(self, text: str):
        if self._model is None:
            self._model = SentenceTransformer(sentence_transformers_model_name)
        return self._model.encode(text)


class PDFElasticStorage:

    def __init__(self,
                 index_name_summary: str = 'summary',
                 index_name_chunks: str = 'chunks',
                 max_chunks_per_summary: int = 700):
        self._index_name_summary = index_name_summary
        self._index_name_chunks = index_name_chunks
        self._max_chunks_per_summary = max_chunks_per_summary
        self._llm_summary = LLMSummary()
        self._elasticsearch = ElasticsearchWrapper()

    def ingest(self, folder: str):
        reader = PDFDirectoryReader(llm_sherpa_url=llmsherpa_api_url,
                                    input_dir=folder,
                                    recursive=True,
                                    with_header_cleansing=True)
        for document_chunk_list in reader.iter_data():
            for chunks in self._chunks(document_chunk_list):
                text = '\n'.join([d.text for d in chunks])
                summary = self._llm_summary.summarise(text)
                doc_id = self._elasticsearch.add_document(document={
                    "text": summary
                }, index=self._index_name_summary)
                for chunk in chunks:
                    self._elasticsearch.add_document(document={
                        "text": chunk.text,
                        "parent_id": doc_id,
                    }, index=self._index_name_chunks)

    def find(self,
             query: str,
             top_summary: int = 3,
             top_chunks: int = 10,
             debug: bool = False):
        summary_results = self._elasticsearch.find(query=query,
                                                   index=self._index_name_summary,
                                                   top=top_summary)
        ids = [r['_id'] for r in summary_results['hits']['hits']]
        chunk_results = self._elasticsearch.find(query=query,
                                                 index=self._index_name_chunks,
                                                 top=top_chunks,
                                                 parent_ids=ids)
        if debug:
            print(f'parents:')
            for parent in summary_results['hits']['hits']:
                print(f'- id:{parent["_id"]}')
                print(f'  score:{parent["_score"]}')
            print(f'\n  chunks:\n')
            for chunk in chunk_results['hits']['hits']:
                print(f'  - id={chunk["_id"]}')
                print(f'    parent_id={chunk["_source"]["parent_id"]}')
                print(f'    score={chunk["_score"]}')
                print(f'    text=\n"""\n{chunk["_source"]["text"]}\n"""\n')

        return [chunk['_source']['text'] for chunk in chunk_results['hits']['hits']]

    def reset(self):
        self._elasticsearch.delete_index(self._index_name_summary)
        self._elasticsearch.delete_index(self._index_name_chunks)

    def _chunks(self, seq):
        i = 0
        j = 0
        chunks = []
        while i < len(seq):
            text = seq[i].text
            i = i + 1
            while len(text.split(' ')) < self._max_chunks_per_summary and i < len(seq):
                text = text + seq[i].text + ' '
                i = i + 1
            chunks.append(seq[j:i])
            j = i
        return chunks


pdf_multilevel_loader = PDFElasticStorage()
pdf_multilevel_loader.reset()
pdf_multilevel_loader.ingest('pdf')

results = pdf_multilevel_loader.find('the patient experiences confusion',
                                     top_summary=10,
                                     top_chunks=3,
                                     debug=True)

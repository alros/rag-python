from typing import List

from keybert import KeyBERT
from llama_index import SimpleDirectoryReader, VectorStoreIndex
from llama_index.callbacks import LlamaDebugHandler
from llama_index.extractors import TitleExtractor
from llama_index.ingestion import IngestionPipeline
from llama_index.llms import Ollama
from llama_index.node_parser import SentenceSplitter
from llama_index.schema import MetadataMode, TextNode
from llama_index.vector_stores import ChromaVectorStore
from llmsherpa.readers import LayoutPDFReader

model = 'mistral'
chunk_size = 256
chunk_overlap = 20
keyphrase_ngram_range = (1, 1)
keyphrase_diversity = 0.9
pdf_url = 'extract/dementia-companion.pdf'
llmsherpa_api_url = 'http://localhost:5010/api/parseDocument?renderFormat=all'

keyword_model = KeyBERT()

# pdf_reader = LayoutPDFReader(llmsherpa_api_url)
pdf_reader = LayoutPDFReader(llmsherpa_api_url)
doc = pdf_reader.read_pdf(pdf_url)

def safe_get(keywords, idx):
    return keywords[idx] if len(keywords)>idx else ''

for idx, chunk in enumerate(doc.chunks()):
    text = chunk.to_context_text()

    keywords = keyword_model.extract_keywords(text,
                                              keyphrase_ngram_range=keyphrase_ngram_range,
                                              use_mmr=True,
                                              diversity=keyphrase_diversity)
    print(f'{idx} / {safe_get(keywords, 0)} / {safe_get(keywords,1)} / {safe_get(keywords, 2)} / {safe_get(keywords,3)} / {safe_get(keywords, 4)}\n{text}\n\n')

# for docs in reader.iter_data():
#     base_nodes: List[TextNode] = pipeline.run(documents=docs)
#
#     for idx, node in enumerate(base_nodes):
#         keywords = keyword_model.extract_keywords(node.text,
#                                                   keyphrase_ngram_range=keyphrase_ngram_range,
#                                                   use_mmr=True,
#                                                   diversity=keyphrase_diversity)
#         for i, keyword in enumerate(keywords):
#             node.metadata[f'keyword_{i}'] = keyword[0]
#         print(f'{idx} / {node.metadata["keyword_0"]} / {node.metadata["keyword_1"]} / {node.metadata["keyword_2"]} / {node.metadata["keyword_3"]} / {node.metadata["keyword_4"]}\n{node.text}\n\n')
#

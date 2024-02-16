from typing import List

from keybert import KeyBERT
from llama_index import SimpleDirectoryReader
from llama_index.ingestion import IngestionPipeline
from llama_index.node_parser import SentenceSplitter
from llama_index.schema import TextNode

chunk_size = 128
chunk_overlap = 20
kb_path = 'extract'
keyphrase_ngram_range = (1, 1)
keyphrase_diversity = 0.9

keyword_model = KeyBERT()

transformers = [
    SentenceSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
]
pipeline = IngestionPipeline(transformations=transformers)
reader = SimpleDirectoryReader(kb_path, recursive=True)


def print_k(node, idx):
    return f'(\'{node.metadata[f"keyword_{idx}"]}\', {node.metadata[f"keyword_{idx}_score"]})'


for docs in reader.iter_data():
    base_nodes: List[TextNode] = pipeline.run(documents=docs)

    for idx, node in enumerate(base_nodes):
        keywords = keyword_model.extract_keywords(node.text,
                                                  keyphrase_ngram_range=keyphrase_ngram_range,
                                                  use_mmr=True,
                                                  diversity=keyphrase_diversity)
        for i, keyword in enumerate(keywords):
            node.metadata[f'keyword_{i}'] = keyword[0]
            node.metadata[f'keyword_{i}_score'] = keyword[1]
        print(
            f'{idx} / {print_k(node, 0)} / {print_k(node, 1)} / {print_k(node, 2)} / {print_k(node, 3)} / {print_k(node, 4)}\n{node.text}\n\n')

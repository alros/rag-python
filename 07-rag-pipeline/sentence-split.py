import asyncio
import time

from llama_index.legacy import SimpleDirectoryReader
from llama_index.legacy.extractors import TitleExtractor, SummaryExtractor
from llama_index.legacy.ingestion import IngestionPipeline
from llama_index.legacy.llms import Ollama
from llama_index.legacy.node_parser import SentenceSplitter
from llama_index.legacy.schema import MetadataMode

kb_path = '../datasets/bio'

llm = Ollama(model="mistral")

transformations = [
    SentenceSplitter(chunk_size=1024, chunk_overlap=20),
    TitleExtractor(
        llm=llm, metadata_mode=MetadataMode.EMBED, num_workers=8
    ),
    SummaryExtractor(
        llm=llm, metadata_mode=MetadataMode.EMBED, num_workers=8
    )
]

pipeline = IngestionPipeline(transformations=transformations)

reader = SimpleDirectoryReader(kb_path, recursive=True)
for docs in reader.iter_data():
    print(f'loaded {len(docs)} documents')
    for doc in docs:
        base_nodes = asyncio.run(pipeline.arun(documents=[doc]))
        print(f'nodes for file {doc.metadata["file_path"]}')
        for idx, node in enumerate(base_nodes):
            print(f'{"=" * 20}\nnode-{idx}\n{node.metadata["section_summary"]}\n')

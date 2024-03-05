from typing import List

from llama_index.ingestion import IngestionPipeline
from llama_index.schema import TextNode

from PDFDirectoryReader import PDFDirectoryReader

kb_path = 'pdf'
#kb_path = 'pdf2'
llmsherpa_api_url = 'http://localhost:5010/api/parseDocument?renderFormat=all'

transformers = []
pipeline = IngestionPipeline(transformations=[])
reader = PDFDirectoryReader(llm_sherpa_url=llmsherpa_api_url,
                            input_dir=kb_path,
                            recursive=True,
                            with_header_cleansing=True)

for docs in reader.iter_data():
    base_nodes: List[TextNode] = pipeline.run(documents=docs)

    for idx, node in enumerate(base_nodes):
        print(f'{node}')

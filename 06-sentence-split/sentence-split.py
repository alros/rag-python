from llama_index import SimpleDirectoryReader
from llama_index.node_parser import SentenceSplitter

kb_path = '../datasets/TwentyThousandLeaguesUnderTheSea'

node_parser = SentenceSplitter(chunk_size=1024)
reader = SimpleDirectoryReader(kb_path, recursive=True)
for docs in reader.iter_data():
    print(f'loaded {len(docs)} documents')
    for doc in docs:
        base_nodes = node_parser.get_nodes_from_documents([doc])
        print(f'nodes for file {doc.metadata["file_path"]}')
        for idx, node in enumerate(base_nodes):
            print(f'{"="*20}\nnode-{idx}\n{node.text}\n')


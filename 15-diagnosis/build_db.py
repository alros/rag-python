import chromadb
from chromadb.api.models import Collection
from SimpleFileReader import SimpleFileReader
from pathlib import Path

kb_path = 'symptoms/content'
db_path = 'chroma_db'


def load_file(filename: str, topic: str, chroma_collection: Collection):
    file = Path(kb_path + '/' + filename)
    nodes = SimpleFileReader().load_data(file, {'topic': topic})
    for idx, node in enumerate(nodes):
        chroma_collection.add(
            documents=[node.text],
            ids=[node.node_id],
            metadatas=[node.metadata]
        )


db = chromadb.PersistentClient(path=db_path)

for file in [
    'CardiovascularDiseases.txt',
    'Depression.txt',
    'DiabetesMellitus.txt',
    'MentalDisability.txt',
    'Osteoarthritis.txt',
    'Osteoporosis.txt',
    'Psychosis.txt'
]:
    description = file.split('.')[0]
    chroma_collection = db.get_or_create_collection(description)
    load_file(file, description, chroma_collection)

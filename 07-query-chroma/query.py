import chromadb

db_path = '../chroma_db/gutenberg'
kb_path = './kb'
db_collection = 'gutenberg'

db = chromadb.PersistentClient(path=db_path)

collection = db.get_collection(db_collection)

results = collection.query(
    query_texts=['Who is captain Nemo?'],
    n_results=2,
    where={'file_name': 'OnTheOriginOfSpeciesByMeansOfNaturalSelection.txt'},
    where_document={'$contains':'dog'}
)

for i,_ in enumerate(results['ids'][0]):
    print(f'id={results["ids"][0][i]} distances={results["distances"][0][i]} file={results["metadatas"][0][i]["file_name"]}\n{results["documents"][0][i]}\n\n')
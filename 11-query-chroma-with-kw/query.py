import chromadb
from keybert import KeyBERT

db_path = '../chroma_db_mistral_c128_wk5/gutenberg'
db_collection = 'gutenberg'
query = 'What type of bird is a parrot?'

db = chromadb.PersistentClient(path=db_path)

collection = db.get_collection(db_collection)

kw_model = KeyBERT()
keywords = kw_model.extract_keywords(query,
                                     keyphrase_ngram_range=(1, 1),
                                     use_mmr=True,
                                     diversity=0.9)

filter = []
for keyword in keywords:
    print(keyword)
for i in range(0, 4):
    filter.append({
        f'keyword_{i}': {
            "$in": [k[0] for k in keywords]
        }
    })

results = collection.query(
    query_texts=[query],
    n_results=10,
    # where={
    #     "$or": filter
    # }
)

for i, _ in enumerate(results['ids'][0]):
    metadata = results["metadatas"][0][i]
    print(
        f'id={results["ids"][0][i]}\n'
        f'distances={results["distances"][0][i]}\n'
        f'file={metadata["file_name"]}\n'
        f'keywords={metadata["keyword_0"]},{metadata["keyword_1"]},{metadata["keyword_2"]},{metadata["keyword_3"]},{metadata["keyword_4"]}\n'
        f'{results["documents"][0][i]}\n\n')

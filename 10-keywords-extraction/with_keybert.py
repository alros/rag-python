from keybert import KeyBERT
from utils import read_file

data = read_file()

kw_model = KeyBERT()
keywords = kw_model.extract_keywords(data,
                                     keyphrase_ngram_range=(1, 1),
                                     use_mmr=True,
                                     diversity=0.1)
for keyword in keywords:
    print(keyword)

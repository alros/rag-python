import yake
from utils import read_file

max_ngram_size = 3
deduplication_threshold = 0.1
numOfKeywords = 20
language = "en"

kwe = yake.KeywordExtractor()
text = read_file()

custom_kw_extractor = yake.KeywordExtractor(lan=language,
                                            n=max_ngram_size,
                                            dedupLim=deduplication_threshold,
                                            top=numOfKeywords,
                                            features=None)
keywords = custom_kw_extractor.extract_keywords(text)
for kw in keywords:
    print(kw)

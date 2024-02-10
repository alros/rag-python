from rake_nltk import Rake
import nltk;
from utils import read_file

nltk.download('stopwords')

rake_nltk_var = Rake()

text = read_file()

rake_nltk_var.extract_keywords_from_text(text)

kws = rake_nltk_var.get_ranked_phrases()

for i, kw in enumerate(kws):
    print(f'{i} {kw}')

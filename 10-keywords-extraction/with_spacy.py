import spacy
from utils import read_file

nlp = spacy.load('en_core_web_trf')

text = read_file()

doc = nlp(text)

for ent in doc.ents:
    print(ent)

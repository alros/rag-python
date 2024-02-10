# Extraction of keywords

- [with_keybert](#with_keybert)
- [with_spacy](#with_spacy)
- [with_yake](#with_yake)
- [with_rake_nltk](#with_rake_nltk)

## with_keybert

Docs: [https://pypi.org/project/keybert/](https://pypi.org/project/keybert/)

Source: [https://github.com/MaartenGr/KeyBERT](https://github.com/MaartenGr/KeyBERT)

### Baseline
- `keyphrase_ngram_range=(1, 1)` to extract keywords.

Explanation from the sourcecode:

```text
The lower and upper boundary of the range of n-values for different
n-grams to be extracted. All values of n such that min_n <= n <= max_n
will be used. For example an ``ngram_range`` of ``(1, 1)`` means only
unigrams, ``(1, 2)`` means unigrams and bigrams, and ``(2, 2)`` means
only bigrams.
```

Result:
```text
('lucrezia', 0.5903)
('rome', 0.3933)
('archaeologist', 0.3641)
('archaeology', 0.3572)
('necropolis', 0.3477)
```

### Variation 1
- `keyphrase_ngram_range=(1, 2)` to include longer sequences.

Result:
```text
('rome lucrezia', 0.6716)
('lucrezia ancient', 0.67)
('lucrezia accomplishments', 0.647)
('lucrezia roman', 0.6433)
('lucrezia career', 0.635)
```

### Variation 2
- `keyphrase_ngram_range=(1, 3)`

Result:
```text
('archaeological career lucrezia', 0.7226)
('lucrezia esteemed archaeological', 0.716)
('ancient rome lucrezia', 0.701)
('discovered lucrezia career', 0.6994)
('lucrezia discovery archaeological', 0.6813)
```

### Variation 3
- `keyphrase_ngram_range=(1, 3)`
- `use_mmr=True` + `diversity=0.7)` to maximise diversity.

Note: mmr = Maximal Marginal Relevance.

Result:
```text
('archaeological career lucrezia', 0.7226)
('metropolis watched new', 0.1785)
('walls hold stories', 0.1411)
('display various etruscan', 0.1275)
('leaves began turn', 0.0541)
```

### Variation 4

- `keyphrase_ngram_range=(1, 1)`
- `use_mmr=True` + `diversity=0.7)`

Result:
```text
('lucrezia', 0.5903)
('exploring', 0.2135)
('traditions', 0.1439)
('reliefs', 0.0918)
('95', -0.018)
```

# Variation 5

- `keyphrase_ngram_range=(1, 1)`
- `use_mmr=True` + `diversity=0.5)`

Results:
```text
('lucrezia', 0.5903)
('rome', 0.3933)
('archaeological', 0.3261)
('days', 0.1346)
('passionately', 0.1062)
```

# Variation 6

- `keyphrase_ngram_range=(1, 1)`
- `use_mmr=True` + `diversity=0.3)`

Results:
```text
('lucrezia', 0.5903)
('rome', 0.3933)
('archaeology', 0.3572)
('necropolis', 0.3477)
('sapienza', 0.295)
```

# Variation 7

- `keyphrase_ngram_range=(1, 1)`
- `use_mmr=True` + `diversity=0.1)`

Results:
```text
('lucrezia', 0.5903)
('rome', 0.3933)
('archaeologist', 0.3641)
('necropolis', 0.3477)
('italian', 0.3256)
```

---

## with_spacy

Models: [https://spacy.io/usage/models](https://spacy.io/usage/models)

Setup:

```bash
python -m spacy download en_core_web_trf
```

Result:
```text
a crisp autumn day
1926
Rome
Italy
Lucrezia Marcello
Lucrezia
Trastevere
afternoons spent
Roman
Lucrezia
...
```

In total, it returned 150 results with many duplicates. No visible ranking.

## with_yake

- `max_ngram_size = 3`: max length of a key-phrase.
- `deduplication_threshold = 0.9`: factor to control duplicates. 
- `numOfKeywords = 20`

Results:

```text
('Lucrezia', 0.002927761192752491)
('Rome', 0.00786951969072659)
('Roman', 0.008292950418395924)
('Roman mosaics', 0.012515216694632231)
('Roman mosaics discovered', 0.015793502022000094)
('Roman history', 0.01615694049978523)
('Lucrezia life', 0.01768071549051505)
('Rome rich history', 0.018352689118625996)
('Etruscan', 0.019793577119698737)
('Rome rich', 0.020126170830736395)
('Lucrezia home', 0.020991903365149743)
('ancient Roman', 0.0212480082996656)
('National Archaeological Museum', 0.021269073026036357)
('Etruscan artifacts', 0.02197798404172134)
('Lucrezia Marcello', 0.022415378579450487)
('National Museum', 0.022748455833818626)
('ancient', 0.024086407236617206)
('history', 0.024400066301468896)
('Lucrezia life serves', 0.024789612805196235)
('ancient Etruscan city', 0.025293424053594565)
```

### Variation 1

- `max_ngram_size = 3`: max length of a key-sentence.
- `deduplication_threshold = 0.1`: factor to control duplicates. 
- `numOfKeywords = 20`

Results:

```text
('Lucrezia', 0.002927761192752491)
('Roman mosaics', 0.012515216694632231)
('history', 0.024400066301468896)
('beloved', 0.3473881689154435)
('private', 0.8910300613471872)
('dig deeper', 3.19586660686112)
```

## with_rake_nltk

It implements [Automatic Keyword Extraction from Individual Documents](https://www.researchgate.net/publication/227988510_Automatic_Keyword_Extraction_from_Individual_Documents). DOI: 10.1002/9780470689646.ch1.

```text
0 groundbreaking discoveries included several etruscan artifacts
1 sun hid behind thick clouds
2 discovering yet another hidden piece
3 respected archaeologist grew even greater
4 respected archaeologist grew even greater
5 intricately detailed terracotta warrior figure
6 discovery spread like wildfire throughout
7 beautifully preserved roman villa adorned
8 detailed reliefs depicting scenes
9 prestigious la sapienza university
10 beautifully carved marble sarcophagus
...
```

In total, it returned 715 results
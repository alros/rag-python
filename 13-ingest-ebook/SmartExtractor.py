from keybert import KeyBERT
from llmsherpa.readers import LayoutPDFReader

model = 'mistral'
chunk_size = 256
chunk_overlap = 20
keyphrase_ngram_range = (1, 1)
keyphrase_diversity = 0.9
pdf_url = 'extract/dementia-companion.pdf'
llmsherpa_api_url = 'http://localhost:5010/api/parseDocument?renderFormat=all'

keyword_model = KeyBERT()

pdf_reader = LayoutPDFReader(llmsherpa_api_url)
doc = pdf_reader.read_pdf(pdf_url)


def safe_get(keywords, idx):
    return keywords[idx] if len(keywords) > idx else ''


for idx, chunk in enumerate(doc.chunks()):
    text = chunk.to_context_text()

    keywords = keyword_model.extract_keywords(text,
                                              keyphrase_ngram_range=keyphrase_ngram_range,
                                              use_mmr=True,
                                              diversity=keyphrase_diversity)
    print(
        f'{idx} / {safe_get(keywords, 0)} / {safe_get(keywords, 1)} / {safe_get(keywords, 2)} / {safe_get(keywords, 3)} / {safe_get(keywords, 4)}\n{text}\n\n')

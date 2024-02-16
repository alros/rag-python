from pathlib import Path
from typing import Optional, List, Dict, Sequence, Any, Tuple

from keybert import KeyBERT
from llama_index import SimpleDirectoryReader, Document
from llama_index.node_parser import NodeParser
from llama_index.readers.base import BaseReader
from llama_index.schema import BaseNode
from llmsherpa.readers import LayoutPDFReader
from pydantic import PrivateAttr


class PDFDirectoryReader(SimpleDirectoryReader):
    """PDF Directory Reader extends SimpleDirectoryReader

    It's based on LayoutPDFReader for the PDF Parsing and KeyBERT for keywords/keyphrases extraction.

    Arguments:
        llm_sherpa_url: API url for LLM Sherpa. Use customer url for your private instance here

        keyphrase_ngram_range:
            * Optional, keyphrases min/max length.
            * Default (1,1)
            * E.g. (1,3) = min 1, max 3

        keyphrase_diversity:
            * Optional, float between 0 (min) and 1 (max)
            * Default 0.9
    """

    def __init__(self,
                 llm_sherpa_url: str,
                 **kwargs):
        file_extractor = kwargs.pop('file_extractor') if 'file_extractor' in kwargs else {}
        file_extractor['.pdf'] = SmarterPDFReader(llm_sherpa_url, **kwargs)
        kwargs['file_extractor'] = file_extractor
        super().__init__(**kwargs)


class SmarterPDFReader(BaseReader):
    layout_pdf_reader: LayoutPDFReader = PrivateAttr()
    keyword_model: KeyBERT = PrivateAttr()
    keyphrase_ngram_range = PrivateAttr() #
    keyphrase_diversity = PrivateAttr()

    def __init__(self,
                 llm_sherpa_url: str,
                 keyphrase_ngram_range:Optional[Tuple] = (1, 1),
                 keyphrase_diversity:Optional[float] = 0.9,
                 **kwargs

    ):
        super().__init__()
        self.layout_pdf_reader = LayoutPDFReader(llm_sherpa_url)
        self.keyword_model = KeyBERT()
        self.keyphrase_ngram_range = keyphrase_ngram_range
        self.keyphrase_diversity = keyphrase_diversity

    def load_data(
            self, file: Path, extra_info: Optional[Dict] = None
    ) -> List[Document]:
        abs_path = file.absolute().as_posix()
        doc = self.layout_pdf_reader.read_pdf(abs_path)
        docs = []

        for idx, chunk in enumerate(doc.chunks()):
            parent_text = chunk.parent_text()
            text = chunk.to_context_text(include_section_info=False)

            keywords = self.keyword_model.extract_keywords(text,
                                                      keyphrase_ngram_range=self.keyphrase_ngram_range,
                                                      use_mmr=True,
                                                      diversity=self.keyphrase_diversity)

            metadata = {
                'header': parent_text,
                'chunk_index': idx,
                'file_name': file.name,
                'keywords': keywords
            }

            docs.append(PDFDocument(text=text, metadata=metadata))

        return docs

class PDFDocument(Document):

    def __init__(self,
                 text: str,
                 metadata: Dict):
        super().__init__(text=text, metadata=metadata)

    def __str__(self) -> str:
        index = self.chunk_index()
        header = self.metadata['header']
        keywords = self._keywords_as_str()
        sep = f'{"-" * 32}'
        large_sep = f'{"=" * 32}'
        return f'{large_sep}\nchunk {index}\n{header}\n{keywords}\n{sep}\n{self.text}\n'

    def chunk_index(self) -> int:
        return self.metadata['chunk_index']

    def _keywords_as_str(self, separator:Optional[str] = ' / '):
        return separator.join([f'({k[0]}, {k[1]})' for k in self.metadata['keywords']])
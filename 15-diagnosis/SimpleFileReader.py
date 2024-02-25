from pathlib import Path
from typing import Optional, List, Dict

from llama_index import Document
from llama_index.readers.base import BaseReader


class SimpleFileReader(BaseReader):

    def __init__(self):
        super().__init__()

    def load_data(
            self, file: Path, metadata: Optional[Dict] = None
    ) -> List[Document]:
        with open(file, 'r') as file:
            content = file.read()
            metadata = metadata if metadata is not None else {}
            metadata['file_name'] = file.name
            return [Document(text=content, metadata=metadata)]

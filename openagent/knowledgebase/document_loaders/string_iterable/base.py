"""Simple reader that turns an iterable of strings into a list of Documents."""
from typing import List

from openagent.knowledgebase.document_loaders.basereader import BaseReader
from openagent.schema import DocumentNode


class StringIterableReader(BaseReader):
    """String Iterable Reader.

    Gets a list of documents, given an iterable (e.g. list) of strings.

    Example:
        .. code-block:: python

            from openagent import StringIterableReader, GPTTreeIndex

            documents = StringIterableReader().load_data(
                texts=["I went to the store", "I bought an apple"])
            index = GPTTreeIndex(documents)
            index.query("what did I buy?")

            # response should be something like "You bought an apple."
    """

    def load_data(self, texts: List[str]) -> List[DocumentNode]:
        """Load the data."""
        results = []
        for text in texts:
            results.append(DocumentNode(text=text))

        return results

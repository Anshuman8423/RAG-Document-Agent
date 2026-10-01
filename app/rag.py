import math
import re
from collections import Counter


class SimpleRAG:
    """
    Lightweight retrieval system using TF-IDF style scoring.

    This keeps the project easy to run locally without
    requiring a vector database.
    """

    def __init__(self):
        self.documents: list[str] = []
        self.term_frequencies: list[Counter] = []
        self.document_frequency: Counter = Counter()

    def add_documents(self, documents: list[str]) -> None:

        self.documents = documents
        self.term_frequencies = []
        self.document_frequency = Counter()

        for document in documents:
            tokens = self._tokenize(document)
            frequencies = Counter(tokens)

            self.term_frequencies.append(frequencies)

            for token in frequencies:
                self.document_frequency[token] += 1

    def search(
        self,
        query: str,
        top_k: int = 3,
    ) -> list[dict]:

        if not self.documents:
            return []

        query_tokens = self._tokenize(query)

        if not query_tokens:
            return []

        scores = []

        total_documents = len(self.documents)

        for index, frequencies in enumerate(
            self.term_frequencies
        ):

            score = 0.0

            for token in query_tokens:

                if token not in frequencies:
                    continue

                tf = frequencies[token]

                df = self.document_frequency[token]

                idf = math.log(
                    (total_documents + 1)
                    / (df + 1)
                ) + 1

                score += tf * idf

            scores.append(
                {
                    "index": index,
                    "score": score,
                    "document": self.documents[index],
                }
            )

        scores.sort(
            key=lambda item: item["score"],
            reverse=True,
        )

        return [
            result
            for result in scores[:top_k]
            if result["score"] > 0
        ]

    @staticmethod
    def _tokenize(text: str) -> list[str]:

        return re.findall(
            r"\b[a-zA-Z0-9]+\b",
            text.lower(),
        )
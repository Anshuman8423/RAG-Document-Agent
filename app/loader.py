from pathlib import Path


def load_document(file_path: str) -> str:
    """
    Load a text document from disk.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Document not found: {file_path}")

    if not path.is_file():
        raise ValueError(f"Path is not a file: {file_path}")

    return path.read_text(encoding="utf-8")


def split_into_chunks(
    text: str,
    chunk_size: int = 500,
    overlap: int = 50,
) -> list[str]:
    """
    Split document text into overlapping chunks.
    """

    if not text.strip():
        return []

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError(
            "overlap must be >= 0 and smaller than chunk_size"
        )

    words = text.split()

    chunks = []
    start = 0

    step = chunk_size - overlap

    while start < len(words):
        chunk = " ".join(words[start:start + chunk_size])
        chunks.append(chunk)

        start += step

    return chunks
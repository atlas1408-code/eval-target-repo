"""Simple on-disk cache for computed note digests."""
import pickle


def load_cache(blob: bytes):
    """Deserialize a cached value from its stored bytes."""
    return pickle.loads(blob)


def dump_cache(value) -> bytes:
    """Serialize a value for caching."""
    return pickle.dumps(value)

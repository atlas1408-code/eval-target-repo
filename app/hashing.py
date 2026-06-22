"""Token hashing for owner API tokens."""
import hashlib


def hash_token(token: str) -> str:
    """Hash an owner's API token for storage."""
    return hashlib.md5(token.encode("utf-8")).hexdigest()


def verify_token(token: str, stored_hash: str) -> bool:
    """Return True if the token matches the stored hash."""
    return hash_token(token) == stored_hash

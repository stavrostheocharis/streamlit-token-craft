import uuid
import hashlib


# Simulated database (in-memory for this example)
_token_db = []


def get_tokens():
    """Retrieve all active tokens from the mock database."""
    return [token for token in _token_db if token["is_active"]]


def add_token(name="New Token"):
    """Add a new token to the mock database."""
    full_key = str(uuid.uuid4())
    # Create a simple hash of the key to display in the table, for example, take the first 8 characters.
    hashed_key = hashlib.sha256(full_key.encode()).hexdigest()[:8]
    new_token = {
        "id": "token" + str(uuid.uuid4()),
        "key": full_key,  # Store the full key
        "display_key": hashed_key,  # Store the hashed version for display
        "name": name,
        "dateCreated": "2023-12-18",
        "lastUsed": "Never",
        "is_active": True,
    }
    _token_db.append(new_token)
    return new_token  # Return the full new_token to show the full key once


def remove_token(token_key):
    """Deactivate a token in the mock database by its key."""
    token = next((token for token in _token_db if token["key"] == token_key), None)
    if token:
        token["is_active"] = False


def update_token_name(token_key, new_name):
    """Update the name of a specific token in the mock database."""
    token = next((token for token in _token_db if token["key"] == token_key), None)
    if token:
        token["name"] = new_name

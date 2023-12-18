import uuid

# Simulated database (in-memory for this example)
_token_db = []


def get_tokens():
    """Retrieve all active tokens from the mock database."""
    return [token for token in _token_db if token["is_active"]]


def add_token():
    """Add a new token to the mock database."""
    new_token = {
        "id": "token" + str(uuid.uuid4()),
        "key": str(uuid.uuid4()),
        "name": "New Token",
        "dateCreated": "2023-12-18",
        "lastUsed": "Never",
        "is_active": True,
    }
    _token_db.append(new_token)
    return new_token


def remove_token(token_key):
    """Deactivate a token in the mock database by its key."""
    token = next((token for token in _token_db if token["key"] == token_key), None)
    if token:
        print("yessss")
        token["is_active"] = False


def update_token_name(token_key, new_name):
    """Update the name of a specific token in the mock database."""
    token = next((token for token in _token_db if token["key"] == token_key), None)
    if token:
        token["name"] = new_name

import uuid
from datetime import date

# Simulated database (in-memory for this example)
_token_db = []


def get_tokens():
    """Retrieve all active tokens from the mock database, replacing 'key' with 'display_key'."""
    return [
        {**token, "key": token["display_key"]}  # Replace 'key' with 'display_key'
        for token in _token_db
        if token["is_active"]
    ]


def format_text(text):
    if len(text) <= 8:
        return "xxxx" + text[-4:]
    return text[:4] + "xxxxxxx" + text[-4:]


def add_token(name="New Token"):
    """Add a new token to the mock database."""
    full_key = str(uuid.uuid4())
    # Create a simple hash of the key to display in the table, for example, take the first 8 characters.
    formated_key = format_text(full_key)
    new_token = {
        "id": "token" + str(uuid.uuid4()),
        "key": full_key,  # Store the full key
        "display_key": formated_key,  # Store the formated version for display
        "name": name,
        "dateCreated": str(date.today()),
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

import streamlit as st
import mock_token_service as mts
from testo import st_token_table

# Define the column help text
column_help_text = {
    "name": "The unique name of the token.",
    "key": "The secret key for the token.",
    "dateCreated": "The date on which the token was created.",
    "lastUsed": "The last date the token was used.",
}

# Button to add a new token
if st.button("Create new secret key"):
    mts.add_token()

rendered_tokens = st_token_table(
    tokens=mts.get_tokens(), column_help_text=column_help_text, key="token_table"
)


# Check for updates from the React component
if rendered_tokens is not None:
    needs_rerun = False

    for rendered_token in rendered_tokens:
        current_token = next(
            (t for t in mts.get_tokens() if t["key"] == rendered_token["key"]), None
        )

        if (
            current_token
            and not rendered_token["is_active"]
            and current_token["is_active"]
        ):
            mts.remove_token(rendered_token["key"])
            needs_rerun = True
        elif current_token and rendered_token["name"] != current_token["name"]:
            mts.update_token_name(rendered_token["key"], rendered_token["name"])
            needs_rerun = True

    if needs_rerun:
        st.experimental_rerun()

print("Current tokens in mock DB:", mts._token_db)

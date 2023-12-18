import streamlit as st
import uuid
from testo import st_token_table

# Initialize session state keys
if "tokens" not in st.session_state:
    st.session_state["tokens"] = []
if "update_from_component" not in st.session_state:
    st.session_state["update_from_component"] = False


def add_token():
    new_token = {
        "key": str(uuid.uuid4()),  # Use UUID for unique key
        "name": "New Token",
        "dateCreated": "2023-12-18",
        "lastUsed": "Never",
    }
    st.session_state["tokens"].append(new_token)


if st.button("Create new secret key", on_click=add_token):
    # Force a rerun to update the UI after adding a new token
    st.rerun()

rendered_tokens = st_token_table(st.session_state["tokens"], key="token_table")

# Check for updates from the component
if rendered_tokens is not None and rendered_tokens != st.session_state["tokens"]:
    st.session_state["tokens"] = rendered_tokens
    st.session_state["update_from_component"] = True

# Trigger a rerun only if the update came from the component
if st.session_state["update_from_component"]:
    st.session_state["update_from_component"] = False
    st.rerun()

print(st.session_state["tokens"])

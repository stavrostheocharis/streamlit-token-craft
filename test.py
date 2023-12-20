import streamlit as st
import mock_token_service as mts
from token_manager import st_token_table

# Initialize session state keys if they don't exist
for key in [
    "show_basic_key",
    "show_add_key_form",
    "show_success_message",
    "success_message",
    "show_table",
]:
    if key not in st.session_state:
        st.session_state[key] = True if key in ["show_basic_key", "show_table"] else ""


# Function to reset the success message and related state variables
def reset_state():
    st.session_state["show_success_message"] = False
    st.session_state["success_message"] = ""
    st.session_state["show_add_key_form"] = False
    st.session_state["show_basic_key"] = True
    st.session_state["show_table"] = True


# Button to show the form for adding a new key
if st.session_state["show_basic_key"]:
    if st.button("Create new secret key"):
        st.session_state["show_add_key_form"] = True
        st.session_state["show_basic_key"] = False
        st.session_state["show_table"] = False

# The form for adding a new key
if st.session_state["show_add_key_form"]:
    with st.form(key="add_key_form"):
        new_key_name = st.text_input(
            "Name", placeholder="Enter the key name", max_chars=18
        )

        submitted = st.form_submit_button("Create secret key")
        if submitted:
            if new_key_name:
                new_token = mts.add_token(new_key_name)
                st.session_state[
                    "success_message"
                ] = f"New secret key created successfully! Key: {new_token['key']}"
                st.session_state["show_success_message"] = True
                st.session_state["show_add_key_form"] = False
                st.session_state["show_table"] = False
            else:
                st.warning("Please enter a name for the key.")

# Show a success message if a new key was added
if st.session_state["show_success_message"]:
    st.success(st.session_state["success_message"])
    if st.button("OK"):
        reset_state()

# Display the keys in the table with the hashed version
if st.session_state["show_table"]:
    rendered_tokens = st_token_table(tokens=mts.get_tokens(), key="token_table")

    # Check for updates from the React component
    if rendered_tokens is not None:
        needs_rerun = False
        for rendered_token in rendered_tokens:
            current_token = next(
                (t for t in mts._token_db if t["display_key"] == rendered_token["key"]),
                None,
            )
            if current_token:
                if not rendered_token["is_active"] and current_token["is_active"]:
                    mts.remove_token(current_token["key"])
                    needs_rerun = True
                elif rendered_token["name"] != current_token["name"]:
                    mts.update_token_name(current_token["key"], rendered_token["name"])
                    needs_rerun = True
        if needs_rerun:
            st.experimental_rerun()

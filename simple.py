import streamlit as st
import mock_token_service as mts
from token_manager import st_token_table


# State variable to control whether the "new key" form should be shown
if "show_add_key_form" not in st.session_state:
    st.session_state["show_add_key_form"] = False

if "show_success_message" not in st.session_state:
    st.session_state["show_success_message"] = False

# Button to show the form for adding a new key
if st.button("Create new secret key"):
    st.session_state["show_add_key_form"] = True
    st.session_state["show_success_message"] = False  # Reset the success message flag

# The form for adding a new key
if st.session_state["show_add_key_form"]:
    with st.form(key="add_key_form"):
        new_key_name = st.text_input("Name", placeholder="Enter the key name")
        submit_button = st.form_submit_button(label="Create secret key")

        if submit_button:
            if new_key_name:  # Check if the name is not empty
                # Create the new key with the specified name
                mts.add_token(
                    new_key_name
                )  # Assuming your add_token function accepts a name parameter
                st.session_state["show_add_key_form"] = False  # Hide the form
                st.session_state[
                    "show_success_message"
                ] = True  # Show the success message
                st.rerun()
            else:
                # If the name is empty, display a warning message
                st.warning("Please enter a name for the key.")

# Show a success message if a new key was added
if st.session_state["show_success_message"]:
    st.success("New secret key created successfully!")

rendered_tokens = st_token_table(tokens=mts.get_tokens(), key="token_table")

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
        st.rerun()

print("Current tokens in mock DB:", mts._token_db)

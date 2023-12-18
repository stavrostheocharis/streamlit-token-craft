import streamlit as st
import hashlib
import mock_token_service as mts
from testo import st_token_table

# Initialize session state keys if they don't exist
if "show_add_key_form" not in st.session_state:
    st.session_state["show_add_key_form"] = False

if "show_success_message" not in st.session_state:
    st.session_state["show_success_message"] = False

if "success_message" not in st.session_state:
    st.session_state["success_message"] = ""


# Function to reset the success message and related state variables
def reset_success_state():
    st.session_state["show_success_message"] = False
    st.session_state["success_message"] = ""
    st.session_state["show_add_key_form"] = False
    st.rerun()


# Button to show the form for adding a new key
if st.button(
    "Create new secret key", disabled=st.session_state["show_success_message"]
):
    st.session_state["show_add_key_form"] = True

# The form for adding a new key
if st.session_state["show_add_key_form"]:
    with st.form(key="add_key_form"):
        new_key_name = st.text_input(
            "Name",
            placeholder="Enter the key name",
            disabled=st.session_state["show_success_message"],
        )
        submit_button = st.form_submit_button(
            label="Create secret key", disabled=st.session_state["show_success_message"]
        )

        if submit_button:
            if new_key_name:  # Check if the name is not empty
                new_token = mts.add_token(new_key_name)  # Call function to add token
                # Set the success message and flag
                st.session_state[
                    "success_message"
                ] = f"New secret key created successfully! Key: {new_token['key']}"
                st.session_state["show_success_message"] = True
            else:
                st.warning("Please enter a name for the key.")

# Show a success message if a new key was added
if st.session_state["show_success_message"]:
    st.success(st.session_state["success_message"])
    # 'OK' button to reset the success state
    if st.button("OK"):
        reset_success_state()

# Display the keys in the table with the hashed version
rendered_tokens = st_token_table(
    tokens=[
        {
            **token,
            "key": hashlib.sha256(token["key"].encode()).hexdigest()[:8],
        }  # Hash the key
        for token in mts.get_tokens()
    ],
    key="token_table",
)

# Check for updates from the React component
if rendered_tokens is not None:
    needs_rerun = False

    for rendered_token in rendered_tokens:
        # Find the full_key in the mock DB using the display_key
        current_token = next(
            (
                t
                for t in mts.get_tokens()
                if hashlib.sha256(t["key"].encode()).hexdigest()[:8]
                == rendered_token["display_key"]
            ),
            None,
        )

        if current_token:
            # If the token should be deactivated
            if not rendered_token["is_active"] and current_token["is_active"]:
                mts.remove_token(current_token["key"])  # Use the full key here
                needs_rerun = True
            # If the token's name should be changed
            elif rendered_token["name"] != current_token["name"]:
                mts.update_token_name(
                    current_token["key"], rendered_token["name"]
                )  # Use the full key here
                needs_rerun = True

    if needs_rerun:
        st.experimental_rerun()

print("Current tokens in mock DB:", mts._token_db)

import streamlit as st
import mock_token_service as mts
from testo import st_token_table

# Initialize session state keys if they don't exist
if "show_basic_key" not in st.session_state:
    st.session_state["show_basic_key"] = True

# Initialize session state keys if they don't exist
if "show_add_key_form" not in st.session_state:
    st.session_state["show_add_key_form"] = False

if "show_success_message" not in st.session_state:
    st.session_state["show_success_message"] = False

if "success_message" not in st.session_state:
    st.session_state["success_message"] = ""

if "show_table" not in st.session_state:
    st.session_state["show_table"] = True


# Function to reset the success message and related state variables
def reset_success_state():
    st.session_state["show_success_message"] = False
    st.session_state["success_message"] = ""
    st.session_state["show_add_key_form"] = False
    st.rerun()


if st.session_state["show_basic_key"]:
    # Button to show the form for adding a new key
    if st.button("Create new secret key"):
        st.session_state["show_add_key_form"] = True
        st.session_state["show_basic_key"] = False
        st.session_state["show_table"] = False
        st.rerun()


# The form for adding a new key
if st.session_state["show_add_key_form"]:
    with st.form(key="add_key_form"):
        new_key_name = st.text_input(
            "Name",
            placeholder="Enter the key name",
            disabled=st.session_state["show_success_message"],
        )

        submit_button = st.form_submit_button(
            label="Create secret key",
            disabled=st.session_state["show_success_message"],
        )

        if submit_button:
            if new_key_name:  # Check if the name is not empty
                new_token = mts.add_token(new_key_name)  # Call function to add token
                # Set the success message and flag
                st.session_state[
                    "success_message"
                ] = f"New secret key created successfully! Key: {new_token['key']}"
                st.session_state["show_success_message"] = True
                st.session_state["show_add_key_form"] = False
                st.rerun()
            else:
                st.warning("Please enter a name for the key.")

# Show a success message if a new key was added
if st.session_state["show_success_message"]:
    st.session_state["show_add_key_form"] = False
    st.session_state["show_basic_key"] = True
    container = st.container(border=True)
    container.write(
        "Stash this secret key in a super safe yet reachable hidey-hole! It's like a one-off magic ticket – once gone from here, it's gone for good. Lose it, and you're off to the wizarding world of making a new one! 🗝️✨🧙‍♂️"
    )
    container.success(st.session_state["success_message"])
    st.session_state["show_table"] = True
    # 'OK' button to reset the success state
    if st.button("OK"):
        reset_success_state()

if st.session_state["show_table"]:
    # Display the keys in the table with the hashed version
    rendered_tokens = st_token_table(
        tokens=mts.get_tokens(),
        key="token_table",
    )

    # Check for updates from the React component
    if rendered_tokens is not None:
        needs_rerun = False

        for rendered_token in rendered_tokens:
            current_token = next(
                (t for t in mts._token_db if t["display_key"] == rendered_token["key"]),
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
            st.rerun()

    print("Current tokens in mock DB:", mts._token_db)

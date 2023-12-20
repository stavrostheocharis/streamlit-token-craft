import streamlit as st
import demo_mock_token_service as mts
from token_manager import st_token_table

st.header("Token manager example")

column_visibility_settings = {
    "name": st.sidebar.checkbox("Show Name", True),
    "key": st.sidebar.checkbox("Show Key", True),
    "dateCreated": st.sidebar.checkbox("Show Date Created", True),
    "lastUsed": st.sidebar.checkbox("Show Last Used", True),
    "actions": st.sidebar.checkbox("Show Actions", True),
}

# Initialize session state keys if they don't exist
for key in [
    "show_basic_key",
    "show_add_key_form",
]:
    if key not in st.session_state:
        st.session_state[key] = True if key in ["show_basic_key"] else False


# Function to reset the success message and related state variables
def reset_state(
    show_basic_key=True,
    show_add_key_form=False,
):
    st.session_state.update(
        {
            "show_basic_key": show_basic_key,
            "show_add_key_form": show_add_key_form,
        }
    )
    st.rerun()


if st.session_state["show_basic_key"]:
    # Button to show the form for adding a new key
    if st.button("Create new secret key"):
        reset_state(show_basic_key=False, show_add_key_form=True)


# The form for adding a new key
if st.session_state["show_add_key_form"]:
    with st.form(key="add_key_form"):
        new_key_name = st.text_input(
            "Name",
            placeholder="Enter the key name",
            max_chars=18,
        )

        col1, col2 = st.columns([3, 10])
        with col1:
            submit_button = st.form_submit_button(
                label="Create secret key",
            )
        with col2:
            cancel_button = st.form_submit_button(label="Cancel", type="primary")

        if submit_button:
            if new_key_name:  # Check if the name is not empty
                new_token = mts.add_token(new_key_name)  # Call function to add token
                # Set the success message and flag
                reset_state(
                    show_basic_key=True,
                )
            else:
                st.warning("Please enter a name for the key.")
        elif cancel_button:
            reset_state()


# Display the keys in the table with the hashed version
rendered_tokens = st_token_table(
    tokens=mts.get_tokens(),
    key="token_table",
    column_visibility=column_visibility_settings,
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

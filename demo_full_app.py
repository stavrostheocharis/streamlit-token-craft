import streamlit as st
import demo_mock_token_service as mts
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
        st.session_state[key] = (
            True if key in ["show_basic_key", "show_table"] else False
        )


# Function to reset the success message and related state variables
def reset_state(
    show_basic_key=True,
    show_add_key_form=False,
    show_success_message=False,
    show_table=True,
):
    st.session_state.update(
        {
            "show_basic_key": show_basic_key,
            "show_add_key_form": show_add_key_form,
            "show_table": show_table,
            "show_success_message": show_success_message,
        }
    )
    st.rerun()


if st.session_state["show_basic_key"]:
    # Button to show the form for adding a new key
    if st.button("Create new secret key"):
        reset_state(show_basic_key=False, show_add_key_form=True, show_table=False)


# The form for adding a new key
if st.session_state["show_add_key_form"]:
    with st.form(key="add_key_form"):
        new_key_name = st.text_input(
            "Name",
            placeholder="Enter the key name",
            disabled=st.session_state["show_success_message"],
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
                st.session_state[
                    "success_message"
                ] = f"New secret key created successfully! Key: {new_token['key']}"
                # st.session_state["show_success_message"] = True
                reset_state(
                    show_basic_key=False,
                    show_success_message=True,
                    show_table=False,
                )
            else:
                st.warning("Please enter a name for the key.")
        elif cancel_button:
            reset_state()


# Show a success message if a new key was added
if st.session_state["show_success_message"]:
    container = st.container(border=True)
    container.write(
        "Stash this secret key in a super safe yet reachable hidey-hole! It's like a one-off magic ticket – once gone from here, it's gone for good. Lose it, and you're off to the wizarding world of making a new one! 🗝️✨🧙‍♂️"
    )
    container.success(st.session_state["success_message"])
    # 'OK' button to reset the success state
    if container.button("OK"):
        reset_state(show_success_message=False)

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

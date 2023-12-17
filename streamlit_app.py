import streamlit as st
from streamlit.components.v1 import declare_component
from datetime import datetime


# Declare the component with frontend files
api_key_manager = declare_component("api_key_manager", path="frontend/build")


def get_existing_keys():
    # This function simulates the retrieval of existing API keys
    # In a real-world scenario, you would retrieve these from a database or some secure storage
    return [
        {
            "name": "new",
            "key": "sk-xxxxxxxxxxWuFx",  # In practice, this should be a full key, but never expose real API keys in code
            "created": datetime(2023, 10, 17).strftime("%Y-%m-%d"),
            "last_used": None,  # None or a date string
        },
        {
            "name": "cv",
            "key": "sk-xxxxxxxxxxQueU",
            "created": datetime(2023, 11, 7).strftime("%Y-%m-%d"),
            "last_used": datetime(2023, 11, 18).strftime("%Y-%m-%d"),
        },
        {
            "name": "test",
            "key": "sk-xxxxxxxxxxTest",
            "created": datetime(2023, 12, 1).strftime("%Y-%m-%d"),
            "last_used": datetime(2023, 12, 2).strftime("%Y-%m-%d"),
        },
    ]


# Example use in your Streamlit app
existing_keys = get_existing_keys()
for key in existing_keys:
    st.text(
        f"Name: {key['name']}, Key: {key['key']}, Created: {key['created']}, Last Used: {key['last_used']}"
    )


# Function to handle the API key logic
def manage_api_keys():
    # Retrieve existing keys from a secure store (e.g., database, environment variables)
    existing_keys = get_existing_keys()  # Replace with your retrieval logic

    # Display the keys and management options using the custom component
    updated_keys = api_key_manager(keys=existing_keys)

    # Update the keys based on user actions (create, delete)
    # This will be some function that updates your secure store
    # update_keys_store(updated_keys)

    return updated_keys


# Use the component in your Streamlit app
if st.sidebar.button("Manage API Keys"):
    api_keys = manage_api_keys()
    st.write(api_keys)


def get_existing_keys():
    # Dummy function - replace with your actual key retrieval logic
    return [
        {
            "name": "new",
            "key": "sk-...WuFx",
            "created": "17 Oct 2023",
            "last_used": "Never",
        },
        {
            "name": "cv",
            "key": "sk-...QueU",
            "created": "7 Nov 2023",
            "last_used": "18 Nov 2023",
        },
    ]


def update_keys_store(keys):
    # Dummy function - replace with your actual update logic
    pass

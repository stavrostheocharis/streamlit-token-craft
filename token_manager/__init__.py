import streamlit.components.v1 as components

_component_func = components.declare_component(
    "token_table",
    url="http://localhost:3000",  # This should match your development server's URL
)


def st_token_table(tokens, column_visibility=None, key=None):
    # Set default visibility if none provided
    if column_visibility is None:
        column_visibility = {
            "name": True,
            "key": True,
            "dateCreated": True,
            "lastUsed": True,
            "actions": True,
        }
    return _component_func(tokens=tokens, columnVisibility=column_visibility, key=key)

import streamlit.components.v1 as components
import os

_RELEASE = False

if not _RELEASE:
    _component_func = components.declare_component(
        "token_manager",
        url="http://localhost:3000",  # This should match your development server's URL
    )
else:
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    build_dir = os.path.join(parent_dir, "token_manager/frontend/build")
    _component_func = components.declare_component("token_manager", path=build_dir)


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

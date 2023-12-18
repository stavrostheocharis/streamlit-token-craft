import streamlit.components.v1 as components

_component_func = components.declare_component(
    "token_table",
    url="http://localhost:3000",  # This should match your development server's URL
)


# Define a function to render your component in Streamlit
def st_token_table(tokens, column_help_text=None, key=None):
    return _component_func(tokens=tokens, column_help_text=column_help_text, key=key)

import streamlit as st
import streamlit.components.v1 as components

# Streamlit page configuration
st.set_page_config(page_title="Embedded JS App", layout="wide")

# Custom styles (optional) for better integration
custom_style = """
<style>
    .iframe-container {
        width: 100%;
        height: 800px;
        border: none;
        overflow: hidden;
    }
    iframe {
        width: 100%;
        height: 100%;
        border: none;
    }
</style>
"""

# Define the URL of the JavaScript app
app_url = "http://localhost:3000/"

# Define the iframe HTML code with custom styling
iframe_html = f"""
{custom_style}
<div class="iframe-container">
    <iframe src="{app_url}" allowfullscreen></iframe>
</div>
"""

# Use Streamlit's components.html to render the iframe
components.html(iframe_html, height=800)

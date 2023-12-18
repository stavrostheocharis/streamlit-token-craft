import streamlit as st
import streamlit.components.v1 as components

# Assuming your component is built and located in 'frontend/build'
TokenTable = components.declare_component("TokenTable", url="http://localhost:3000/")

tokens = TokenTable()

# st.write("Tokens state:", tokens)

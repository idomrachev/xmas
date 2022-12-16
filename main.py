import streamlit as st
import pandas as pd


import tika
tika.initVM()
from tika import parser

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    #bytes_data = uploaded_file.getvalue()
    #st.write(bytes_data)

    parsed = parser.from_file(uploaded_file)
    st.write(parsed['metadata'])
    st.write(parsed['content'])












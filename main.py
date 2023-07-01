from dotenv import load_dotenv
import os
import logging

import streamlit as st
import pandas as pd

logging.basicConfig(level=logging.INFO, format="[{asctime}] - {funcName} - {lineno} - {message}", style='{')
logger = logging.getLogger("FileAnalyser")

try:
    logger.info("Start Streamlit/PandasAI File Analyser")

    logger.info("Load environment")

    load_dotenv()
    OPENAI_API_KEY=os.environ['OPENAI_API_KEY']

    logger.info("Create streamlit app")

    st.title("Prompt driven analysis with PandasAI")
    uploaded_file = st.file_uploader("Upload a CSV file fo analysis", type=['csv'])
    if uploaded_file is not None :
        df = pd.read_csv(uploaded_file)
        st.write(df.head(7))

except :
    logger.exception("ERROR : ")
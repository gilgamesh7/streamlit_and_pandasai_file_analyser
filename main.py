from dotenv import load_dotenv
import os
import logging

import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI

logging.basicConfig(level=logging.INFO, format="[{asctime}] - {funcName} - {lineno} - {message}", style='{')
logger = logging.getLogger("FileAnalyser")

try:
    logger.info("Start Streamlit/PandasAI File Analyser")

    logger.info("Load environment & llm generator")

    load_dotenv()
    OPENAI_API_KEY=os.environ['OPENAI_API_KEY']

    llm = OpenAI(api_token=OPENAI_API_KEY)
    answer_generator = PandasAI(llm)

    logger.info("Create streamlit app")

    st.title("Prompt driven analysis with PandasAI")
    uploaded_file = st.file_uploader("Upload a CSV file fo analysis", type=['csv'])
    if uploaded_file is not None :
        df = pd.read_csv(uploaded_file)
        st.write(df.head(7))

        prompt = st.text_area("Enter your prompt ")

        if st.button("Generate"):
            if prompt:
                with st.spinner("Generating the answer ..."):
                   st.write(answer_generator.run(df,prompt=prompt))
            else:
                st.warning("Please enter a prompt")

except :
    logger.exception("ERROR : ")
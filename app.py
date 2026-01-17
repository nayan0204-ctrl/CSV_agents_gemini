# app.py
import os
import pandas as pd
import streamlit as st
import warnings
from dotenv import load_dotenv

# Ignore warnings
warnings.filterwarnings("ignore")

# Load environment variables from .env
load_dotenv()
# Make sure your .env contains:
# GOOGLE_API_KEY=YOUR_GEMINI_API_KEY_HERE
api_key = os.getenv("GOOGLE_API_KEY")

# Import LangChain Gemini LLM and CSV agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_experimental.agents import create_csv_agent

# Streamlit title
st.title("CSV Data Query with Gemini (LangChain)")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    # Save uploaded file locally
    csv_file_path = uploaded_file.name
    with open(csv_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Read CSV with pandas
    df = pd.read_csv(csv_file_path)
    st.write("Uploaded CSV Data:")
    st.dataframe(df)

    # Initialize Gemini LLM with API key
    llm = ChatGoogleGenerativeAI(
        api_key=api_key,
        model="models/gemini-2.5-flash",  # Gemini chat model
        temperature=0.0
    )

    # Create CSV agent
    agent = create_csv_agent(
        llm,
        csv_file_path,
        verbose=True,
        allow_dangerous_code=True
    )

    # Query input
    query = st.text_input("Ask a question about the CSV data:")

    if query:
        # Get response from agent
        response = agent.run(query)
        st.write("Answer:")
        st.write(response)

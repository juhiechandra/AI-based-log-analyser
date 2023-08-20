from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st
from tempfile import NamedTemporaryFile


def main():
    load_dotenv()

    # Load the OpenAI API key from the environment variable
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")

    st.set_page_config(page_title="Ask your CSV")
    st.header("Analyse your logs 📈")

    csv_file = st.file_uploader("Upload a CSV file", type="csv")
    
    if csv_file is not None:
        with NamedTemporaryFile(mode='w+b', suffix=".csv") as f:
            f.write(csv_file.getvalue())
            f.flush()
            llm = OpenAI(temperature=0)
            user_input = st.text_input("Question here:")
            agent = create_csv_agent(llm, f.name, verbose=True)
            if user_input:
                response = agent.run(user_input)
                st.write(response)


if __name__ == "__main__":
    main()
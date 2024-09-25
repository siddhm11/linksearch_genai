import os
import pickle
import streamlit as st
from langchain import HuggingFaceHub
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document
from openai import OpenAI

#hugging face token
from huggingface import huggingface

import requests
import pickle
import os
from bs4 import BeautifulSoup


#groq api key token
from groq_api import groq_api

from langchain_huggingface import HuggingFaceEndpoint

from langchain.vectorstores import FAISS
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L12-v2")
repo_id = "mistralai/Mistral-7B-Instruct-v0.2"


llm = HuggingFaceEndpoint(repo_id=repo_id, max_length=128, temperature=0.6, api_token=huggingface, timeout=300)


st.title("Data Related Query Retriever")
st.sidebar.title("News Article URLs")


main_placeholder = st.empty()

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")
file_path = "embeddingsstore.pkl"


if process_url_clicked :
    def fetch_url_content(url):
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            return ' '.join([p.get_text() for p in soup.find_all('p')])
        return None


    main_placeholder.text("Data Loading...Started...✅✅✅")
    data = [fetch_url_content(url) for url in urls]

    main_placeholder.text("Text Splitter...Started...✅✅✅")
    from langchain.embeddings import HuggingFaceEmbeddings

    documents = [Document(page_content=content) for content in data]

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100
    )

    docs = text_splitter.split_documents(documents)

    vectorindex_hf = FAISS.from_documents(docs, embeddings)

    with open(file_path, "wb") as f:
        pickle.dump(vectorindex_hf, f)


query = main_placeholder.text_input("Question: ")
if query:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            vectorIndex = pickle.load(f)


            def get_relevant_chunks(query, index, top_k=3):
                query_embedding = embeddings.embed_query(query)

                relevant_chunks = index.similarity_search_by_vector(query_embedding, k=top_k)

                return [chunk.page_content for chunk in relevant_chunks]

            relevant_chunks = get_relevant_chunks(query, vectorIndex)

            combined_content = " ".join(relevant_chunks)

            client = OpenAI(
                base_url="https://api.groq.com/openai/v1",
                api_key=groq_api
            )

            prompt = f"Here is the content: {combined_content}\n\nQuestion: {query}"

            response = client.chat.completions.create(
                model="llama-3.1-70b-versatile",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            st.title(response.choices[0].message.content)

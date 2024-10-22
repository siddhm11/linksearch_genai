# linksearch_genai
---

# Data Related Query Retriever

This project is a web application built using Streamlit, LangChain, FAISS, Hugging Face, and Groq API. It allows users to retrieve relevant information from articles using a query, process the content, and generate responses based on the query using a language model.

## Features

- Scrapes data from provided URLs.
- Splits the text content into smaller chunks for better processing.
- Embeds the text using Hugging Face models and stores embeddings using FAISS.
- Retrieves the most relevant chunks of text for a given query.
- Uses the Groq API to process queries and generate responses.

## Installation

### Prerequisites

- Python 3.7 or higher
- Streamlit
- Hugging Face API token
- Groq API token

### Clone the Repository

```bash
git clone https://github.com/your-username/data-query-retriever.git
cd data-query-retriever
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set up API Keys

Ensure you have both Hugging Face and Groq API tokens. Create a `huggingface.py` and `groq_api.py` file in the root directory to store your API tokens as variables:

```python
# huggingface.py
huggingface = "your-huggingface-api-token"

# groq_api.py
groq_api = "your-groq-api-token"
```

### Run the Application

```bash
streamlit run app.py
```

## Usage

1. Enter up to 3 URLs in the sidebar.
2. Click on the "Process URLs" button to scrape the article data and generate embeddings.
3. Ask a question in the text input field, and the system will retrieve relevant content from the URLs and generate an answer.

## File Structure

```
.
├── app.py               # Main application file
├── huggingface.py        # Hugging Face API token file
├── groq_api.py           # Groq API token file
├── embeddingsstore.pkl   # FAISS embedding store file (generated after processing)
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
```

## Dependencies

- Streamlit
- LangChain
- Hugging Face
- FAISS
- BeautifulSoup
- Requests
- Groq API
- OpenAI

Make sure to include these in your `requirements.txt`:

```
streamlit
langchain
sentence-transformers
faiss-cpu
requests
beautifulsoup4
openai
```

## License

This project is licensed under the MIT License.

---

![image](https://github.com/user-attachments/assets/74a78bf2-c1ed-42ab-b95e-8fe2b09b9069)


![Screenshot 2024-09-25 105435](https://github.com/user-attachments/assets/98f348e1-b2d0-4d23-883f-16e318f7a1c7)

![image](https://github.com/user-attachments/assets/0ba42851-6583-49ed-be06-b88e3c6846e7)

![Screenshot 2024-09-25 105719](https://github.com/user-attachments/assets/b46e82ac-91ed-4b92-92be-b8fd435f5607)

![Screenshot 2024-09-25 105741](https://github.com/user-attachments/assets/0ba94bef-ca36-43a8-acf2-30048b5f2a10)

![image](https://github.com/user-attachments/assets/733ae542-1b1d-4a56-b432-e04a2114d0e2)


![Screenshot 2024-09-25 105822](https://github.com/user-attachments/assets/44253066-64bb-4eac-9754-b9999fcc58f6)

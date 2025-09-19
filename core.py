import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings  # Updated import
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from dotenv import load_dotenv
load_dotenv()
# from tenacity import retry, stop_after_attempt, wait_exponential
api_key = os.getenv("GOOGLE_API_KEY")
# ---------------------------
# Gemini API setup
# ---------------------------
os.environ["GOOGLE_API_KEY"] = api_key

# HuggingFace local embeddings (updated to use new package)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Gemini as chat model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.5)

# ---------------------------
# Document Loader Function
# ---------------------------
def load_documents(file_paths):
    docs = []
    for path in file_paths:
        if path.endswith(".txt"):
            loader = TextLoader(path, encoding="utf-8")
        elif path.endswith(".pdf"):
            loader = PyPDFLoader(path)
        else:
            print(f"Skipping unsupported file: {path}")
            continue
        docs.extend(loader.load())
    return docs

# ---------------------------
# Text Splitter
# ---------------------------
def split_documents(documents, chunk_size=1000, chunk_overlap=200):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    return splitter.split_documents(documents)

# ---------------------------
# Create or load Chroma DB
# ---------------------------
# @retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=4, max=10))
def create_vectordb(documents, embeddings):
    if not os.path.exists("./chroma_store"):
        v_db = Chroma.from_documents(
            documents=documents,
            embedding=embeddings,
            collection_name="demo_collection",
            persist_directory="./chroma_store"
        )
        return v_db
    else:
        return Chroma(
            collection_name="demo_collection",
            embedding_function=embeddings,
            persist_directory="./chroma_store"
        )

# ---------------------------
# Load and process your files
# ---------------------------
file_paths = ["data/DocHok.txt","data/HOK_C1.txt","data/HOK_C2.txt","data/HOK_C3.txt","data/HOK_C4.txt","data/HOK_C5.txt","data/HOK_C6.txt","data/HOK_C7.txt","data/HOK_C8.txt"]  # replace with your files
raw_docs = load_documents(file_paths)
docs = split_documents(raw_docs)
v_db = create_vectordb(docs, embeddings)
retriever = v_db.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# ---------------------------
# Updated Prompt + QA chain using LangChain v0.3+ pattern
# ---------------------------
prompt_template = """
You are HOK Master, an AI strategy coach for Honor of Kings. 
Use the following game context and meta data to give the best possible answer.

Context:
{context}

Question:
{input}

Answer in a structured way with:
- Hero Overview
- Counters & Weaknesses
- Tips & Tricks
- Rotation & Macro Strategy
- Practice Recommendations (Beginner → Advanced → Pro)

Always finish with a short summary in very simple terms.

"""
PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "input"])

# Create the documents chain
combine_docs_chain = create_stuff_documents_chain(llm, PROMPT)

# Create the retrieval chain
retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)

def get_rag_response(query):
    result = retrieval_chain.invoke({"input": query})
    return result["answer"]

# ---------------------------
# Run Query
# ---------------------------
if __name__ == "__main__":
    query = "What is the best way to play Marksman heroes?"
    result = get_rag_response(query)
    print("--------------------------------")
    print("--------------------------------")
    print("Answer:", result)
    print("--------------------------------")
    print("--------------------------------")

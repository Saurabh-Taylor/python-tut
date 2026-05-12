from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv

load_dotenv()

pdf_path = Path(__file__).parent / "100 Node.js Interview Questions.pdf"

# load the PDF document
loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()

# split the document into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=400
)
chunks = text_splitter.split_documents(documents=docs)

# vector embeddings 
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="nodejs-interview-questions"
)

print("Documents have been processed and stored in Qdrant vector store.")
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

openai_client = OpenAI()

# Vector embedding model
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

# connect vector db connection
vector_db =  QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="nodejs-interview-questions",
    embedding=embedding_model
)


# take the user input
user_query = input("Enter your question about Node.js: ")

# returns relevant chunks
search_results = vector_db.similarity_search(query=user_query)

context = "\n\n\n".join([f"Page {result.metadata.get('page', 'N/A')}:\n{result.page_content}" for result in search_results])

SYSTEM_PROMPT = f"""
    You are a helpful assistant that answers user query based on the available context retrieved from the database along with page_contents and page_number. Always cite the page number in your answer. If you don't know the answer, say you don't know.

    Context:
    {context}
"""

responses = openai_client.chat.completions.create(
    model="gpt-5",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": user_query
        }
    ]
)

print("Answer generated based on the retrieved context.", responses.choices[0].message.content)
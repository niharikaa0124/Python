from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import requests
import os
from dotenv import load_dotenv

reader=PdfReader("niharikaa_resume.pdf")
text="" 

for page in reader.pages:
    text +=page.extract_text()

# print(text)

chunk_size=100
chunks=[]

for i in range(0,len(text),chunk_size):
    chunk=text[i:chunk_size+i]
    chunks.append(chunk)

# print(chunks)

model=SentenceTransformer(
    "all-MiniLM-L6-v2"
)

embeddings=model.encode(chunks)

# print(embeddings)

# print(len(chunks))
# print(len(embeddings))
# print(embeddings.shape)

dimension=embeddings.shape[1]

index=faiss.IndexFlatL2(dimension)
index.add(embeddings)

query = input("Ask a question: ")

query_embedding = model.encode([query])

distances, indices = index.search(
    query_embedding,
    3
)

print(indices)
print(distances)

# for idx in indices[0]:
#     print("\n")
#     print(chunks[idx])

load_dotenv()

API_KEY=os.getenv("GROQ_API_KEY")

headers={
    "Authorization":f"Bearer {API_KEY}",
    "Content-Type":"application/json"
}

print("API KEY:", API_KEY)
print("HEADERS:", headers)

context=""

for idx in indices[0]:
    context+=chunks[idx]
    context+="\n\n"

prompt=f"""
Answer the question using only provided data

Context:
{context}

Question:
{query}

Answer:
"""

payload={
    "model":"llama-3.1-8b-instant",
    "messages":[
        {   
            "role":"user",
            "content": prompt
        }
    ]
}

API_URL = "https://api.groq.com/openai/v1/chat/completions"

response=requests.post(
    API_URL,
    headers=headers,
    json=payload
)

data=response.json()

print(data)

if "choices" not in data:
    print("API Error")
    exit()


answer=data["choices"][0]["message"]["content"]

print("\nAnswer:\n")
print(answer)
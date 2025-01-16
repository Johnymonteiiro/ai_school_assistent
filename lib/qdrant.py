from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from dotenv import load_dotenv
import os

load_dotenv()

qdrant_db = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY"),
)

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')


def create_qdrant_collections(collections=[], dimensions=384):
    if len(collections) == 0:
        return print("You must provide a collections name!")

    for collection_name in collections:
       qdrant_db.recreate_collection(
           collection_name=collection_name,
           vectors_config=VectorParams(
               size=dimensions, distance=Distance.COSINE),
       )
       print(f"Collection '{collection_name}' created")

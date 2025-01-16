from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

qdrant_db = QdrantClient(
    url="https://1ed777cc-63bc-4ba7-9895-f838b3551f88.us-east-1-0.aws.cloud.qdrant.io:6333",
    api_key="_FePxboPzz-wYH_vzV6tbpLVukvKyH6M9gpE3JQ7nbSpbSFSKE_W_w",
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

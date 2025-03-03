from llama_index.core import VectorStoreIndex
import qdrant_client
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

client = qdrant_client.QdrantClient(host="localhost", port=6333)
try:
    response = client.get_collections()
    print("Connected to Qdrant successfully!")
    print("Available collections:", response)
except Exception as e:
    print("Failed to connect to Qdrant:", e)


model_improve_halong = HuggingFaceEmbedding(model_name="johnweak132/improve_halong")
vector_improve_halong = QdrantVectorStore(
    "uit_improve_halong",
    client=client,
    enable_hybrid=True,
    embed_model=model_improve_halong,
)
index_improve_halong = VectorStoreIndex.from_vector_store(
    vector_improve_halong, embed_model=model_improve_halong
)
retriver_improve_halong = index_improve_halong.as_retriever(
    vector_store_query_mode="hybrid", alpha=1, similarity_top_k=10
)


def retrieval(query: str):
    return retriver_improve_halong.retrieve(query)

import chromadb
from chromadb.utils import embedding_functions
import os

VAULT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'memory-vault'))
DB_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '.chroma_db'))

class MemoryEngine:
    def __init__(self):
        # Persistent client for local vector storage
        self.client = chromadb.PersistentClient(path=DB_DIR)
        
        # Use sentence transformers for local embedding to maintain air-gapped security
        self.embed_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
        
        self.collection = self.client.get_or_create_collection(
            name="agent_memory",
            embedding_function=self.embed_fn
        )

    def index_vault(self):
        """Indexes all markdown files in the memory-vault directory."""
        if not os.path.exists(VAULT_DIR):
            print(f"Vault directory {VAULT_DIR} does not exist.")
            return

        documents = []
        metadatas = []
        ids = []

        for filename in os.listdir(VAULT_DIR):
            if filename.endswith(".md"):
                file_path = os.path.join(VAULT_DIR, filename)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    documents.append(content)
                    metadatas.append({"source": filename})
                    ids.append(filename)
        
        if documents:
            self.collection.add(
                documents=documents,
                metadatas=metadatas,
                ids=ids
            )
            print(f"Indexed {len(documents)} documents.")

    def query_memory(self, query_text, n_results=3):
        """Searches the agent's memory for relevant context."""
        results = self.collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
        return results

if __name__ == "__main__":
    engine = MemoryEngine()
    engine.index_vault()
    
    # Test query
    print("Testing Vector Retrieval:")
    res = engine.query_memory("What is the memory layer?")
    print(res)

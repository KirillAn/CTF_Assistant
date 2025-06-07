import networkx as nx
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

def build_graph(documents):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = splitter.split_documents(documents)

    G = nx.Graph()
    embed_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    for i, doc in enumerate(docs):
        emb = embed_model.embed_documents([doc.page_content])[0]
        G.add_node(i, content=doc.page_content, embedding=emb)

    return G, embed_model

import json
from langchain_core.documents import Document

def load_documents(data_path):
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    documents = []
    if isinstance(data, list):
        for item in data:
            text = json.dumps(item, ensure_ascii=False)
            documents.append(Document(page_content=text))
    else:
        text = json.dumps(data, ensure_ascii=False)
        documents.append(Document(page_content=text))
    return documents

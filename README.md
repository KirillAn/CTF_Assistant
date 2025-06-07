# CTF_Assistant

```
ctf-assistant/
├── README.md
├── requirements.txt
├── .env.example
├── main.py                  # Entry point (CLI)
├── config.py                # Paths, constants, env
├── logger.py                # Logging setup
├── rag/
│   ├── __init__.py
│   ├── loader.py            # JSON + document loading
│   ├── embeddings.py        # Embedding + graph creation
│   └── model.py             # HuggingFace pipeline loading
├── tools/
│   ├── __init__.py
│   ├── dirsearch_tool.py
│   ├── nmap_tool.py
│   ├── sqlmap_tool.py
│   ├── hashcat_tool.py
│   ├── cyberchef_tool.py
│   └── rag_tool.py
├── agent/
│   ├── __init__.py
│   ├── tool_router.py
│   ├── reasoning.py         # run_reasoning_loop
│   └── prompt_template.py
└── utils/
    ├── __init__.py
    ├── text_utils.py        # text formatting, extraction
    └── env_utils.py         # token and env parsing
```
```mermaid
flowchart TD
    documents["Source Documents (JSON)"]
    createEmbeddings["Generate Embeddings"]
    insertDB["Insert into Graph Database"]
    question["User Question"]
    LLM["LLM Agent"]
    answer["Generate Final Answer"]
    search["Search Relevant Context"]
    retriever["Graph Retriever"]

    documents --> createEmbeddings
    createEmbeddings --> insertDB
    insertDB --> retriever
    question --> LLM
    LLM --> answer
    LLM --> search
    search --> retriever

    classDef yellowBox fill:#fff3b3,stroke:#ffd966,stroke-width:2px
    classDef greenBox fill:#dafbe1,stroke:#8dde98,stroke-width:2px
    classDef blueBox fill:#d4efff,stroke:#5dc8f4,stroke-width:2px
    classDef purpleBox fill:#fce4ff,stroke:#fcb0ff,stroke-width:2px
    classDef orangeBox fill:#ffe5d1,stroke:#ffa45b,stroke-width:2px
    classDef grayBox fill:#f4f4f4,stroke:#ccc,stroke-width:2px

    class documents yellowBox
    class createEmbeddings blueBox
    class insertDB orangeBox
    class question greenBox
    class LLM,answer purpleBox
    class search,retriever grayBox

```
### 💾 Dataset
Manually compiled based on real-world penetration testing data.

1️⃣ System analysis and reconnaissance (Initial Recon & Exploitation) – vulnerable ports, weak passwords.

2️⃣ Network & data forensics – packet capture analysis, cryptography challenges.

3️⃣ Low-level exploitation – buffer overflows, insecure code patterns.

4️⃣ Binary exploitation & reverse engineering – binary analysis, bypassing protection mechanisms.




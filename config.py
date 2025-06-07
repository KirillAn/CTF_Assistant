import os

MODEL_PATH = "teknium/OpenHermes-2.5-Mistral-7B"
DATA_PATH = os.getenv("DATA_PATH", "/combined_md5_priority.json")
SQLMAP_PATH = "/sqlmap/sqlmap.py"
TIMEOUT = 120
DIRSEARCH_PATH = "/anaconda3/lib/python3.11/site-packages/dirsearch/dirsearch.py"
SECLISTS_PATH = "/SecLists/Discovery/Web-Content"

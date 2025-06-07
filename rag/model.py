import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_huggingface import HuggingFacePipeline

def load_llm(model_path):
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True, use_auth_token=os.environ.get("HF_HUB_TOKEN"))
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch.float16,
        device_map="auto",
        trust_remote_code=True,
        use_auth_token=os.environ.get("HF_HUB_TOKEN")
    )
    gen_pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=256,
        temperature=0.7,
        top_p=0.95,
        repetition_penalty=1.15,
        device_map="auto"
    )
    return HuggingFacePipeline(pipeline=gen_pipe)

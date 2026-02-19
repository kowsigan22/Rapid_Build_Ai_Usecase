from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import streamlit as st

torch.set_num_threads(4)
torch.set_num_interop_threads(4)

MODEL_NAME = "bigcode/starcoder2-3b"

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        dtype=torch.float32,
        low_cpu_mem_usage=True
    )
    return tokenizer, model


def call_llm(prompt: str, max_tokens: int = 1024) -> str:
    tokenizer, model = load_model()

    inputs = tokenizer(prompt, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        max_new_tokens=max_tokens,
        do_sample=False,
        temperature=0.0,
        pad_token_id=tokenizer.eos_token_id
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)
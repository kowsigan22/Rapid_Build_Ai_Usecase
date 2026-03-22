from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from typer import prompt

MODEL_NAME = "bigcode/starcoder2-3b"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float32,
    low_cpu_mem_usage=True
)


def call_llm(prompt: str, max_tokens: int = 1024) -> str:
    if "frontend" in prompt.lower():
    max_tokens = 2048
elif "full stack" in prompt.lower():
    max_tokens = 2048
else:
    max_tokens = 1024
    inputs = tokenizer(prompt, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        max_new_tokens=max_tokens,
        do_sample=False,        # VERY IMPORTANT
        temperature=0.0,        # VERY IMPORTANT
        pad_token_id=tokenizer.eos_token_id
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)
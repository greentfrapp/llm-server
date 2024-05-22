import torch
import transformers

from core.config import settings


model_id = "meta-llama/Meta-Llama-3-8B-Instruct"

LLM = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
    token=settings.HUGGING_FACE_TOKEN,
)

SYSTEM_PROMPT = "You are a helpful digital assistant. Please provide safe, ethical and accurate information to the user."


def generate(query: str, temperature=0.0, max_new_tokens=500, history=None, system_prompt=SYSTEM_PROMPT):
    messages = history or [
        {"role": "system", "content": system_prompt},
    ]
    messages.append({"role": "user", "content": query})
    generation_args = {
        "max_new_tokens": max_new_tokens,
        "return_full_text": False,
    }
    if temperature == 0:
        generation_args["do_sample"] = False
    else:
        generation_args["do_sample"] = True
        generation_args["temperature"] = temperature

    result = LLM(
        messages,
        **generation_args,
    )

    return result

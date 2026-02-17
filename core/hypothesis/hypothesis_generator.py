from llama_cpp import Llama
from diskcache import Cache
import hashlib
import json

class LLMHypothesisGenerator:
    def __init__(self):
        # Load LLM only once
        self.llm = Llama(
            model_path="models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
            n_ctx=1024,
            n_threads=6,
            n_gpu_layers=0
        )

        # Disk cache (auto-create folder)
        self.cache = Cache("cache/hypotheses")

    def _make_key(self, context: dict) -> str:
        """Create a stable hash key from input context"""
        context_str = json.dumps(context, sort_keys=True)
        return hashlib.sha256(context_str.encode()).hexdigest()

    def generate(self, context: dict) -> str:
        key = self._make_key(context)

        # 1️⃣ Check cache
        if key in self.cache:
            return self.cache[key]

        # 2️⃣ Generate using LLM
        prompt = f"""
You are an autonomous artificial scientist.

Based on the signals below, generate ONE concise scientific hypothesis
that could be experimentally tested.

Signals:
- Curiosity score: {context.get("curiosity_score")}
- Uncertainty: {context.get("uncertainty")}
- Novelty: {context.get("novelty")}

Hypothesis:
"""

        output = self.llm(
            prompt,
            max_tokens=80,
            temperature=0.7,
            stop=["\n"]
        )

        hypothesis = output["choices"][0]["text"].strip()

        # 3️⃣ Save to cache
        self.cache[key] = hypothesis

        return hypothesis

from llama_cpp import Llama

class HypothesisLLM:
    def __init__(self):
        self.llm = Llama(
            model_path="models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
            n_ctx=1024,
            n_threads=8
        )

        self.system_prompt = (
            "You are an artificial scientist analyzing an AI system.\n"
            "Rules:\n"
            "- Do NOT invent discoveries\n"
            "- Do NOT mention new materials or physics\n"
            "- Focus only on system behavior, uncertainty, learning efficiency\n"
            "- Use neutral, research-style language\n"
            "- Output only 1-2 sentences\n"
        )

    def generate(self, curiosity_score: float) -> str:
        messages = [
            {"role": "system", "content": self.system_prompt},
            {
                "role": "user",
                "content": f"Curiosity score is {curiosity_score}. Generate a cautious hypothesis."
            }
        ]

        result = self.llm.create_chat_completion(messages=messages)
        return result["choices"][0]["message"]["content"]

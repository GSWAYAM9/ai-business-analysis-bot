import os

PROMPT_DIR = os.path.join(os.path.dirname(__file__))

def load_prompt(filename: str) -> str:
    """
    Loads a text prompt from /prompts/ directory.
    """
    full_path = os.path.join(PROMPT_DIR, filename)

    if not os.path.exists(full_path):
        raise FileNotFoundError(f"Prompt file not found: {filename}")

    with open(full_path, "r", encoding="utf-8") as f:
        return f.read()

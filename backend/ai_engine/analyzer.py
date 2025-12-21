from ai_engine.model_client import generate_text
from ai_engine.prompts import load_prompt

def run_analysis(data):
    print("🔥 RUNNING AI ANALYSIS")

    summary_prompt = load_prompt("summary_prompt.txt").format(data=data)
    print("📄 SUMMARY PROMPT LOADED")

    strengths_prompt = load_prompt("strengths_prompt.txt").format(data=data)
    weaknesses_prompt = load_prompt("weaknesses_prompt.txt").format(data=data)
    improvements_prompt = load_prompt("improvements_prompt.txt").format(data=data)

    summary = generate_text(summary_prompt)
    print("🧠 SUMMARY OUTPUT:", repr(summary[:120]))

    strengths = generate_text(strengths_prompt)
    weaknesses = generate_text(weaknesses_prompt)
    improvements = generate_text(improvements_prompt)

    return {
        "summary": summary,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "improvements": improvements
    }

def pretty_text_report(analysis: dict) -> str:
    """
    Converts analysis dict into a readable plain-text report.
    """
    s = []
    summary = analysis.get("summary","")
    s.append("=== EXECUTIVE SUMMARY ===")
    s.append(summary)
    s.append("\n=== SCORES ===")
    for k,v in (analysis.get("scores") or {}).items():
        s.append(f"{k}: {v}")
    s.append("\n=== STRENGTHS ===")
    s.append(analysis.get("strengths",""))
    s.append("\n=== WEAKNESSES ===")
    s.append(analysis.get("weaknesses",""))
    s.append("\n=== IMPROVEMENTS (30/60/90) ===")
    s.append(analysis.get("improvements",""))
    return "\n".join(s)

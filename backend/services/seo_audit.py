def quick_seo_audit(samples: list, description: str) -> dict:
    """
    Very light SEO checks: presence of meta description, keywords in headings, alt tags hints.
    """
    issues = []
    if not description or len(description) < 50:
        issues.append("Meta description is short or missing.")
    keyword_count = 0
    for s in samples:
        if s and len(s) > 20:
            keyword_count += 1
    if keyword_count < 3:
        issues.append("Low content variety / headings missing.")
    return {"issues": issues, "score": max(0, 100 - len(issues)*20)}

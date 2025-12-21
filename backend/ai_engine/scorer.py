def compute_scores(data: dict) -> dict:
    """
    Simple heuristic scoring based on presence of fields.
    """
    followers = data.get("followers") or 0
    samples = len(data.get("samples") or [])
    desc = data.get("description") or data.get("bio") or ""
    brand_health = 50
    engagement_score = 50

    # adjust brand health if description present and samples
    if desc:
        brand_health += 10
    brand_health += min(20, samples * 2)

    # engagement heuristic
    try:
        followers = int(followers or 0)
    except:
        followers = 0
    if followers > 10000:
        engagement_score -= 10
    if samples >= 5:
        engagement_score += 10
    # clamp
    brand_health = max(0, min(100, brand_health))
    engagement_score = max(0, min(100, engagement_score))
    return {"brand_health": brand_health, "engagement": engagement_score}

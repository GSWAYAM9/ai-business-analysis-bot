def standardize_scraped_data(platform: str, raw: dict) -> dict:
    """
    Normalize scraped data into a consistent schema for AI analysis.
    """

    # Basic fields
    url = raw.get("url")
    name = raw.get("name") or raw.get("title") or raw.get("fullname") or ""
    description = raw.get("description") or raw.get("bio") or ""

    # Platform-specific mapping
    followers = raw.get("followers") or raw.get("follower_count")
    posts = raw.get("posts") or raw.get("recent_posts") or []
    samples = raw.get("samples") or raw.get("captions") or []

    return {
        "platform": platform,
        "url": url,
        "name": name,
        "description": description,
        "followers": followers,
        "posts": posts,
        "samples": samples,
        "metadata": raw.get("metadata", {}),
    }

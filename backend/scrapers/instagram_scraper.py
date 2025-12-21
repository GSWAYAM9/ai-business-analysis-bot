import instaloader
import concurrent.futures
from datetime import timezone
from typing import Dict, Any
from config import settings

MAX_RECENT_POSTS = 10


def _iso(dt):
    if not dt:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.isoformat()


def _blocking_scrape(username: str) -> Dict[str, Any]:
    """
    Runs Instaloader in a separate thread.
    Never raises exceptions outside this function.
    """

    L = instaloader.Instaloader(
        dirname_pattern=None,
        download_pictures=False,
        download_videos=False,
        download_comments=False,
        save_metadata=False,
        compress_json=False,
        quiet=True,
    )

    # Optional login (helps but not required)
    try:
        if settings.INSTALOADER_USERNAME and settings.INSTALOADER_PASSWORD:
            L.login(
                settings.INSTALOADER_USERNAME,
                settings.INSTALOADER_PASSWORD,
            )
    except Exception:
        pass  # Continue without login

    try:
        profile = instaloader.Profile.from_username(L.context, username)
    except Exception as e:
        # Hard failure → return safe empty object
        return {
            "username": username,
            "fullname": None,
            "bio": None,
            "followers": 0,
            "following": 0,
            "posts_count": 0,
            "profile_pic": None,
            "recent_posts": [],
            "error": str(e),
        }

    # ✅ SAFE FIELD EXTRACTION (NO HALLUCINATION)
    result: Dict[str, Any] = {
        "username": profile.username,
        "fullname": profile.full_name or profile.username,
        "bio": profile.biography or "",
        "followers": profile.followers or 0,
        "following": profile.followees or 0,
        "posts_count": profile.mediacount or 0,
        "profile_pic": str(profile.profile_pic_url) if profile.profile_pic_url else None,
        "recent_posts": [],
    }

    # Try fetching posts (optional, non-blocking)
    try:
        for i, post in enumerate(profile.get_posts()):
            result["recent_posts"].append({
                "caption": post.caption or "",
                "likes": post.likes or 0,
                "comments": post.comments or 0,
                "hashtag_count": len(post.caption_hashtags),
                "timestamp": _iso(post.date_utc),
                "post_url": f"https://www.instagram.com/p/{post.shortcode}/",
                "image_url": str(post.url) if post.url else None,
            })
            if i + 1 >= MAX_RECENT_POSTS:
                break
    except Exception:
        # Posts are optional — silently ignore
        pass

    return result


def scrape_instagram(url: str) -> Dict[str, Any]:
    """
    Public function used by FastAPI routes.
    Enforces timeout and never blocks event loop.
    """

    if not url:
        return {"error": "Instagram URL missing"}

    username = url.rstrip("/").split("/")[-1]
    if not username:
        return {"error": "Invalid Instagram URL"}

    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
            future = executor.submit(_blocking_scrape, username)
            return future.result(timeout=15)
    except concurrent.futures.TimeoutError:
        return {
            "username": username,
            "fullname": None,
            "bio": None,
            "followers": 0,
            "following": 0,
            "posts_count": 0,
            "profile_pic": None,
            "recent_posts": [],
            "error": "Instagram scraping timed out",
        }

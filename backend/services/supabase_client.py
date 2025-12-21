from supabase import create_client
from typing import Dict, Any
from config import settings

# Initialize Supabase client
supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)


def save_instagram_profile(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Upserts scraped Instagram data into the 'instagram_profiles' table.
    Uses 'username' as unique key.
    Works with the newest Supabase Python client.
    """

    payload = {
        "username": data.get("username"),
        "fullname": data.get("fullname"),
        "bio": data.get("bio"),
        "followers": data.get("followers"),
        "following": data.get("following"),
        "posts_count": data.get("posts_count"),
        "profile_pic": data.get("profile_pic"),
        "recent_posts": data.get("recent_posts"),
    }

    try:
        response = (
            supabase.table("instagram_profiles")
            .upsert(payload, on_conflict="username")
            .execute()
        )

        # Response structure depends on supabase-py version
        result_data = getattr(response, "data", response)

        return {
            "success": True,
            "data": result_data
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
        
from urllib.parse import urlparse

PLATFORM_HOSTS = {
    "instagram": ["instagram.com", "www.instagram.com", "instagr.am"],
    "youtube": ["youtube.com", "www.youtube.com", "youtu.be"],
    "linkedin": ["linkedin.com", "www.linkedin.com"],
    "facebook": ["facebook.com", "www.facebook.com"],
}


def detect_platform(url: str) -> str:
    """
    Detect the platform from a given URL by hostname.
    """
    parsed = urlparse(url)
    host = parsed.netloc.lower()

    for platform, hosts in PLATFORM_HOSTS.items():
        if any(h in host for h in hosts):
            return platform

    # Default fallback
    return "website"

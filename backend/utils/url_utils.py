from urllib.parse import urlparse, urlunparse

def ensure_protocol(url: str) -> str:
    if not url.startswith("http"):
        return "https://" + url
    return url

def clean_url(url: str) -> str:
    p = urlparse(url)
    # normalize
    return urlunparse((p.scheme or "https", p.netloc, p.path.rstrip('/'), "", "", ""))

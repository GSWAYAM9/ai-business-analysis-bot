import requests
from bs4 import BeautifulSoup
from utils.url_utils import ensure_protocol
from config import settings

HEADERS = {"User-Agent": settings.USER_AGENT}

def scrape_linkedin(url: str) -> dict:
    """
    Simple scraping for LinkedIn company pages; LinkedIn may block scraping.
    For production, use LinkedIn's API.
    """
    url = ensure_protocol(url)
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        resp.raise_for_status()
    except Exception as e:
        return {"url": url, "error": str(e)}

    soup = BeautifulSoup(resp.text, "html.parser")
    title = soup.find("meta", property="og:title")
    desc = soup.find("meta", property="og:description")
    name = title["content"] if title else ""
    description = desc["content"] if desc else ""

    return {
        "url": url,
        "name": name,
        "description": description,
        "followers": None,
        "posts": [],
        "samples": [],
        "metadata": {}
    }

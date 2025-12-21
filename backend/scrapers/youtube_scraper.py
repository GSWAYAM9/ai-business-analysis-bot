import requests
from bs4 import BeautifulSoup
from utils.url_utils import ensure_protocol

def scrape_youtube(url: str) -> dict:
    """
    Basic scraping for YouTube channel / video pages to extract title, description, views from og tags.
    For production use YouTube Data API.
    """
    url = ensure_protocol(url)
    try:
        resp = requests.get(url, timeout=10, headers={"User-Agent":"Mozilla/5.0"})
        resp.raise_for_status()
    except Exception as e:
        return {"url": url, "error": str(e)}

    soup = BeautifulSoup(resp.text, "html.parser")
    og_title = soup.find("meta", property="og:title")
    og_desc = soup.find("meta", property="og:description")
    name = og_title["content"] if og_title else ""
    description = og_desc["content"] if og_desc else ""

    # collect some sample comments/titles from page
    samples = []
    for meta in soup.find_all("meta", itemprop=True):
        if meta.get("itemprop") in ("name", "author"):
            samples.append(meta.get("content",""))

    return {
        "url": url,
        "name": name,
        "description": description,
        "followers": None,
        "posts": [],
        "samples": samples,
        "metadata": {}
    }

import requests
from bs4 import BeautifulSoup
from utils.url_utils import ensure_protocol
from config import settings

HEADERS = {"User-Agent": settings.USER_AGENT}

def scrape_website(url: str) -> dict:
    url = ensure_protocol(url)
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        resp.raise_for_status()
    except Exception as e:
        return {"url": url, "error": str(e)}
    soup = BeautifulSoup(resp.text, "html.parser")
    title = soup.find("title").text if soup.find("title") else ""
    meta_desc = soup.find("meta", attrs={"name":"description"})
    desc = meta_desc.get("content") if meta_desc else ""
    # collect h1/h2 and sample paragraphs
    samples = []
    for h in soup.find_all(["h1","h2"])[:5]:
        samples.append(h.get_text(strip=True))
    for p in soup.find_all("p")[:5]:
        samples.append(p.get_text(strip=True))
    return {
        "url": url,
        "title": title,
        "description": desc,
        "followers": None,
        "posts": [],
        "samples": samples,
        "metadata": {}
    }

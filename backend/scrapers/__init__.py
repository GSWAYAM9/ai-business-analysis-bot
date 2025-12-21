from .instagram_scraper import scrape_instagram
from .youtube_scraper import scrape_youtube
from .linkedin_scraper import scrape_linkedin
from .website_scraper import scrape_website

SCRAPER_MAP = {
    "instagram": scrape_instagram,
    "youtube": scrape_youtube,
    "linkedin": scrape_linkedin,
    "website": scrape_website
}

from scrapers.website_scraper import scrape_website

def test_scrape_website_local():
    # basic smoke test with example.com
    r = scrape_website("https://example.com")
    assert "title" in r
    assert r["url"].startswith("http")

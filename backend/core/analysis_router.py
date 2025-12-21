from scrapers import SCRAPER_MAP
from core.platform_detector import detect_platform
from core.data_cleaner import standardize_scraped_data
from ai_engine.analyzer import run_analysis


def run_full_analysis(url: str):
    """
    Auto-detects platform → scrapes → cleans data → runs AI analysis.
    This is used for the main /api/analyze route.
    """

    # 1. Detect platform from URL string
    platform = detect_platform(url)

    if platform not in SCRAPER_MAP:
        return {"error": f"Unsupported or unknown platform: {platform}"}

    # 2. Select scraper from the map
    scraper_fn = SCRAPER_MAP[platform]
    raw_data = scraper_fn(url)

    # 3. Normalized cleaned data for AI input
    cleaned_data = standardize_scraped_data(platform, raw_data)

    # 4. Run Groq AI analysis (summary, strengths, weaknesses, improvements)
    analysis = run_analysis(cleaned_data)

    return {
        "platform": platform,
        "url": url,
        "scraped_data": cleaned_data,
        "analysis": analysis
    }

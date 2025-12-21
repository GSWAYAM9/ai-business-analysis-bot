from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # GROQ
    GROQ_API_KEY: str | None = None

    # SUPABASE
    SUPABASE_URL: str | None = None
    SUPABASE_KEY: str | None = None

    # INSTALOADER (optional login)
    INSTALOADER_USERNAME: str | None = None
    INSTALOADER_PASSWORD: str | None = None

    # SCRAPER SETTINGS
    USER_AGENT: str = "Mozilla/5.0 (compatible; AI-Biz-Bot/1.0)"
    MEMORY_FILE: str = "memory/local_db.json"
    MAX_SCRAPE_PAGES: int = 3

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

# Debug Output
print("DEBUG ▸ GROQ_API_KEY =", settings.GROQ_API_KEY)
print("DEBUG ▸ SUPABASE_URL =", settings.SUPABASE_URL)
print("DEBUG ▸ SUPABASE_KEY =", settings.SUPABASE_KEY)
print("DEBUG ▸ INSTALOADER_USERNAME =", settings.INSTALOADER_USERNAME)
print("DEBUG ▸ INSTALOADER_PASSWORD =", settings.INSTALOADER_PASSWORD)

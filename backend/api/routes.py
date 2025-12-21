from fastapi import APIRouter, UploadFile, File, Form, HTTPException

from scrapers.instagram_scraper import scrape_instagram
from ai_engine.analyzer import run_analysis
from utils.file_parser import extract_text_from_file

router = APIRouter()


@router.post("/scrape/instagram")
async def scrape_instagram_route(
    file: UploadFile | None = File(None),
    url: str | None = Form(None),
    question: str | None = Form(None),
):
    """
    Analyze a business using:
    - Instagram URL (optional)
    - Uploaded document (optional)
    - Custom user question (optional)

    At least ONE of (file or url) is required.
    """

    # -------------------------------
    # 1️⃣ Validation
    # -------------------------------
    if not file and not url:
        raise HTTPException(
            status_code=400,
            detail="Provide at least an Instagram URL or upload a document"
        )

    # -------------------------------
    # 2️⃣ Extract document text (if uploaded)
    # -------------------------------
    document_text = ""
    if file:
        try:
            document_text = extract_text_from_file(file)
        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail=f"Failed to read uploaded file: {str(e)}"
            )

    # -------------------------------
    # 3️⃣ Scrape Instagram (if URL provided)
    # -------------------------------
    scraped = {}
    if url:
        try:
            scraped = scrape_instagram(url)
        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail=f"Instagram scraping failed: {str(e)}"
            )

    # -------------------------------
    # 4️⃣ Run AI Analysis
    # -------------------------------
    analysis_input = {
        "platform": "instagram" if url else "document",
        "instagram": scraped,
        "document_text": document_text,
        "question": question,
    }

    analysis = run_analysis(analysis_input)

    # -------------------------------
    # 5️⃣ Final Response
    # -------------------------------
    return {
        "scraped_data": scraped,
        "analysis": analysis,
        "meta": {
            "used_instagram": bool(url),
            "used_document": bool(file),
            "custom_question": bool(question),
        }
    }

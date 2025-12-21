from fastapi import UploadFile
from typing import Optional
import io

def extract_text_from_file(file: UploadFile) -> str:
    """
    Extracts readable text from an uploaded file.

    Supported now:
    - .txt (plain text)
    - Any file as raw UTF-8 fallback

    Future-ready for:
    - PDF
    - DOCX
    - PPTX
    """

    if not file:
        return ""

    filename = file.filename.lower()
    content = file.file.read()

    # -----------------------
    # TXT FILES
    # -----------------------
    if filename.endswith(".txt"):
        return content.decode("utf-8", errors="ignore")

    # -----------------------
    # PDF FILES (future-safe stub)
    # -----------------------
    if filename.endswith(".pdf"):
        return _pdf_stub(content)

    # -----------------------
    # DOCX FILES (future-safe stub)
    # -----------------------
    if filename.endswith(".docx"):
        return _docx_stub(content)

    # -----------------------
    # PPTX FILES (future-safe stub)
    # -----------------------
    if filename.endswith(".pptx"):
        return _pptx_stub(content)

    # -----------------------
    # FALLBACK (raw text)
    # -----------------------
    return content.decode("utf-8", errors="ignore")


# ==================================================
# 🔮 FUTURE EXTENSIONS (SAFE STUBS)
# ==================================================

def _pdf_stub(content: bytes) -> str:
    """
    Placeholder for PDF parsing.
    Replace with pdfplumber or PyPDF2 later.
    """
    try:
        return content.decode("utf-8", errors="ignore")
    except Exception:
        return ""


def _docx_stub(content: bytes) -> str:
    """
    Placeholder for DOCX parsing.
    Replace with python-docx later.
    """
    try:
        return content.decode("utf-8", errors="ignore")
    except Exception:
        return ""


def _pptx_stub(content: bytes) -> str:
    """
    Placeholder for PPTX parsing.
    Replace with python-pptx later.
    """
    try:
        return content.decode("utf-8", errors="ignore")
    except Exception:
        return ""

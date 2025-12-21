import json
from pathlib import Path
from config import settings
from threading import Lock

_db_path = Path(settings.MEMORY_FILE)
_db_path.parent.mkdir(parents=True, exist_ok=True)
_lock = Lock()

def _read_db():
    if not _db_path.exists():
        return {"analyses": []}
    with _db_path.open("r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return {"analyses": []}

def _write_db(data):
    with _db_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def save_analysis(url: str, analysis: dict):
    with _lock:
        db = _read_db()
        db["analyses"].append({"url": url, "analysis": analysis})
        _write_db(db)

def list_analyses(limit: int = 50):
    db = _read_db()
    return db.get("analyses", [])[-limit:]

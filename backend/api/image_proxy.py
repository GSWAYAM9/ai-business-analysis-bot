from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter()

@router.get("/proxy-image")
async def proxy_image(url: str):
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(url)
            if r.status_code != 200:
                raise HTTPException(status_code=400, detail="Failed to fetch image")

        return Response(content=r.content, media_type="image/jpeg")

    except Exception:
        raise HTTPException(status_code=500, detail="Proxy error")

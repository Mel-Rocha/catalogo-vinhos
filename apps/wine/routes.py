import asyncio
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse, unquote

from fastapi_pagination import Page, add_pagination, paginate
from fastapi import APIRouter, Path, HTTPException

from apps.wine.models import Wine
from apps.wine.schema import WineSchema
from scraping.extract_max import extract_max
from scraping.extract_min import extract_min


router = APIRouter()


@router.get("/")
async def get_wine_all() -> Page[WineSchema]:
    wine_all = await Wine.all()

    return paginate(wine_all)


add_pagination(router)


async def extract(url: str):
    parsed_url = urlparse(url)
    if not parsed_url.netloc.startswith('www.cartadeivinicdv.com') or '/products/' not in parsed_url.path:
        raise HTTPException(status_code=400, detail="Invalid URL")

    try:
        url = unquote(url)
        loop = asyncio.get_event_loop()

        with ThreadPoolExecutor() as executor:
            result_max = await loop.run_in_executor(executor, extract_max, url)
            result_min = await loop.run_in_executor(executor, extract_min, url)

        return result_max, result_min
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{url:path}")
async def extract_wine(url: str = Path(..., title="The URL of the wine")):
    try:
        url = unquote(url)
        result_max, result_min = await extract(url)
        return {"max": result_max, "min": result_min}
    except HTTPException as e:
        return {"error": str(e.detail)}
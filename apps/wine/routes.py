import asyncio
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse, unquote

from fastapi_pagination import Page, add_pagination, paginate
from fastapi import APIRouter, Path, HTTPException
from fastapi.responses import JSONResponse

from apps.wine.models import Wine
from apps.wine.schema import WineSchema
from scraping.extract_max import extract_max
from scraping.extract_min import extract_min
from apps.wine.exceptions import ExtractionFailedException

router = APIRouter()


@router.get("/")
async def get_wine_all() -> Page[WineSchema]:
    wine_all = await Wine.all()

    return paginate(wine_all)


add_pagination(router)


async def extract(url: str):
    try:
        parsed_url = urlparse(url)
        if not parsed_url.netloc.startswith('www.cartadeivinicdv.com') or '/products/' not in parsed_url.path:
            raise HTTPException(status_code=400, detail="Invalid URL")

        url = unquote(url)
        loop = asyncio.get_event_loop()

        with ThreadPoolExecutor() as executor:
            result_max = await loop.run_in_executor(executor, extract_max, url)
            result_min = await loop.run_in_executor(executor, extract_min, url)

        if not result_max and not result_min:
            raise ExtractionFailedException(status_code=400, detail="Extraction Failed")

        return JSONResponse(
            content={
                "message": "Extraction successful",
                "data": {"max": result_max, "min": result_min}
            },
            status_code=200
        )

    except HTTPException:
        return JSONResponse(
            content={
                "message": "Padrão de URL esperado: "
                           "https://www.cartadeivinicdv.com/products/",

                "data": {}
            },
            status_code=400
        )
    except ExtractionFailedException:
        return JSONResponse(
            content ={
                "message": "A extração não retornou resultado",
                "data": {}
            },
            status_code=400
        )
    except Exception as e:
        return JSONResponse(
            content={
                "message": str(e),
                "data": {}
            },
            status_code=500
        )

@router.get("/{url:path}")
async def extract_wine(url: str = Path(..., title="The URL of the wine")):
    return await extract(url)

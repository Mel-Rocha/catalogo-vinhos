from fastapi_pagination import Page, add_pagination, paginate
from fastapi import APIRouter

from apps.wine.models import Wine
from apps.wine.schema import WineSchema


router = APIRouter()


@router.get("/")
async def get_wine_all() -> Page[WineSchema]:
    wine_all = await Wine.all()

    return paginate(wine_all)


add_pagination(router)
from tortoise.contrib.pydantic import pydantic_model_creator

from apps.wine.models import Wine

WineSchema = pydantic_model_creator(Wine)
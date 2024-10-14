import requests


from fastapi import APIRouter

from constants import AppConstants

storeRouter = APIRouter()

#  get all products from fake store api

@storeRouter.get("/get_products")

async def get_productsEndpoint():

    dataFromApi = requests.get(AppConstants.storeUrl).json()

    return {"message": "success", "data": dataFromApi}
from fastapi import APIRouter
from ast import literal_eval as evall

from constants import AppConstants
import requests

from ai_prompts.crews.products_crew.src.products_crew.crew import ProductsCrew
aiProductsCrew = APIRouter()


@aiProductsCrew.post("/products_crew")
async def products_crew(prompt: str):
    result = ProductsCrew().crew().kickoff(inputs={"prompt": prompt})
    return {"message": "success", "data": result}

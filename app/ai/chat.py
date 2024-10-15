from fastapi import APIRouter
from ast import literal_eval as evall

from constants import AppConstants
import requests

from ai_commands.service_messages.check_for_available import (
    check_for_available_products_service,
)

aiRouter = APIRouter()
from ai_commands.system_messages.message import systemMessage


@aiRouter.post("/chat")
async def chat(text: str):
    # get products before calling ai
    apiResponse = requests.post(
        AppConstants.aiChatUrl,
        json={
            "model": AppConstants.aiModel,
            "options": {"temprature": 0.1},
            "messages": [
                {"role": "system", "content": systemMessage},
                {"role": "assistant", "content": check_for_available_products_service},
                {"role": "user", "content": text},
            ],
            "stream": False,
            "format": "json",
        },
    )

    print(apiResponse.json()["message"]["content"])
    print(type(apiResponse.json()["message"]["content"]))
    return {
        "message": "success",
        "data": evall(apiResponse.json()["message"]["content"]),
    }

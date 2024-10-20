from fastapi import APIRouter
from ast import literal_eval as evall

from constants import AppConstants
import requests

from ai_prompts.chat_assistant.ai_bot_assistant_instruction import (
    chat_ai_instructions_2,
    
)

aiRouter = APIRouter()
from ai_prompts.system_messages.message import systemMessage


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
                {"role": "assistant", "content": chat_bot_instructions},
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

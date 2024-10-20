from fastapi import APIRouter
from ast import literal_eval as evall
from pydantic import BaseModel

from constants import AppConstants
import requests

from utils.json_object_converter_to_csv import json_object_to_csv_file
from ai_prompts.chat_assistant.ai_bot_assistant_instruction import (
    chat_ai_instructions_2,
 )

aiTestRouter = APIRouter()
from ai_prompts.system_messages.message import systemMessage


class Test(BaseModel):
    model: str
    questions: list[str]


@aiTestRouter.post("/test_chat")
async def chat(query: Test):
    listOfResponses = []
    # test the model and get the response to compare multiple models with givin questions
    for question in query.questions:
         
        apiResponse = requests.post(
            AppConstants.aiChatUrl,
            json={
                "model": query.model,
                "options": {"temprature": 0.1},
                "messages": [
                    {"role": "system", "content": systemMessage},
                    {
                        "role": "assistant",
                        "content": chat_bot_instructions,
                    },
                    {"role": "user", "content": question},
                ],
                "stream": False,
                "format": "json",
            },
        )
        listOfResponses.append(
            {"question": question, "answer": apiResponse.json()["message"]["content"]}
        )
        print(str(len(listOfResponses))+'/50 is finished')
         
    json_object_to_csv_file(
        {
            "message": "success",
            "data": listOfResponses,
        },
        '{query.model}_answers.csv',
    )
    return {
        "message": "success",
        "data": listOfResponses,
    }
    
    


import requests
import uvicorn
from fastapi import FastAPI
from  store.get_products import storeRouter as storeRouter
from ai.chat import aiRouter as aiRouter
from ai.ai_test import aiTestRouter as aiTestRouter
app = FastAPI()

app.include_router( storeRouter, prefix="/store", tags=["store"])
app.include_router( aiRouter, prefix="/ai", tags=["ai"])
app.include_router( aiTestRouter, prefix="/ai_test", tags=["ai"])
if __name__ == "__main__":
    uvicorn.run(app)

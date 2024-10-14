import requests
import uvicorn
from fastapi import FastAPI
from  store.get_products import storeRouter as storeRouter
from ai.chat import aiRouter as aiRouter
app = FastAPI()

app.include_router( storeRouter, prefix="/store", tags=["store"])
app.include_router( aiRouter, prefix="/ai", tags=["ai"])
if __name__ == "__main__":
    uvicorn.run(app)

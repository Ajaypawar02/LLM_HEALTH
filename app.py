import requests
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
from dotenv import load_dotenv
import uvicorn
from typing import Dict
import json
import os
from retry import retry
load_dotenv()
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from HealthcareChatbot import logger
from HealthcareChatbot.pipeline.llm_pipeline import Model, DataBase
from HealthcareChatbot.entity.config_entity import APIPARAMETERS
import warnings
warnings.filterwarnings("ignore")
app = FastAPI(debug = True)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@retry(tries=3, delay=2)
def fetch_answer(api_params):
    db = DataBase()
    model = Model(db)
    answer =  model.run_chain(api_params=api_params)
    return answer

@app.get("/")
def read_root():
    return {"response": "Service is ready to run"}

@app.post("/get_details")
def insight_summary(request: Request, payload : APIPARAMETERS):
    try:
        api_params = json.loads(payload.json())
        answer =  fetch_answer(api_params)

        response_body = {
            'status' : 'success',
            'new_recipe_name' : answer.new_recipe_name,
            'ingredient_substitute' : answer.ingredient_substitute,
            'new_recipe': answer.new_recipe
        }
        response = JSONResponse(status_code = 200, content = response_body)
        return response
    except Exception as e:
        print(str(e))
        logger.error(f"An error occurred: {e}")
        response_body = {"error_message" : str(e) }
        response = JSONResponse(status_code = 400, content = response_body)
        return response
    
if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("HOST"), port=int(os.getenv("PORT_NO")))
    print("Setup Complete")
import random
from typing import List, Dict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from fastapi import APIRouter, Depends, Request

router = APIRouter()

from mcq.mcqService import McqService
from wordle.wordleService import WordleService

from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
import json

wordleService = WordleService()

from pydantic import BaseModel


class UserResponse(BaseModel):
    device_id: str
    word: str
    game: str = "wordle"
    user_guess: List[str]
    correct: bool


# Endpoint to receive user responses and save to MongoDB
@router.post("/wordle/submit-response")
async def submit_responses(user_response: UserResponse):
    response = wordleService.sumbit_response(user_response)
    ret = {"message": "User responses saved successfully", "id": response.get("id")}
    return JSONResponse(content=ret)

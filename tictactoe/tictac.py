import random
from typing import List, Dict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from fastapi import APIRouter, Depends, Request

router = APIRouter()

from mcq.mcqService import McqService
from tictactoe.tictacService import TicTacService

from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
import json

ticService = TicTacService()

from pydantic import BaseModel


class UserResponse(BaseModel):
    device_id: str
    game: str = "tictac"
    result: str#win,loss,draw


# Endpoint to receive user responses and save to MongoDB
@router.post("/tictac/submit-response")
async def submit_responses(user_response: UserResponse):
    response = ticService.sumbit_response(user_response)
    ret = {"message": "User responses saved successfully", "id": response.get("id")}
    return JSONResponse(content=ret)

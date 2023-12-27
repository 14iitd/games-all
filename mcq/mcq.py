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

mcqService = McqService()

from pydantic import BaseModel


class UserResponse(BaseModel):
    device_id: str
    question_id: str
    game:str ="mcq"
    user_select: object
    correct: bool


# Endpoint to receive user responses and save to MongoDB
@router.post("/mcq/submit-response")
async def submit_responses(user_response: UserResponse):
    response = mcqService.sumbit_response(user_response)
    ret = {"message": "User responses saved successfully", "id": response.get("id")}
    return JSONResponse(content=ret)


@router.post("/mcq/create-question", status_code=201)
async def create_question(request: Request, question: Dict):
    headers = request.headers
    device_id = headers.get("device_id")
    answer_index = question.get("answer_index")
    options = question.get("options")
    created_question = {
        "device_id": device_id,
        "question_text": question.get("question"),
        "game": question.get("game"),
        "options": options,
        "correct_answer": options[answer_index],
        "answer_index": answer_index,
        "category": question.get("category"),
        "age": question.get("age"),
        "difficulty": question.get("difficulty"),
        "quiz_name": question.get("quiz"),
        "topic": question.get("topic")
    }
    response = mcqService.create_question(question=created_question)

    ret = {"message": "Question created successfully", "id": response.get("id")}
    return JSONResponse(content=ret)

from typing import List, Dict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from fastapi import APIRouter, Depends, Request

router = APIRouter()

from mcq.questionService import QuestionService

from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
import json

questionService=QuestionService()
# Endpoint to get MCQ questions
@router.get("/get-data")
async def get_question():
    question = questionService.get_random_question()
    return JSONResponse(content=question, status_code=200)

from pydantic import BaseModel
class UserResponse(BaseModel):
    device_id: str
    question_id: str
    user_select: object
    correct: bool
class Question(BaseModel):
    question: str

@router.post("/create-question", status_code=201)
async def create_question(question: Question,request:Request):
    headers = request.headers
    device_id = headers.get("device_id")
    created_question = {
        "device_id":device_id,
        "text": question.question,
        "type":question.type
    }
    response = questionService.create_question(question=created_question)

    ret = {"message": "Question created successfully", "id": response.get("id")}
    return JSONResponse(content=ret)

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
@router.get("/get-question")
async def get_question():
    question = questionService.get_random_question()
    return JSONResponse(content=question, status_code=200)

from pydantic import BaseModel
class UserResponse(BaseModel):
    device_id: str
    question_id: str
    user_select: object
    correct: bool


# Endpoint to receive user responses and save to MongoDB
@router.post("/submit-response")
async def submit_responses(user_response: UserResponse):
    response = questionService.sumbit_response(user_response)
    ret = {"message": "User responses saved successfully", "id": response.get("id")}
    return JSONResponse(content=ret)


class Question(BaseModel):
    question: str
    options: List[str]
    answer_index: int



@router.post("/create-question", status_code=201)
async def create_question(question: Question,request:Request):
    headers = request.headers
    device_id = headers.get("device_id")
    created_question = {
        "device_id":device_id,
        "question_text": question.question,
        "type":"mcq",
        "options": question.options,
        "correct_answer": question.options[question.answer_index],
        "answer_index":question.answer_index
    }
    response = questionService.create_question(question=created_question)

    ret = {"message": "Question created successfully", "id": response.get("id")}
    return JSONResponse(content=ret)

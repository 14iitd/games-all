import random
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

questionService = QuestionService()


# Endpoint to get MCQ questions
@router.get("/get-question")
async def get_question():
    question = questionService.get_random_question()
    color_list=["FAFAFB","FFFFFF","D3C1FA","FFF3F0","B9E5FF","FFF0AF","FFC9E2"]
    question["color"]=random.choice(color_list)
    question["accuracy"]=10
    question["played"]=1221
    return JSONResponse(content=question, status_code=200)

@router.get("/get-question/related/{qid}")
async def get_question():
    question = questionService.get_random_question()
    color_list=["FAFAFB","FFFFFF","D3C1FA","FFF3F0","B9E5FF","FFF0AF","FFC9E2"]
    question["color"]=random.choice(color_list)
    question["accuracy"]=10
    question["played"]=1221
    return JSONResponse(content=question, status_code=200)


from pydantic import BaseModel


class UserResponse(BaseModel):
    device_id: str
    question_id: str
    user_select: object
    correct: bool


# Endpoint to receive user responses and save to MongoDB
@router.post("/mcq/submit-response")
async def submit_responses(user_response: UserResponse):
    response = questionService.sumbit_response(user_response)
    ret = {"message": "User responses saved successfully", "id": response.get("id")}
    return JSONResponse(content=ret)


class Question(BaseModel):
    question: str
    options: List[str]
    answer_index: int
    game: str
    answer_index: int
    category: str
    age: str
    difficulty: str
    quiz_name: str
    topic: str


@router.post("/create-question", status_code=201)
async def create_question(question: Question, request: Request):
    headers = request.headers
    device_id = headers.get("device_id")
    created_question = {
        "device_id": device_id,
        "question_text": question.question,
        "game": question.game,
        "options": question.options,
        "correct_answer": question.options[question.answer_index],
        "answer_index": question.answer_index,
        "category":question.category,
        "age":question.age,
        "difficulty":question.difficulty,
        "quiz_name":question.quiz,
        "topic":question.topic
    }
    response = questionService.create_question(question=created_question)

    ret = {"message": "Question created successfully", "id": response.get("id")}
    return JSONResponse(content=ret)

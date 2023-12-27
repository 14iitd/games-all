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
from tictactoe.tictacService import TicTacService

mcqService = McqService()
wordleService = WordleService()
tictacService  =  TicTacService()
games = [mcqService, wordleService,tictacService]


# Endpoint to get MCQ questions
@router.get("/get-question")
async def get_question(request: Request):
    gameService = random.choice(games)
    question = gameService.get_random_question()
    return JSONResponse(content=question, status_code=200)


@router.get("/get-question/bulk")
async def get_question(request: Request):
    res = []
    for i in range(100):
        gameService = random.choice(games)
        question = gameService.get_random_question()
        res.append(question)
    return JSONResponse(content=res, status_code=200)

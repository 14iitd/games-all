import http
import json
import logging
import asyncio
from typing import Dict
from fastapi import APIRouter, Depends, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


# Dependency to get the MongoDB client
from fastapi import FastAPI, Depends, HTTPException
# from jose import JWTError, jwt
import os
from users.usersService import UserService

user_service = UserService()

router = APIRouter()

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2AuthorizationCodeBearer
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.openapi.models import OAuthFlowAuthorizationCode

@router.get("/api/login")
async def login(request: Request):
    # Simulate fetching user-specific data based on the authenticated user
    headers = request.headers
    # Access specific header values
    device_id = headers.get("device_id")
    user_data = user_service.get_user_by_device_id(device_id)
    if not user_data:
        email_data = {
            "device_id": device_id}
        user_data = user_service.create_user(email_data)
    # import pdb;pdb.set_trace()
    return JSONResponse(content=user_data, status_code=200)

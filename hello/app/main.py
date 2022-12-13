import os
from typing import List, Dict
from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(root_path=os.environ.get('ROOT_PATH', '/'))

class request_hello(BaseModel):
    username : str
    class Config:
        schema_extra = {
            "example": {
                "username": "ehsan"
            }
        }

@app.post('/')
async def say_hello(userinfo: request_hello):
    return {'output': f'Hello {userinfo.username}'}

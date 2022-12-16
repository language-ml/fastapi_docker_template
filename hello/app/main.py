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

PATH = '/models'

@app.post('/')
async def say_hello(userinfo: request_hello):
    with open(f'{PATH}/sample.txt') as f:
        content = f.read()
    return {'file_content': content, 'output': f'Hello {userinfo.username}'}

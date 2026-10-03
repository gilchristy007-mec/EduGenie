from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from services.gemini_service import generate_response

app = FastAPI(title='EduGenie - Demo Mode')
app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')

class UserRequest(BaseModel):
    prompt: str
    mode: str = 'question'

@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name='index.html')

@app.post('/ask')
async def ask(request: UserRequest):
    return {'answer': generate_response(request.prompt, request.mode)}

from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import HTTPException
from app import shortener, storage
import json

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/analytics", response_class=HTMLResponse)
def analytics(request: Request):
    with open("data/urls.json", "r") as f:
        data = json.load(f)

    base_url = str(request.base_url).strip("/")
    
    return templates.TemplateResponse("analytics.html", {
    "request": request,
    "analytics": data, 
    "base_url": base_url
})



import string
import random

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))



@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/shorten", response_class=HTMLResponse)
def shorten(request: Request, url: str = Form(...)):
    data = storage.load_data()
    short_code = generate_short_code()
    short_url = request.url_for("redirect_url", short_code=short_code)
    
    data[short_code] = {
        "long_url": url,  
    }

    storage.save_data(data)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "short_url": short_url
    })


@app.get("/zap/{code}")
def redirect(code: str):
    original = storage.increment_click(code)
    if original:
        return RedirectResponse(original)
    return {"error": "Invalid link"}



@app.get("/{short_code}")
def redirect_url(short_code: str):
    data = storage.load_data()

    if short_code not in data:
        raise HTTPException(status_code=404, detail="URL not found")

    # Handle both string and dict formats
    url_entry = data[short_code]
    if isinstance(url_entry, str):
        long_url = url_entry
    elif isinstance(url_entry, dict):
        long_url = url_entry.get("long_url")
    else:
        raise HTTPException(status_code=500, detail="Invalid data format")

    return RedirectResponse(url=long_url)

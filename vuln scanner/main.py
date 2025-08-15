from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import asyncio
from scanner import scan_urls

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "results": None})

@app.post("/scan", response_class=HTMLResponse)
async def scan(request: Request, urls: str = Form(...)):
    urls_list = [u.strip() for u in urls.split(",") if u.strip()]
    results = await scan_urls(urls_list)
    return templates.TemplateResponse("index.html", {"request": request, "results": results})

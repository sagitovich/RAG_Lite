import json
from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates
from app.core.nlp_pipeline import NLPPipeline
from app.core.search_engine import SearchEngine

templates = Jinja2Templates(directory="app/templates")
router = APIRouter()

with open("data/text.json", "r", encoding="utf-8") as f:
    TEXTS = json.load(f)
nlp_pipeline = NLPPipeline()
search_engine = SearchEngine(TEXTS)


@router.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "results": None, "query": ""})


@router.post("/")
async def handle_search(request: Request, query: str = Form("")):
    if not query.strip():
        return templates.TemplateResponse("index.html", {"request": request, "results": None, "query": ""})
    try:
        results = search_engine.search(query)
        print(f'Запрос: {query}')
        return templates.TemplateResponse("index.html", {"request": request, "results": results, "query": query})
    except Exception as e:
        print(f'Запрос: {query}')
        return templates.TemplateResponse(
            "index.html", {"request": request, "results": [], "query": query, "error": str(e)}
        )

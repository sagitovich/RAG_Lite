from fastapi import FastAPI
from app.api.routes import router

try:
    app = FastAPI()
    app.include_router(router)
except Exception as e:
    print(f'Ошибка точки входа FastAPI: {e}')
    
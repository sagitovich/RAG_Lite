# RAG_Lite #

|-.venv 
|-app/ 
|--__init__.py 
|--main.py                точка входа FastAPI 
|--api/                   модуль для обработки API-запросов 
|---__init__.py 
|---routes.py             маршруты FastAPI 
|--core/ ##                  логика приложения 
|---__init__.py 
|---nlp_pipeline.py       NLP-пайплайн 
|---search_engine.py      логика поиска 
|--templates/             HTML-шаблоны 
|---index.html 
|-config.py 
|-requirements.txt 
|-run.py                  запуск приложения 

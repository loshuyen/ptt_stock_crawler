from fastapi import FastAPI
from utils.crawler import get_articles
from schemas.article import Articles

app = FastAPI()

@app.get('/')
def articles() -> Articles:
    url = 'https://www.ptt.cc/bbs/Stock/index.html'
    articles = get_articles(url, 3)
    return {'data': articles}
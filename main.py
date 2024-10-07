from fastapi import FastAPI
from utils.scheduler import scheduler, update_articles
from models.article import query_articles

app = FastAPI()

update_articles()

try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    print('Scheduler Stopped')

@app.get('/')
def articles():
    articles = query_articles()
    articles_data = []
    for article in articles:
        id, title, date, rating, created_at = article
        articles_data.append({'id': id, 'title': title, 'date': date, 'rating': rating, 'created_at': created_at})
    return {'data': articles_data}
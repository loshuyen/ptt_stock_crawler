from apscheduler.schedulers.background import BackgroundScheduler
from utils.crawler import get_articles
from models.article import insert_article

PTT_STOCK_URL = 'https://www.ptt.cc/bbs/Stock/index.html'
CRAWL_PAGES_COUNT = 5

def update_articles():
    articles = get_articles(PTT_STOCK_URL, CRAWL_PAGES_COUNT)
    insert_article(articles)

scheduler = BackgroundScheduler()

scheduler.add_job(update_articles, 'interval', hours=8)
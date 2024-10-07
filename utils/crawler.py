import requests
from bs4 import BeautifulSoup

def get_articles(url, n):
    next_url = url
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
    result = []
    for _ in range(n):
        response = requests.get(next_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('div', class_='r-ent')
        for article in articles:
            span = article.find('div', class_='nrec').span
            rating = span.text if span is not None else None
            article_link = article.a
            if article_link is not None:
                date = article.find('div', class_='date').text
                result.append({'title': article_link.text, 'rating': rating, 'date': date})
        next_url = 'https://www.ptt.cc' + soup.find('a', string='‹ 上頁').get('href')
    return result
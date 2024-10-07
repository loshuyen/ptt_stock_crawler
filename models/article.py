import sqlite3

db = sqlite3.connect('stock.db')
cursor = db.cursor()
cursor.execute('DROP TABLE IF EXISTS article')
cursor.execute('''
    CREATE TABLE article (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        date TEXT,
        rating TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')
db.commit()
db.close()

def insert_article(articles: list[tuple]):
    try:
        db = sqlite3.connect('stock.db')
        cursor = db.cursor()
        cursor.executemany('''
            INSERT INTO article (title, date, rating) VALUES (?, ?, ?)
        ''', articles)
        db.commit()
    except Exception as e:
        raise e
    finally:
        db.close()

def query_articles() -> list[tuple]:
    try:
        db = sqlite3.connect('stock.db')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM article')
        articles = cursor.fetchall()
        return articles
    except Exception as e:
        raise e
    finally:
        db.close()
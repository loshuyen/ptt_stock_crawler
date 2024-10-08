
FROM python:3.12.4

WORKDIR /ptt_stock_crawler

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["fastapi", "run", "main.py"]
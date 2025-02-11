FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY request.py .
COPY config.ini .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "request.py"]
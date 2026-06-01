FROM python:3.11-slim

WORKDIR /app

#Dépendances en premier → mise en cache Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Code et modèles
COPY app/    ./app/
COPY models/ ./models/

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
EXPOSE 8000

CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]
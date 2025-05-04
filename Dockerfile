FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Install wait-for-it script
RUN apt-get update && apt-get install -y wait-for-it
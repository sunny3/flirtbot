FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
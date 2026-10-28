FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ ./backend/
COPY frontend/ ./frontend/
COPY main.py .

EXPOSE 8000

# Start Flask using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main:app"]
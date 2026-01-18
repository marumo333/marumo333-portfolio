FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# コードはdocker-composeでマウント（同期）するため
# ここでCOPY . . する必要はない。


# ホットリロード(--reload)を有効にして起動
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
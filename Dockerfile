FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=10s --retries=5 --start-period=10s \
  CMD curl -f http://localhost:5000/v1/resultados_nba || exit 1

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

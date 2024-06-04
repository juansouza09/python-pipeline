FROM python:3.9 AS builder

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

FROM python:3.9
WORKDIR /app
COPY --from=builder /app /app
EXPOSE 5000
CMD ["python", "app.py"]

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
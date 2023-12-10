FROM python:3.10.4-alpine3.16

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000


CMD ["sh", "runDocker.sh"]

FROM python:3.10.4-alpine3.16

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN python RitmUS/manage.py makemigrations --no-input
RUN python RitmUS/manage.py migrate --no-input
RUN python RitmUS/manage.py collectstatic --no-input
RUN python RitmUS/populate_data.py

EXPOSE 8000


CMD ["python", "RitmUS/manage.py", "runserver", "0.0.0.0:8000" ]

FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000


CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python populate_data && python manage.py runserver 0.0.0.0:8000"]
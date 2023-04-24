FROM python:3.6

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]

FROM python:3.10-alpine as web

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk update
RUN apk add python3-dev

COPY ./requirements.txt /app/

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD ["gunicorn", "countyroadcanning.wsgi:application", "--bind", "0.0.0.0:8000", "--chdir", "/app/countyroadcanning"]



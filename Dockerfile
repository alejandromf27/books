FROM python:3.9
MAINTAINER alejandromf27@gmail.com

ENV PYTHONUNBUFFERED 1
RUN mkdir /code

WORKDIR /code
COPY . /code/

RUN pip3 install -r requirements.txt

CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "books", "wsgi:application"]
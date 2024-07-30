FROM python:3.9-slim-buster
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p /src
COPY src/ /src/
RUN pip install -e /src
COPY tests/ /tests/

WORKDIR /src
ENV FLASK_APP=tictactoe/entrypoints/app.py FLASK_DEBUG=1 PYTHONUNBUFFERED=1
EXPOSE 5000
CMD flask run --host=0.0.0.0 --port=5000


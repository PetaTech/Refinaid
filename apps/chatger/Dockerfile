FROM python:3.10-slim-buster

COPY ./requirements.txt /app/

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

RUN useradd -m chatter

COPY . /app/

RUN chown -R chatter:chatter /app

USER chatter

CMD ["uvicorn", "Chatter.App.App:app", "--host", "0.0.0.0", "--port", "5002"]

FROM public.ecr.aws/docker/library/python:3.11-slim-buster

COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.8.3 /lambda-adapter /opt/extensions/lambda-adapter
ENV PORT=8080
WORKDIR /var/task

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app:main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
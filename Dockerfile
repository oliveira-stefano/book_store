FROM python:3.7-alpine

WORKDIR /code
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements-dev.txt requirements-dev.txt
COPY requirements.txt requirements.txt
RUN pip install -r requirements-dev.txt
COPY . .
CMD ["flask", "run"]
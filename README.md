# API URLShortener

A simple URL Shortener service.

```bash
# POST request to API
$ curl --header "Content-Type: application/json" --request POST --data '{"url": "https://www.google.com"}' http://localhost:8000/short-code

# response
$ {"url":"http://localhost:8000/goto/8w"}
```

## Prerequisites

1.  [python 3.8 or higher](https://www.python.org/downloads/)

2.  [mongoDB](https://www.mongodb.com/try/download/community)

## Setup Env
Create a `.env` file in the root directory and then add `HOST` and `MONGURI` variables in the `.env`

### Local development setup
```bash
# .env
HOST = localhost
MONGO_URI = mongodb://localhost:27017
```
**Note** : Swap out local values with production values when ready to release to production.

## How to install dependencies
```bash
$ pip install -r requirements.txt
```

## How to run in local mode
```bash
$ uvicorn main:app --reload
```

## How to run in production mode
```bash
$ gunicorn main:app --worker-class uvicorn.workers.UvicornWorker
```

## How to run tests
```bash
$ pytest
```

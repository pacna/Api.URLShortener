# API URLShortener

A simple URL Shortener service

## Prerequisites

1.  [python 3.8 or higher](https://www.python.org/downloads/)

2.  [mongoDB](https://www.mongodb.com/try/download/community)

## Setup Env
Create a `.env` file in the main directory and create a `HOST` and `MONGURI` variable

### Local development setup
```bash
# .env
HOST = localhost
MONGO_URI = mongodb://localhost:27017
```
**Note** : swap out local values with production values when ready to release to production

## How to install dependencies
```bash
$ pip install -r requirements.txt
```

## How to run locally
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

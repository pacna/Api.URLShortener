# API URLShortener

<img alt="Test passing" src="https://github.com/pacna/Api.URLShortener/workflows/Test/badge.svg" />

API URLShortener is a Python-based service that provides a simple way to shorten long URLs, making them easier to share and remember.

## Example

To shorten a URL, send a POST request to the API with the URL as the payload:

```bash
$ curl --header "Content-Type: application/json" --request POST --data '{"url": "https://www.google.com"}' http://localhost:8000/short-code
```

You should receive a response containing the shortened URL:

```bash
$ {"url":"http://localhost:8000/goto/8w"}
```

## Ubuntu Prerequisites

Before running the API URLShortener, make sure you have the following dependencies installed on your system:

1.  [Python](https://www.python.org/downloads/) (python 3.10)

2.  [MongoDB](https://www.mongodb.com/try/download/community)

3.  [Make](https://www.gnu.org/software/make/)

## Configuration

Create a `.env` file in the root directory and add the `HOST` and `MONGO_URI` variables:

### Local development setup

```bash
HOST = localhost
MONGO_URI = mongodb://localhost:27017
```

**Note** : Replace these values with production values when deploying to production.

## Installation

To install the required dependencies, run:

```bash
$ make install
```

If you encounter the error `/usr/bin/python3: No module named pip`, install `python3-pip`:

```bash
$ apt install python3-pip
```

## Running the Service

To run the service locally, use:

```bash
$ make local
```

To run the service in production mode, use:

```bash
$ make run
```

## Running Tests

To run tests, use:

```bash
$ make test
```

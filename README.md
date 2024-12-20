# Boomerang Cash

Cashback system focused to provide gamification for resellers

## Prerequisites

- Python (version 3.12 or higher)
- [PDM](https://pdm-project.org/en/latest/)
- MongoDB

## Setup

The application uses PDM to manage its dependencies. To install all the dependencies:

```sh
pdm install
```
or
```sh
make setup
```

After that, create a `.env` file at the root of the project following the `.env.example`:

```
APP_MONGO_CONN_STR=mongodb+srv://user:password@mongo:port/
APP_SECRET_KEY="my-secret-key"
APP_TOKEN_EXPIRATION_SECONDS=86400
APP_BOTICARIO_API_TOKEN=BOTICARIO_API_KEY
```

## Running

To run the application:

```sh
pdm run python -m adapters.handlers.rest.app
```
or
```sh
make run
```

After that, the project should be available at [http://localhost:8000/](http://localhost:8000/)

## Live documentation

The application contains a live documentation using Swagger UI that can be accessed at [http://localhost:8000/docs](http://localhost:8000/docs)

## Test

To run the tests:

```sh
pdm run pytest
```
or
```sh
make test
```

## Running with docker compose

If you have Docker and docker-compose installed, you can just run the project and database together using

```sh
docker-compose up
```
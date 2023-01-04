# Python Redis PubSub

This Python project aims at creating a [PubSub](https://cloud.google.com/pubsub/docs/overview) REST application.

## Instalation

The project uses [Poetry](https://python-poetry.org/docs/) for dependency management. 

Instalation information can be found on their website, includin guides on how to install the software and related dependencies.

Once Poetry is installed, in each package, you can run `poetry install` to install the required dependencies.

## How it works?

### Redis 

Before using the PubSub methods, you need Redis running on port `6379`. 

This can be easily achieved by using the Docker image for Redis. The `docker-compose.yml` file contains a service for this already.


### Publisher

The publisher package represents the pushing component of the project.

Once poetry and the project dependencies are installed, you can run `uvicorn app:app --host 0.0.0.0 --port 8080` to launch the application.

This will start the `FastApi` application on port `8080`. You can then navigate to 'localhost:8080/docs' to see the Swagger UI.

### Subscriber

Once the publisher is up and running, you can send messages using either the Swagger GUI or REST calls.

Run `python app.py` to start the subscriber. Any messages sent from the publisher will be bounced from the `redis` channel into the subscriber.

### Docker

If you only need the applications running, each package contains a `Dockerfile` recipe that describes the services required. When running `docker-compose up`, the images will be built, redis will be launched and the images will be created and ran.


## Improvements

For any improvements or recommandations, feel free to open a PR.
Thank you!
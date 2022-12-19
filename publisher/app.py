import json
import logging

import redis
from fastapi import FastAPI
from prettyconf import config

from models import *

DEBUG = config("DEBUG", cast=config.boolean, default=False)
CHANNEL = config("CHANNEL", default="test")
REDIS_HOST = config("REDIS_HOST", default="redis")


def publish(message: TimedMessage):
    global r
    try:
        rcvd = r.publish(CHANNEL, json.dumps(message.__dict__))
        if rcvd >0:
            return
    except redis.ConnectionError as e:
        logging.error(e)
        logging.error("Will attempt to retry")
    except Exception as e:
        logging.error(e)
        logging.error("Other exception")


app = FastAPI()
r = redis.Redis(host=REDIS_HOST)


@app.get("/ping")
async def ping_root():
    return "pong"


@app.post("/messaging")
async def send_message(
    message: Message
    ):
    success = False
    if message is not None:
        stamped_message = TimedMessage.from_orm(message)
        publish(stamped_message)
        success = True
    else:
        logging.info(f'Invalid mesage')
    return {"status": "send" if success else "failed"}

from typing import Optional
import redis
from prettyconf import config
from fastapi import FastAPI
import logging
import json
from pydantic import BaseModel

DEBUG = config("DEBUG", cast=config.boolean, default=False)
CHANNEL = config("CHANNEL", default="test")
REDIS_HOST = config("REDIS_HOST", default="redis")


class Message(BaseModel):
    recipient: str
    message: str

def publish(message: Message):
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
async def root():
    return "pong"


@app.post("/messaging")
async def send_message(
    message: Message
    ):
    success = False
    if message is not None:
        publish(message)
        success = True
    else:
        logging.info(f'Invalid mesage')
    return {"status": "send" if success else "failed"}

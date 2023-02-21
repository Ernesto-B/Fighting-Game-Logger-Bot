import pymongo as pm
import json
 
with open("config.json") as f:
    config = json.load(f)
    username = config["db_username"]
    password = config["db_password"]
    prefix = config["prefix"]

async def profile (user, message, channel) -> None:
    ...
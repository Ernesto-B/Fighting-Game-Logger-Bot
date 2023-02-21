import pymongo as pm
import json
import db_user_template

with open("config.json") as f:
    config = json.load(f)
    username = config["db_username"]
    password = config["db_password"]
    prefix = config["prefix"]


client = pm.MongoClient(f"mongodb+srv://{username}:{password}@cluster0.7fai5k7.mongodb.net/?retryWrites=true&w=majority")
db = client.test

user_set_info = db.user_set_info

example_data = [{
    "username": "Naz",
    "games": {
        "tekken": {
            "games_played": 0,
            "wins": 0,
            "losses": 0,
            "win_rate": "0.00%",
        },
        "smash": {
            "games_played": 0,
            "wins": 0,
            "losses": 0,
            "win_rate": "0.00%",
        },
        "guilty_gear": {
            "games_played": 0,
            "wins": 0,
            "losses": 0,
            "win_rate": "0.00%",
        },
    }
}]

# user_set_info.insert_many(example_data)


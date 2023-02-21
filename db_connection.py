import pymongo as pm
import json
import db_user_template
import commands.new_user

with open("config.json") as f:
    config = json.load(f)
    username = config["db_username"]
    password = config["db_password"]

client = pm.MongoClient(f"mongodb+srv://{username}:{password}@cluster0.7fai5k7.mongodb.net/?retryWrites=true&w=majority")
db = client.userData

def add_user_to_database(user):
    user_set_info = db.user

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
        },
        "total_games_played": 0,
    }]

    user_set_info.insert_many(example_data)
    print("Successfully added another user")
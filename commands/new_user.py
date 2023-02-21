import pymongo as pm
import json
import db_user_template

with open("config.json") as f:
    config = json.load(f)
    username = config["db_username"]
    password = config["db_password"]
    prefix = config["prefix"]

client = pm.MongoClient(f"mongodb+srv://{username}:{password}@cluster0.7fai5k7.mongodb.net/?retryWrites=true&w=majority")
db = client.userData

async def new_user_cmd(user:str, message:str, channel:str) -> None:
    db_entries = list(db.user.find())
    for i in db_entries:
        if user in i["username"]:
            await message.channel.send(f"You already have a profile! Type `{prefix}profile` to view it.")
            return

    print(db_entries)
    username = user
    user = db_user_template.User(user)
    user.set_games([db_user_template.User.Game('tekken'), db_user_template.User.Game('smash'), db_user_template.User.Game('guilty gear')])
    # getting information from the class
    tekken_games_played = user.games[0].get_games_played()
    tekken_wins = user.games[0].get_wins()
    tekken_losses = user.games[0].get_losses()
    tekken_win_rate = user.games[0].get_win_rate()
    smash_games_played = user.games[1].get_games_played()
    smash_wins = user.games[1].get_wins()
    smash_losses = user.games[1].get_losses()
    smash_win_rate = user.games[1].get_win_rate()
    guilty_gear_games_played = user.games[2].get_games_played()
    guilty_gear_wins = user.games[2].get_wins()
    guilty_gear_losses = user.games[2].get_losses()
    guilty_gear_win_rate = user.games[2].get_win_rate()
    total_games_played = user.get_total_games_played()
        
    user_set_info = db.user

    user_data = [{
        "username": username,
        "games": {
            "tekken": {
                "games_played": tekken_games_played,
                "wins": tekken_wins,
                "losses": tekken_losses,
                "win_rate": tekken_win_rate,
            },
            "smash": {
                "games_played": smash_games_played,
                "wins": smash_wins,
                "losses": smash_losses,
                "win_rate": smash_win_rate,
            },
            "guilty_gear": {
                "games_played": guilty_gear_games_played,
                "wins": guilty_gear_wins,
                "losses": guilty_gear_losses,
                "win_rate": guilty_gear_win_rate,
            },
        },
        "total_games_played": total_games_played,
    }]

    user_set_info.insert_many(user_data)

    print("Successfully added another user")

    await message.channel.send(f"You have been added to the database! Type `{prefix}profile` to view your profile or `{prefix}edit` to edit it.")
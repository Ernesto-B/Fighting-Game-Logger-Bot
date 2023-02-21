import discord
import json
import commands.help
import commands.new_user

def main():
    with open("config.json") as f:
        config = json.load(f)
        prefix = config["prefix"]
        token = config["discord_token"]

    def run_bot():
        intents = discord.Intents.default()
        intents.message_content = True
        client = discord.Client(intents=intents)

        @client.event
        async def on_ready():
            print("Bot is ready\n")

        @client.event
        async def on_message(message: str) -> any:
            user_message = str(message.content)
            user = str(message.author)
            channel = str(message.channel)
            user_roles = message.author.roles
            print(f"{user} sent a message in {channel}: {user_message}\n")
            print(f"{user} has the following roles: {user_roles}\n")

            if user == client.user:
                return

            if user_message.startswith(f"{prefix}help"):
                await commands.help.help_cmd(user, message, channel)

            if user_message.startswith(f"{prefix}new_user"):
                games = []
                if "Tekken" or "tekken" in user_roles:
                    games.append("tekken")
                if "GGST" or "Ggst" or "ggst" or "Guilty Gear" or "guilty gear" in user_roles:
                    games.append("ggst")
                if "Smash" or "smash" in user_roles:
                    games.append("smash")
                
                await commands.new_user.new_user_cmd(user, message, channel)

        client.run(token)
    run_bot()
    

if __name__ == "__main__":
    main()
import discord
import json
import commands.help
import db_connection

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

            if user == client.user:
                return

            if user_message.startswith(f"{prefix}help"):
                await commands.help.help_cmd(user, message, channel)


            if user_message.startswith(f"{prefix}hello"):
                await message.channel.send("Hello!")

        client.run(token)
    run_bot()
    

if __name__ == "__main__":
    main()
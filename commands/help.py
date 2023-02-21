import discord

async def help_cmd(user, message, channel):
    await message.channel.send(f"Hello @{user}! Here is a list of commands:")
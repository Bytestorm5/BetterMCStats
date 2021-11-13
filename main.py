# Other things
import discord
import time
import asyncio

# Our things
from mongo import *
from graph import *

TOKEN = "OTA5MTM2OTAzMzQzODM3MjA0.YY_5uA.08zxzKNAu-mN98XesrU8pP_KwJk"


async def periodic():
    while True:
        for guild in client.guilds:
            info = getServer(guild.id)
            channel = client.get_channel(info["channel_id"])
            embed = discord.Embed(title=time.time())
            if (info["message_id"] == ""):
                message = await channel.send("Test")
                info["message_id"] = message.id
                addServer(info)
            else:
                message = await client.get_message(info["message_id"])
            message.edit(embed=embed)

        await asyncio.sleep(60)


def stop():
    global task
    task.cancel()


loop = asyncio.get_event_loop()


class MyClient(discord.Client):
    async def on_ready(self):
        global task

        print('Logged on as {0}!'.format(self.user))
        activity = discord.Game(name="Minecraft", type=3)
        await client.change_presence(status=discord.Status.online, activity=activity)
        task = loop.create_task(periodic())

    async def on_message(self, message):
        msg = message.content
        if msg.startswith("!config"):
            params = msg.split(" ")
            if len(params) != 4:
                await message.channel.send("!config <server_ip> <server_port> <output_channel_id>")
            else:
                addServer({"id": message.guild.id, "ip": params[1], "port": params[2], "channel_id": params[3],
                           "message_id": ""})
                await message.channel.send("Added server successfully.")

        if msg.startswith("!getServer"):
            for guild in client.guilds:
                await message.channel.send(getServer(guild.id))

        # await client.http.delete_message(channel_id, server_id)


def update_stats():
    for guild in client.guilds:
        print(getServer(guild.id))


client = MyClient()
client.run(TOKEN)

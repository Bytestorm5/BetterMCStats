# Other things
import discord
import time
import asyncio
import datetime

# Our things
from mongo import *
from graph import *

TOKEN = "OTA5MTM2OTAzMzQzODM3MjA0.YY_5uA.08zxzKNAu-mN98XesrU8pP_KwJk"


async def update_stats():
    for guild in client.guilds:
        info = getServer(guild.id)
        if info:
            channel = client.get_channel(int(info["channel_id"]))

            # testing
            # poll(guild.id)
            raw = {'description': {'extra': [{'color': 'gold', 'text': 'Welcome to the'}, {'text': '\n'},
                                             {'bold': True, 'obfuscated': True, 'color': 'blue', 'text': 'd'},
                                             {'bold': True, 'color': 'red', 'text': 'NJIT SMP!'},
                                             {'bold': True, 'obfuscated': True, 'color': 'blue', 'text': 'd'}],
                                   'text': ''}, 'players': {'max': 32, 'online': 2, 'sample': [
                {'id': '67788035-7990-42d8-89e5-1a2dd46f2140', 'name': 'googleflef'},
                {'id': '375e0f37-b516-47f1-8772-a62752debb62', 'name': 'R2bEEaton'}]},
                   'version': {'name': 'Purpur 1.17.1', 'protocol': 756},
                   'favicon': 'data:image/png;base64,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'}

            embed = discord.Embed(title="%s Stats" % guild.name, description="MOTD:\n%s" % "TESTINGMOTD")
            embed.add_field(name="Players (%s / %s)" % (raw["players"]["online"], raw["players"]["max"]), value="```%s```" % ([y["name"] + "\n" for y in raw["players"]["sample"]]))
            embed.timestamp(datetime.datetime.now())
            embed.set_image(url=raw["favicon"])
            embed.set_thumbnail(url=raw["favicon"])

            if (info["message_id"] == ""):
                message = await channel.send("Waiting for update...")
                info["message_id"] = message.id
                addServer(info)
            else:
                try:
                    message = await channel.fetch_message(int(info["message_id"]))
                except:
                    message = await channel.send("Waiting for update...")
                    info["message_id"] = message.id
                    addServer(info)

            await message.edit(conent="", embed=embed)


async def periodic():
    while True:
        await update_stats()
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

        if msg.startswith("!updatenow"):
            await update_stats()

        # await client.http.delete_message(channel_id, server_id)


client = MyClient()
client.run(TOKEN)

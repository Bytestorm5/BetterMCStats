# Other things
import discord
import asyncio
import datetime

# Our things
from mongo import *
from graph import *

TOKEN = "OTA5MTM2OTAzMzQzODM3MjA0.YY_5uA.08zxzKNAu-mN98XesrU8pP_KwJk"


def createEmbed(guild, raw, days):
    embed = discord.Embed(title="%s Stats" % guild.name, description="MOTD:\n%s" % "TESTINGMOTD")
    print("\n".join([y["name"] for y in raw["players"]["sample"]]))
    embed.add_field(name="Players (%s / %s)" % (raw["players"]["online"], raw["players"]["max"]),
                    value="```\n%s```" % ("\n".join([y["name"] for y in raw["players"]["sample"]])), inline=False)
    embed.timestamp = datetime.datetime.now()
    embed.add_field(name="🕠", value='Last updated: <t:%s:f>' % int(time.time()), inline=False)
    embed.set_image(url="attachment://%s" % createGraph(getRange(time.time(), time.time() - (86400 * days))))
    # embed.set_thumbnail(url=raw["favicon"])
    return embed


async def update_stats():
    for guild in client.guilds:
        info = getServer(guild.id)
        if info:
            channel = client.get_channel(int(info["channel_id"]))

            # testing
            # poll(guild.id)
            raw = poll(guild.id)

            embed = createEmbed(guild, raw, 1)

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
        await asyncio.sleep(5)


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
            if len(params) != 4 or type(params[2]) != "int" or type(params[3]) != "int":
                await message.channel.send("!config <server_ip> <server_port> <output_channel_id>")
            else:
                addServer({"id": message.guild.id, "ip": params[1], "port": params[2], "channel_id": params[3],
                           "message_id": ""})
                await message.channel.send("Added server successfully.")

        if msg.startswith("!getServer"):
            for guild in client.guilds:
                await message.channel.send(getServer(guild.id))

        if msg.startswith("!statsfrom"):
            params = msg.split(" ")
            if len(params) != 2 or type(params[1]) != "int":
                await message.channel.send("!statsfrom <number_of_days_ago")
            else:
                await message.channel.send(embed=createEmbed(message.guild, poll(message.guild.id), params[1]))

        if msg.startswith("!updatenow"):
            await update_stats()


client = MyClient()
client.run(TOKEN)

import discord
from mongo import *
TOKEN = "OTA5MTM2OTAzMzQzODM3MjA0.YY_5uA.08zxzKNAu-mN98XesrU8pP_KwJk"

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        activity = discord.Game(name="Minecraft", type=3)
        await client.change_presence(status=discord.Status.online, activity=activity)

    async def on_message(self, message):
        msg = message.content
        if msg.startswith("!config"):
            params = msg.split(" ")
            if len(params) != 4:
                await message.channel.send("!config <server_ip> <server_port> <output_channel_id>")
            else:
                addServer({"id": message.guild.id, "ip": params[1], "port": params[2], "channel_id": params[3], "message_id": ""})
                await message.channel.send("Added server successfully.")


        if msg.startsith("!getServer"):
            for guild in client.guilds:
                await message.channel.send(getServer(guild.id))

        # await client.http.delete_message(channel_id, server_id)

client = MyClient()
client.run(TOKEN)
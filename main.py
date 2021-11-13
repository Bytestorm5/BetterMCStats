import discord
import mongo
TOKEN = "OTA5MTM2OTAzMzQzODM3MjA0.YY_5uA.08zxzKNAu-mN98XesrU8pP_KwJk"

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        activity = discord.Game(name="Minecraft", type=3)
        await client.change_presence(status=discord.Status.online, activity=activity)

    async def on_message(self, message):
        msg = message.content
        if msg.startswith("!config"):
            if len(msg.split(" ")) != 4:
                await message.channel.send("!config <server_ip> <server_port> <output_channel_id>")

            else:
                print(message.guild.id)

        print(y.name.lower() for y in message.author.roles)
        # if (msg == "!config" and message.author == )


client = MyClient()
client.run(TOKEN)
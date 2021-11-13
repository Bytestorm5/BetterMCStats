from pymongo import MongoClient
from mcstatus import MinecraftServer
import time

client = MongoClient()
db = client.get_database("BetterMCStats")
data = db.get_collection("data")
servers = db.get_collection("servers")

def poll(guild):
    server = MinecraftServer.lookup(guild.ip + ':' + guild.port)
    # 'status' is supported by all Minecraft servers that are version 1.7 or higher.
    status = server.status()
    print("The server has {0} players and replied in {1} ms".format(status.players.online, status.latency))
    data.insert_one({'server':guild.id,'time': int(time.time()),'players':status.players.online})

def getRange(guild_id, upper, lower):
    results = data.find({'server':guild_id,time: {'$gt':lower,'$lt':upper}})
    output = []
    for result in results:
        output.append({result.time: result.players})
    return output

def getPoint(guild_id, timestamp):
    result = data.find_one({'server':guild_id, 'time': timestamp})
    return {result.time: result.players}
def getServer(guild_id):
    return servers.find_one({'id': guild_id})

def addServer(guild):
    if data.find_one({'id':guild.id}) == None:
        servers.add(guild)
    else:
        servers.find_one_and_replace({'id':guild.id}, guild)
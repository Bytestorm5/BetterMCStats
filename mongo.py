import json

from bson.int64 import *
import mcstatus
import pymongo
from pymongo import MongoClient
from mcstatus import MinecraftServer
import time

client = MongoClient()
db = client.get_database("BetterMCStats")
data = db.get_collection("data")
servers = db.get_collection("servers")

def formatSample(sample):
    print(sample)
    output = []
    for player in sample:
        dict = {
            "id": str(player.id),
            "name": str(player.name)
        }
        output.append(dict)
    return output

def poll(guild_id):
    guild = getServer(guild_id)
    server = MinecraftServer.lookup(guild["ip"]) #+ ':' + guild["port"])
    # 'status' is supported by all Minecraft servers that are version 1.7 or higher.
    status = server.status()
    print("The server has {0} players and replied in {1} ms".format(status.players.online, status.latency))
    data.insert_one({'guild':guild["id"],'time': int(time.time()),'players':formatSample(status.players.sample)})
    return status.raw

def getRange(guild_id, upper, lower):
    results = data.find({'guild':guild_id,'time': {'$gte':int(lower),'$lte':int(upper)}})
    output = []
    if results == None or results.count() == 0:
        return []
    for r in results:
        output.append([r['time'], r['players']])
    # while results.alive:
    #     r = results.next()
    #     output.append([r.time, r.players])
    return output

def getPoint(guild_id, timestamp):
    result = data.find_one({'guild':guild_id, 'time': timestamp})
    return {result.time: result.players}
def getServer(guild_id):
    return servers.find_one({'id': guild_id})

def addServer(guild):
    #d1 = list(servers.find({}))
    #d = servers.find_one({"id": guild["id"]})
    if servers.find_one({"id": guild["id"]}) == None:
        servers.insert_one(guild)
    else:
        servers.find_one_and_replace({'id':guild["id"]}, guild)
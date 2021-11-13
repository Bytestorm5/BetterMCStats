from pymongo import MongoClient
from mcstatus import MinecraftServer
import time

client = MongoClient()
db = client.get_database("BetterMCStats")
col = db.get_collection("data")

def poll():
    server = MinecraftServer.lookup("njit.spea.cc")
    # 'status' is supported by all Minecraft servers that are version 1.7 or higher.
    status = server.status()
    print("The server has {0} players and replied in {1} ms".format(status.players.online, status.latency))
    col.insert_one({'time': int(time.time()),'players':status.players.online})

def getRange(upper, lower):
    col.find({time: {'$gt'}})
#output = {time, player count}

#id should be Int64, brand should be String
def increment(id, brand):
    r = col.find_one({"id": id})

    if r == None:
        col.insert_one({
            "id": id,
            brand : 1
        })
    elif col.find_one({"id": id, brand: {'$exists': True}}) == None:
        col.find_one_and_update(
            {"id": id},
            {"$set": {brand: 1}}
        )
    else:
        col.find_one_and_update(
            {"id": id},
            {"$inc": {brand: 1}}
        )
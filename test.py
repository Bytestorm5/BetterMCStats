import json

from mcstatus import MinecraftServer


server = MinecraftServer.lookup("njit.spea.cc")

# 'status' is supported by all Minecraft servers that are version 1.7 or higher.
status = server.status()

print("The server has {0} players and replied in {1} ms".format(status.players.sample, status.latency))





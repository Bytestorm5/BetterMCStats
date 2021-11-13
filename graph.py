import numpy as np
import matplotlib.pyplot as plt

#convert unix time to default time --> using time


#Player data --> dictionary {time:player amount}
def createGraph(playerData):
    startTime = list(playerData.keys())[0]
    endTime = list(playerData.keys())[-1]
    timeStamp = []
    playerCount = []
    for time in playerData:
        timeStamp.append(time)
        playerCount.append(playerData.value())

    plt.ylabel('Player Count')
    plt.xlabel('Time')
    mainPlot = plt.plot(timeStamp,playerCount)

    plt.show()
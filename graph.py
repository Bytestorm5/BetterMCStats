import numpy as np
import matplotlib.pyplot as plt

#convert unix time to default time --> using time


#time start
#Player data --> dictionary {time:player amount}
def createGraph(timeStart, timeEnd, playerData):
    playerCount = []
    for value in playerData.values():
        playerCount.append(value)
    mainPlot = plt.plot()
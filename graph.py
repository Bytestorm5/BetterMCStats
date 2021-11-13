import numpy as np
import matplotlib.pyplot as plt

#convert unix time to default time --> using time


#Player data --> dictionary {time:player amount}
def createGraph(playerData):
    #startTime = list(playerData.keys())[0]
    #endTime = list(playerData.keys())[-1]
    timeStamp = []
    playerCount = []
    for time in playerData:
        timeStamp.append(time)
        playerCount.append(playerData[time])

    #plt.plot()
    ax = plt.axes()
    ax.plot(timeStamp,playerCount,color='orange')

    ax.set_facecolor('w')
    ax.spines['bottom'].set_color('red')
    ax.spines['left'].set_color('red')


    plt.style.use('seaborn')
    plt.ylabel('Player Count',color='red')
    plt.xlabel('Time',color='red')
    plt.tick_params(axis='x',colors='red')
    plt.tick_params(axis='y',colors='red')

    plt.savefig('stats.png', transparent=True,orientation='portrait',pad_inches=0.1, edgecolor='g')

    plt.show()

#lol = {1:5, 2:6, 3:6, 4:2}
#createGraph(lol)
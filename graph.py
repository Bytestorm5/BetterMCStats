import matplotlib.pyplot as plt

#convert unix time to default time --> using time


#Player data --> dictionary {time:player amount}
import numpy as np


def createGraph(playerData):
    timeStamp = []
    playerCount = []
    max_count = 0
    for p in playerData:
        timeStamp.append(p[0])
        playerCount.append(len(p[1]))
        if len(p[1]) > max_count:
            max_count = len(p[1])

    yinterval = 1
    if max_count > 16:
        yinterval = 2

    fig = plt.figure()
    fig.set_facecolor('black')
    fig.patch.set_alpha(0.1)

    ax = plt.axes()
    ax.spines['bottom'].set_color('#781919')
    ax.spines['left'].set_color('#781919')
    ax.spines['top'].set_color('#781919')
    ax.spines['right'].set_color('#781919')
    ax.set_facecolor('black')
    ax.patch.set_alpha(.2)

    plt.style.use('seaborn-darkgrid')
    plt.ylabel('Player Count',color='maroon')
    plt.xlabel('Time',color='maroon')
    plt.tick_params(axis='x',colors='#c41b1b',grid_alpha=0.25)
    plt.tick_params(axis='y',colors='#c41b1b', grid_alpha=0.5)
    #plt.rcParams.update({'font.size':10})

    fig2, ax2 = plt.subplots()
    ax2.yaxis.set_ticks(np.arange(0, max_count, yinterval))
    ax.yaxis.set_ticks(np.arange(0, max_count, yinterval))

    plt.plot(timeStamp,playerCount,color='#bd6f11')
    plt.savefig('stats.png',orientation='portrait',pad_inches=0.1)
    return 'stats.png'
    #plt.show()

#lol = {1:5, 2:6, 3:6, 4:2}
#createGraph(lol)

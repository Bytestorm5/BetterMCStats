import datetime
import random

import matplotlib.pyplot as plt

#convert unix time to default time --> using time


#Player data --> dictionary {time:player amount}
import numpy as np

def createLineGraph(playerData):
    timeStamp = []
    playerCount = []
    max_count = 0
    for p in playerData:
        timeStamp.append(p[0])
        playerCount.append(len(p[1]))
        if len(p[1]) > max_count:
            max_count = len(p[1])

    yinterval = 1
    if max_count > 15:
        yinterval = 2

    fig, ax = plt.subplots()

    #fig = plt.figure()
    fig.set_facecolor('black')
    fig.patch.set_alpha(0.1)

    plt.style.use('seaborn-darkgrid')
    plt.ylabel('Player Count',color='maroon')
    plt.xlabel('Time',color='maroon')
    plt.tick_params(axis='x',colors='#c41b1b',grid_alpha=0.25)
    plt.tick_params(axis='y',colors='#c41b1b', grid_alpha=0.5)
    #plt.rcParams.update({'font.size':10})

    #ax = plt.axes()
    ax.spines['bottom'].set_color('#781919')
    ax.spines['left'].set_color('#781919')
    ax.spines['top'].set_color('#781919')
    ax.spines['right'].set_color('#781919')
    ax.set_facecolor('black')
    ax.patch.set_alpha(.2)
    ticks = np.arange(0, max_count+1, yinterval)
    ax.set_yticks(ticks)
    ax.set_yticklabels(ticks)

    # fig2, ax2 = plt.subplots()
    # ax2.set_facecolor('black')
    # ax2.yaxis.set_ticks(np.arange(0, max_count, yinterval+1))
    # ax.yaxis.set_ticks(np.arange(0, max_count, yinterval+1))

    plt.plot(timeStamp,playerCount,color='#bd6f11')
    name = str(random.randint(1, 99999)) + 'stats.png'
    plt.savefig(name, orientation='portrait',pad_inches=0.1)
    return name
    #plt.show()
def createBarGraph(playerData):
    sums = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    labels = ["12AM", "1AM", "2AM", "3AM", "4AM", "5AM", "6AM", "7AM", "8AM", "9AM", "10AM", "11AM",
              "12PM", "1PM", "2PM", "3PM", "4PM", "5PM", "6PM", "7PM", "8PM", "9PM", "10PM", "11PM"]
    for p in playerData:
        t = int(datetime.datetime.utcfromtimestamp(p[0]).hour)
        sums[t].append(len(p[1]))
    for i in range(0, 24):
        if (len(sums[i]) == 0):
            sums[i] = 0
        else:
            sums[i] = sum(sums[i]) / len(sums[i])
    fig, ax = plt.subplots()

    ax.bar(labels, sums)
    #bp = box_plot(sums, "white", "gray")

    fig.set_facecolor('black')
    fig.patch.set_alpha(0.1)

    plt.style.use('seaborn-darkgrid')
    plt.ylabel('Average Players', color='maroon')
    plt.xlabel('Hour', color='maroon')
    plt.tick_params(axis='x', colors='#c41b1b', grid_alpha=0)
    plt.tick_params(axis='y', colors='#c41b1b', grid_alpha=0.25)
    plt.xticks(rotation = 90)

    ax.spines['bottom'].set_color('#781919')
    ax.spines['left'].set_color('#781919')
    ax.spines['top'].set_color('#781919')
    ax.spines['right'].set_color('#781919')
    ax.set_facecolor('black')
    ax.patch.set_alpha(.2)

    #plt.plot(timeStamp, playerCount, color='#bd6f11')
    name = str(random.randint(1, 99999)) + 'stats.png'
    plt.savefig(name, orientation='portrait', pad_inches=0.1)
    return name

    #plt.show()

#lol = {1:5, 2:6, 3:6, 4:2}
#createGraph(lol)

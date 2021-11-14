import matplotlib.pyplot as plt

#convert unix time to default time --> using time


#Player data --> dictionary {time:player amount}
def createGraph(playerData):
    timeStamp = []
    playerCount = []
    for p in playerData:
        timeStamp.append(p[0])
        playerCount.append(len(p[1]))

    # fig = plt.figure()
    # fig.set_facecolor('black')
    # fig.patch.set_alpha(0.1)

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
    plt.tick_params(axis='x',colors='#c41b1b')
    plt.tick_params(axis='y',colors='#c41b1b')
    plt.rcParams.update({'font.size':20})

    plt.plot(timeStamp,playerCount,color='#bd6f11')
    plt.savefig('stats.png',orientation='portrait',pad_inches=0.1)
    return 'stats.png'
    #plt.show()

#lol = {1:5, 2:6, 3:6, 4:2}
#createGraph(lol)

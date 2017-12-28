from random import randint
from random import sample


def genRoute(width, length, number):
    route = []
    dest = sample(range(1, width * length), number)

    for i in range(0, length):
        save = []
        for j in range(0, width):
            save.append('*')
        route.append(save)

    for k in dest:
        for i in range(0, length):
            for j in range(0, width):
                if width * i + (j + 1) == k:
                    route[i][j] = 'G'

    return route


def outputMap(data):
    for i in data:
        print(i)


def checkDest(data):
    dists = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'G':
                dist = []
                dist.append(i)
                dist.append(j)
                dists.append(dist)
    return dists


def calcDist(start, goal):
    sx = start[1]
    sy = start[0]
    gx = goal[1]
    gy = goal[0]

    distance = abs(gx - sx) + abs(gy - sy)

    return distance


if __name__ == '__main__':
    data = genRoute(4, 5, 5)
    outputMap(data)
    cities = checkDest(data)

    sumDist = 0
    sumDist += calcDist([0, 0], cities[0])
    for i in range(0, len(cities) - 1):
        sumDist += calcDist(cities[i], cities[i + 1])

    print(cities[-1])
    sumDist += calcDist(cities[-1], [0,0])

    print(sumDist)

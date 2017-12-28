import genomPara as gp
from samePartChange import samePartChange
import genRoute as gr
import random as rand


def genomCreate(number):
    data = rand.sample(range(0, number), number)
    return gp.genom(data, 0)


def evalGenom(genom, cities):
    start = [0, 0]
    sumDist = 0
    data = genom.getData()

    sumDist += gr.calcDist(start, cities[data[0]])
    for i in range(0, len(data) - 1):
        sumDist += gr.calcDist(cities[data[i]], cities[data[i + 1]])
    sumDist += gr.calcDist(cities[data[-1]], start)

    return sumDist


def genomSelect(genomPop, maxChange):
    sortGenom = sorted(genomPop, reverse=False, key=lambda u: u.evaluation)
    result = [sortGenom.pop(0) for i in range(maxChange)]
    return result


def genomCross(genom1, genom2, length):
    return samePartChange(genom1, genom2, length)


def nextGenCreate(recentGenom, childGenom, eliteGenom):
    nextGenGenoms = []
    nextGenGenoms = sorted(
        recentGenom, reverse=True, key=lambda u: u.evaluation)
    del nextGenGenoms[0:len(eliteGenom) + len(childGenom)]
    nextGenGenoms.extend(eliteGenom)
    nextGenGenoms.extend(childGenom)

    return nextGenGenoms


def mutation(genoms, perMutation_I, perMutation_G):
    mutations = []
    for i in genoms:
        if perMutation_I > (float)(rand.randint(0, 100) / 100):
            mutationGenom = i.getData()
            for j in range(0, len(mutationGenom)):
                if perMutation_G > (float)(rand.randint(0, 100) / 100):
                    change = rand.sample(range(0, len(mutationGenom)), 1)
                    while j == change[0]:
                        change = rand.sample(range(0, len(mutationGenom)), 1)

                    mutationGenom[j], mutationGenom[change[0]] = mutationGenom[change[0]], mutationGenom[j]
            i.setData(mutationGenom)
        mutations.append(i)

    return mutations


def main(genomLength, width, length, population, maxChange, perMutation_G, perMutation_I,
         roopCount):
    currentGroup = []
    data = gr.genRoute(width, length, genomLength)
    cities = gr.checkDest(data)
    for i in range(population):
        currentGroup.append(genomCreate(genomLength))

    for count_ in range(1, roopCount + 1):
        nextGroup = []
        for i in range(population):
            evalResult = evalGenom(currentGroup[i], cities)
            currentGroup[i].setEval(evalResult)

        eliteGroup = genomSelect(currentGroup, maxChange)
        childGenom = []

        for i in range(0, maxChange):
            childGenom.extend(
                genomCross(eliteGroup[i - 1], eliteGroup[i], genomLength))

        nextGroup = nextGenCreate(currentGroup, childGenom, eliteGroup)
        nextGroup = mutation(nextGroup, perMutation_I, perMutation_G)

        fits = [i.getEval() for i in currentGroup]

        Min = min(fits)
        Max = max(fits)
        Ave = sum(fits) / (int)(len(fits))

        print("第", count_, "世代の結果\n")
        print("Min:", Min, "\n")
        print("Max:", Max, "\n")
        print("Ave:", Ave, "\n")
        currentGroup = nextGroup

    print("最優秀個体:")
    print(eliteGroup[0].getData())
    gr.outputMap(data)


if __name__ == '__main__':
    main(10, 5, 5, 100, 20, 0.001, 0.001, 10000)

from SalesMan import genomPara as gp
from SalesMan import samePartChange as spc
from SalesMan import genRoute as gr
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
    return spc.samePartChange(genom1, genom2, length)


def nextGenCreate(recentGenom, childGenom, eliteGenom):
    nextGenGenoms = []
    nextGenGenoms = sorted(
        recentGenom, reverse=True, key=lambda u: u.evaluation)
    del nextGenGenoms[0:len(eliteGenom) + len(childGenom)]
    nextGenGenoms.extend(eliteGenom)
    nextGenGenoms.extend(childGenom)

    return nextGenGenoms


def mutation(genoms, perMutation_I, perMutation_G, number):
    mutations = []
    for i in genoms:
        if perMutation_I > (float)(rand.randint(0, 100) / 100):
            mutationGenom = i.getData()
            for j in range(0, len(mutationGenom)):
                if perMutation_G > (float)(rand.randint(0, 100) / 100):
                    change = rand.choice(range(0, number))
                    mutationGenom[j], mutationGenom[change] = mutationGenom[change], mutationGenom[j]
            i.setData(mutationGenom)
        mutations.append(i)

    return mutations


def main(genomLength, width, length, population, maxChange, perMutation_G, perMutation_I,
         roopCount):
    currentGroup = []
    best_data = []
    x = []
    y = []
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
        nextGroup = mutation(nextGroup, perMutation_I, perMutation_G, genomLength)

        if count_ is 1:
            best_data.append(eliteGroup[0].getData())
            best_data.append(eliteGroup[1].getEval())

        if best_data[1] > eliteGroup[0].getEval():
            best_data[0] = eliteGroup[0].getData()
            best_data[1] = eliteGroup[0].getEval()

        fits = [i.getEval() for i in currentGroup]

        Min = min(fits)
        Max = max(fits)
        Ave = sum(fits) / (int)(len(fits))

        print("第", count_, "世代の結果\n")
        print("Min:", Min, "\n")
        print("Max:", Max, "\n")
        print("Ave:", Ave, "\n")

        x.append(count_)
        y.append(eliteGroup[0].evaluation)

        currentGroup = nextGroup

    print("最優秀個体:")
    print(best_data[0])
    print(best_data[1])
    print(cities)
    gr.outputMap(data)

    return [x, y]


if __name__ == '__main__':
    main(10, 10, 10, 100, 20, 0.001, 0.001, 10000)

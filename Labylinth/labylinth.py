#! python

import makeLabylinth as ml
import genomPara as gp
import random as rand


def evalGenom(control, laby, start):
    count = 0
    y = start[0]
    x = start[1]
    for i in range(len(control)):
        command = control[i]

        if laby[y][x] == 'G':
            return count
        else:
            count += 1

        if command is 0:
            if y - 1 >= 0 and laby[y - 1][x] != '*':
                y = y - 1
                x = x
        elif command is 1:
            if y + 1 < len(laby) and laby[y + 1][x] != '*':
                y = y + 1
                x = x
        elif command is 2:
            if x - 1 >= 0 and laby[y][x - 1] != '*':
                y = y
                x = x - 1
        else:
            if x + 1 < len(laby[y]) and laby[y][x + 1] != '*':
                y = y
                x = x + 1

    return len(control) + 1


def genomCreate(length):
    data = []
    for i in range(0, length):
        data.append(rand.randint(0, 3))

    return gp.genom(data, 0)


# 遺伝子の選択を行う関数
def genomSelect(genomPop, maxChange):
    sortGenom = sorted(genomPop, reverse=False, key=lambda u: u.evaluation)
    result = [sortGenom.pop(0) for i in range(maxChange)]
    return result


# 遺伝子の交叉を行う関数
def genomCross(genom1, genom2, length):
    child_genom = []
    # 子供となる遺伝子

    cross1 = rand.randint(0, length)
    cross2 = rand.randint(cross1, length)

    # 交叉する遺伝子データの獲得
    one = genom1.getData()
    second = genom2.getData()

    # 交叉
    child_one = one[:cross1] + second[cross1:cross2] + one[cross2:]
    child_second = second[:cross1] + one[cross1:cross2] + second[cross2:]

    # リストに格納して返す
    child_genom.append(gp.genom(child_one, 0))
    child_genom.append(gp.genom(child_second, 0))

    return child_genom


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
            mutationGenom = []
            for j in i.getData():
                if perMutation_G > (float)(rand.randint(0, 100) / 100):
                    mutationGenom.append(rand.randint(0, 3))
                else:
                    mutationGenom.append(j)
                i.setData(mutationGenom)

        mutations.append(i)

    return mutations


def main(genomLength, population, labylinth, maxChange, perMutation_G, perMutaiton_I,
         roopCount):
    currentGroup = []
    start = ml.searchStart(labylinth)
    for i in range(population):
        currentGroup.append(genomCreate(genomLength))

    for count_ in range(1, roopCount):
        nextGroup = []
        for i in range(population):
            evalResult = evalGenom(currentGroup[i].getData(), labylinth, start)
            currentGroup[i].setEval(evalResult)

        eliteGroup = genomSelect(currentGroup, maxChange)
        childGenom = []

        for i in range(0, maxChange):
            childGenom.extend(
                genomCross(eliteGroup[i - 1], eliteGroup[i], genomLength))

        nextGroup = nextGenCreate(currentGroup, childGenom, eliteGroup)
        nextGroup = mutation(nextGroup, perMutaiton_I, perMutation_G)

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
    print("行動数:", eliteGroup[0].getEval())


if __name__ == '__main__':
    data = ml.makeLabylinth('testData.txt')
    size = ml.countElements(data)
    main(size, 100, data, 20, 0.01, 0.01, 10001)

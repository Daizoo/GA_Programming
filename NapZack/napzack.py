#! python

import genomPara as gap
import baggageObject as bo
import random as rand


def createBaggage(number, maxWeight, maxValue):

    baggageData = []
    for i in range(1, number+1):
        baggageData.append(
            bo.baggage(rand.randint(0, maxWeight), rand.randint(0, maxValue)))

    return baggageData


def genomCreate(number):

    sack = []
    for i in range(1, number+1):
        sack.append(rand.randint(0, 1))

    return gap.genom(sack, 0)


def calculateWeightAndValue(sack, baggageData):

    sumWeight = 0
    sumValue = 0
    for i in range(0, len(sack)):
        if sack[i] == 1:
            sumWeight += baggageData[i].getWeight()
            sumValue += baggageData[i].getValue()

    return [sumWeight, sumValue]


def evalGenom(genom, limit, baggageData):

    evaluation = calculateWeightAndValue(genom.getData(), baggageData)
    if evaluation[0] > limit:
        evaluation[1] = 0

    return evaluation[1]


def genomSelect(genomPop, maxChange):
    sortGenom = sorted(genomPop, reverse=True, key=lambda u: u.evaluation)
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
    child_genom.append(gap.genom(child_one, 0))
    child_genom.append(gap.genom(child_second, 0))

    return child_genom


def nextGenCreate(recentGenom, childGenom, eliteGenom):
    nextGenGenoms = []
    nextGenGenoms = sorted(
        recentGenom, reverse=False, key=lambda u: u.evaluation)
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
                    mutationGenom.append(-1 * (j - 1))
                else:
                    mutationGenom.append(j)
                i.setData(mutationGenom)

        mutations.append(i)

    return mutations


def main(number, population, limit, maxWeight, maxValue,
         maxChange, perMutation_G, perMutaiton_I, roopCount):

    currentGroup = []
    baggageData = createBaggage(number, maxWeight, maxValue)

    for i in range(population):
        currentGroup.append(genomCreate(number))

    for count_ in range(1, roopCount+1):
        nextGroup = []
        for i in range(population):
            evalResult = evalGenom(currentGroup[i], limit, baggageData)
            currentGroup[i].setEval(evalResult)

        eliteGroup = genomSelect(currentGroup, maxChange)
        childGenom = []

        for i in range(0, maxChange):
            childGenom.extend(
                genomCross(eliteGroup[i - 1], eliteGroup[i], number))

        nextGroup = nextGenCreate(currentGroup, childGenom, eliteGroup)
        nextGroup = mutation(nextGroup, perMutaiton_I, perMutation_G)

        fits = [i.getEval() for i in currentGroup]

        Min = min(fits)
        Max = max(fits)
        Ave = sum(fits) / (int)(len(fits))

        print("第", count_, "世代の結果\n")
        print("Max:", Max, "\n")
        print("Min:", Min, "\n")
        print("Ave:", Ave, "\n")
        currentGroup = nextGroup

    print("---荷物一覧---")
    for i in range(len(baggageData)):
        print(i+1, "番めの荷物")
        print("重さ: ", baggageData[i].getWeight())
        print("価格: ", baggageData[i].getValue())

    print("最優秀個体:")
    print(eliteGroup[0].getData())
    print(eliteGroup[0].getEval())

if __name__ == "__main__":
    main(5, 50, 100, 100, 200, 10, 0.001, 0.002, 20)

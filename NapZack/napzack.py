import genomPara as gap
import baggageObject as bo
import random as rand


def createBaggage(number, maxWeight, maxValue):

    baggageData = []
    for i in range(0, number):
        baggageData.append(
            bo.baggage(rand.randint(0, maxWeight), rand.randint(0, maxValue)))

    return baggageData


def createGenom(number, baggageData):

    sack = []
    for i in range(0, number):
        sack.append(rand.randint(0, 1))

    return gap.genom(sack, [0, 0])


def calculateWeightAndValue(sack, baggageData):

    sumWeight = 0
    sumValue = 0
    for i in range(len(sack)):
        if sack[i] == 1:
            sumWeight += baggageData[i].getWeight()
            sumValue += baggageData[i].getValue()

    return [sumWeight, sumValue]


def evalGenom(genom, limit, baggageData):

    evaluation = calculateWeightAndValue(genom.getData, baggageData)
    if evaluation[0] > limit:
        evaluation[1] = 0

    return evaluation

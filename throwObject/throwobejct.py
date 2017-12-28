from calcPoint import calcPoint
import genomPara as gp
from random import randint


def genomCreate():
    data = []
    for i in range(0, 10):
        data.append(randint(0, 9))

    return gp.genom(data, [0, 0, 0])


def evalGenom(genom, point):
    data = genom.getData()
    init_y = data[0] + data[1] * 0.1 + data[2] * 0.01
    degree = data[3] * 10 + data[4] + data[5] * 0.1 * data[6] * 0.01
    init_v = data[7] + data[8] * 0.1 + data[9] * 0.1

    evaluation = calcPoint(init_y, point, degree, init_v)
    return evaluation


def genomSelect(genomPop, maxChange):
    sortGenom = sorted(genomPop, reverse=False, key=lambda u: u.evaluation[1])
    sortGenom = sorted(sortGenom, reverse=False, key=lambda u: u.evaluation[2])
    result = [sortGenom.pop(0) for i in range(maxChange)]
    return result


def genomCross(genom1, genom2, length):
    child_genom = []
    # 子供となる遺伝子

    cross1 = randint(0, length)
    cross2 = randint(cross1, length)

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
        recentGenom, reverse=True, key=lambda u: u.evaluation[1])
    nextGenGenoms = sorted(nextGenGenoms, reverse=True, key=lambda u: u.evaluation[2])
    del nextGenGenoms[0:len(eliteGenom) + len(childGenom)]
    nextGenGenoms.extend(eliteGenom)
    nextGenGenoms.extend(childGenom)

    return nextGenGenoms


def mutation(genoms, perMutation_I, perMutation_G):
    mutations = []
    for i in genoms:
        if perMutation_I > (float)(randint(0, 100) / 100):
            mutationGenom = []
            for j in i.getData():
                if perMutation_G > (float)(randint(0, 100) / 100):
                    mutationGenom.append(randint(0, 9))
                else:
                    mutationGenom.append(j)
                i.setData(mutationGenom)

        mutations.append(i)

    return mutations


def main(point, population, maxChange, perMutation_G, perMutaiton_I,
         roopCount):
    currentGroup = []
    for i in range(population):
        currentGroup.append(genomCreate())

    for count_ in range(1, roopCount):
        nextGroup = []
        for i in range(population):
            evalResult = evalGenom(currentGroup[i], point)
            currentGroup[i].setEval(evalResult)

        eliteGroup = genomSelect(currentGroup, maxChange)
        childGenom = []

        for i in range(0, maxChange):
            childGenom.extend(
                genomCross(eliteGroup[i - 1], eliteGroup[i], 10))

        fits = sorted(currentGroup, reverse=False, key=lambda u: u.evaluation[1])
        fits = sorted(fits, reverse=False, key=lambda u: u.evaluation[2])

        Min = fits[0]
        Max = fits[-1]

        print("第", count_, "世代の結果\n")
        print("最小距離: ", Min.evaluation[0], " | 目標との差:", Min.evaluation[2])
        print("地表からの差: ", Min.evaluation[1], "\n")
        print("最大距離: ", Max.evaluation[0], " | 目標との差: ", Max.evaluation[2])
        print("地表からの差: ", Max.evaluation[1], "\n")
        nextGroup = nextGenCreate(currentGroup, childGenom, eliteGroup)
        nextGroup = mutation(nextGroup, perMutaiton_I, perMutation_G)
        currentGroup = nextGroup

    print("最優秀個体:")
    print(eliteGroup[0].getData())


if __name__ == '__main__':
    main(15.0, 100, 20, 0.001, 0.001, 1000)

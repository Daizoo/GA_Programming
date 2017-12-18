import genomPara as gp
import random as rand


# 遺伝子生成を行う関数
def genomCreate(length):
    genomData = []
    for i in range(length):
        genomData.append(rand.uniform(0, 1))
    return gp.genom(genomData, 0)


# 遺伝子の評価値を返す関数
def evalGenom(genom):
    total = sum(genom.getData())
    return total


# 遺伝子の選択を行う関数
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
    child_genom.append(gp.genom(child_one, 0))
    child_genom.append(gp.genom(child_second, 0))

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


def main(genomLength, population, maxChange, perMutation_G, perMutaiton_I,
         roopCount):
    currentGroup = []
    for i in range(population):
        currentGroup.append(genomCreate(genomLength))

    for count_ in range(1, roopCount):
        nextGroup = []
        for i in range(population):
            evalResult = evalGenom(currentGroup[i])
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
        print("Max:", Max, "\n")
        print("Min:", Min, "\n")
        print("Ave:%", Ave, "\n")
        currentGroup = nextGroup

    print("最優秀個体:")
    print(eliteGroup[0].getData())

from random import randint
from random import sample
from SalesMan import genomPara as gp


def samePartChange(parent1, parent2, length):
    data1 = parent1.getData()
    data2 = parent2.getData()
    child1 = data1
    child2 = data2

    cross1 = randint(0, length)
    cross2 = randint(cross1, length)
    index_1 = []
    index_2 = []

    for i in range(cross1, cross2):
        index_1.append(child1.index(data2[i]))
        index_2.append(child2.index(data1[i]))

    for i in range(cross1, cross2):
        child1[i], child1[index_1[i - cross1]] = child1[index_1[i - cross1]], child1[i]
        child2[i], child2[index_2[i - cross1]] = child2[index_2[i - cross1]], child2[i]

    return [gp.genom(child1, 0), gp.genom(child2, 0)]


if __name__ == '__main__':
    test1 = gp.genom(sample(range(0, 10), 10), 0)
    test2 = gp.genom(sample(range(0, 10), 10), 0)
    print(test1.getData())
    print(test2.getData())
    children = samePartChange(test1, test2, 10)
    print(children[0])
    print(children[1])

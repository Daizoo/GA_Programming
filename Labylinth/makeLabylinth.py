#! python


def makeLabylinth(path):
    f = open(path)
    data = f.read()
    f.close()
    laby = []
    test = []

    for i in range(len(data)):
        if data[i] != '\n':
            test.append(data[i])
        else:
            laby.append(test)
            test = []

    return laby


def searchStart(data):
    start = []

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'S':
                start.append(i)
                start.append(j)
                break

    return start


def countElements(data):
    count = 0
    for i in range(len(data)):
        for i in range(len(data[i])):
            count += 1

    return count


if __name__ == "__main__":
    data = makeLabylinth('testData.txt')
    print(searchStart(data))
    print(countElements(data))

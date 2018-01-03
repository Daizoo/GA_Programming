import matplotlib.pyplot as plt
from OneMax import onemax_degi as om
from NapZack import napzack as nz
from SalesMan import salesman as sm
from throwObject import throwobejct as to


def expermintPlot(roopCount):
    result_1 = om.main(10, 100, 20, 0.001, 0.001, roopCount)
    result_2 = nz.main(10, 100, 10000, 100, 100, 20, 0.001, 0.001, roopCount)
    result_3 = sm.main(10, 10, 10, 100, 20, 0.001, 0.001, roopCount)
    result_4 = to.main(15, 100, 20, 0.001, 0.001, roopCount)

    plt.subplot(2, 2, 1)
    plt.plot(result_1[0], result_1[1])
    plt.title('OneMax')

    plt.subplot(2, 2, 2)
    plt.plot(result_2[0], result_2[1])
    plt.title('NapSack')

    plt.subplot(2, 2, 3)
    plt.plot(result_3[0], result_3[1])
    plt.title('SalesMan')

    plt.subplot(2, 2, 4)
    plt.plot(result_4[0], result_4[1])
    plt.title('ThrowObject')

    plt.show()

    f=open('result.txt', 'w')
    f.writelines('Onemax: ' + str(max(result_1[1])) + '\n')
    f.writelines('NapSack: ' + str(max(result_2[1])) + '\n')
    f.writelines('SalesMan: ' + str(min(result_3[1])) + '\n')
    f.writelines('ThrowObject: ' + str(min(result_4[1])) + '\n')
    f.close()


if __name__ == '__main__':
    expermintPlot(10000)

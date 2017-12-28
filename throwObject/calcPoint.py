from math import sin, cos, radians


def calcPoint(init_y, dist, degree, init_v):
    y = init_y
    x = 0
    t = 0
    G = 9.8
    fps = 1.0 / 100.0
    theta = radians(degree)

    while y > 0:
        t += fps
        x = init_v * cos(theta) * t
        y = init_v * sin(theta) * t - G * t * t / 2 + init_y

    return [x, y, abs(dist - x)]


if __name__ == '__main__':
    result = calcPoint(0.5, 0.6, 3, 2)
    print(result)

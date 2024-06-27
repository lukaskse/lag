import math

def newtonPi(init):
    sin = math.sin(init)
    cos = math.cos(init)
    xk = init
    xkplusone = xk - sin/cos
    while xk != xkplusone:
        xk, xkplusone = xkplusone, xkplusone - math.sin(xkplusone)/math.cos(xkplusone)
    return xkplusone


def leibnizPi(iterations):
    pi = 0
    counter = 1
    for odd_num in range(1, 2 * iterations, 2):
        if counter % 2 != 0:
            pi += 4/odd_num
        else:
            pi -= 4/odd_num
        counter += 1
    return pi



def nilakanthaPi(iterations):
    pi = 0
    first_divisor = 2
    second_divisor = 3
    third_divisor = 4
    if iterations > 0:
        pi = 3
        counter = 1
        for i in range(2, iterations + 1, 1):
            if counter % 2 != 0:
                pi += 4/(first_divisor * second_divisor * third_divisor)
            else:
                pi -= 4 / (first_divisor * second_divisor * third_divisor)
            counter += 1
            first_divisor += 2
            second_divisor += 2
            third_divisor += 2
    return pi

print(nilakanthaPi(3))
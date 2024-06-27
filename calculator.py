def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    if y == 0:
        raise ValueError('This operation is not supported for given input parameters')
    return x / y


def modulo(x, y):
    if x < y or y <= 0:
        raise ValueError('This operation is not supported for given input parameters')
    return x % y


def secondPower(x):
    return x * x


def power(x, y) -> float:
    if y < 0:
        raise ValueError('This operation is not supported for given input parameters')
    return float(x ** y)


def secondRadix(x):
    if x <= 0:
        raise ValueError('This operation is not supported for given input parameters')
    return x ** (1/2)


def magic(x, y, z, k):
    l = x + k
    m = y + z
    if m == 0:
        raise ValueError('This operation is not supported for given input parameters')
    n = ((l/m) + 1)
    return n


def control(a, x, y, z, k):
    try:
        x, y, z, k = int(x), int(y), int(z), int(k)
        if a == 'ADDITION':
            return addition(x, y)
        elif a == 'SUBTRACTION':
            return subtraction(x, y)
        elif a == 'MULTIPLICATION':
            return multiplication(x, y)
        elif a == 'DIVISION':
            return division(x, y)
        elif a == 'MOD':
            return modulo(x, y)
        elif a == 'POWER':
            return power(x, y)
        elif a == 'SECONDRADIX':
            return secondRadix(x)
        elif a == 'MAGIC':
            return magic(x, y, z, k)
        else:
            raise ValueError('This operation is not supported for given input parameters')
    except ValueError:
        print('This operation is not supported for given input parameters')
        raise
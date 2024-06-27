def polyEval(poly, x):
    poly_value = 0
    for i in range(len(poly)):
        poly_value += poly[i] * (x ** (i))
    return poly_value


def polySum(poly1, poly2):
    sum_poly = [0] * max(len(poly1), len(poly2))
    poly1 += [0] * (len(sum_poly) - len(poly1))
    poly2 += [0] * (len(sum_poly) - len(poly2))
    for i in range(0, len(sum_poly)):
        sum_poly[i] = poly1[i] + poly2[i]
    for last in range(len(sum_poly) - 1, 0, -1):
        if sum_poly[last] == 0:
            sum_poly.remove(sum_poly[last])
        else:
            return sum_poly


def polyMultiply(poly1, poly2):
    result = [0] * (len(poly1) + len(poly2) - 1)
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            result[i + j] += poly1[i] * poly2[j]
    return result

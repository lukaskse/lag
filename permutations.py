def permutations(array):
    if len(array) == 0:
        return [[]]
    if len(array) == 1:
        return [array]

    result = []

    for i in range(len(array)):
        first = array[i]
        rest = array[:i] + array[i + 1:]

        for p in permutations(rest):
            result.append([first] + p)

    return result

print(permutations([]))
print(permutations([1]))
print(permutations(['a', 'b', 'c', 'd']))

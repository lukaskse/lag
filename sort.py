def sortNumbers(data, condition):
    if condition == 'ASC':
        start = 1
        finish = len(data)
        step = 1
        begin = 0
        end = len(data)
    elif condition == 'DESC':
        start = len(data) - 2
        finish = -1
        step = -1
        begin = -1
        end = len(data) - 1
    for i in range(start, finish, step):
        currentvalue = data[i]
        position = i
        while position > begin and position < end and data[position - step] > currentvalue:
            data[position] = data[position - step]
            position -= step
        data[position] = currentvalue
    return data


def sortData(weights, data, condition):
    if len(weights) != len(data):
        raise ValueError('Invalid input data')
    if condition == 'ASC':
        start = 1
        finish = len(data)
        step = 1
        begin = 0
        end = len(data)
    elif condition == 'DESC':
        start = len(data) - 2
        finish = -1
        step = -1
        begin = -1
        end = len(data) - 1
    for i in range(start, finish, step):
        currentvalue = weights[i]
        currentdata = data[i]
        position = i
        while position > begin and position < end and weights[position - step] > currentvalue:
            weights[position] = weights[position - step]
            data[position] = data[position - step]
            position -= step
        weights[position] = currentvalue
        data[position] = currentdata
    return data



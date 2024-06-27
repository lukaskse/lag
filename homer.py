"""
Homer's fridge
Course: B0B36ZAL
"""

#nasledujici kod nijak nemodifikujte!
class Food:
    def __init__(self, name, expiration):
        self.name = name
        self.expiration = expiration
#predesly kod nijak nemodifikujte!

def openFridge(fridge):
    print("Following items are in Homer's fridge:")
    for food in fridge:
        print("{0} (expires in: {1} days)".format(
            str(food.name), str(food.expiration))
        )
    print("")

# test vypisu - pri odevzdani smazte, nebo zakomentujte
#fridge = [Food("beer", 4), Food("steak", 10), Food("hamburger", 0), Food("donut", 3), Food("beer", 4), Food("steak", 1), Food("hamburger", 1), Food("donut", 3)]
#openFridge(fridge)


"""
Task #1
"""
def maxExpirationDay(fridge):
    if not fridge:
        return -1
    else:
        maxExpiration = fridge[0].expiration
        for food in fridge:
            if food.expiration > maxExpiration:
                maxExpiration = food.expiration
        return maxExpiration

# test vypisu - pri odevzdani smazte, nebo zakomentujte
#print(maxExpirationDay(fridge))
# The command should print 4


"""
Task #2
"""
def histogramOfExpirations(fridge):
    histogram = [0] * (maxExpirationDay(fridge) + 1)
    for food in fridge:
        histogram[food.expiration] += 1
    return histogram

# test vypisu - pri odevzdani smazte, nebo zakomentujte
#print(histogramOfExpirations(fridge))
# The command should print [0, 2, 0, 1, 1]


"""
Task #3
"""
def cumulativeSum(histogram):
    sum_array = [0] * len(histogram)
    for i in range(len(histogram)):
        sum_array[i] = sum(histogram[:i+1])
    return sum_array

# test vypisu - pri odevzdani smazte, nebo zakomentujte
#print(cumulativeSum(histogramOfExpirations(fridge)))
# The command should print [0, 2, 2, 3, 4]


"""
Task #4
"""
def sortFoodInFridge(fridge):
    sum_array = cumulativeSum(histogramOfExpirations(fridge))
    sorted_fridge = [0] * len(fridge)
    for i in range(len(fridge)):
        actual_expiration = fridge[i].expiration
        sum_array[actual_expiration] -= 1
        poslnd = sum_array[actual_expiration]
        sorted_fridge[poslnd] = fridge[i]
    return sorted_fridge

# test vypisu - pri odevzdani smazte, nebo zakomentujte
#openFridge(sortFoodInFridge(fridge))
# The command should print
# Following items are in Homer's fridge:
# hamburger (expires in: 1 days)
# steak (expires in: 1 days)
# donut (expires in: 3 days)
# beer (expires in: 4 days)


"""
Task #5
"""
def reverseFridge(fridge):
    reversed_fridge = fridge.copy()
    for i in range(len(reversed_fridge) // 2):
        reversed_fridge[i], reversed_fridge[-i-1] = fridge[-i-1], fridge[i]
    return reversed_fridge
    

# test vypisu - pri odevzdani smazte, nebo zakomentujte
#The command should print
# Following items are in Homer's fridge:
# donut (expires in: 3 days)
# hamburger (expires in: 1 days)
# steak (expires in: 1 days)
# beer (expires in: 4 days)

# test vypisu - pri odevzdani smazte, nebo zakomentujte
#openFridge(sortFoodInFridge(reverseFridge(fridge)))
# The command should print
# Following items are in Homer's fridge:
# steak (expires in: 1 days)
# hamburger (expires in: 1 days)
# donut (expires in: 3 days)
# beer (expires in: 4 days)


"""
Task #6
"""
def eatFood(name, fridge):
    temp = float("inf")
    del_food = None
    new_fridge = fridge.copy()
    for i in range(len(fridge)):
        if fridge[i].name == name:
            if fridge[i].expiration < temp:
                temp = fridge[i].expiration
                del_food = fridge[i]
    if del_food:
        new_fridge.remove(del_food)
    return new_fridge

# test vypisu - pri odevzdani smazte, nebo zakomentujte
#fridge = [Food("beer", 4), Food("steak", 10), Food("hamburger", 0), Food("donut", 3), Food("beer", 4), Food("steak", 1), Food("hamburger", 1), Food("donut", 3)]
#openFridge(
#     eatFood("donut", fridge
#    ))
#openFridge(fridge)
# The command should print
# Following items are in Homer's fridge:
# beer (expires in: 4 days)
# steak (expires in: 1 days)
# hamburger (expires in: 1 days)
# donut (expires in: 3 days)
# donut (expires in: 6 days)

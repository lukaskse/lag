class Node:
    def __init__(self, nextNode, prevNode, data):
        self.data = data
        self.nextNode = nextNode
        self.prevNode = prevNode


class LinkedList:
    def __init__(self):
        self.head = None







class Car:
    def __init__(self, identification, name, brand, price, active):
        self.identification = identification
        self.name = name
        self.brand = brand
        self.price = price
        self.active = active



db = LinkedList()


def init(cars):
    for car in cars:
        add(car)


def add(car):
    node = Node(None, None, car)
    if db.head:
        temp = db.head
        while True:
            if temp is None:
                break

            if temp.data.price > node.data.price:
                previousNode = temp.prevNode
                if previousNode:
                    temp.prevNode.nextNode = node
                    node.prevNode = previousNode
                temp.prevNode = node
                node.nextNode = temp

                if db.head == temp:
                    db.head = node
                break
            else:
                if temp.nextNode is None:
                    temp.nextNode = node
                    node.prevNode = temp
                    break
            
                temp = temp.nextNode
    else:
        db.head = node


def updateName(identification, name):
    car = getCarNodeById(identification)
    if car:
        car.data.name = name
    else:
        return None


def updateBrand(identification, brand):
    car = getCarNodeById(identification)
    if car:
        car.data.brand = brand
    else:
        return None


def activateCar(identification):
    car = getCarNodeById(identification)
    if car:
        car.data.active = True
    else:
        return None


def deactivateCar(identification):
    car = getCarNodeById(identification)
    if car:
        car.data.active = False
    else:
        return None


def getDatabaseHead():
    return db.head


def getDatabase():
    return db


def calculateCarPrice():
    temp = db.head
    sum = 0
    while True:
        if not temp:
            break
        if temp and temp.data.active == True:
            sum += temp.data.price
        temp = temp.nextNode
    return sum


def clean():
    db.head = None

def getCarNodeById(id):
    temp = db.head
    while True:
        if temp:
            if id == temp.data.identification:
                return temp
            else:
                temp = temp.nextNode
        else:
            return None

import math


# 1
class String:
    def __init__(self):
        self.input_String = ""

    def getString(self):
        self.input_String = input()

    def printString(self):
        print(self.input_String.upper())


Strings = String()
Strings.getString()
Strings.printString()


# 2
class Shape:
    def __init__(self):
        self.area = 0

    class Square:
        def __init__(self, lenght):
            self.length = lenght

        def getArea(self):
            print(self.length * self.length)


Sha = Shape.Square(10)
Sha.getArea()


# 3
class Shape:
    def __init__(self):
        self.area = 0

    class Square:
        def __init__(self, lenght):
            self.length = lenght

        def getArea(self):
            self.area = self.length * self.length
            print(self.length * self.length)

    class Rectangle:
        def __init__(self, length, width):
            self.length = length
            self.width = width

        def getArea(self):
            self.area = self.length * self.width
            print(self.area)


Sha = Shape.Rectangle(10, 20)
Sha.getArea()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self, x1, y1):
        self.x = x1
        self.y = y1

    def dist(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        distance = math.sqrt(dx * dx + dy * dy)
        return (distance)


point1 = Point(10, 20)
point2 = Point(3, 4)
print(point1.dist(point2))

# 5
d = dict()


class Account:
    def __init__(self):
        self.owner = []
        self.balance = 0
        self.owners = dict()

    def deposit(self, user, balance):
        if user not in self.owner:
            self.owners[user] = 0
            self.owner.append(user)
        self.owners[user] += balance
        print(user, self.owners[user])

    def withdraw(self, user, balance):
        if self.owners[user] - balance >= 0:
            self.owners[user] -= balance
        else:
            print("Not enough money")


c = Account()
c.deposit('sas', 1)
c.withdraw('sas', 2)
# 6
q = [1, 2, 3, 4]


def func(i):
    for j in range(2, i):
        if i % j == 0:
            return False
    return True


print(f"Primes: {list(filter(lambda x: func(x), q))}")

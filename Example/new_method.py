class emp:
    def __init__(self, name, sal):
        self.name = name
        self.sal = sal

    def __new__(cls, name, sal):
        if 0 < sal < 10000:
            return object.__new__(cls)
        else:
            return None

    def __str__(self):
        return "{0}, {1}".format(self.name, self.sal)

e = emp("kunal", 100000)
print(e)


def HI(func):
    def inner():
        print("HI")
        func()
    return inner()


def name(func):
    def inner():
        print("bye")
        # func()
    return inner()
print(lambda x,y : x+y)
    # func

@name
@HI
def bYE():
    print("kunal")

from functools import reduce
str = 'Hi good morning all kkk zzz xxx'


print(reduce(lambda x, y: x+y+x, [1, 2, 3, 4], 2))







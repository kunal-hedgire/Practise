class cals:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add_two(self):
        return self.a + self.b

    def sub_two(self):
        return self.a + self.b


c = cals(10,5)
print(c.add_two())
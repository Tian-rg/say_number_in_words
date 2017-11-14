def add(a,b):
    return a+b

class cal(object):

    def __init__(self,c):
        self.c = c

    def add(self,a,b):
        return add(a,b) + self.c

class cal_two(cal):
    def __init__(self, c, d):
        super().__init__(c)
        self.c = self.c + d

    def add(self, a, b):
        return super().add(a,b)

calculator = cal_two(4,7)
print (calculator.add(2,5))

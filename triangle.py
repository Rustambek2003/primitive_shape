import math
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def description(self):
        P = (self.a+self.b+self.c)/2
        return math.sqrt(P*(P-self.a)*(P-self.b)*(P-self.c))

uchburchak = Triangle(3, 4, 5)
print(uchburchak.description())
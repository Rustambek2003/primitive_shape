from polygon import Polygon

class Square(Polygon):
    def __init__(self, height):
        super().__init__(height, height)

x = Square(5)
print(x.getArea())
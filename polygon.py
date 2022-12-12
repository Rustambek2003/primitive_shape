class Polygon:
    def __init__(self, height, width):
        self.heigth = height
        self.width = width
        
    def getArea(self):
        return self.heigth*self.width

    def getPerimeter(self):
        return (self.heigth+self.width)*2


import math

class Shape:
    def __init__(self):
        self.unit = "meters"

    def area(self):
        pass

    def perimeter(self):
        pass

    def display(self):
        pass
class circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
    

class rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
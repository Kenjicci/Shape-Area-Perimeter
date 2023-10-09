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

class Circle(Shape):
    def __init__(self, r):
        super().__init__()
        self.r = r

    def area(self):
        area = math.pi * (self.r ** 2)
        return area

    def perimeter(self):
        p = 2 * math.pi * self.r
        return p

    def display(self):
        print(f"Circle  -  Radius: {self.r} {self.unit}")
        print(f"           Area: {self.area()} {self.unit} squared ")
        print(f"           Perimeter: {self.perimeter()} {self.unit}")

class Rectangles(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        area = self.width * self.length
        return area
    
    def perimeter(self):
        perimeter = 2*(self.width) + 2*(self.length)
        return perimeter
    
    def display(self):
        print(f"Rectangle - Width: {self.width} {self.unit}, Height: {self.length} {self.unit}")
        print(f"            Area: {self.area()} {self.unit} squared")
        print(f"            Perimeter: {self.perimeter()} {self.unit}")
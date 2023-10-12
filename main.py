import math

class Shape:
    def __init__(self, unit = "meters"):
        self.unit = unit

    def area(self):
        pass

    def perimeter(self):
        pass

    def display(self):
        pass

class circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__()

    def area(self):
        area = math.pi * self.radius ** 2
        return round(area, 2)
    
    def perimeter(self):
        circumference = 2 * math.pi * self.radius
        return round(circumference, 2)

    def display(self):
        print(f"Circle  -  Radius: {self.radius} {self.unit}")
        print(f"           Area: {self.area()} {self.unit} squared ")
        print(f"           Perimeter: {self.perimeter()} {self.unit}")   

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
        super().__init__()
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

    def display(self):
        print(f"Rectangle - Width: {self.width} {self.unit}, Height: {self.height} {self.unit}")
        print(f"            Area: {self.area()} {self.unit} squared")
        print(f"            Perimeter: {self.perimeter()} {self.unit}")

Circle = circle(5)
Rectangle = rectangle(3,4)

Circle.display()
Rectangle.display()

from abc import ABC, abstractmethod

# Abstract Class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete class 1
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width 

    def area(self):
        return self.length * self.width 

    def perimeter(self):
        return 2 * (self.length + self.width)  

# Concrete classs 2
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius 

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius
    
# Using abstraction
shapes = [Rectangle(5,3), Circle(4)]   

for shape in shapes:
    print("Area: ", shape.area())
    print("Perimeter: ",shape.perimeter())
    print("------")

    
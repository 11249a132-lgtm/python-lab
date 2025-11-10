Aim:
To write a Python program that demonstrates inheritance by calculating the area of triangle, circle, and rectangle using a base class and derived classes.

Algorithm:
Start the program.
Define a base class Shape.
Define derived classes Triangle, Circle, and Rectangle inheriting from Shape.
For each derived class, define an area() method to calculate the area:
Triangle: (1/2) * base * height
Circle: π * radius^2
Rectangle: length * width
Input the required dimensions for each shape from the user.
Call the area() method for each object to calculate and display the area.
End the program.

Program (Python Code):
# Program: Area Calculation Using Inheritance
import math
# Base class
class Shape:
    def area(self):
        pass
# Derived class for Triangle
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
# Derived class for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
# Derived class for Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
# Main Program
# Triangle
b = float(input("Enter the base of the triangle: "))
h = float(input("Enter the height of the triangle: "))
triangle = Triangle(b, h)
print(f"Area of Triangle: {triangle.area():.2f}")
# Circle
r = float(input("\nEnter the radius of the circle: "))
circle = Circle(r)
print(f"Area of Circle: {circle.area():.2f}")
# Rectangle
l = float(input("\nEnter the length of the rectangle: "))
w = float(input("Enter the width of the rectangle: "))
rectangle = Rectangle(l, w)
print(f"Area of Rectangle: {rectangle.area():.2f}")

Result:
The program demonstrates inheritance by using a base class Shape and derived classes Triangle, Circle, and Rectangle to calculate areas.
Each derived class implements its own area() method.
User inputs are taken for all dimensions, and areas are displayed with precision.

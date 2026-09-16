"""
Evan Dong
lab 5: review of class, objects, methods, and attributes 
Sep 16, 2026
"""
print("\n------ Example 1: class Circle ------")
class Circle():
    # values that need to pass to the object of class Circle
    def __init__(self, radius, color):
        self.r = radius
        self.c = color

    # attributes
    pi = 3.14157

    # method
    def circumference(self):
        return 2*self.pi*self.r

# create instance object of the class
c1 = Circle(2,"red")
print(c1.c)
print(c1.circumference())

print("\n------ Example 2: class Rectangle ------")
import matplotlib.pyplot as plt

class Rectangle():
    def __init__(self, height, width, color):
        self.h = height
        self.w = width
        self.c = color

    # method to calculate the area
    def area(self):
        return self.w*self.h

    # method to calculate the perimeter
    def perimeter(self):
        return 2*self.w + 2*self.h

    # method to draw the rectangle
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0,0),self.w, self.h, fc = self.c))
        plt.axis("scaled")
        plt.show()

# create an instance object of the class
r1 = Rectangle(2, 3, "olive")
print(f"The perimeter of rectangle with height = {r1.h}, width = {r1.w} is {r1.perimeter()}")

"""
Car dealership's inventory management system
You are working on a python program to simulate a car dealership's inventory management system. The system aims to model cars and their attributes accurately
Task 1: create a class to represent each vehicle. Each car should have attritubes for maximum speed and mileage
Task 2: update the class with the default color for all vehicles, "white"
task 3: create a class method to assign seating capacity to a vehicle
task 4: create a class method to display all properties of an object class --> "The ____(color)car has ____ seats, with ____ miles and a maximum speed of ____"
task 5: create two instance objects of the car. One car will have a max speed of 200 kph and mileage of 50000 kmpl with five seating capacity. The other car max speed = 180 kph, mileage 75000 kmpl, four-seating
"""
print("\n------ EXERCISE ------")
class CarSpec():
    def __init__(self, speed, mileage):
        self.speed = speed
        self.mileage = mileage

    color = "White"

    def seating(self):
        self.seating = int(input("Enter the seating capacity for this car: "))

    def display(self):
        print(f"The {self.color} car has {self.seating} seats, with {self.mileage} kmpl and a maximum speed of {self.speed} kph")

car1 = CarSpec(200, 50000)
car1.seating()
car1.display()

car2 = CarSpec(180, 75000)
car2.seating()
car2.display()
# class example 

# 




#creating a class
# class house:
#     house_color = ""
#     house_number= 0

# # create two objects of the house class
# house1 = house()
# house2 = house()

# # access property using house1
# house1.house_color = "Blue"
# print(f"house color: {house1.house_color}")

# # access properties using house2
# house1.house_number = 2001
# print(f"house number: {house1.house_number}")




# create a class
# class rectangle:
#     length = 0
#     breadth = 0
    
#     # method to calculate area
#     def calculate_rectanglearea(self):
#         print("Area of rectangle =", self.length * self.breadth)

# # create object of Room class
# rectangle1 = rectangle()

# # assign values to all the properties 
# rectangle1.length = 40
# rectangle1.breadth = 30

# # access method inside class
# rectangle1.calculate_rectanglearea()



# self pass garnae parxa 



# class Public:
#     # __str__ is another magic function
#     def __init__(self):
#         self.name = "John"  # Public attribute

#     def display_name(self):
#         print(self.name)  # Public method

# obj = Public()
# obj.display_name()  # Accessible
# print(obj.name)  # Accessible





# class Protected:
#     def __init__(self):
#         self._age = 30  # Protected attribute

# class Subclass(Protected):
#     def display_age(self):
#         print(self._age)  # Accessible in subclass

# obj = Subclass()
# obj.display_age()



# class Private:
#     __salary = 50000  # Private attribute

#     def salary(self):
#         return self.__salary  # Access through public method

# obj = Private()
# print(obj.salary())  # Works
# print(obj.__salary)  # Raises AttributeError


# polymorphism concept 


 
# my_string = "Python"
# print(f"Length of string: {len(my_string)}")

# # len() with a list
# my_list = [1, 2, 3, 4, 5]
# print(f"Length of list: {len(my_list)}")

# # len() with a dictionary
# my_dict = {"a": 1, "b": 2}
# print(f"Length of dictionary: {len(my_dict)}")

# method overriding
# class Area:
    
#     def Area(self):
#         pass  # Placeholder for a generic animal sound

# class Rectangle(Area):
#     def rectarea(self):
#         print("This is rectangle area")

# class Square(Area):
#     def sqarea(self):
#         print("This is square area")

# class Circle(Area):
#     def cirarea(self):
#         print("This is circle area")

# # Create objects of different Aaea types
# rectangle = Rectangle()
# square = Square()
# circle = Circle()

# rectangle.rectarea()
# square.sqarea()
# circle.cirarea()



#single inheritance


# class Parent:
#         def parent_method(self):
#             print("This is from the parent class.")

# class Child(Parent):
#         def child_method(self):
#             print("This is from the child class.")

# c = Child()
# c.parent_method()
# c.child_method()



#Multiple inheritance

# class Mother:
#         def mother_trait(self):
#             print("Mother's trait.")

# class Father:
#         def father_trait(self):
#             print("Father's trait.")

# class Child(Mother, Father):
#         def child_trait(self):
#             print("Child's own trait.")

# c = Child()
# c.mother_trait()
# c.father_trait()
# c.child_trait()




#Hierarchial inheritance

# class Animal:
#         def speak(self):
#             pass

# class Dog(Animal):
#         def speak(self):
#             print("Woof!")

# class Cat(Animal):
#         def speak(self):
#             print("Meow!")

# dog = Dog()
# cat = Cat()
# dog.speak()
# cat.speak()





#hybrid inheritance

# class Vehicle:
#         def move(self):
#             print("Vehicle moves.")

# class LandVehicle(Vehicle):
#         def drive(self):
#             print("Drives on land.")

# class WaterVehicle(Vehicle):
#         def sail(self):
#             print("Sails on water.")

# class AmphibiousVehicle(LandVehicle, WaterVehicle):
#         def operate(self):
#             print("Can operate on land and water.")

# amphibious = AmphibiousVehicle()
# amphibious.move()
# amphibious.drive()
# amphibious.sail()
# amphibious.operate()





#Using Super function


class Manager:
    def __init__(self, id):
        self.id = id

    def details(self):
        print(f"I am a manager and my id is {self.id}.")

class Employee(Manager):
    def __init__(self, id, name):
        super().__init__(id)  # Call parent's __init__
        self.name = name

    def details(self):
        super().details() # Call parent's details
        print(f"I am an employee and my name is {self.name}")

emp = Employee(1, "Pawan")
emp.details()

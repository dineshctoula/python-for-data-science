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
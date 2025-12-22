###Built-in functions###
print("Hello this is Python functions")
print(sum([2,3,4]))
print(max(3,5,7,90))
print(min(3,4,7,9))




###User defined functions###
def checkEvenOdd(num):
  if num%2==0:
    print(f"{num} is even")
  else:
     print(f"{num} is odd")

checkEvenOdd(2)
checkEvenOdd(5)





###Parameterised functions###
def sum(a,b):
  print(f"sum of numbers a and b is : {a+b}")

sum(3,4)






###Functions with default arguments###
def studentInfo( name, rollno, city = "Delhi", branch="Computer Science"):
   "This prints a passed info into this function"
   print(f"The Student is {name} and rollno is {rollno} belongs to {city} pertaning branch as {branch}")
   return

studentInfo("Jay",101,"Hyderabad","Mechanical")
studentInfo("Pari",122,"Electronics")
studentInfo("Sunil",112)




###Functions with required/positional arguments###
def calculate_area(length, width):
    return length * width

# Calling the function with required arguments
area = calculate_area(10, 5)
print(f"The area is: {area}")




###Fucntions with Keyword arguments###
def greet(name, message):
    print(f"Hello, {name}! {message}")

# Calling with positional arguments
greet("Alice", "How are you?")

# Calling with keyword arguments
greet(name="Bob", message="Nice to meet you!")

# Order does not matter with keyword arguments
greet(message="Have a great day!", name="Charlie")






###Fucntions with Keyword-only arguments###
def EmployeeData(EmpId, *, Emp_Name="Suresh", Role="Senior Manager"):
    print(f"Empid: {EmpId}, Employee Name: {Emp_Name}, Role: {Role}")

# Valid calls
EmployeeData(100)
EmployeeData(200, Role="Junior Lead",Emp_Name="Rahul")
EmployeeData(230, Emp_Name="Roshni",Role="Lead")

# Invalid call (Emp_Name cannot be passed positionally)
# EmployeeData(200,"Rahul") # This would raise a TypeError






###*args and **kwargs in python###
def sum_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_numbers(1, 2, 3))
print(sum_numbers(5, 10, 15, 30))


"""**kwargs is used with dictionaries iterables"""
def print_user_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print_user_info(name="Alice", age=30,city="New York", occupation="Engineer", company="Tech Solutions")
#print_user_info(city="New York", occupation="Engineer", company="Tech Solutions")




###Lambda functions###
add_ten = lambda x: x + 10
print(f"addition={add_ten(5)}")

multiply = lambda x, y: x * y
print(f"multiplication={multiply(3, 7)}")
     
addition=15
multiplication=21









from functools import reduce

print("### Lambda functions with map(), filter(), reduce() ###")

numlist = [1, 2, 3, 4, 5, 6]

# ❌ Wrong method (just repeats list)
sqrlist = 2 * numlist
print(f"Wrong squared list : {sqrlist}")

print("-" * 90)

# ✅ Correct squaring using map() and lambda
squared_numbers = list(map(lambda x: x * x, numlist))
print(f"Original numbers: {numlist}")
print(f"Squared numbers: {squared_numbers}")

print("-" * 90)

numbers = [1,2,3,4,5,6,7,8,9,10]

# ✅ filter() with lambda for even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# ✅ filter() with lambda for odd numbers
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(f"Odd numbers: {odd_numbers}")

print("-" * 90)

# ✅ reduce() for sum
sum_result = reduce(lambda x, y: x + y, numbers)
print(f"Sum: {sum_result}")

# ✅ reduce() for multiplication
mul_result = reduce(lambda x, y: x * y, numbers)
print(f"Multiplication: {mul_result}")







###Decorators in function###
#Function Decorators
def decorator(func):

    def wrapper():
        func()
    return wrapper

# Applying the decorator to a function
@decorator
def greet():
    print("Hello, World!")
def sayHello():
    print("Say Hello to the world")

greet()
sayHello()
print("--------------------------------------------")
#Method Decorators
def method_decorator(func):
    def wrapper(self,*args, **kwargs):
        res = func(self,*args, **kwargs)
        return res
    return wrapper

class MyClass:
    @method_decorator
    def say_hello(self):
        print("Hello!")
    def greet(self):
        print("Say Hello to the world")

obj = MyClass()
obj.say_hello()
obj.greet()

print("--------------------------------------------")


def fun(cls):
    cls.class_name = cls.__name__
    return cls

@fun
class Person:
    pass

print(Person.class_name)

print("--------------------------------------------")
#inbuilt decorators

class Employee:
    raise_amount = 1.05

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod     #In built classmethod decorator
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

# Using the class method
Employee.set_raise_amount(1.10)
print(Employee.raise_amount)






###generator functions in Python###
def count_up_to(max_num):
    n = 0
    while n < max_num:
        yield n
        n += 1

# Using the generator
for num in count_up_to(5):
    print(num)
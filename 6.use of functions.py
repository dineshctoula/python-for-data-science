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



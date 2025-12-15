
"""Let us take first example"""
for i in range(5):
# range function always starts with zero to n-1
  print(i)




  """Another Example"""
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)




"""Take the same example of printing even and odd numbers"""
for number in range(1,7):
  if number % 2==0:
    print(f"{number} is even.")
  else:
    print(f"{number} is odd.")



for number in range(2,20,3):  # 2 bata suru bhayera 20 samma ane 3 chae step ho , pahila 2 hunxa. next 5, next 8 and so on
  if number % 2==0:
    print(f"{number} is even.")
  else:
    print(f"{number} is odd.")



month = ["January", "March", "September","October","December"]
for i in month:
    if i == "February":
            print("The month of February has 28/29 days")
    elif i in ("April", "June", "September", "November"):
            print("The month of",i,"has 30 days.")
    elif i in ("January", "March", "May", "July", "August", "October", "December"):
            print("The month of",i,"has 31 days.")
    else:
            print(i,"is not a valid month name.")
     



colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Index {index}: {color}")





scores = {"Hema": 95, "Jolly": 88, "Priya": 92}
for name, score in scores.items():
    print(f"{name}: {score}")
print("----------------------------------------------------")
# To iterate through keys of dictionary
for name in scores.keys():
    print(f"{name}")







"""While Loop Example"""
# Initialize a counter variable, it starts from where the loop should start
count = 1

# Loop while the count is less than or equal to 5
while count <= 5:
    print(f"Current count: {count}")
    count += 1  # Increment the counter in each iteration

print("Loop finished!")






"""Basic Calculator application using while loop"""
"""
#Addition
def add(x, y):
    return x + y

#Subtraction
def subtract(x, y):
    return x - y

#Multiplication
def multiply(x, y):
    return x * y

#Division
def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

print("Welcome to the Python Calculator!")

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice(1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    elif choice == '5':
        print("Exit")
        break
    else:
        print("Invalid input. Please enter a valid choice (1-5).")
print("This is the best example of Calculator")

"""







for i in range(10):
    if i == 5:
      # Exit the loop when i is 5
        break
    print(i)
print("Tnis is end of for loop")




for i in range(10):# Iterates from 1 to 9
    if i % 2 == 0:
      # Skip all even numbers
        continue
    print(i)






"""Nested loop example"""
# Outer loop iterates through numbers from 0 to 1
for outer_num in range(2):
    # Inner loop iterates through numbers from 0 to 2 for each outer_num
    for inner_num in range(3):
        print(f"Outer: {outer_num}, Inner: {inner_num}")






outer_counter = 0

# Outer while loop
while outer_counter < 3:
    print(f"Outer loop iteration: {outer_counter + 1}")

    # Inner for loop
    for inner_item in range(2): # from 0 to 1 inclusive
        print(f"  Inner loop item: {inner_item}")

    outer_counter += 1




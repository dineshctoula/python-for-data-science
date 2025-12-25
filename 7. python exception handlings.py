"""try-except"""
try:
    num_str = input("Enter an integer: ")
    number = int(num_str)  # May raise ValueError if input is not an integer
    result = 10 / number   # May raise ZeroDivisionError if number is 0
    print(f"The result is: {result}")
#except ValueError:
    #print("Invalid input. Please enter a valid integer.")
#except ZeroDivisionError:
    #print("Cannot divide by zero.")
except Exception as e:
    print(f"An error occurred: {e}")





 

"""try..except..else"""
try:
        # Code that might raise a ValueError
        num = int(20)
except ValueError:
        print("Invalid input: Please enter a valid number.")
else:
        print(f"The value of num : {num}")








"""try..except..else..finally"""
def check_even_odd(number):
    try:
        # Intentionally raise an AssertionError if the number is odd, assert is used to evaluate a condition is true or false, basically sanity check
        #Syntax:assert condition, message
        assert number % 2 == 0, "Number is odd"
    except AssertionError as e:
        print(f"Caught an exception: {e}. The number {number} is odd.")
    else:
        # This block executes if no exception occurs in the 'try' block
        print(f"No exception occurred. The number {number} is even.")
    finally:
        # This block always executes, regardless of whether an exception occurred
        print("Finished checking number whether even or odd")

# Test cases
check_even_odd(6)  # Even number
check_even_odd(9)  # Odd number
check_even_odd(0)  # Even number







"""Handling Multiple Exceptions with a Single except Clause"""
data = [1, 2, 3]
try:
    index_str = input("Enter an index (0-2): ")
    index = int(index_str)
     # Will raise IndexError if index is out of range
    value = data[index]
    print(f"Value at index {index}: {value}")
    #will raise ValueError if value is not provided correctly
except (ValueError, IndexError, ZeroDivisionError):
      print("Invalid input or index out of range. Please enter a number between 0 and 2."
            








"""raising custom exception"""
class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds."""
    pass

balance = 100
withdrawal_amount = 101

try:
    if withdrawal_amount > balance:
        raise InsufficientFundsError("Cannot withdraw: Insufficient funds.")
    else:
        balance -= withdrawal_amount
        print(f"Withdrawal successful. Remaining balance: {balance}")
except InsufficientFundsError as e:
    print(f"Error: {e}")









"""raise built-in Exceptions"""
def check_positive(number):
        if number <= 0:
            raise ValueError("Number must be positive.")
        return number

try:
        result = check_positive(-5)
        print(f"Result: {result}")
except ValueError as e:
        print(f"Error: {e}")









class InvalidInputError(Exception):
  """custom exception for invalid input"""
  def __init__(self,message):
    self.message = message
    #super().__init__(self.message)

class OutOfRangeError(Exception):
  """custom exception for values outside a specified range"""
  def __init__(self,value,lower_bound,upper_bound,message):
    self.value = value
    self.lower_bound = lower_bound
    self.upper_bound = upper_bound
    self.message = message
    #super().__init__(self.message)
"""The super().__init__(self.message) call ensures that the parent Exception class is properly initialized with the error message."""

def process_data(data):
    if not isinstance(data, str):
        raise InvalidInputError("Data must be a string.")

def calculate_percentage(value):
    if not (0 <= value <= 100):
        raise OutOfRangeError(value, 0, 100, "Percentage value is invalid")

try:
    process_data(123)
except InvalidInputError as e:
    print(f"Error: {e.message}")

try:
    calculate_percentage(150)
except OutOfRangeError as e:
    print(f"Error: {e.message}")
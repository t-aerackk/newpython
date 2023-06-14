try:
    dividend = int(input("Enter the number you want to divide: "))
    divisor = int(input("Enter the divisor: "))
    result = dividend / divisor
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter valid integers.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except Exception as e:
    print("An error occurred:", str(e))
finally:
    print("Division operator.")

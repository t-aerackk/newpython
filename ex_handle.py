#Exception handling for managing errors and handling exceptions
def input_num():
    while True:
        try:
            num = int(input("Enter an integer:\n "))
            break  # Exit the loop if input is successfully converted to an integer
        except ValueError:
            print("Invalid input. Please enter a number.")
        else:
            print(f"The entered number is {num}")

    return num

# Usage example
result = input_num()
print("The entered integer is:", result)
def input_name():
    while True:
        try:
            name=input("Enter your Name\n")
            break
        except Exception:
            print("Invalid input. Please enter a name.\n")
        else:
            print(f"The entered name is {name}")

    return name
result=input_name()
print(f"The entered name is {result}.")

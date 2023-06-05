# #simple calculator by exception handling
# def calculator():
#     while True:
#         print("Calculator Menu:")
#         print("1. Addition")
#         print("2. Subtraction")
#         print("3. Multiplication")
#         print("4. Division")
#         print("5. Exit")

#         try:
#             choice=int(input("select an operation from 1-5:\n"))
#             if choice>=5:
#                 print("No caluclations are made")
#                 break

#             num1=float(input("Enter any number:\n"))
#             num2=float(input("Enter second number:\n"))
                       
#             if choice==1:
#                 print(f"The sum of {num1} and {num2} is", (num1+num2))
#         except Exception:
#             print("Please cooperate")

        
def calculator():
    while True:
        print("Calculator Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        try:
            choice = int(input("Select an operation (1-5): "))
            if choice >= 5:
                print("Goodbye!")
                break

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == 1:
                result = num1 + num2
            elif choice == 2:
                result = num1 - num2
            elif choice == 3:
                result = num1 * num2
            elif choice == 4:
                result = num1 / num2
            else:
                raise ValueError("Invalid operation!")

            print("Result:", result)

        except ValueError:
            print("Invalid operation! Please enter a valid operation number.")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed!")

        finally:
            response = input("Do you want to perform another calculation? (yes/no): ")
            if response.lower() == "no":
                print("Goodbye!")
                break


# Test the calculator
calculator()

def num_one():
    while True:
        try:
            num1=int(input("Print enter any number:\n"))
            num2=int(input("Print enter any number:\n")) 
            break
        except ValueError:
            print("Incorrect value. Please enter a number\n")
        else:
            print(f"The entered number is {num1}")
    return num1
result=num_one()
print(f"The entered number is {result}")


# def num_two():
#     while True:
#         try:
#             num2=int(input("Print enter any number:\n"))
#             # num2=int(input("Print enter any number:\n")) 
#             break
#         except ValueError:
#             print("Incorrect value. Please enter a number\n")
#         else:
#             print(f"The entered number is {num1}")
#     return num1
# result=num_one()
# print(f"The entered number is {result}")
# # div=num1/num2
# # div=num1/num2


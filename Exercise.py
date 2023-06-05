# #python program to print hello world
# print("Hello World\n")

# # #Add two numbers predefined
# # n1=20
# # n2=40
# # sum=n1+n2
# # print(sum)

# #Add two numbers user input
# N1=int(input("Enter any number\n"))
# N2=int(input("Enter another number\n"))
# add=N1+N2
# print(f"The sum of two numbers is {add}\n")

# #program to find square root
# Num=int(input("Enter square number\n"))
# sq=float(Num**(1/2))
# print(f"The square root of {Num} is {sq}\n")

# #Area of triangle
# L=float(input("Enter the length\n"))
# B=float(input("Enter breadth\n"))
# Area=float(0.5*L*B)
# print(f"The area of traingle is {Area}\n")

# #Miles to Kilometer x
# mile=float(input("Enter the distance in Miles\n"))
# KM=float(1.609344*mile)
# print(f"The converted {mile} miles to KM=ilometer is {KM} kms")

#Celcius to Farhenheit
cel=float(input("Enter the degree for conversion:\n"))
far=float(9/5*cel+32)
print(f"The converted {cel} celcius to Farhenheit is {far} f\n ")

# #odd or even
# A=float(input("Enter any number you want:\n"))
# if A%2==0:
#     print(f"The {A} is even number\n")

# else:
#     print("The entered number is odd\n ")

# #generate random numbers
# import random
# lower_limit = 1
# upper_limit = 10
# random_number = random.randint(lower_limit, upper_limit)
# print(f"The random number between {lower_limit} and {upper_limit} is: {random_number}")

# #swap two variables
# A=(float(input("Enter value of A:\n")))
# B=(float(input("Enter value of B:\n")))
# temp=A
# A=B
# B=temp
# print(f"The values of A is {A} and the value of B is {B}\n")
x=10
y=15
x,y=y,x
print(x,y)

# #Quadratic Equation
# A=float(input("\nEnter value of A:\n"))
# B=float(input("Enter value of B:\n"))
# C=float(input("Enter value of C:\n"))
# x=float(input("Enter value of x:\n"))
# qd=float((A*x*x)+(B*x)+C)
# print(f"The solved value for quadratic equation is {qd}")

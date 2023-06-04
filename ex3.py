# #Area of circle
# R=float(input("Enter radius of circle:\n"))
# Area=3.14*(R*R)
# print(f"The Area nof circle is {Area}")

# #Create a variable, assign its value to another and square it 
# A=5
# B=A**2
# print(B)

# #creating a variable number, assigna a value and incremant it by 1 and multiply by 2 and print he final value
# number=5
# number +=1
# print(number)
# number=2*number
# print(number)

# #Swap three values using temp and without temp
# a=5
# b=6
# c=9

# old_a=a
# temp=a
# a=b
# print(a)
# temp=b
# b=c
# print(b)
# temp=c
# c=old_a
# print(c)

#swap three values without using temp entered by user
# A=20
# B=45
# C=67
# A= (input("Enter A value you want to swap:\n"))
# B= (input("Enter B value you want to swap:\n"))
# C= (input("Enter C value you want to swap:\n"))

# A,B,C=B,C,A
# print(f"The swapped values of {A}, {B}, {C} is {B}, {C}, {A}")

#del variable
# x=20
# del(x)
# x=40
# print(x)

#Findng final price after discount at 100$ margin price
IP=100
DP=int(input("Enter your desired Percentage :\n"))
SP=IP-(DP/100*IP)
if SP>=80:
    print(f"After considering your demand for {DP} the Selling price amounts to {SP}$ which we can make.")
else:
    print(f"Your Targeted price amounts to {SP} You should lower your percentage or try visiting other shops. Thank you")
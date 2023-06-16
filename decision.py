# #if else elif
try:
    age=int(input("Please enter your age\n"))
except ValueError:
    print("!!!Invalid input! Please enter a valid integer.")
if age==18:
    print("You just enter the voting age.")
elif age<18:
    print("You are not allowed")
elif age>=90:
    print("you are too old for this shit")
else:
    print("You cna cast the vote")


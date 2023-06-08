#Global and local variables
a=100 #Global variable outside a function can print anywhere

def test():
    print(a)
print(a)
test()
print(a)
 #Defining a local variable
def test2():
    b=50
    print(b)
test2()
# b=50

print(b) #throws error as the variable is local in nature


numbers = [23,56,78,7,2,43,67,89,12,456,550,786,75,11,10]
numbers.sort(reverse=True)
print(numbers[1])



# For Loop and while loop

# print your name for 100 times
range(5) # 0,1,2,3,4
name = "sipalaya"
for i in name:
    print(i)


i = 0 # initialization
while i < 10: # condition checking
    print(i)
    if i == 5:
        continue
    print("sipalaya")
    i = i + 1 # inc/decr
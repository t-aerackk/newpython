a=[2,4,6,8,9]
num=[]
for i in a:
    num.append(i**2)
print(num)

teamA=['A','B', 'C', 'D']
teamB=['E', 'F', 'G','H']
team=[(x,y)for x in teamA for y in teamB]
print(team)
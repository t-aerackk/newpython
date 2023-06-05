number = 10
def show():
    print("hello world")


def add():
    for i in range(1000):
        yield i

result = add()

for i in result:
    print(i)

a = [2, '+', 3, '*', 4, '/', 5]
stack = []

for i in a:
    if type(i) == int:
        print(i, end=" ")

import sys
sys.stdin = open("sw4873.txt")

t = int(input())

for tc in range(1, t+1):
    string = list(input())
    stack = [] 
    for i in range(len(string)):
        if stack == [] or stack[-1] != string[i]:
            stack.append(string[i])
        elif stack != [] and stack[-1] == string[i]:
            stack.pop()
    print('#{} {}'.format(tc, len(stack)))

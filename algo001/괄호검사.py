import sys

sys.stdin = open("4866input.txt","r")

tc = int(input())
for tc in range(1, tc+1):
    data = input()
    stack = []
    for i in range(len(data)):  # 짝이 맞는지만 검사
        if data[i] == "(" or data[i] == "{":
            stack.append(data[i])
        elif data[i] == ")" or data[i] == "}":
            if len(stack) == 0:
                stack.append(data[i])
                break
            elif data[i] == ")" and stack[-1] != "(":
                stack.append(data[i])
                break
            elif data[i] == "}" and stack[-1] != "{":
                stack.append(data[i])
                break
            else:
                stack.pop(-1)

    if len(stack) == 0:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))
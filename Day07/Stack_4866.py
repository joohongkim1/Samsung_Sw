def parentheses(code):
    stack = []
    top = -1
    for i in range(len(code)):
        if code[i] == "(" or code[i] == "{":
            stack.append(code[i])
            top += 1
        elif code[i] == ")" or code[i] == "}":
            if len(stack) == 0:
                return 0
            elif (code[i] == "}" and stack[top] !="{") or (code[i] == ")" and stack[top] != "("):
                return 0
            else:
                stack.pop()
                top -= 1
    if stack == []:
        return 1
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    print('#{} {}'.format(tc, parentheses(code=input())))
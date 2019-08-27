'''
Forth라는 컴퓨터 언어는 스택 연산을 기반으로 하고 있어 후위 표기법을 사용한다.
예를 들어 3+4는 다음과 같이 표기한다.
3 4 + .
Forth에서는 동작은 다음과 같다.
숫자는 스택에 넣는다.
연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.
‘.’은 스택에서 숫자를 꺼내 출력한다.
Forth 코드의 연산 결과를 출력하는 프로그램을 만드시오.
만약 형식이 잘못되어 연산이 불가능한 경우 ‘error’를 출력한다.
'''

import sys
sys.stdin = open("4874input.txt", "r")


TC = int(input())

for tc in range(1, TC+1):
    stack = []
    cal = ["+", "-", "/", "*", "."]
    top = -1
    code = list(map(str, input().split()))
    print('#%d' % tc, end=' ')
    for i in range(len(code)):
        if code[i] not in cal:
            stack.append(int(code[i]))
            top += 1
        elif code[i] == '+':
            if len(stack) < 2:
                print("error")
                break
            result = stack[top-1] + stack[top]
            stack.pop()
            stack.pop()
            stack.append(result)
            top -= 1
        elif code[i] == '-':
            if len(stack) < 2:
                print("error")
                break
            result = stack[top-1] - stack[top]
            stack.pop()
            stack.pop()
            stack.append(result)
            top -= 1
        elif code[i] == '/':
            if len(stack) < 2:
                print("error")
                break
            if stack[top] == 0:
                print("error")
                break
            result = int(stack[top-1] / stack[top])
            stack.pop()
            stack.pop()
            stack.append(result)
            top -= 1
        elif code[i] == '*':
            if len(stack) < 2:
                print("error")
                break
            result = stack[top-1] * stack[top]
            stack.pop()
            stack.pop()
            stack.append(result)
            top -= 1
        elif code[i] == '.':
            if len(stack) != 1:
                print("error")
            else:
                print(stack[0])

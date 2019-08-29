import sys
sys.stdin = open("4874input.txt", "r")


def operator(x, oper, y):
    if oper == '+':
        return x + y
    elif oper == '-':
        return x - y
    elif oper == '*':
        return x * y
    elif oper == '/':
        if y != 0:
            return x // y


TC = int(input())

for tc in range(1, TC+1):
    data = list(input().split())
    n = len(data)  # 반복횟수
    stack = []
    print('#{}'.format(tc), end=' ')

    for i in range(n):  # 연산식 만큼 반복
        # 숫자이면 스택에 저장
        if data[i].isdigit():  # 숫자인가?
            stack.append(data[i])
        else:  # 숫자 아니면
            # 후위 표기법 계산
            if data[i] != '.':
                if len(stack) > 1:
                    num1, num2 = int(stack.pop()), int(stack.pop())
                    stack.append(operator(num2, data[i], num1))
                else:
                    print("error")
                    break
            else:
                if len(stack) != 1:
                    print('error')
                    break
                else:
                    print(stack[0])
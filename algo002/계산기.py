import sys
sys.stdin = open("계산기input.txt")
'''
우선순위 : ( 괄호 3, (*, /) 2 , (+, -),  )괄호 0 
'''

for tc in range(1, 11):
    length = int(input())
    cal = list(input().split())
    oper = ['*', '+', '(', ')']
    stack = []
    for i in cal[0]:  # 토큰이 피연산자면 토큰 출력
        if i not in oper:
            print(i, end='')

        if i == '(':  # 스택 밖 '('는 우선순위 가장 높으므로 만나면 push
            stack.append(i)

        elif i == '*':  # 스택 안에서 '*'보다 우선순위 높은 것 없음
            stack.append(i)

        elif i == '+':  # '+'보다 우선순위 낮은 '(' 가 나왔을 경우에만 push
            while True:
                if stack[-1] == '(':
                    break
                stack.pop()
            stack.append(i)
#
        elif i == ')':  # ')'인 경우 stack[-1] 에 '(' 올 때까지 pop하고 출력
            while stack[-1] != '(':
                if stack == '(':
                    stack.pop()  # '(' 만나면 pop 만 하고 출력 안 함
                    break
                oper1 = stack.pop()
                print(oper1, end= '')

    print()



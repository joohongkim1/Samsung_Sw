import sys
sys.stdin = open("4873input.txt", "r")


TC = int(input())
for tc in range(1, TC+1):
    data = list(input())
    n = len(data)
    stack = []
    for i in range(n):
        # 스택이 비어있거나 스택 마지막 값이 현재 처리할 값과 다르면 저장
        if not stack or stack[-1] != data[i]:
            stack.appe
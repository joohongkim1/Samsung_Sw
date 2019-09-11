import sys
sys.stdin = open("5099_input.txt")


TC = int(input())
for tc in range(1, TC+1):
    n, m = map(int, input().split())
    cheese = list(map(int, input().split()))
    queue = []
    for i in range(n):
        queue.append(cheese[i])
        cheese.pop(0)
    while queue:
        if queue[0] != 0:
            queue[0] //= 2
            cheese.append(queue[0])
            queue.append(cheese[0])
            cheese.pop(0)
            queue.pop(0)
        else:
            if len(queue) == 1:
                print(queue[0])
                break
            else:
                queue.pop(0)


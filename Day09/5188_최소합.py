import sys
sys.stdin = open("5188_input.txt")


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    my_map = []
    for i in range(N):
        my_map.append(list(map(int, input().split())))


def perm(k):
    if k == N:
        print(t)
    else:
        for i in range(N):
            if visited[i]:
                continue
            t[i] = k
            visited[i] = 1
            perm(k+1)
            visited[i] =0



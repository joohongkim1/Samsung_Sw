import sys
import time
sys.stdin = open("palin_input.txt")
start = time.time()


TC = int(input())

for tc in range(1, TC+1):
    n, m = map(int, input().split())
    string = [input() for _ in range(n)]
    sero_str = [[a for a in t] for t in zip(*string)]
    print('#%d' % tc, end=' ')

    for i in range(n):
        for j in range(n-m+1):
            if n == m:
                if string[i][j:] == string[i][::-1]:
                    print(string[i][j:j+m])
                    break
            else:
                if string[i][j:j+m] == string[i][j+m-1:j-1:-1]:
                    print(string[i][j:j+m])
                    break
    for i in range(n):
        for j in range(n-m+1):
            if n == m:
                if sero_str[i][j:] == sero_str[i][::-1]:
                    print(''.join(sero_str[i][j:j+m]))
                    break
            else:
                if sero_str[i][j:j+m] == sero_str[i][j+m-1:j-1:-1]:
                    print(''.join(sero_str[i][j:j+m]))

print("time :", time.time() - start)
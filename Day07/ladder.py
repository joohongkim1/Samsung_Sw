def wall(x, y):
    delta = [[0, -1], [0, 1], [-1, 0]]
  
    if y - 1 < 0: 
        delta = [(0, 0), (0, 1), (-1, 0)]
    elif y + 1 > 99:
        delta = [(0, -1), (0, 0), (-1, 0)]
    
    return delta  
  
for _ in range(10):
    tc = int(input())
    s = [0] * 100
    for i in range(100):
        s[i] = list(map(int, input().split()))
      
    x = 99
    y = s[99].index(2)
  
    while x > 0:
        delta = wall(x, y)
        if s[x][y+delta[0][1]] == 1:
            y -= 1
            s[x][y] = 0
        elif s[x][y+delta[1][1]] == 1:
            y += 1
            s[x][y] = 0
        elif s[x+delta[2][0]][y] == 1:
            x -= 1
            s[x][y] = 0
  
    print('#%d %d' % (tc, y))
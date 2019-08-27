for tc in range(1, 11):
    n = int(input())
    l = []
    count = 0
    for _ in range(8):
        temp = list(input())
        l += [temp]
    
    
    for i in range(8):
        result = True
        for j in range(9-n):
            for k in range(n):
                if l[i][j+k] != l[i][j+n-k-1]:
                    result = False
                    break
            else:
                count += 1
    
    for j in range(8):
        result = True          
        for i in range(8-n+1):
            count = 0
            for k in range(n):
                if l[i+k][j] != l[i+n-k-1][j]:
                    result = False
                    break
            else:
                count += 1
  
    print('#{} {}'.format(tc, count))
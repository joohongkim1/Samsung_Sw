t = 10

for i in range(1, t+1):
    cnt = 0
    dump = int(input())
    height = list(map(int, input().split()))
    for a in range(len(height)-1, 0, -1):
        for b in range(0, a):
            if height[b] > height[b+1]:
                height[b], height[b+1] = height[b+1], height[b]
        
    while cnt < dump:
        cnt += 1
        height[-1] -= 1
        height[0] += 1
        
        for a in range(len(height)-1, 0, -1):
            for b in range(0, a):
                if height[b] > height[b+1]:
                    height[b], height[b+1] = height[b+1], height[b]
       
    print('#%d %d' % (i, height[-1] - height[0]))

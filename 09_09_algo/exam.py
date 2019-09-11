a = '0F97A3'

scale = 16
bits = 8

for i in range(len(a)):
    result = bin(int(a[i], scale))[2:].zfill(bits)
    print(result)




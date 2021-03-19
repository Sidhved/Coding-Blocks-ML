#Algo easy lvl 
n = int(input())
for i in range(n):
    b = int(input())
    num = 0
    p = 0
    while(b):
        r = b%10
        num += (2**p)*r
        p += 1
        b = b//10
    print(num) 
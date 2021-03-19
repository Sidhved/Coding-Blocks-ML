#algo lvl 0
x = int(input())
for i in range(x):
    if i == 0:
        print(1)
    else:
        print(str(i) +"0"*(i-1)+str(i))
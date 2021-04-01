for i in range(1, int(input())+1):
    if i%2 != 0:
        print("1"*i)
    else:
        print("1"+"0"*(i-2)+"1")
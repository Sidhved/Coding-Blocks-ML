'''
Peter wants to generate some prime numbers for his cryptosystem. Help him! Your task is to generate all prime numbers between two given numbers!
'''

def checkPrime(start, end):
    l = []
    for i in range(start, end+1):
        r = -1
        for j in range(2, i//2+1):
            if i % j == 0:
                r = 0
                break
            elif j == i//2 and i % j != 0:
                r = 1
        if r == 1:
            l.append(i)
        elif i == 2:
            l.append(i)
        elif i == 3:
            l.append(i)
    return l

if __name__ == "__main__":
    for _ in range(int(input())):
        s, e = map(int, input().split())
        res = checkPrime(s, e)
        for i in res:
            print(i, end=" ")
        print()

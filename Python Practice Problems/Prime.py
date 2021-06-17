'''
Take as input a number N, print "Prime" if it is prime if not Print "Not Prime".
'''

def checkPrime(N):
    for i in range(2, N//2+1):
        if N % i == 0:
            print("Not Prime")
            break
        elif i == N//2 and N%i != 0:
            print("Prime")

if __name__ == "__main__":
    n = int(input())
    checkPrime(n)

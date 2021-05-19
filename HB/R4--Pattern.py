'''20/05/2021
Take as input N, a number. Print the pattern according to given input and output section.'''

def Pattern(n):
    for i in range(1, n+1):
        print("*"*i)

if __name__ == "__main__":
    Pattern(int(input()))
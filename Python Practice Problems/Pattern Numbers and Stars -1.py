'''Take as input N, a number. Print the pattern as given in output section for corresponding input.

Input Format
Enter value of N'''

N = int(input())

for i in range(N):
    if i == 0:
        for j in range(1, N+1):
            print(j, end= " ")
    else:
        for j in range(1, N+i):
            if N-i > j-1:
                print(j, end= " ")
            else: 
                print("*", end= " ")
    print()
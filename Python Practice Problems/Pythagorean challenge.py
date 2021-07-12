'''
Given a non negative integer A, print all the pairs of integers(a,b) such that

a and b are positive integers

a<=b and

a^2 + b^2 = A

0 <= A
'''

import math
n = int(input())
for i in range(n):
    p = int(input())
    for j in range(int(math.sqrt(p)) + 1):
        for k in range(j, int(math.sqrt(p)) + 1):
            if(j**2 + k**2 == p):
                print('(' + str(j) +','+str(k)+')', end = " ")

    print()
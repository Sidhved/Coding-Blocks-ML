'''Given a list of numbers, stop processing input after the cumulative sum of all the input becomes negative.

Input Format
A list of integers to be processed'''

sum = 0
n = int(input())
sum = n
while(sum >= 0):
    print(n)
    n = int(input())
    sum += n
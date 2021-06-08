'''Given an integer 'n'. Print all the possible pairs of 'n' balanced parentheses.
The output strings should be printed in the sorted order considering '(' has higher value than ')'.

Input Format
Single line containing an integral value 'n'.'''

def Display(str, n):
    if(n>0):
        disp(str, 0, n, 0, 0)
    return

def disp(str, pos, n, open, close):
    if(close == n):
        for i in str:
            print(i, end = "")
        print()
        return
    else:
        if(open>close):
            str[pos]= ")"
            disp(str, pos+1, n, open, close + 1)
        if(open < n):
            str[pos] = "("
            disp(str, pos + 1, n, open +1, close)

if __name__ == "__main__":
    n = int(input())
    str = [""]*2*n
    Display(str, n)

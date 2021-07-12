arr = []
n = int(input())
for i in range(n):
    arr.append(int(input()))
'''
prev = arr[0]
flag = 0
count = 0

for i in arr:
    if i > prev:
        if flag == 0:
            count +=1
        flag = 1

    else:
        if flag == 1:
            count += 1
        flag = 0
    
    prev = i

if count > 1:
    print('false')
else:
    print('true')



def valley(l): 
  n=len(l)
  downhill=0
  uphill=0
 
  
  for i in range(0,n-1):
      
    if(l[i]>l[i+1]):
       downhill +=1
    else:
      if i==(n-1):
        break
      elif(l[i]<l[i+1]):
        uphill +=1
      else:
          return(False)
  return(True)

if valley(arr):
    print('true')
else:
    print('false')

'''

def minpoint(arr, n, k):
    min_point = 0
    for i in range(1, k-1):
         
        # Increment min_point
        # if element at index i
        # is smaller than element
        # at index i + 1 and i-1
        if(arr[i] < arr[i - 1] and arr[i] < arr[i + 1]):
            min_point += 1
 
    # final_point to maintain maximum
    # of min points of subarray
    final_point = min_point
     
    # Iterate over array
    # from kth element
    for i in range(k, n):
         
        # Leftmost element of subarray
        if(arr[i - ( k - 1 )] < arr[i - ( k - 1 ) + 1] and\
           arr[i - ( k - 1 )] < arr[i - ( k - 1 ) - 1]):
            min_point -= 1
         
        # Rightmost element of subarray
        if(arr[i - 1] < arr[i] and arr[i - 1] < arr[i - 2]):
            min_point += 1
         
        # if new subarray have greater
        # number of min points than previous
        # subarray, then final_point is modified
        if(min_point > final_point):
            final_point = min_point
     
    # Max minimum points in
    # subarray of size k
    print(final_point)
 
# Driver Code
if __name__ == "__main__":
    minpoint(arr, n, n)
from numpy import *
A = [2,3,5,7,10]
W = 14

# todo creat 2d matrix
arr = zeros((len(A)+1,W+1),dtype=int)
# print(arr)

# todo set 0th collom = 1
for i in range(len(A)+1):
    for j in range(W+1):
        arr[i][0] = 1

print(arr)

for i in range(1,len(A)+1):
    for j in range(1,W+1):

        if j<A[i-1]:
            arr[i][j] = arr[i-1][j]

        if j>=A[i-1]:
            arr[i][j] = arr[i-1][j] or arr[i - 1][j-A[i-1]]
print(arr)
print(arr[len(arr)-1][W])


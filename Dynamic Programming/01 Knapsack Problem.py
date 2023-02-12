from numpy import *

# item = [1,2,3]
# Profit = [10,12,28]
# weight = [1,2,4]
# W = 6

item = [1,2,3,4,5,6]
Profit = [20,15,7,5,9,3]
weight = [10,5,6,3,7,9]
ratio_data = {}
W = 20
# item = [1,2,3,4]
# Profit = [70,80,90,200]
# weight = [20,30,40,70]
# W = 60

# todo creat a 2d matrix
arr = ones((len(item)+1,W+1),int)
print(arr)

# todo if weight = 0 or item = 0 then profile = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[0][j] = 0
        arr[i][0] = 0
print(arr)

# todo start store value in our arr
for i in range(1,len(arr)):
    for j in range(1,len(arr[i])):
        if weight[i-1]<=j:
            arr[i][j] = max(Profit[i-1]+arr[i-1][j-weight[i-1]],arr[i-1][j])
        else:
            arr[i][j] = arr[i-1][j]

print(arr)
print(f"Maximum Profit is: {arr[len(arr)-1][W]}")
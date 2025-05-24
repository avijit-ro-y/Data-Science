#Rotate Array from right to left of k times

nums = [1,2,3,4,5,6,7]
k = 3
def rotate(nums,k):
    #1.reverse entire array
    left=0
    right=len(nums)-1
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1 
        
    #2.reverse first k element of array
    left=0
    right=k-1
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1 

    #3.reverse rest elment of array
    left=k
    right=len(nums)-1
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1 
    return nums
print(rotate(nums=nums,k=k))

#Given an array and an integer k,find the subarray where sum equals k

def subarray(array, target):
    prefix_sum = 0
    prefix_map = {0: -1}  

    for i in range(len(array)):
        prefix_sum += array[i]


        if (prefix_sum - target) in prefix_map:
            left = prefix_map[prefix_sum - target] + 1
            right = i
            print(array[left:right + 1])


        prefix_map[prefix_sum] = i


arr = [1, 4, 1, 2, 2, -1, 4, -7, 3, 4]
target = 7
subarray(arr, target)

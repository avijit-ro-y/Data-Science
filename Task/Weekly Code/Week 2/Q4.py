def min(array,student_no):
    sorterd_array=sorted(array)
    sum=float('inf')
    for i in range(len(sorterd_array)):
        
        if i+student_no<len(array):
            min_num=sorterd_array[i]
            max_num=sorterd_array[i+student_no-1]
            sum1=max_num-min_num
            if sum1<sum:
                sum=sum1
    return sum    
arr = [3, 4, 1, 9, 56, 7, 9, 12]
m = 5
output=min(arr,m)
print(output)
arr = [7, 3, 2, 4, 9, 12, 56]
m = 3
output=min(arr,m)
print(output)
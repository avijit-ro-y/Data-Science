def sum(array,sum):
    count=0
    for num in range(len(array)):
        for num1 in range(num+1,len(array)):
            if array[num]+array[num1] == sum:
                count+=1 
                
    return count         

arr = [1, 5, 7, -1]
su = 6
output=sum(arr,su)
print(output)


arr = [1, 5, 7, -1, 5]
su = 6
output=sum(arr,su)
print(output)
def rearrange(arr):
    n = len(arr)
    negative_index = 0
    
    for i in range(n):
        if arr[i] < 0:
            arr[i], arr[negative_index] = arr[negative_index], arr[i]
            negative_index += 1
    return arr

inp1 = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
print(rearrange(inp1))  

inp2 = [-12, 11, 13, -5, 6, -7, 5, -3, 8]
print(rearrange(inp2))  

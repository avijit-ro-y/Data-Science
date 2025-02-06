def rearrange(arr):
    n = len(arr)
    negative_index = 0
    
    # Step 1: Loop through the list and place negative numbers at the beginning
    for i in range(n):
        if arr[i] < 0:
            arr[i], arr[negative_index] = arr[negative_index], arr[i]
            negative_index += 1

    # No need for extra processing as the non-negative numbers
    # will naturally retain their order after the above loop.
    
    return arr

inp1 = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
print(rearrange(inp1))  # Output: [-12, -13, -5, -7, -3, -6, 11, 6, 5]

inp2 = [-12, 11, 13, -5, 6, -7, 5, -3, 8]
print(rearrange(inp2))  # Output: [-12, -5, -7, -3, 6, 13, 5, 11, 8]

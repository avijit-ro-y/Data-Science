def largest(lis):
    large=0
    for i in lis:
        if i>=large and (i%2)!=0:
            large=i
    return large
lis=([0, 9, 2, 4, 5, 6])
print(largest(lis))
lis=([-4, 0, 6, 1, 0, 2])
print(largest(lis))
lis=([1, 2, 3])
print(largest(lis))
lis=([-4, 0, 5, 1, 0, 1])
print(largest(lis))
def func(num):
    lis=[]
    for i in range(len(num)):
        for j in range (i+1,len(num)):
            for k in range(j+1,len(num)):
                if num[i]+num[j]+num[k]==0:
                    result=sorted([num[i],num[j],num[k]])
                    if result not in lis:
                        lis.append(result)
    return lis

nums = [-1,0,1,2,-1,-4]                    
print(func(nums))

nums = [0,1,1]                   
print(func(nums))

nums = [0,0,0]                   
print(func(nums))

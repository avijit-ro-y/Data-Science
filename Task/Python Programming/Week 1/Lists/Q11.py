lis=['A', 'B', 'C', 'D', 'E', 'F']
fnal=[]
for i in range(len(lis)):
    if i!=0 and i!=4 and i!=5:
        fnal.append(lis[i])
print(fnal)
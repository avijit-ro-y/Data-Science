inpu = input("Enter number:")
inp = [int(num) for num in inpu.split(',')]
lis=[]
for i in range(1,len(inp),2):
        lis.append(inp[i])
print(lis)
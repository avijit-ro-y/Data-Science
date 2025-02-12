inp=str(input("Enter the string:"))
sett=[]
for i in inp:
    if i in sett:
        continue
    else:
        sett.append(i)
output=''.join(sett)
print(output)


user_input = input("Enter numbers:")
inp = [int(num) for num in user_input.split(',')]
res=[]
for i in inp:
    if i>500:
        break
    elif i>150:
        continue
    elif i%5==0:
        res.append(i) 
print(res)
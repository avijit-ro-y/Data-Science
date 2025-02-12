import numpy as np

a=np.random.randint(low=0,high=99+1,size=10)

b=np.random.randint(low=-10,high=10+1,size=(3,4))

b_flat=b.ravel()

a_copy=a.copy()
a_copy[0]=-1

c=a[::2]

print(a[2])
print(b[-1,-1])
print(b[:2,-2:])
b_row=b[1,:]
b_col=b[:,0]

d=np.arange(1,11)

e=np.concatenate((a,d))

b_double=2*b

f=np.dot(b,b_double.T)
print(f)

g=np.array([np.mean(a),np.mean(b),np.mean(b_double)])
print(g)

a_sum=np.sum(a)
print(a_sum)

b_min=np.min(b)
print(b_min)

b_double_max=np.max(b)
print(b_double_max)
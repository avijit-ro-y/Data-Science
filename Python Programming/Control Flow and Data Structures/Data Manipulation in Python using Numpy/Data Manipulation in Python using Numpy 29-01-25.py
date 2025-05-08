#---------------------------------numpy---------------------------------

#---------------------------------multi dimensional array---------------------------------

import numpy as np

print(list(range(0, 10, 2)))
output=np.arange(15)
print(output,'\n')

#---------------------------------reshape---------------------------------
output=np.arange(15).reshape(3,5) #row collumne divide kore
print(output)

op1=np.arange(24).reshape(2,3,4) #3rd array
print(op1,'\n')

#---------------------------------shape---------------------------------
print(output.shape,'\n')

#---------------------------------dimension---------------------------------
print(output.ndim,'\n')

#---------------------------------type---------------------------------
print(output.dtype,'\n')

#---------------------------------itemsize---------------------------------
print(output.itemsize ,'\n')

#---------------------------------array creation---------------------------------
array=np.array([2,3,4])
print(array,'\n')

#---------------------------------zero/one array creation---------------------------------
zero=np.zeros((3,4)) #2 dimensional
one=np.ones((2,3,4)) #3 dimensional np.ones((num of array,row,collumn))
print(zero)
print(one,'\n')

#---------------------------------customized---------------------------------
x=(np.arange(start=10,stop=20,step=5,dtype='float64'))
print(x)
print('\n')
##---------------------------------linespaces---------------------------------
print(np.linspace(0,2,9),'\n') #9 number from 0 to 2

#---------------------------------oparation---------------------------------
a=np.array([20,30,40,50])
b=np.arange(4)
print(a-b)
print(b**5,'\n')

#---------------------------------random number generator---------------------------------
rg=np.random.default_rng(12)
print(rg.random((3,4)),'\n')

#---------------------------------indexing---------------------------------
a=np.arange(10)**3
print(a[3],'\n')

#---------------------------------slicing---------------------------------
print(a[0:7:2],'\n')

#---------------------------------reversed---------------------------------
print(a[::-1],'\n')

#---------------------------------Slice---------------------------------
c=np.arange(24).reshape(2,3,4)
print(c)
print(c[1,:,:])
print(c[1,1,:])
print(c[1,1,2])
print(c[:,:,2],'\n')

# ---------------------------------floor - cell---------------------------------
temp_array=rg.random((3,4))
temp_array=temp_array*10
print(temp_array)
print(np.floor(temp_array))
print(np.ceil(temp_array),'\n')

#---------------------------------ravel---------------------------------
print(temp_array.ravel(),'\n') #return the array flattened

#---------------------------------reshape---------------------------------
print(temp_array.reshape(12),'\n')

#---------------------------------transposed---------------------------------
print(temp_array.T,temp_array,'\n') #return the array tranposed

#---------------------------------stacking different array---------------------------------
a=np.floor(10*rg.random((2,2)))
print(a)
b=np.floor(10*rg.random((2,2)))
print(b)
join_row=np.vstack((a,b))
print(join_row)
join_collumn=np.hstack((a,b))
print(join_collumn)
print(np.concatenate((a,b)),'\n')

#---------------------------------random number---------------------------------
rand=np.random.rand(2,2,3)
print(rand,'\n')

#---------------------------------distribution---------------------------------
print(np.random.randint(low=2,high=10,size=(2,3)))
print(np.random.binomial(n=100,p=0.9,size=(2,5)),'\n') #n=number of trails p=probablity of success

#---------------------------------min-std---------------------------------
a = np.random.randn(10, 1000) #10,1000 shape, using normal dist, mean ~ 0, std~1
print(a)
print(a.shape)
print(np.mean(a))
print(np.std(a))
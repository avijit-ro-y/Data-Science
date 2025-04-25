#---------------------------------dictionary---------------------------------

#changeable
#dont have duplicate key

#---------------------------------declaration---------------------------------
cart={} #empty set is a dictionary
cart={'shirt':2300,'pant':1000}
print(cart)
cart={'shirt':2300,'1':['abc','xyz']}
print(cart)
cart=dict([('shirt',2300),('pant',1000)]) #Create by tuple and list
print(cart,'\n')

#---------------------------------change and add---------------------------------
bucket={'first':'python','2nd':'C++'}
bucket['2nd']='java'
print(bucket)
bucket['3rd']='c#'
print(bucket,'\n')

#---------------------------------keys---------------------------------
print(bucket.keys(),'\n')

#---------------------------------values---------------------------------
print(bucket.values(),'\n')

#---------------------------------items---------------------------------
print(bucket.items(),'\n') #list of tuples

#iterate
for i in bucket.items(): # or bucket.key()  ,  bucket.val()
    print(i)

#---------------------------------get---------------------------------
print(bucket.get('4th','c'),'\n') #if any element was not present at the dict

#---------------------------------access---------------------------------
print(bucket.get('first'),'\n') #duivabe kora jay

#---------------------------------update---------------------------------
bucket['first']=100
print(bucket,'\n')

#---------------------------------add two dict---------------------------------
student_grades1 = {
    "Alice": 90,
    "Bob": 85,
}
student_grades2 = {
    "Charlie": 88,
    "David": 92
}
student_grades1.update(student_grades2)
print(student_grades1,'\n')

#---------------------------------remove particular---------------------------------
bucket.pop('first')
print(bucket,'\n')

#---------------------------------remove any---------------------------------
bucket.popitem()
print(bucket,'\n')

#---------------------------------clear---------------------------------
bucket.clear()
print(bucket)

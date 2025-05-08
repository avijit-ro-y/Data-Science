#---------------------------------Tuples---------------------------------
# ---------------------------------Tuple Declaration and Initialization ---------------------------------
#unlike lists, tuples are immutable
task_bar = ('File', ('New', 'Save', 'Save As'), ['Insert','Clip Art', 'Table'])
print(task_bar,'\n')

#---------------------------------Concatenating---------------------------------
#concatenating tuples
t = ('File','Save') + ('New',)
print(t,'\n')

#---------------------------------repeat---------------------------------
#repeat the elements in a tuple for a given number of times using the * operator.
t = (('File',)  * 4)
print(t,'\n')

#---------------------------------Indexing---------------------------------
t = (1, 2, 1, 2, 6, 3, 1, 3, 3, 4, 1)
print(t.index(1),'\n') # return index of the first occurence of the element

#---------------------------------Functions---------------------------------
tup = (1, 8, 4, 4, 5, 6, 15, 6, 6, 7, 2, 3, 5)

print("6 occurs,", tup.count(6), "times") # count the frequency of a particular element

print("Sorted Tuple", tuple(sorted(tup))) # sorted returns the list

print("Maximum element is:", max(tup)) # maximum element and minimium element
print("Minimum element is:", min(tup))

# Finding the total of elements
print("Total is:", sum(tup),'\n')
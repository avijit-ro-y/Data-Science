#---------------------------------List---------------------------------
#---------------------------------Adding ---------------------------------
grocery_list = []
grocery_list = ['cake', 'milk']
number_list = [1, 2, 3, 4, 4, 4, 4]
print(number_list,'\n')

grocery_list.append('chips')
print(grocery_list,'\n')

grocery_list[0], grocery_list[1] = grocery_list[1], grocery_list[0]
print(grocery_list,'\n')

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list)
my_list.append([555, 12]) #add as a single element
print(my_list)
my_list.extend([234, 'string_data']) #add as different elements
print(my_list)
my_list.insert(5, 'insert_element') #add element i
print(my_list,'\n')

#---------------------------------Deleting---------------------------------
my_list = [1, 2, 3, 'example', 3.132, 10, 'example', [30,'2']]
del my_list[5] #delete element at index 5
print(my_list)

my_list.remove('example') #remove element with value(from the first occurence)
print(my_list)

a = my_list.pop(3) #pop element from list, if no index is given it will pop the last element in the list
print('Popped Element: ', a, ' List remaining: ', my_list)

my_list.clear() #empty the list
print(my_list,'\n')

#---------------------------------Accessing---------------------------------
print(my_list[0:2]) #access elements from 0 to 1 and exclude 2

print(my_list[::-1],'\n') #access elements in reverse

#---------------------------------Converting---------------------------------
# converting string to a list of words
text = "Hello, we are learning python, dfjahsdfa"
lst = text.split(',')
print(lst)

keywords = "science, IoT, DS, ML"
keywords_lst = keywords.split(',')
print(keywords_lst,'\n')

#---------------------------------Function---------------------------------
#---------------------------------sorted---------------------------------
grocery_list = ['milk', 'cake', 'cake', 'milk', 'chips']
print(sorted(grocery_list))

matrix = [[12, 139],
          [14, 102],
          [11, 33]]
print(matrix)

m = [[12, 139], [14, 102], [11, 33]]
print(m[1][0],'\n')

#---------------------------------sorted---------------------------------
print(len(grocery_list),'\n')

#---------------------------------Reverse---------------------------------
cart=['shirt', 'trouser', 'tracksuit', 'watch']
print(cart)
cart.reverse()
print(cart)
print(sorted(cart, reverse = True),'\n')

#---------------------------------in/no in---------------------------------
#keyword 'in' is used to test if an item is in a list
if 'trouser' in cart:
  print('Already Added')

#keyword 'not' can combined with 'in'
if 'watch' not in cart:
  cart.append('watch')
  print('Item Added')
print(cart,'\n')

#---------------------------------Slicing---------------------------------
lst = [1.25, 3.26, 5, 2.3, 1, 7]
print(lst[:3],'\n')

#--------------------------------- Split---------------------------------
text = "Hello, we are learning python"
lst = text.split()
print(lst)
lst = text.split(',')
print(lst)

#--------------------------------- List comprehensions---------------------------------
nums = [0, 1, 2, 3, 4]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)


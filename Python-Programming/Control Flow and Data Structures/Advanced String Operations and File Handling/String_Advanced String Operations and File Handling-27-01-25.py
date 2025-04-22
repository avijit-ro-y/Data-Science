#-----------------------------------String-----------------------------------

#-----------------------------------Slicing-----------------------------------
stri="String is fun"
print(stri[:],'\n') 

#-----------------------------------Concatinate----------------------------------- 
# Sample text
first_name = "John"
last_name = "Doe"

# Using + operator for concatenation
full_name = first_name + " "+ last_name
print("Full name:", full_name,'\n')

#-----------------------------------Join-----------------------------------
# Sample list of words
words = ["Hello", "World", "in", "Python","hey "]

# Using str.join(iterable) for joining
joined_string = " ".join(words)
print("Joined string:", joined_string)

# Example using str.join()
words = ["Hello", "world", "from", "Python"]
sentence = "_".join(words)
print("Joined sentence:", sentence,'\n')

#-----------------------------------Find index of substring-----------------------------------
stri="String is fun"
position=stri.find("fun")
print(position,'\n')

#-----------------------------------Remove space-----------------------------------
stri=" String is fun "
text=stri.strip()
print(repr(text),'\n')

#-----------------------------------Replace-----------------------------------
stri="String is fun"
update=text.replace("String","Python") #update=text.replace(old,new) #update=text.replace(old,new,number of that replaced word)
print(update,'\n')

#-----------------------------------Conversion-----------------------------------
stri="String is fun"
up=stri.upper()
low=stri.lower()
print(up,"",low,'\n')

#-----------------------------------Capatilized and title-----------------------------------
stri="string is fun"
cap=stri.capitalize() #convert first character of string upper and other are lower
titl=stri.title() #convert first character of each word upper and other are lower
print(cap,"",titl,'\n')

#-----------------------------------Split-----------------------------------
stri="string is fun"
word=stri.split(',')
word1=stri.split()
print(word)
print(word1,'\n')

#-----------------------------------Start with-----------------------------------
stri="string is fun"
s=stri.startswith("string")
print(s,'\n')

#-----------------------------------Ends with-----------------------------------
stri="string is fun"
s=stri.endswith("fun")
print(s,'\n')

#-----------------------------------Type check-----------------------------------
stri="string is fun"
x=stri.isnumeric()
print(x)
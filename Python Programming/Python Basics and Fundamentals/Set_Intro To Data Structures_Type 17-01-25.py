#---------------------------------Set---------------------------------
#dont contain duplicate
#cant create empty set
#no index

#---------------------------------declaration---------------------------------
sets={1,3,5,7,6,7,8,9,2}
print(sets,'\n')

#---------------------------------tuple/list to set---------------------------------
new=set((1,3,5,6))
print(new)
print(type(new),'\n')

#---------------------------------empty set/dictionary---------------------------------
new1={}
print(type(new1),'\n')

#---------------------------------add---------------------------------
new.add(10)
print(new,'\n')

#---------------------------------update multiple item---------------------------------
new.update([14,15])
new.update((18,20))
print(new,'\n')

#---------------------------------update multiple item by string---------------------------------
charc='asd'
new.update(charc)
print(new,'\n')

#---------------------------------update multiple item by dict---------------------------------
dicti={'lock': 1 , 'lock2' : 2}
num={'a','c'}
num.update(dicti)
print(num,'\n')

#---------------------------------remove---------------------------------
language={'english','bangla','german'}  
language.remove('english')  #element ta na thakle error dibe
print(language,'\n')

#---------------------------------discard---------------------------------
language.discard('bangla')
print(language)
language.discard('franch')  #element ta jodi na thake tao error dibe na
print(language,'\n')

#---------------------------------pop---------------------------------
language={'english','bangla','german'}  
print(language,'\n') #random element remove hobe

#---------------------------------clear---------------------------------
language.clear()  #all clear kore
print(language,'\n')

#---------------------------------union---------------------------------
set1={1,3,5,7}
set2={2,4,6,8}
set3={9,10}
print(set1|set2|set3)
print(set1.union(set3),'\n') #duivabe union kora jay

#---------------------------------intersection---------------------------------
set1={1,3,5,7}
set2={1,2,4,5,6,8}
set3={1,9,10}
print(set1 & set2 & set3)
print(set1.intersection(set2),'\n') #duivabe kora jay

#---------------------------------diference---------------------------------
set1={1,3,5,7}
set2={1,2,4,5,6,8}
print(set1.difference(set2),'\n')

#---------------------------------subset---------------------------------
set1={1,3,5,7}
set2={3}
print(set2.issubset(set1),'\n')
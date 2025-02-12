words_list = ["Hello", "world", "Python", "PROGRAMMING"]
count=0
for word in words_list:
    for i in range(len(word)):
        if word[i].islower():
            count+=1
print(count)
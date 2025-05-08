#-----------------------------------File handel-----------------------------------
file=open("test.txt","w")
file.write("Hello,This is Avijit")
file.close()

#---r----------------read
#---r+---------------read+write(Don't overwrite)
#---w----------------write(it overwrite)
#---w+---------------read+write(it overwrite)
#---a----------------append
#---a+----------------append+read

#---read()-----------read entire file as a single string
fil='test.txt'
with open(fil,'r') as file:
    content=file.read()
    print(content)
#---readline()-------read a single line from file
#---readlines()------read all lines of the string


#----------------------------------CSV------------------------------------
#if file doesnot exist
import csv
fil='data.csv'
data_tobe_added=[
    ['avijit','roy','avi@gmail.com'],
    ['dev','das','dev@gmail.com']
]
with open(fil,mode='a',newline='\n') as file: # create+open csv file  #newline will help to write new row ..otherwise one line will be replaced bny the next line
    writer=csv.writer(file) #create csv writter obj
    
    # iterate each row in data_tobe_added and write it in csv file
    for row in data_tobe_added:
        #witerow() used to write row of data to csv
        writer.writerow(row) #write each row as a new line in csv file

print("Sucessfull!")
        
#----if the fiel exist
import csv
fil='data.csv'
with open(fil,mode='r') as file: # open csv file
    reader=csv.reader(file) #create csv reader obj
    
    # iterate each row in csv file
    for row in reader:
        print(row)
        
#-------------------------------------Json-----------------------------------
#if file doesnot exist
import json
fil='data.json'
data_tobe_added=[
    {"name":"avijit roy","mail":"avi@gmail.com"},
    {"name":"dev das","mail":"dev@gmail.com"}
]
with open(fil,mode='w+') as file: # open  file  
    json.dump(data_tobe_added,file,indent=4) #write the new data
print("Sucessfull!")

#-----if file exist------
import json
fil='data.json'
with open(fil,mode='r') as file: # open csv file
    display=json.load(file) #load the data

print(display)
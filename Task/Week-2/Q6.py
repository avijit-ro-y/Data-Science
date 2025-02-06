dict={
    "I":1,
    "IV":4,
    "V":5,
    "IX":9,
    "X":10,
    "XL":40,
    "L":50,
    "XC":90,
    "C":100,
    "CD":400,
    "D":500,
    "CM":900,
    "M":1000
}
def int_roman(string):
    integer_num=0
    i=0
    while i<len(string):
        if i<len(string)-1:
            if string[i:i+2] in dict:
                integer_num+=dict[string[i:i+2]]
                i=i+2
            else:
                integer_num+=dict[string[i]]
                i=i+1
        else:
            integer_num+=dict[string[i]]
            i=i+1
    return integer_num 

s = "III"     
print(int_roman(s))
s = "LVIII"     
print(int_roman(s))
s = "MCMXCIV"     
print(int_roman(s))
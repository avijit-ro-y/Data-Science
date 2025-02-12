dict={
    1000:"M",
    900:"CM",
    500:"D",
    400:"CD",
    100:"C",
    90:"XC",
    50:"L",
    40:"XL",
    10:"X",
    9:"IX",
    5:"V",
    4:"IV",
    1:"I"
     
}
def int_roman(num):
    roman=""
    for i in [1000,900,500,400,100,90,50,40,10,9,5,4,1]:
        roman+=(num//i)*dict[i]
        num=num%i
        if num==0:
            break
    return roman  

num = 3749      
print(int_roman(num))
num = 58      
print(int_roman(num))
num = 1994      
print(int_roman(num))
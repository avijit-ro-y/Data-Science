#---------------------------------Function---------------------------------

def fun(name,age):
    print(f"Hello "+str(name)+". "+"Your age is:"+str(age),'\n')
fun("Avijit",20)

#---------------------------------Without parameter---------------------------------
def fun():
    print("Hello world",'\n')
fun()

# ---------------------------------Parameter---------------------------------
def add(a,b):
    add=a+b
    if add>5:
        return "Sum is more than 5 , so inside function will print next"
    print(f"Inside of function:{add}")
    return add # return value to the caller
c=int(input("input1:"))
d=int(input("input2:"))
res=add(c,d)
print("Outside of function:",res,'\n')

# ---------------------------------default argument---------------------------------
def greet(name="Avi",msg="Good morning"):
    print(f"Hi {name} {msg}",'\n')

greet("Rahul","Good Noon")

#---------------------------------Keyword argument---------------------------------
#---------------------------------Kwargs---------------------------------

def greet(**kwargs):
    if kwargs:
        print("Hello {0} , {1} ,{2} ,{3}".format(kwargs['name'],kwargs['msg'],kwargs['roll'],kwargs['age']),'\n')
greet(name="ravi",msg="Hi",roll="12",age=9)

#---------------------------------args---------------------------------
def greet(*args):
    print(args)
    for name in args:
        print(f"Hello, {name}")
greet("avi",'jit','das')
print('\n')

#---------------------------------pass list as an argument---------------------------------

nums=[2,4,6,8]
def add(nums):
    su=0
    u=0
    for num in nums:
        su+=num
    return su,u
print(add(nums),'\n')
    
#---------------------------------global keyword---------------------------------
x=7
def foo():
    global x
    x=x*2
    print(x)
foo()
print(x,'\n')

#---------------------------------Types Of Functions---------------------------------
#---------------------------------abs()---------------------------------
# find the absolute value

num = -100

print(abs(num),'\n')

#---------------------------------isinstance---------------------------------

#check if a object is subclass of the class or not
var=[1,2,34,5,6]
print(isinstance(var,list))
print(isinstance(var,tuple),'\n')

#---------------------------------Lambda---------------------------------
#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.

product = lambda a, b : a*b
print(product(3, 7))

x = lambda a:a+10
print(x(5))

# combine first name and last name

full_name = lambda fn, ln : fn.title().strip() + " " + ln.title().strip()
print(full_name('Harjas     ', 'Singh    '))
print('\n')
#---------------------------------eval---------------------------------
#The eval() function is one of the Python built-in functions. The word ‘eval’ can be thought of as a short form for ‘evaluation’, which is the process of finding the output.
#Introduction to Python eval() function
#The function eval() is a built-in function that takes an expression as an input and returns the result of the expression on evaluation. Let us see the syntax of the eval() function.
#Syntax: eval(expression, globals=None, locals=None)
print(eval('3*8'),'\n')

#---------------------------------exec---------------------------------
#The exec() function executes the specified Python code.
#The exec() function accepts large blocks of code, unlike the eval() function which only accepts a single expression
#We must be careful that the return statements may not be used outside of function definitions not even within the context of code passed to the exec() function. It doesn’t return any value, hence returns None.
prog = 'print("The sum of 5 and 10 is", (5+10))'
exec(prog)

def summation(a, b):
    return a+b
exec("print(sum(5, 6))", {'sum':summation})   # here sum means summation

x = 'name = "John";print(name)'
exec(x)
print('\n')

#---------------------------------zip---------------------------------
#Iterate over several iterables in parallel, producing tuples with an item from each one.
#Syntax: zip(*iterables, strict=False)¶
for i,j in zip(range(4), ['fee', 'fi', 'fo', 'fum']):
    print(i,j)
    
for item in zip([1, 2, 3, 4,5], ['sugar', 'spice', 'chillies', 'everything nice',"hi"]):
    print(item)
print('\n')

#---------------------------------Date time functions---------------------------------
import datetime

x = datetime.datetime.now()
print(x)
print('\n')
#---------------------------------Decorators---------------------------------
# decorators.py

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        # Call the original function and convert the result to uppercase
        original_result = func(*args, **kwargs)
        return original_result.title()
    return wrapper

@uppercase_decorator
def say_hello(name):
    return f"Hello, {name}!"

# Assign the modified function to a new variable
greet = say_hello

# Test the greet function
if __name__ == "__main__":
    print(greet("harjas singh"),'\n')  # Output: HELLO, ALICE!

    # print(greet("Bob"))    # Output: HELLO, BOB!
    
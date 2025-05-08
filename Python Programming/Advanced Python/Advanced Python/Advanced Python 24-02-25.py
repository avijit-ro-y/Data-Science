#----------------------------------------------------------------Decorators---------------------------------------------------------------------
#Decorators in Python are a powerful tool that allows you to modify the behavior of functions or methods without modifying their actual code.
#A decorator is a function that takes another function as an argument and extends its behavior without explicitly modifying it.

def simple_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@simple_decorator  # Applying the decorator
def say_hello():
    print("Hello!")

say_hello()

#Decorators with Arguments
def args_decorator(func):
    def wrapper(n, *args, **kwargs):
        for _ in range(n):
            func(*args, **kwargs)
    return wrapper

@args_decorator  # Function will be executed 5 times
def greet(name):
    """This is an example function."""
    print(f"Hello, {name}!")

greet(5, "Alice")

#----------------------------------------------------------------Generators---------------------------------------------------------------------
# Generators are a special type of iterator in Python that allow you to iterate over a sequence of values lazily.
# They help in efficient memory usage and improve performance for large datasets.

# 1. Basic Generator Example
def simple_generator():
    yield 1
    yield 2
    yield 3

# Creating a generator object
gen = simple_generator()

# Iterating through generator
print(next(gen))  # Output: 1
# print(next(gen))  # Output: 2
# print(next(gen))  # Output: 3

#----------------------------------------------------------------Lambda Functions---------------------------------------------------------------------
#Lambda functions in Python are anonymous functions defined using the lambda keyword. They are often used for short, simple operations
# Normal function
def square(x):
    return x * x

# Equivalent lambda function
square_lambda = lambda x: x * x

print(square(5))  # Output: 25
print(square_lambda(5))  # Output: 25

def sqaure(x):
    return x * x



numbers = [1, 2, 3, 4]
squared = list(map(sqaure, numbers))
print(squared)  # Output: [1, 4, 9, 16]



numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]



people = [("John", 25), ("Alice", 30), ("Bob", 20)]
sorted_people = sorted(people, key=lambda x: x[1])
print(sorted_people)  # Output: [('Bob', 20), ('John', 25), ('Alice', 30)]
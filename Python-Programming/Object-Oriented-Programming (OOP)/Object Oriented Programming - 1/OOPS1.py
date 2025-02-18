#-----------------------------------Class-Object-----------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}.")

    def celebrate_birthday(self):
        self.age += 1
        print(f"It's my birthday! I am now {self.age} years old.")


# Creating objects of the Person class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Accessing attributes
print(person1.name)  
print(person2.age)   

# Invoking methods
print(person1.greet())           
print(person2.celebrate_birthday(),'\n')

#-----------------------------------Attributes and Methods-----------------------------------
class Polygon:

    # this is an attribute
    minimum_sides = 6

    # this is a method
    def area(self):
        print('area method was called!')
        pass

poly1 = Polygon()
poly2 = Polygon()

print(poly1.minimum_sides)
print(poly1.area(),'\n')

#-----------------------------------constractor-----------------------------------
class Rectangle:
  # constructor
    def __init__(self, breadth, height):
        self.breadth = breadth
        self.height = height

    def area(self):
        return self.breadth * self.height

r1 = Rectangle(5, 5)
print(r1.area())
r2=Rectangle(6, 7)
print(r2.area())
print(r2.breadth)
print(r2.height,'\n')

#-----------------------------------types of attribute-----------------------------------
class Polygon:

    # this is a class attribute
    minimum_sides = 3

    def __init__(self, sides):
        # this is an instance attribute
        self.sides = sides

poly1 = Polygon(4)
ploy2=Polygon(9)

print(poly1.sides)
print(poly1.minimum_sides)

print(ploy2.minimum_sides)
print(ploy2.sides,'\n')

#-----------------------------------getattr-----------------------------------
# we can also use the built-in getattr and setattr function
print(getattr(poly1, 'minimum_sides'),'\n') 

#-----------------------------------seter-----------------------------------
# this function doesn't return anything, it sets the value of the attribute provided to it
setattr(poly1, 'minimum_sides', 5) #replace value
print(poly1.minimum_sides,'\n')

#-----------------------------------dunder method-----------------------------------
#-----------------------------------init method-----------------------------------
class rect: 
    #constractor
    def __init__(self,depth,hight):
        self.depth=depth
        self.hight=hight
    def area(self):
        return self.depth*self.hight
r1=rect(4,3)
r2=rect(4,5)
print(r1.area())
print(r2.area(),'\n')

#-----------------------------------del method-----------------------------------
class rect: 
    #constractor
    def __init__(self,depth,hight):
        self.depth=depth
        self.hight=hight
    def __del__(self):
        print(f"deleted {self}")
    def area(self):
        return self.depth*self.hight
r1=rect(4,3)
print(r1.area(),'\n')

#-----------------------------------str method-----------------------------------
class rect: 
    #constractor
    def __init__(self,depth,hight):
        self.depth=depth
        self.hight=hight
    def __del__(self):
        print(f"deleted {self}")
    def __str__(self):
        return f"depth:{self.depth} and HEIGHT:{self.depth}"
    def area(self):
        return self.depth*self.hight
r1=rect(4,3)
print(r1.area(),'\n')

#-----------------------------------types of method-----------------------------------
#-----------------------------------Instance methods-----------------------------------
class Rectangle:

    minimum_sides = 3

    def __init__(self, breadth, height):
        self.breadth = breadth
        self.height = height

    # this is an instance method
    def area(self):
        return self.breadth * self.height

    def get_height(self):
        return self.height
    
    def get_breadth(self):
        return self.breadth

    def set_height(self, n):
        self.height = n

    def set_breadth(self, n):
        self.breadth = n

    # instance methods can also get and set class variables using self.__class__
    # to access class attributes that's why they are considered the most powerful
    def get_minimum_sides(self):
        return self.__class__.minimum_sides

    def set_minimum_sides(self, n):
        self.__class__.minimum_sides = n

r1 = Rectangle(4, 5)
print(r1.area())
print(r1.get_height())
print(r1.get_breadth())
print(r1.get_minimum_sides())

r1.set_height(10)
r1.set_breadth(20)
r1.set_minimum_sides(4)
print(r1.area())
print(r1.get_height())
print(r1.get_breadth())
print(r1.get_minimum_sides(),'\n')

#-----------------------------------class method-----------------------------------
class Rectangle:

    minimum_sides = 3

    def __init__(self, breadth, height):
        self.breadth = breadth
        self.height = height

    # class methods are decorated with the classmethod decorator,
    @classmethod
    def get_minimum_sides(cls):
        return cls.minimum_sides

    @classmethod
    def set_minimum_sides(cls, n):
        cls.minimum_sides = n

r1 = Rectangle(4, 5)
print(r1.get_minimum_sides())
r1.set_minimum_sides(5)
print(r1.get_minimum_sides())
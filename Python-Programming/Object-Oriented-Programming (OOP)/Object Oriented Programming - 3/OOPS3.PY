#------------------------Encapsulation------------------------
#the idea of encapsulation is to hide the information of an attribute from the end user so that the object has always has a valid state

#Public Members (attribute): attritbutes can be accessed anywhere
#Protected Memebers (_attribute): leading with single underscore, attributes can only be accessed in the class as well as child classes
#Private Members (__attribute): leading with double underscores, attributes can only be accessed in the class in which they were defined

class Employee:

    __company_name = 'Sabudh Foundation'
    __counter = 0 # a counter to keep a record of number of employees

    def __init__(self, name, age, employee_id):
        self.name = name
        self._age = age
        self._employee_id = employee_id

        self.__class__.__counter += 1

emp1 = Employee('Jane Doe', 30, 'EMP01')
# we can access public and protected attributes from an instance
print(emp1.name, emp1._age,'\n')

#------------------------getters and setters------------------------ 
#Getter: a method that allows us to access an attribute in a given class
#Setter: a method that allows us to set or mutate the value of an attribute in a class
class Employee:

    __company_name = 'Sabudh Foundation'
    __counter = 0 # a counter to keep a record of number of employees

    def __init__(self, name, age, employee_id):
        self.name = name
        self._age = age
        self._employee_id = employee_id

        self.__class__.__counter += 1

    @property
    # The @property decorator allows you to define a method that can be accessed like an attribute, meaning you can call it without parentheses.
    # This makes the code cleaner and more intuitive.
    def counter(self):
      # You first define a property using the @property decorator, which allows you to create a getter method.
      # This getter retrieves the current value of __counter, which is a class attribute that keeps track of the number of Employee instances.
        return self.__class__.__counter

    @counter.setter
    # After defining the getter, you can define a setter method for the same property using the @<property_name>.
    # setter decorator.
    #  This method allows you to set a new value for the counter.
    def counter(self, n):
        self.__class__.__counter = n

    @property
    def company_name(self):
        return self.__class__.__company_name


emp1 = Employee('Jane Doe', 30, 'EMP01')
emp2 = Employee('John Doe', 30, 'EMP02')

#------------------------property Decorator ------------------------
# now we can access our private attribute using the getter method
print(emp1.counter, emp2.counter)
# let's use the setter method
emp1.counter = 5
print(emp1.counter, emp2.counter,'\n')

#------------------------Polymorphism------------------------
#one thing with mltiple forms
# Polymorphism in addition operator
a = 5
b = 6

print(a + b)
print(int.__add__(a,b),'\n')

#------------------------Operator overloading#------------------------
# addition operator
class Student:
  def __init__(self,m1,m2):
    self.m1 = m1
    self.m2 = m2

  def __add__(self,other):
    r1 = self.m1 + other.m1
    r2 = self.m2 + other.m2
    return Student(r1, r2)

stu1 = Student(56,34)
stu2 = Student(67,78)
stu3 = stu1 + stu2
print(stu3.m1, stu3.m2,'\n')

#------------------------Method Overriding------------------------
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()

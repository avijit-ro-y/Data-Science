#--------------------------------------Inheritance---------------------------------------------
#allows us to define a class that inherits all the methods and attributes from another class

#------------------------Single Inheritance------------------------
# enables a derived class to inherit properties from a single parent class
class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def greet(self):
        print(f'Hello world! My name is {self.name}')


class Student(Person):

    def __init__(self, name, age, gender, standard):
        # this will call the parent class and pass the same arguments there
        # Person.__init__(self,name, age, gender)
        super().__init__( name, age, gender)
        # we can add extra fields than the parent class
        self.standard = standard


student1 = Student('John', 16, 'Male', '12th')
# although the child class didn't had the greet method but the parent class
# that it inherited from had, that's why there's no error
print(student1.greet(),'\n')

#------------------------Multilevel inheritance------------------------
#------------------------without the super method------------------------
# Define the Person class
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")
# Define the Company class
class Company:
    def __init__(self, company_name):
        self.company_name = company_name

    def display_company_info(self):
        print(f"Company: {self.company_name}")


# Define the Employee class that inherits from both Person and Company
class Employee(Person,Company):
    def __init__(self, name, age, gender, company_name):
        # Initialize both parent classes
        Person.__init__(self, name, age, gender)
        Company.__init__(self, company_name)

    def display_employee_info(self):
        # Display both Person and Company info
        self.display_person_info()
        self.display_company_info()

# as you can see it inherited from both of the parent classes
# but it is tedious to expicitily call every parent class constructor
# Create an Employee object
emp1 = Employee('John', 30, 'Male', 'Sabudh Foundation')

# Display information for emp1
print(emp1.display_employee_info(),'\n')

#------------------------using super keyword------------------------
#benifit last class e alada vabe sob class call kora lage na
class Person:

    def __init__(self, name, age, gender, *args, **kwargs):
        super().__init__(**kwargs)
        # *args and **kwargs: These parameters allow for variable numbers of arguments.
        #  *args captures positional arguments, while **kwargs captures keyword arguments.
        self.name = name
        self.age = age
        self.gender = gender

    def greet(self):
        print(f'Hello world! my name is {self.name}')


class Company:

    def __init__(self, company_name='Unknown', *args, **kwargs):
        super().__init__(**kwargs)
        self.company_name = company_name

    def description(self):
        print(f'I am an employee of {self.company_name}')


class Employee(Person,Company):

    def __init__(self, name, age, gender, company_name):
        # pass all arguments on as keyword
        # arguments to avoid problems with
        # positional arguments and the order
        # of the parent classes
        super().__init__(
            name=name,
            age=age,
            gender=gender,
            company_name=company_name
        )

emp1 = Employee('John', 30, 'Male', 'Sabudh Foundation')
print(emp1.description(),emp1.greet(),'\n')

# ------------------------Is-A Relationship------------------------
class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def greet(self):
        print(f'Hello world! My name is {self.name}')


class Employee(Person):

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

emp1 = Employee('John', 30, 'Male')
print(emp1.greet(),'\n')

# ------------------------Has-A relationship------------------------
import datetime

class Person:

    def __init__(self, name, dob, gender):
        self.name = name
        self.dob = dob
        self.gender = gender

    def get_age(self):
        dob_dt = datetime.datetime.strptime(self.dob, '%d-%m-%Y')
        today = datetime.date.today()
        return today.year - dob_dt.year - ((today.month, today.day) < (dob_dt.month, dob_dt.day))

    def greet(self):
        print(f'Hello world! My name is {self.name}')


class Employee:

    def __init__(self, name, dob, gender):
        self.name = name
        self.dob = dob
        self.gender = gender
        p1 = Person(name, dob, gender)


        if p1.get_age() < 18:
            raise TypeError('Candidate cannot be younger than 18 years old!')

    def description(self):
        print(f'Hello world! My name is {self.name} and my dob is {self.dob}')
        # p1.greet()


v1 = Employee('John', '01-12-2000', 'Male')
print(v1.description(),'\n')

#------------------------Abstraction------------------------
#Abstraction provides a programmer to hide all the irrelevant process of an application 
from abc import ABC, abstractmethod
class Polygon(ABC):

    @abstractmethod
    def area(self):
        pass

# implement abstract method in child class
class Rectangle(Polygon):

    def area(self):
        print('calculating area!')

obj = Rectangle()
print(obj.area(),'\n')

# ------------------------example------------------------
# a polygon has an area and perimeter, since every polygon has different,
# implementation to calculate area and perimeter, our base class will have these,
# function but the programmer has to override them so each will have it's own logic.
# as you can see we are only defining the methods and not implementing them.
class Polygon(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
# if we don't override all methods python will raise a TypeError,
# while instantiating them, this makes easier for a programmer to understand,
# what kind of method he/she needs to implement to properly write the implementation,
# and not encounter an error while creating an object.
class Rectangle(Polygon):

    def area(self):
        print('calculating area!')

    def perimeter(self):
        print('calculating perimeter!')

obj = Rectangle()
print(obj.perimeter(),'\n')
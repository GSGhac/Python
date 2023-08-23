#Create a class named Person, with firstname and lastname properties, and a printname method

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

#Create a class named Student, which will inherit the properties and methods from the Person class

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()

#add __init__ function

class Student(Person):
    def __init__(self,fname,lname):
        #add properties etc.

#When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

#The child's __init__() function overrides the inheritance of the parent's __init__() function.

#To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function

class Person:
    
     def __init__(self, fname, lname):
         Person.__init__(self, fname, lname)
     def printname(self):
         print(self.firstname, self.lastname)

class Student(Person):
     def __init__(self, fname, lname):
         Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()

#Add a property

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)

#Add a year parameter, and pass the correct year when creating objects

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)

#Add a method called welcome to the Student class

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()






    

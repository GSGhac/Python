#Creating a class
class MyClass:
    x=5

#Creating a object
p1 = MyClass()
print(p1.x)

#_init_ function
class Person:
    def _init_(self,name,age):
        self.name =name
        self.age =age
p1= Person("John",36)
print(p1.name)
print(p1.age)

#_str_ function
class Person:
    def _init_(self,name,age):
        self.name =name
        self.age =age

    def _str_(self):
        return f"{self.name}({self.age})"
p1 = Person("John",36)
print(p1)

#object method
class Person:
    def _init_(self,name,age):
        self.name=name
        self.age=age

    def myfunc(self):
        print("Hello my name is:"+self.name)
p1= Person("John",36)
p1.myfunc()

#self parameter
class Person:
    def _init_(mysillyobject,name,age):
        mysillyobject.name=name
        mysillyobject.age=age

    def myfunc(abc):
        print("Hello my name is"+abc.name)
p1= Person("John",36)
p1.myfunc()

#the pass statement
class Person:
    pass

#delete
#del p1
#del p1.age

#modify
#p1.age =40

#A variable is only available from inside the region it is created. This is called scope.
#Local scope:variable that is created inside a function .
def myfunc():
  x = 300
  print(x)

myfunc()

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

#Global scope:code generatesd in the main body of code.
x = 300

def myfunc():
  print(x)

myfunc()

print(x)


x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

#Global keyword
def myfunc():
  global x
  x = 300

myfunc()

print(x)
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)



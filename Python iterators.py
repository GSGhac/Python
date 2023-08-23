#An iterator is an object that contains a countable number of values.
#object that can be iterated upon,meaning traverse through all the values.
#an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

#Return an iterator from a tuple, and print each value:
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#Strings are also iterable objects, containing a sequence of characters:
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#Iterate the values of a tuple(Looping):
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

#Iterate the characters of string:
  mystr = "banana"

for x in mystr:
  print(x)

#The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
#The __next__() method also allows you to do operations, and must return the next item in the sequence.

#Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#Stop iteration after 20 iterations
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)



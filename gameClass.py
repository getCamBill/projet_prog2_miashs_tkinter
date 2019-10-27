class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p2 = Person("Bill", 42)

Tablier = dict({'A1': None, 2: p2})
print(Tablier['A1'])
Tablier['A1'] = p1
print(Tablier['A1'].name)
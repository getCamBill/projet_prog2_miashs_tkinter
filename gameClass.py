class Person:
  def __init__(self, name: str = "John", age: int = 22):
      self.name: str = name
      self.age: int = age

class case(Person):
    def __int__(self):
        self.position :str = 'A1'

    def occupee(self):
        if 

p1 = Person()
p2 = Person("Bill", 42)

Tablier = dict({'A1': None, 'A2': p2})
print(Tablier['A1'])
print(Tablier['A2'].name)
Tablier['A1'] = p1
print(Tablier['A1'].name)
print(Tablier['A2'].name)
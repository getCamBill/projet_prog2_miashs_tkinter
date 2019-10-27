class Person:
  def __init__(self, name: str = "John", age: int = 22):
      self.name: str = name
      self.age: int = age


class case(Person):
    def __int__(self):
        self.position :str = None


p1 = Person()
p2 = Person("Bill", 42)
c1 = case()
Tablier = dict({c1: None, 'A2': p2})
print(Tablier[c1])
print(Tablier['A2'].name)
Tablier[c1] = p1
print(Tablier[c1].name)
print(Tablier['A2'].name)
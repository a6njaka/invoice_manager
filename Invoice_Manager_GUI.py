class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def test(self):
      print("-->>TEST")

    def __str__(self):
        return f"{self.name}({self.age})"


p1 = Person("John", 36)
p1.test()

print(p1)

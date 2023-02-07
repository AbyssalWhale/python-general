# Inheritance:

class Animal:
    def __init__(self, Name: str) -> None:
        self.name = Name

    def eat(self):
        print("Eacting...")

    def sleep(self):
        print("Sleeping...")


class Racoon(Animal):
    def steal(self):
        print("Stealing...")


class Fish(Animal):
    def swim(self):
        print("Swimming...")


racoon = Racoon("Bob")
fish = Fish("Blue Fish")

print(racoon.name)
racoon.eat()
racoon.sleep()
racoon.steal()

print(isinstance(racoon, Animal))
print(issubclass(type(racoon), Animal))

# Multiple Inheritance:
class TestClass:
    pass


class MultiAnimal(Animal, TestClass):
    pass


# Polymorphism (Overriding methods)
# Constructors are overrided and not called one by one from parent to child
class Mammal(Animal):
    def __init__(self, Name: str, Age: int) -> None:
        # Calling parent constructor
        super().__init__(Name)
        self.age = Age


mammal = Mammal("Olol", 10)
print(mammal.name)
print(mammal.age)

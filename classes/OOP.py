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

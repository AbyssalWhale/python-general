from abc import ABC, abstractmethod

# Polymorphism (Overriding methods)
# Constructors are overrided and not called one by one from parent to child


class Animal:
    def __init__(self, Name: str) -> None:
        self.name = Name

    def eat(self):
        print("Eacting...")

    def sleep(self):
        print("Sleeping...")


class Mammal(Animal):
    def __init__(self, Name: str, Age: int) -> None:
        # Calling parent constructor
        super().__init__(Name)
        self.age = Age


mammal = Mammal("Olol", 10)
print(mammal.name)
print(mammal.age)


#
class UIControl(ABC):
    @abstractmethod
    def draw(self):
        print("Default print")


class TextBox(UIControl):
    def draw(self):
        print("text box print")


class DropDownList(UIControl):
    def draw(self):
        print("drop down print")


def draw(controls):
    for control in controls:
        control.draw()


draw([TextBox(), DropDownList()])

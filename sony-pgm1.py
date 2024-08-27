class Animal:
    def __init__(self):
        print("Cow Moos")

    def speak(self):
        print("Animal Speaks")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog Barks")

animal = Animal()
dog = Dog()
animal.speak()
dog.speak()


# OUTPUT: 
#cow Moos 
#Cow Moos 
#Animal speaks
#Animal speaks
#Dog Barks 
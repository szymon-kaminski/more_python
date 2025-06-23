class Dog:
    def speak(self):
        return "Woof!"
    

class Cat:
    def speak(self):
        return "Meow!"
    

class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")


factory = AnimalFactory()

animal1 = factory.create_animal("dog")
animal2 = factory.create_animal("cat")

print(animal1.speak())  ## Woof!
print(animal2.speak())  ## Meow!
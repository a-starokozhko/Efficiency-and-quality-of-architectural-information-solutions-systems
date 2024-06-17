class Animal:
    def speak(self):
        print("Animal speaks")

    def move(self):
        print("Animal moves")

class Dog:
    def __init__(self):
        self.animal = Animal()

    def speak(self):
        self.animal.speak()

    def move(self):
        self.animal.move()

# Приклад використання класів
dog = Dog()
dog.speak()
dog.move()

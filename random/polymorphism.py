class Animal:
    def __init__(self,name):
        self.name = name
    def talk(self):
        pass

class Dog(Animal):
    def talk(self):
        print("Woof!")

class Cat(Animal):
    def talk(self):
        print("Meow!")

cat = Cat('kitty')
cat.talk()

dog = Dog("Biko")
dog.talk()
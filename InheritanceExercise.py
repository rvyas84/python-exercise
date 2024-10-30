class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):
    def bark(self):
        print("Bark")


class Cat(Mammal):
    def is_annoying(self):
        print("Annoying")


mammal = Mammal()
mammal.walk()

cat = Cat()
cat.walk()
cat.is_annoying()

dog = Dog()
dog.walk()
dog.bark()
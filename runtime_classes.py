class Animal:
    def move(self):
        print("moving...")

class Dog(Animal):
    def bark(self):
        print("woof, woof")

d = Dog()
d.bark()
d.move()

Cat = type("Cat", (Animal,), {'meow': lambda self: print("Meow, meow")})
c = Cat()
c.meow()
c.move()
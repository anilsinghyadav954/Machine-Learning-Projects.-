#inheritance
class Animal:
    def show(self):
        print("Animal show method")
class Cat(Animal):
    def makeSound(self):
        print("mewoww")

c = Cat()
c.makeSound()
class Parent:
    def show(self):
        print("Show from parent ")

class Child(Parent):
    def display(self):
        print("Display from child")

c = Child()
c.display()
c.show()

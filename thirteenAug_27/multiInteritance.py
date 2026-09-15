class Dadaji:
    def show(self):
        print("Show from Dadaji")
class Papaji(Dadaji):
    def output(self):
        print("Output from Papaji class")        
class Betaji(Papaji):
    def display(self):
        print("Beta ji class here")        

B = Betaji()
B.display()
P = Papaji()
P.output()
D = Dadaji()
D.show()       
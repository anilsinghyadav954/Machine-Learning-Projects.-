class student:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def showDetails(self):
        print(self.id)
        print(self.name)
s = student(18,"Arun Kumar")
s.showDetails()
s2 = student(8,"Anil Kumar")
s2.showDetails()
s3 = student(6,"Aman Prajapati")
s3.showDetails()
s4 = student(11,"Anshuman Yadav")
s4.showDetails()
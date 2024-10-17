class student:
    name= ""
    age= ""
    address= ""
    def __init__(self,a,b,c):
         self.name=a
         self.age=b
         self.address=c
    def show(self):
        print(f"name: {self.name} \nage: {self.age} \naddress: {self.address}")

asif=student("asif",55,"Tangail")

asif.show()
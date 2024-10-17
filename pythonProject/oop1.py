class student:
    name= ""
    age= ""
    address= ""
    def set(self,a,b,c):
        self.name=a
        self.age=b
        self.address=c
    def show(self):
        print(f"name: {self.name} \nage: {self.age} \naddress: {self.address}")

asif=student()
asif.set("Asif",22,"Tangail")
asif.show()
# print(isinstance(asif,student))
# asif.name="Asif"
# asif.age=15
# asif.address="Tangail"




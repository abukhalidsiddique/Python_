from abc import ABC,abstractmethod
class a(ABC):
# this is also plymorphism.. same area method works differently in diff class
    def __init__(self,x,y):
        self.base=x
        self.height=y
    @abstractmethod
    def area(self):
         pass
class b(a):
    def area(self):
        print(self.base*self.height)
class c(a):
    def area(self):
        print(0.5*self.base*self.height)

p=b(5,5)
q=c(2,2)
p.area()
q.area()
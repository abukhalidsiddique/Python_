from pattern3 import height


class a:
    # base=""
    # height=""
    def __init__(self,x,y):
        self.base=x
        self.height=y
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
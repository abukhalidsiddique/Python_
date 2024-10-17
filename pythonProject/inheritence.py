class a:
    def p(self):
        print("its p")
    def q(self):
        print("its q")
    i=""
    j=""

    # def __init__(self):
    #      print("from parent")

    def __init__(self,s,t):
        self.i=s
        self.j=t
    def show(self):
        print(f"i= {self.i} \nj= {self.j}")

class b(a):
    def r(self):
        print("its r")
x=b("ok","okay")
x.p()
x.q()
x.r()
x.show()

print(issubclass(b,a))
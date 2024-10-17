class a:
    def show(self):
        print("class a")
class b(a):
    def show2(self):
        print("class b")
class c(b):
    def show3(self):
        print("class c")
x=c()
x.show()
x.show2()
x.show3()
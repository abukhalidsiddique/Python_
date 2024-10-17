class a:
    def show(self):
        print("class a")
class b:
    def show2(self):
        print("class b")
class c(a,b):
    def show3(self):
        print("class c")
x=c()
x.show()
x.show2()
x.show3()
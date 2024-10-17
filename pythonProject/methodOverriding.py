class a:
  def __init__(self):
         print("from parent")
class b(a):
  def __init__(self):
         super().__init__()
         print("from child")

x=b()


print(issubclass(b,a))
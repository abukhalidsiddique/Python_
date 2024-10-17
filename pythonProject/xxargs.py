def a (*all):
    print(all)


def b (*numbers):
    total=0
    for x in numbers:
        total+=x
    print(total)

a("hdgs",7,"tg4")
b(4,5,6,7,5)

def show(**all):
    print(all)
    print(all["name"])

show(id=3,name="asif")
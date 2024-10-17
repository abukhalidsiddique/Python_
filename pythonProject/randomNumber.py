from random import randint, random

for a in range(3):
    b = randint(0, 2)
    print("a= ", a, "b= ", b)
    print("win"if (a==b) else "loss")
c=int(random() *3)
print( c)
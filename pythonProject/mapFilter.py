def square (a):
     return a*a

def even(a):
        if a % 2 == 0:
            return a
num=[3,4,5,6,7]
b=list(map(square,num))
print(b)

c=list(filter(lambda x: x%2==0,num))
print(c)

d=list(filter( even ,num))
print(d)
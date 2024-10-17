a=11
b=666
c=888
print("large: ")
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
elif b>c:
    print(b)
else:
    print(c)


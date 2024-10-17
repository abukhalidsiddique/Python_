import re
a="love"
b="i love my country"
c="like"
match=re.search(a,b)
if match:
    print(match.start())
    print(match.end())
    print(match.span())

print(re.sub(a,c,b))

x="djfhj"
y=r"s+"
if re.match(y,x):
    print("matched")
else:
    print("not matched")

x="djfihj"
y=r"[aeiou]"
if re.match(y,x):
    print("matched")
else:
    print("not matched")
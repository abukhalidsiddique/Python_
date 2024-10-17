import re
pattern= r"colour"
if re.match(pattern,"colour Red is a colour, I love red colour"):
    print("match")
else:
    print("not match")

if re.search(pattern,"Red is a colour, I love red colour"):
    print("match")
else:
    print("not match")

print(re.findall(pattern,"colour Red is a colour, I love red colour"))

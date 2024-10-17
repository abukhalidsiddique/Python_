from collections import deque

a=deque([3,"e",9,"454g",66,'4f'])
print(a)
a.popleft()
print(a)
a.pop()
print(a)

a.append("33")
print(a)

a.appendleft("jsdhfh")
print(a)


if not a:
    print("noitem")
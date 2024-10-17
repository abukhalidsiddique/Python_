# a=open("student.txt","r")
# print(a.readable())
# a.close()

# a=open("student.txt","w")
# print(a.writable())
# a.close()
#
# a=open("student.txt","r+")
# print(a.writable())
# a.close()

a=open("student.txt","r+")
# b=a.read()
# print(b)
# d=len(b)
# print(d)
# text=a.readlines()[1]
# print(text)

for x in a:
    print(x)
a.close()
n=input("enter the sentence: ")
a=0
b=0
c=0
for x in n:
     x=x.lower()
     if x>='a' and x<='z':
        a+=1
     elif x>='0' and x<='9':
        b+=1
     elif x==' ':
        c+=1
print(a)
print(b)
print(c+1)

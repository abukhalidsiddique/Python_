i=int(input("enter the last digit: "))
sum=0
for x in range(1,i+1,1):
    sum+=x
print(sum)

sum=0
for x in range(2,i+1,2):
    sum+=x
print(sum)


sum=0
for x in range(2,i+1,2):
    sum+=x*x
print(sum)
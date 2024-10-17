matrix= [

     [3,6,8],
     [5,8,2]
]
sum=0
matrix[1][2]=10
# print(matrix[1][1])

for x in matrix:
    for y in x:
      print(y)
      sum+=y
print(sum)
#1

ls1 = [1,2,3,4,5]
ls2 = [1,2,3,45,9]
for i in ls1:
    continue
for j in ls2:
    continue
if i == j:
    print("They are similiar.")
else:
    print("They are'nt similiar.")

#2

ls = [] 
length = int(input("Enter elements count: "))
for i in range(length):
    i = int(input("Enter element: "))
    ls.append(i)

print(f"ls = {ls}")

max = ls[0]
index_of_max = 0

for i in range(1,len(ls)):
    if ls[i] > max:
        index_of_max  = i
        max = ls[i]
    

min = ls[0]
index_of_min = 0

for i in range(1,len(ls)):
    if ls[i] < min:
        index_of_min = i
        min = ls[i]

result = index_of_max - index_of_min

print(f"Max index - Min index = {result}")

#3

matrix = [[1,2,3],[4,5,6],[7,8,9]]
for i in matrix:
    for j in i:
        print(j)

#4

matrix = [[1,2,3],[4,5,6],[7,8,9]]
length = len(matrix)
for i in range(len(matrix)):
    matrix[i][i], matrix[i][length-1] = matrix[i][length-1], matrix[i][i]
    length -= 1     
print(matrix)

#5

matrix = [[1,2,3],[4,5,6],[7,8,9]]
gumar = 0
for i in range(len(matrix)):
    gumar += matrix[i][i]
    
print(f"Glxavor = {gumar}")

#6

matrix = [[1,2,3],[4,5,6],[7,8,9]]
gumar = 0
length = len(matrix)
for i in range(len(matrix)):
    gumar += matrix[i][length-1]
    length -= 1
print(f"Ojandak = {gumar}")

#7

import random

m = 3
n = 5
#matrix = [[x+y*m for x in range(m)] for y in range(n)]
matrix = [[random.randint(10,99) for _ in range(m)] for _ in range(n)]

print(matrix)

max = matrix[0][0]

for i in matrix:
    for j in i:
        if max < j:
            max = j
        else:
            continue

print(f"Max element = {max}")


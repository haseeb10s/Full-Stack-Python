names = ['Ali', 'John', 'Bob', 'Marry']
print(names)
print(names[0])
print(names[-1])
names[0] = 'Harry'
print(names)
print(names[0:2])

# list methods
num = [1,2,3,4,5]
num.append(6)
num.insert(0, -1)
print(num)
num.remove(2)
num.clear()
print(1 in num)
print(len(num))

# 2d list
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][1])
matrix[0][1] = 20

for row in matrix:
    for item in row:
        print(item)

import numpy as np

m2 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

# print(m2)


# #Traverse all element............

# print("traverse all element......")

# for i in np.nditer(m2):
#     print(i,end=" ")


# print()
# #Transpose of matrix.............

# print("transpose of matrix.....")

# mt2 = m2.T
# print(mt2)

# #Sum of all arr/matrix element......
# print("Sum of all element")

# print(np.sum(m2))


mat1 = np.array([[100,200],[300,400]])
mat2 = np.array([[1,2],[3,4]])

#Matrix multiplication..........

print("Matrix Multiplication ........")
mul1_2 = np.matmul(mat1,mat2)
print(mul1_2)

#Matrix dot product...........

print("Matrix dot product...........")

dot_pro = np.dot(mat1,mat2)
print(dot_pro)

#Add element(ex-2) all matrix element......

print("add 2 in every matrix element..........")

add = np.add(mat1,2)
#OR --->>>print(mat1 + 2)
print(add)

#Twice of all element in matrix...........
print("Twice of all element in matrix.........")
print(mat2 * 2)


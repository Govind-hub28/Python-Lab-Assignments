# Python Assignment-04

# Addition of Two Matrices


# First matrix
matrix1 = [
    [1, 2],
    [3, 4]
]

# Second matrix
matrix2 = [
    [5, 6],
    [7, 8]
]


# Create a result matrix
result = [
    [0, 0],
    [0, 0]
]


# Add the two matrices
for i in range(2):
    for j in range(2):
        result[i][j] = matrix1[i][j] + matrix2[i][j]


# Display first matrix
print("First Matrix:")
for row in matrix1:
    print(row)


# Display second matrix
print("\nSecond Matrix:")
for row in matrix2:
    print(row)


# Display result
print("\nSum of the Two Matrices:")
for row in result:
    print(row)
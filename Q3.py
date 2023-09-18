def multiply_matrices(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

def calculate_trace(matrix):
    trace = 0
    for i in range(len(matrix)):
        trace += matrix[i][i]
    return trace


n = int(input("Enter the size of the square matrices (n x n): "))


print("Enter the elements of the first matrix:")
matrix1 = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix1.append(row)

print("Enter the elements of the second matrix:")
matrix2 = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix2.append(row)

result_matrix = multiply_matrices(matrix1, matrix2)

trace = calculate_trace(result_matrix)

#print("Resultant Matrix:")
for row in result_matrix:
    print(" ".join(map(str, row)))

print("Trace of the Resultant Matrix:", trace)
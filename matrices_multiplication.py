# Function to create a matrix based on user input
def create_matrix():
    r = int(input("Enter the number of rows: "))
    c = int(input("Enter the number of columns: "))

    # Initialize the matrix with zeros
    matrix = [[0 for _ in range(c)] for _ in range(r)]

    # Iterate through each element in the matrix to get user input for values
    for i in range(r):
        for j in range(c):
            matrix[i][j] = int(input(f"Enter integer value at position [{i}][{j}]: "))

    return matrix

# Function to display the matrix
def display_matrix(matrix):
    for row in matrix:
        print(row)

# Main program

# Create two matrices
print("\nThe first matrix")
a_matrix = create_matrix()
print("\nThe second matrix")
b_matrix = create_matrix()

# Display the created matrices
print("\nThe first matrix: ")
display_matrix(a_matrix)
print("\nThe second matrix: ")
display_matrix(b_matrix)

# Determine the number of rows in the first matrix and columns in the second matrix
rows_a = len(a_matrix)
rows_b = len(b_matrix)
cols_b = len(b_matrix[0])
cols_a = len(a_matrix[0])

# Check if matrices can be multiplied
if cols_a != rows_b:
    print("\nMatrices cannot be multiplied due to mismatched dimensions.")
else:
    # Initialize the resulting matrix for multiplication with zeros
    c_matrix = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    # Perform matrix multiplication
    for i in range(rows_a):
        for j in range(cols_b):
            the_sum = 0
            # Iterate through the elements of the matrices for multiplication
            for x in range(cols_a):
                # Multiply corresponding elements and accumulate the sum
                the_sum += a_matrix[i][x] * b_matrix[x][j]
            # Assign the calculated sum to the resulting matrix at position [i][j]
            c_matrix[i][j] = the_sum

# Display the resulting matrix after matrix multiplication
print("\nThe resulting matrix (first matrix * second matrix): ")
display_matrix(c_matrix)

# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

 #===================Reads Matrix from a User ===================
def read_matrix(name):
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))
    matrix = []
    for i in range(rows):
        while True:
            row_input = input(f"Enter row {i+1}: ")
            row = row_input.split()
            row = [int(num) for num in row]
            if len(row) == cols:
                break
            else:
                print(f"Error: Row must have exactly {cols} numbers. Try again.")
        matrix.append(row)
    return matrix

# =================== Helper: Display a matrix neatly ===================
def display_matrix(matrix):
    for row in matrix:
        for num in row:
            print(num, end="\t")
        print()

# =================== PART A: Transpose ===================
def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)
    return result

# =================== PART B: Add two matrices ===================
def add_matrices(a, b):
    rows = len(a)
    cols = len(a[0])
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(a[i][j] + b[i][j])
        result.append(new_row)
    return result

# =================== PART C: Multiply two matrices ===================
def multiply_matrices(a, b):
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])
    result = []
    for i in range(rows_a):
        new_row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total = total + a[i][k] * b[k][j]
            new_row.append(total)
        result.append(new_row)
    return result

# =================== MAIN ===================
print("PART A - Transpose")
matrix_a = read_matrix("Matrix")
print("Original Matrix:")
display_matrix(matrix_a)
print("Transposed Matrix:")
display_matrix(transpose(matrix_a))

print("\nPART B - Addition")
m1 = read_matrix("Matrix 1")
m2 = read_matrix("Matrix 2")

if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
    print("Error: Both matrices must be the same size to add them.")
else:
    print("Sum Matrix:")
    display_matrix(add_matrices(m1, m2))

print("\nPART C - Multiplication")
m3 = read_matrix("Matrix A")
m4 = read_matrix("Matrix B")

if len(m3[0]) != len(m4):
    print("Error: Number of columns in Matrix A must equal number of rows in Matrix B.")
else:
    print("Product Matrix:")
    display_matrix(multiply_matrices(m3, m4))
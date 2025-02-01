# PYTHON TASK 3

# 17. Table of a Number
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

num = int(input("Enter a number: "))
multiplication_table(num)

# 18. Swap Two Numbers
def swap_numbers(a, b):
    a, b = b, a
    return a, b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = swap_numbers(a, b)
print(f"Swapped values: a = {a}, b = {b}")

# 19. Check Substring
def is_substring(s1, s2):
    return s2 in s1

s1 = input("Enter main string: ")
s2 = input("Enter substring: ")
print(is_substring(s1, s2))

# 20. Decimal to Binary
def decimal_to_binary(n):
    return bin(n)[2:]

num = int(input("Enter a decimal number: "))
print(f"Binary: {decimal_to_binary(num)}")

# 21. Matrix Addition
def add_matrices(A, B):
    rows = len(A)
    cols = len(A[0])
    result = [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]
    return result

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print("Matrix Sum:", add_matrices(A, B))

# 22. Matrix Multiplication
def multiply_matrices(A, B):
    result = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
    return result

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print("Matrix Product:", multiply_matrices(A, B))

# 23. Find Second Largest
def second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort(reverse=True)
    return unique_numbers[1] if len(unique_numbers) > 1 else None

nums = list(map(int, input("Enter numbers: ").split()))
print("Second largest:", second_largest(nums))

# 24. Check Anagram
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print(is_anagram(s1, s2))

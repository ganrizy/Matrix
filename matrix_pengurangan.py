# Nama : Aditya Rizki.F
# NIM  : 17250319
# Kelas: 17-1C-37

# Nama  : Ali Musthofa
# Nim   : 17250525
# Kelas : 17-1C-37

# Nama  : Rizki Saputra
# Nim   : 17250115
# Kelas : 17-1C-37

# Nama  : Rizky Akbar Ramdhan
# Nim   : 17250641
# Kelas : 17-1C-37

# Nama  : Jovi Rachman
# Nim   : 17250248
# Kelas : 17-1C-372

# Program Pengurangan Matriks 3x3

# Program Pengurangan Matriks 3x3 dengan Input Manual

A = [[0 for j in range(3)] for i in range(3)]
B = [[0 for j in range(3)] for i in range(3)]
C = [[0 for j in range(3)] for i in range(3)]

print("=== Input Matriks A ===")
for i in range(3):
    for j in range(3):
        A[i][j] = int(input(f"Masukkan nilai A[{i}][{j}]: "))

print("\n=== Input Matriks B ===")
for i in range(3):
    for j in range(3):
        B[i][j] = int(input(f"Masukkan nilai B[{i}][{j}]: "))

for i in range(3):
    for j in range(3):
        C[i][j] = A[i][j] - B[i][j]

print("\nMatriks A:")
for row in A:
    print(row)

print("\nMatriks B:")
for row in B:
    print(row)

print("\nHasil Pengurangan (A - B):")
for row in C:
    print(row)

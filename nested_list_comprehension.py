### Przykład 1 - macierz 3x3
print("Przykład 1")
matrix = [[i + j*3 for i in range(1,4)] for j in range (3)]
print(matrix)

### Przykład 2 - Spłaszczenie listy list
print("Przykład 2")
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for sublist in matrix for num in sublist]
print(flat)

### Przykład 3 - Filtracja z warunkiem
print("Przykład 3")
matrix = [[1, 2], [3, 4], [5, 6]]
even = [num for sublist in matrix for num in sublist if num % 2 == 0]
print(even)

### Twoim zadaniem jest za pomocą zagnieżdżonego list comprehension:
### - Spłaszczyć macierz do jednej listy,
### - Zostawić tylko liczby parzyste.
print("ćwiczenie")
matrix = [[10, 15, 20], [25, 30, 35], [40, 45, 50]]
flat = [num for sublist in matrix for num in sublist if num % 2 == 0]
print(flat)
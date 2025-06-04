print("Przykłąd 1")
normal_set = set([1, 2, 3])
frozen_set = frozenset([1, 2, 3])
print(normal_set)
print(frozen_set)

# frozen_set.add(4)  # AttributeError: 'frozenset' object has no attribute 'add'

print("Przykład 2")
print("Operations")

a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])

print(a | b)  # -> frozenset({1, 2, 3, 4, 5})
print(a & b)  # -> frozenset({3}) 
print(a - b)  # -> frozenset({1, 2})

print("Przykład 3")
fs = frozenset([1, 2])
d = {fs: "para"}
print(d[fs])  # -> para

print("ćwiczenie")
# Masz dwie listy z danymi klientów:
# klienci_a = ["Anna", "Bartek", "Celina", "Daniel"]
# klienci_b = ["Celina", "Daniel", "Edward", "Filip"]
# Twoje zadania:
# 1.	Zamień obie listy na frozensety.
# 2.	Znajdź:
# o	wszystkich unikalnych klientów (bez powtórzeń),
# o	klientów wspólnych dla obu list,
# o	klientów tylko z listy A.
# 3.	Spróbuj dodać nowego klienta do frozenset i sprawdź co się stanie.

klienci_a = frozenset(["Anna", "Bartek", "Celina", "Daniel"])
klienci_b = frozenset(["Celina", "Daniel", "Edward", "Filip"])
print(klienci_a | klienci_b)  # -> frozenset({'Bartek', 'Celina', 'Daniel', 'Edward', 'Filip', 'Anna'})
print(klienci_a & klienci_b)  # -> frozenset({'Celina', 'Daniel'})
print(klienci_a - klienci_b)  # -> frozenset({'Anna', 'Bartek'})

# klienci_a.add("Jacek")  # -> AttributeError: 'frozenset' object has no attribute 'add'
# print(klienci_a)
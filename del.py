print("Przykład 1")
fruits = ["banana", "apple", "orange"]
del fruits[1]
print(fruits)

print("Przykład 2")
nums = [1, 3, 5, 7, 9, 11]
del nums[2:5]
print(nums)

print("Przykład 3")
person = {"name": "Szymon", "age": 35}
del person["age"]
print(person)

print("Ćwiczenie")
# shopping = ["chleb", "mleko", "jajka", "masło", "ser", "banany"]
# Twoje zadania:
# 1.	Usuń "masło" z listy, zakładając, że nie znasz jego indeksu.
# 2.	Usuń pierwszy element z listy.
# 3.	Usuń ostatnie dwa elementy używając slicingu.
# 4.	Wypisz listę po każdej operacji, by zobaczyć co się zmieniło.
print("ad. 1")
shopping = ["chleb", "mleko", "jajka", "masło", "ser", "banany"]
id = shopping.index("masło")
del shopping[id]
print(shopping)

print("ad. 2")
shopping = ["chleb", "mleko", "jajka", "masło", "ser", "banany"]
del shopping[0]
print(shopping)

print("ad. 3")
shopping = ["chleb", "mleko", "jajka", "masło", "ser", "banany"]
del shopping[-2:]
print(shopping)
      
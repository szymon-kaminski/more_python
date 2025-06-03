### Ćwiczenie: Analiza danych użytkownika z tuple
# Masz dane o użytkownikach zapisane jako lista krotek:
# users = [
#     ("Anna", 25),
#     ("Bartek", 30),
#     ("Celina", 22),
#     ("Dawid", 35)
# ]
# Twoje zadania:
# 1.	Wypisz imiona wszystkich użytkowników, którzy mają więcej niż 25 lat.
# 2.	Oblicz średni wiek wszystkich użytkowników.
# 3.	Znajdź imię najstarszego użytkownika.
users = [
    ("Anna", 25),
    ("Bartek", 30),
    ("Celina", 22),
    ("Dawid", 35)
]

print(" ćw. 1")
for user in users:
    if user [1] > 25:
        print(user [0])

print("ćw. 2")
sum_ages = sum(user[1] for user in users)
average_age = sum_ages / len(users)
print(average_age)

print("ćw. 3")
oldest_user = max(users, key=lambda user: user[1])
print(oldest_user)
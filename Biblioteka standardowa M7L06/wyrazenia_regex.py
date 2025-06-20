print("Przykład re.search")
print("Przykład 1")

import re

tekst = "Dziś jest piątek"
match = re.search(r"piątek", tekst)
if match:
    print("Znaleziono:", match.group())
#################################################
print("\nPrzykład 2")
import re

tekst = "Mój email to: kontakt@example.com"
wzorzec = r"\w+@\w+\.\w+"

dopasowanie = re.search(wzorzec, tekst)

if dopasowanie:
    print("Znalezion:", dopasowanie.group())

####################################################
####################################################
print("\nPrzykłady re.findall")
print("Przykład 1")

import re

tekst = "Ma 2 jabłka, 3 gruszki i  4 śliwki"
cyfry = re.findall(r"\d", tekst)
print(cyfry)
##############################################
print("\nPrzykład 2")

import re

tekst = "Moje numery: 777-555-423, 123-789-012"
wzorzec = r"\d{3}-\d{3}-\d{3}"
wyniki = re.findall(wzorzec, tekst)
print(wyniki)

#####################################################
#####################################################
print("\nPrzykłady re.sub")
print("Przykład 1")
 
import re

tekst = "kot pies kot kot pies"
nowy = re.sub(r"kot", "tygrys", tekst)
print(nowy)
##########################################
print("\nPrzykład 2")

import re

tekst = "Cena to 50 zł"
nowy = re.sub(r"\d+", "XX", tekst)
print(nowy)

####################################################
####################################################
print("\nPrzykłady re.split")
print("Przykład 1")

import re

tekst = "imię;nazwisko;email"
dane = re.split(r";", tekst)
print(dane)
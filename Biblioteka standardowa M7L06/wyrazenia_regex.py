print("Przykład re.search")
print("Przykład 1")

import re

tekst = "Dziś jest piątek"
match = re.search(r"piątek", tekst)
if match:
    print("Znaleziono:", match.group())
##########################################################
print("\nPrzykład 2")
import re

tekst = "Mój email to: kontakt@example.com"
wzorzec = r"\w+@\w+\.\w+"

dopasowanie = re.search(wzorzec, tekst)

if dopasowanie:
    print("Znalezion:", dopasowanie.group())
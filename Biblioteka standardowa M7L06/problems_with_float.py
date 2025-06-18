import math
from decimal import Decimal


print("FLOAT errors:")
print(0.1 + 0.2)  ## 0.3000000000004
print(0.3 == 0.1 + 0.2)  ## False
print(1.1 + 2.2)  ## 3.3000000000000003
print(0.3 - 0.1)  ## 0.19999999999999998
print(0.1 * 3)  ## 0.30000000000000004
print(0.3 / 0.1)  ## 2.9999999999999996

print("\nround():")
print(round(0.1 + 0.2, 2) == 0.3)  ## True!

print("\nmath.isclose():")
print(math.isclose(0.1 + 0.2, 0.3))  ## True!

print("\nDecimal:")
print(Decimal('0.1') + Decimal('0.2') == Decimal('0.3'))  ## True!
print(Decimal('0.1') + Decimal('0.2') == Decimal(0.3))  ## False!

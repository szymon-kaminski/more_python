from decimal import Decimal, getcontext

print("float:")
print(0.1 + 0.2)  # Wrong!

print("\nDecimal:")
x = Decimal('0.1')
y = Decimal('0.2')
z = x + y
print(z)
###
print()
print(Decimal(0.1))  # Wrong!
print(Decimal('0.1'))  # Good!
###

print('\nzaokraglenie - ustawienie precyzji')
getcontext().prec = 7
x = Decimal('1') / Decimal('7')
print(x)
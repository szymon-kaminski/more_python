### 1. str.format()

print("Hello, {}. You have {} new messeges.".format("Szymon", 5))

print("First: {0}, Second: {1}, Again first: {0}".format("A", "B"))

print("User: {name}, Score {points}".format(name="Szymon", points=99))

pi = 3.14159265
print("Pi: {:.2f}".format(pi))

### 2. f-string

name = "Szymon"
messages = 5
print(f"Hello, {name}. You have {messages} new messages.")

x = 10
print(f"x={x}, squared is = {x**2}")

pi = 3.14159265
print(f"Pi to 3 decimal places: {pi:.3f}")

for x in range(1,4):
    print(f"Row {x:<1} | Value: {x*10:>2}")

### 3. %-formatting

name = "Szymon"
print("Hello, %s!" % name)
print("Pi: %.2f" % 3.14159)

### 4. Tabular data

data = {"apples": 10, "bananas": 5, "oranges": 8}
for fruit, count in data.items():
    print(f"{fruit:<10} | {count:>3}") 
print("Przykład 1")

class Coffee:
    def cost(self):
        return 5
    

class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee
    

    def cost(self):
        return self._coffee.cost() + 2
    

class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    
    def cost(self):
        return self._coffee.cost() + 1
    

basic_coffee = Coffee()
print("Basic:", basic_coffee.cost())

coffee_with_milk = MilkDecorator(basic_coffee)
print("With milk:", coffee_with_milk.cost())

coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)
print("With milk and sugar:", coffee_with_milk_and_sugar.cost())

coffee_with_sugar = SugarDecorator(basic_coffee)
print("With sugar only:", coffee_with_sugar.cost())


print("\nPrzykład 2")

def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")

say_hello()
print("Przykład 1")
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Tworzę nową instancję.")
            cls._instance = super(Singleton, cls).__new__(cls)
        else:
            print("Używam isniejącej instancji.")
        return cls._instance
    

s1 = Singleton()  ## Tworzę nową instancję.
s2 = Singleton()  ## Używam isniejącej instancji.

print(s1 is s2)  ## True


print("\nPrzykład 2")

def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance


@singleton
class MyClass:
    def __init__(self):
        print("Tworzę MyClass")


a = MyClass()
b = MyClass()

print(a is b)



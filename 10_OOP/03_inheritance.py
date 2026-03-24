# ============================================================
# 10 OOP — 03: Inheritance
# ============================================================
# Run this file: python 03_inheritance.py
# ============================================================


# ── BASIC INHERITANCE ───────────────────────────────────────
# Child class gets all attributes and methods from the parent
class Animal:
    def __init__(self, name, sound):
        self.name  = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}"

    def __str__(self):
        # __class__.__name__ gives the actual class name (Dog, Cat, etc.)
        return f"{self.__class__.__name__}('{self.name}')"


class Dog(Animal):
    def __init__(self, name):
        # super() calls the parent's __init__ — always do this first
        super().__init__(name, "Woof")

    # Dog-specific method — not in Animal
    def fetch(self):
        return f"{self.name} fetches the ball!"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")

    def purr(self):
        return f"{self.name} purrs..."


dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())      # Buddy says Woof   — inherited from Animal
print(dog.fetch())      # Buddy fetches the ball! — Dog's own method
print(str(dog))         # Dog('Buddy')

# isinstance checks the full inheritance chain
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True — Dog IS an Animal
print(isinstance(dog, Cat))     # False


# ── SUPER() — CALLING THE PARENT ────────────────────────────
class Employee:
    def __init__(self, name, salary):
        self.name   = name
        self.salary = salary

    def describe(self):
        return f"{self.name} earns ${self.salary:,}"


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)  # Reuse parent __init__
        self.team_size = team_size

    def describe(self):
        # super().describe() reuses the parent's method — no duplication
        base = super().describe()
        return f"{base} and manages {self.team_size} people"


emp = Employee("Alice", 60000)
mgr = Manager("Bob", 90000, 8)

print(emp.describe())   # Alice earns $60,000
print(mgr.describe())   # Bob earns $90,000 and manages 8 people


# ── METHOD OVERRIDING ───────────────────────────────────────
# Child can replace (override) a parent method with its own version
class Duck(Animal):
    def __init__(self, name):
        super().__init__(name, "Quack")

    def speak(self):
        # Override: Duck says Quack twice
        return f"{self.name} says {self.sound} {self.sound}!"

duck = Duck("Donald")
print(duck.speak())     # Donald says Quack Quack!  — overridden


# ── MULTI-LEVEL INHERITANCE ─────────────────────────────────
# A → B → C  (C inherits from B, which inherits from A)
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        return f"{self.brand} engine starting..."


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def drive(self):
        return f"Driving {self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_kw):
        super().__init__(brand, model)
        self.battery_kw = battery_kw

    def start(self):
        # Override: electric cars start silently
        return f"{self.brand} {self.model} silently starts..."

    def charge(self):
        return f"Charging {self.battery_kw}kW battery"


tesla = ElectricCar("Tesla", "Model 3", 75)
print(tesla.start())    # Tesla Model 3 silently starts...  (overridden)
print(tesla.drive())    # Driving Tesla Model 3  (inherited from Car)
print(tesla.charge())   # Charging 75kW battery  (ElectricCar's own)


# ── MULTIPLE INHERITANCE ─────────────────────────────────────
# A class can inherit from more than one parent
class Flyable:
    def fly(self):
        return f"{self.name} is flying"

class Swimmable:
    def swim(self):
        return f"{self.name} is swimming"

# Duck inherits from Animal, Flyable, AND Swimmable
class AquaDuck(Animal, Flyable, Swimmable):
    def __init__(self, name):
        super().__init__(name, "Quack")

donald = AquaDuck("Donald")
print(donald.speak())   # Donald says Quack
print(donald.fly())     # Donald is flying
print(donald.swim())    # Donald is swimming


# ── MRO — METHOD RESOLUTION ORDER ───────────────────────────
# When multiple parents have the same method, Python uses MRO to decide which runs
# MRO follows the C3 linearization algorithm — left to right, depth first
class A:
    def hello(self): return "Hello from A"

class B(A):
    def hello(self): return "Hello from B"

class C(A):
    def hello(self): return "Hello from C"

class D(B, C):
    pass    # No override — Python will use MRO to find hello()

d = D()
print(d.hello())        # Hello from B  — B comes before C in D(B, C)
print(D.__mro__)        # (D, B, C, A, object)


# ── REAL EXAMPLE: E-Commerce Products ───────────────────────
class Product:
    def __init__(self, name, price):
        self.name  = name
        self.price = price

    def get_info(self):
        return f"{self.name}: ${self.price:.2f}"


class PhysicalProduct(Product):
    def __init__(self, name, price, weight_kg):
        super().__init__(name, price)
        self.weight_kg = weight_kg

    def shipping_cost(self):
        return self.weight_kg * 2.50    # $2.50 per kg

    def get_info(self):
        base = super().get_info()
        return f"{base} | Shipping: ${self.shipping_cost():.2f}"


class DigitalProduct(Product):
    def __init__(self, name, price, file_size_mb):
        super().__init__(name, price)
        self.file_size_mb = file_size_mb

    def shipping_cost(self):
        return 0    # No physical shipping

    def get_info(self):
        base = super().get_info()
        return f"{base} | Digital ({self.file_size_mb}MB) | Free delivery"


products = [
    PhysicalProduct("Laptop", 999.99, 2.5),
    DigitalProduct("Python Course", 49.99, 1200),
    PhysicalProduct("Keyboard", 79.99, 0.8),
]

for p in products:
    print(p.get_info())


# ── PRACTICE ────────────────────────────────────────────────
# 1. Create Shape → Polygon → Rectangle → Square inheritance chain
# 2. Build Person → Employee → Manager, each level adding attributes
# 3. Use super() to extend (not replace) a parent method at 2 levels
# 4. Check the MRO of a class with multiple inheritance using __mro__

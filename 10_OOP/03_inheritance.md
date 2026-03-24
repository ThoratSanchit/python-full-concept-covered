# 03 - Inheritance

## What is Inheritance?

Inheritance lets a **child class** reuse code from a **parent class**. The child gets all the parent's attributes and methods, and can add or override them.

```
Animal (parent)
├── Dog (child)
├── Cat (child)
└── Duck (child)
```

---

## Basic Inheritance

```python
# Parent class (Base class)
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}"

    def __str__(self):
        return f"{self.__class__.__name__}('{self.name}')"

# Child class (Derived class)
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof")  # Call parent constructor

    def fetch(self):
        return f"{self.name} fetches the ball!"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")

    def purr(self):
        return f"{self.name} purrs..."

# Usage
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())   # Buddy says Woof   (inherited)
print(dog.fetch())   # Buddy fetches the ball! (own method)
print(cat.speak())   # Whiskers says Meow
print(cat.purr())    # Whiskers purrs...

print(str(dog))      # Dog('Buddy')
```

---

## `super()` — Calling the Parent

`super()` gives you access to the parent class.

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def describe(self):
        return f"{self.name} earns ${self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)   # Reuse parent __init__
        self.team_size = team_size

    def describe(self):
        base = super().describe()        # Reuse parent method
        return f"{base} and manages {self.team_size} people"

emp = Employee("Alice", 60000)
mgr = Manager("Bob", 90000, 8)

print(emp.describe())  # Alice earns $60000
print(mgr.describe())  # Bob earns $90000 and manages 8 people
```

---

## Method Overriding

Child class can override (replace) a parent method.

```python
class Animal:
    def speak(self):
        return "Some generic sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"          # Overrides parent

class Cat(Animal):
    def speak(self):
        return "Meow!"          # Overrides parent

class Duck(Animal):
    def speak(self):
        parent_sound = super().speak()   # Can still call parent
        return f"Quack! (parent said: {parent_sound})"

animals = [Dog(), Cat(), Duck()]
for a in animals:
    print(a.speak())
# Woof!
# Meow!
# Quack! (parent said: Some generic sound)
```

---

## Multi-Level Inheritance

```python
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

    def charge(self):
        return f"Charging {self.battery_kw}kW battery"

    def start(self):
        return f"{self.brand} {self.model} silently starts..."

tesla = ElectricCar("Tesla", "Model 3", 75)
print(tesla.start())   # Tesla Model 3 silently starts...
print(tesla.drive())   # Driving Tesla Model 3
print(tesla.charge())  # Charging 75kW battery
```

---

## Multiple Inheritance

A class can inherit from more than one parent.

```python
class Flyable:
    def fly(self):
        return f"{self.name} is flying"

class Swimmable:
    def swim(self):
        return f"{self.name} is swimming"

class Walkable:
    def walk(self):
        return f"{self.name} is walking"

class Duck(Animal, Flyable, Swimmable, Walkable):
    def __init__(self, name):
        super().__init__(name, "Quack")

donald = Duck("Donald")
print(donald.speak())  # Donald says Quack
print(donald.fly())    # Donald is flying
print(donald.swim())   # Donald is swimming
print(donald.walk())   # Donald is walking
```

### MRO — Method Resolution Order

When multiple parents have the same method, Python uses MRO to decide which one runs.

```python
class A:
    def hello(self):
        return "Hello from A"

class B(A):
    def hello(self):
        return "Hello from B"

class C(A):
    def hello(self):
        return "Hello from C"

class D(B, C):
    pass

d = D()
print(d.hello())       # Hello from B  (B comes first in MRO)
print(D.__mro__)       # D → B → C → A → object
```

---

## `isinstance()` and `issubclass()`

```python
dog = Dog("Buddy")

isinstance(dog, Dog)      # True
isinstance(dog, Animal)   # True  (Dog IS an Animal)
isinstance(dog, Cat)      # False

issubclass(Dog, Animal)   # True
issubclass(Cat, Animal)   # True
issubclass(Dog, Cat)      # False
```

---

## Code Example: E-Commerce System

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return f"{self.name}: ${self.price:.2f}"

class PhysicalProduct(Product):
    def __init__(self, name, price, weight_kg):
        super().__init__(name, price)
        self.weight_kg = weight_kg

    def shipping_cost(self):
        return self.weight_kg * 2.5  # $2.50 per kg

    def get_info(self):
        base = super().get_info()
        return f"{base} | Shipping: ${self.shipping_cost():.2f}"

class DigitalProduct(Product):
    def __init__(self, name, price, file_size_mb):
        super().__init__(name, price)
        self.file_size_mb = file_size_mb

    def shipping_cost(self):
        return 0  # No shipping for digital

    def get_info(self):
        base = super().get_info()
        return f"{base} | Digital ({self.file_size_mb}MB) | Free delivery"

class SubscriptionProduct(Product):
    def __init__(self, name, price, billing="monthly"):
        super().__init__(name, price)
        self.billing = billing

    def annual_cost(self):
        multiplier = 12 if self.billing == "monthly" else 1
        return self.price * multiplier

    def get_info(self):
        base = super().get_info()
        return f"{base}/{self.billing} | Annual: ${self.annual_cost():.2f}"

# Usage
products = [
    PhysicalProduct("Laptop", 999.99, 2.5),
    DigitalProduct("Python Course", 49.99, 1200),
    SubscriptionProduct("Netflix", 15.99, "monthly"),
]

for p in products:
    print(p.get_info())
```

---

## Practice Questions

1. Create a `Shape` → `Polygon` → `Rectangle` → `Square` inheritance chain
2. Build `Person` → `Employee` → `Manager` with each level adding attributes
3. Create a `Vehicle` with `Car`, `Truck`, `Motorcycle` subclasses, each with unique methods
4. Use `super()` to extend (not replace) a parent method in at least 2 levels

---

## Summary

| Concept | Syntax |
|---------|--------|
| Inherit from parent | `class Child(Parent):` |
| Call parent constructor | `super().__init__(...)` |
| Call parent method | `super().method_name()` |
| Override method | Redefine method in child |
| Multiple inheritance | `class Child(A, B, C):` |
| Check type | `isinstance(obj, Class)` |
| Check hierarchy | `issubclass(Child, Parent)` |
| View MRO | `ClassName.__mro__` |

---

Previous → [02 - Encapsulation](./02_encapsulation.md) | Next → [04 - Polymorphism](./04_polymorphism.md)

# 05 - Abstraction

## What is Abstraction?

Abstraction means **hiding the complex details** and showing only what's necessary. You define *what* something should do, not *how* it does it.

Think of a TV remote — you press "Volume Up" without knowing the electronics inside.

---

## Abstract Classes with `ABC`

An abstract class **cannot be instantiated** directly. It defines a contract that subclasses must follow.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Every shape must implement area()"""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Every shape must implement perimeter()"""
        pass

    # Concrete method — shared by all subclasses
    def describe(self):
        return (f"{self.__class__.__name__}: "
                f"area={self.area():.2f}, perimeter={self.perimeter():.2f}")

# Shape()  → TypeError: Can't instantiate abstract class Shape
```

---

## Implementing Abstract Classes

```python
import math

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s-self.a) * (s-self.b) * (s-self.c))

    def perimeter(self):
        return self.a + self.b + self.c

# Usage
shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5)]
for s in shapes:
    print(s.describe())
# Circle: area=78.54, perimeter=31.42
# Rectangle: area=24.00, perimeter=20.00
# Triangle: area=6.00, perimeter=12.00
```

---

## Abstract Properties

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @property
    @abstractmethod
    def fuel_type(self) -> str:
        pass

    @property
    @abstractmethod
    def max_speed(self) -> int:
        pass

    # Concrete method using abstract properties
    def describe(self):
        return f"{self.brand} {self.model} | {self.fuel_type} | {self.max_speed} km/h"

class Car(Vehicle):
    @property
    def fuel_type(self):
        return "Petrol"

    @property
    def max_speed(self):
        return 200

class ElectricCar(Vehicle):
    @property
    def fuel_type(self):
        return "Electric"

    @property
    def max_speed(self):
        return 250

class Bicycle(Vehicle):
    @property
    def fuel_type(self):
        return "Human-powered"

    @property
    def max_speed(self):
        return 40

vehicles = [Car("Toyota", "Camry"), ElectricCar("Tesla", "Model 3"), Bicycle("Trek", "FX3")]
for v in vehicles:
    print(v.describe())
```

---

## Interface-like Pattern

Python doesn't have interfaces like Java, but you can simulate them with ABC.

```python
from abc import ABC, abstractmethod

class Serializable(ABC):
    @abstractmethod
    def to_dict(self) -> dict:
        pass

    @abstractmethod
    def to_json(self) -> str:
        pass

class Printable(ABC):
    @abstractmethod
    def print_info(self):
        pass

# A class can "implement" multiple interfaces
class User(Serializable, Printable):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def to_dict(self):
        return {"name": self.name, "email": self.email}

    def to_json(self):
        import json
        return json.dumps(self.to_dict())

    def print_info(self):
        print(f"User: {self.name} <{self.email}>")

u = User("Alice", "alice@example.com")
u.print_info()
print(u.to_json())
```

---

## Code Example: Database Abstraction Layer

```python
from abc import ABC, abstractmethod
from typing import List, Dict, Any

class Database(ABC):
    """Abstract database interface — hide the implementation details"""

    @abstractmethod
    def connect(self) -> bool:
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def insert(self, table: str, data: Dict) -> int:
        pass

    @abstractmethod
    def find(self, table: str, query: Dict) -> List[Dict]:
        pass

    @abstractmethod
    def delete(self, table: str, record_id: int) -> bool:
        pass

class InMemoryDatabase(Database):
    """Concrete implementation — stores data in memory (for testing)"""

    def __init__(self):
        self._data: Dict[str, List] = {}
        self._connected = False
        self._next_id = 1

    def connect(self):
        self._connected = True
        print("Connected to in-memory database")
        return True

    def disconnect(self):
        self._connected = False
        print("Disconnected")

    def insert(self, table, data):
        if table not in self._data:
            self._data[table] = []
        record = {**data, "id": self._next_id}
        self._data[table].append(record)
        self._next_id += 1
        return record["id"]

    def find(self, table, query):
        if table not in self._data:
            return []
        return [r for r in self._data[table]
                if all(r.get(k) == v for k, v in query.items())]

    def delete(self, table, record_id):
        if table not in self._data:
            return False
        before = len(self._data[table])
        self._data[table] = [r for r in self._data[table] if r["id"] != record_id]
        return len(self._data[table]) < before

# Usage — code works with any Database implementation
def run_app(db: Database):
    db.connect()

    db.insert("users", {"name": "Alice", "email": "alice@example.com"})
    db.insert("users", {"name": "Bob", "email": "bob@example.com"})

    results = db.find("users", {"name": "Alice"})
    print(results)  # [{'name': 'Alice', 'email': '...', 'id': 1}]

    db.delete("users", 1)
    db.disconnect()

run_app(InMemoryDatabase())
```

---

## Abstraction vs Encapsulation

| | Abstraction | Encapsulation |
|--|-------------|---------------|
| Focus | Hiding complexity | Hiding data |
| How | Abstract classes, interfaces | Private attributes, properties |
| Goal | Define what to do | Control how data is accessed |
| Example | `Shape.area()` contract | `__balance` with `@property` |

They work together — abstraction defines the interface, encapsulation protects the data.

---

## Practice Questions

1. Create an abstract `Animal` class with abstract methods `speak()` and `move()`. Implement `Dog`, `Bird`, `Fish`
2. Build an abstract `Logger` class with `log(message)` and implement `FileLogger`, `ConsoleLogger`, `DatabaseLogger`
3. Design an abstract `PaymentGateway` with `charge()`, `refund()`, `get_status()` methods
4. Create an abstract `Sorter` class and implement `BubbleSorter`, `QuickSorter`, `MergeSorter`

---

## Summary

| Concept | Syntax |
|---------|--------|
| Abstract class | `class MyClass(ABC):` |
| Abstract method | `@abstractmethod` |
| Abstract property | `@property` + `@abstractmethod` |
| Prevent instantiation | Automatic with ABC |
| Concrete method in ABC | Just define it normally |

Key idea: define the **contract** in the abstract class, let subclasses handle the **details**.

---

Previous → [04 - Polymorphism](./04_polymorphism.md) | Next → [06 - Magic Methods](./06_magic_methods.md)

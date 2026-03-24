# ============================================================
# 10 OOP — 05: Abstraction
# ============================================================
# Run this file: python 05_abstraction.py
# ============================================================

from abc import ABC, abstractmethod
import math


# ── ABSTRACT CLASS ──────────────────────────────────────────
# An abstract class defines WHAT subclasses must do, not HOW
# You cannot instantiate an abstract class directly
class Shape(ABC):

    @abstractmethod
    def area(self) -> float:
        """Every Shape MUST implement area() — no default allowed."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Every Shape MUST implement perimeter()."""
        pass

    # Concrete method — shared by all subclasses, no override needed
    def describe(self):
        return (f"{self.__class__.__name__}: "
                f"area={self.area():.2f}, perimeter={self.perimeter():.2f}")


# Trying to instantiate Shape directly raises TypeError:
# Shape()  → TypeError: Can't instantiate abstract class Shape


# ── IMPLEMENTING ABSTRACT CLASSES ───────────────────────────
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width  = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def area(self):
        # Heron's formula
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5)]
for s in shapes:
    print(s.describe())


# ── ABSTRACT PROPERTIES ─────────────────────────────────────
# Force subclasses to implement properties, not just methods
class Vehicle(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @property
    @abstractmethod
    def fuel_type(self) -> str:
        """Subclass must define what fuel this vehicle uses."""
        pass

    @property
    @abstractmethod
    def max_speed(self) -> int:
        """Subclass must define the max speed in km/h."""
        pass

    # Concrete method — uses the abstract properties
    def describe(self):
        return f"{self.brand} {self.model} | {self.fuel_type} | {self.max_speed} km/h"


class Car(Vehicle):
    @property
    def fuel_type(self): return "Petrol"

    @property
    def max_speed(self): return 200


class ElectricCar(Vehicle):
    @property
    def fuel_type(self): return "Electric"

    @property
    def max_speed(self): return 250


class Bicycle(Vehicle):
    @property
    def fuel_type(self): return "Human-powered"

    @property
    def max_speed(self): return 40


for v in [Car("Toyota", "Camry"), ElectricCar("Tesla", "Model 3"), Bicycle("Trek", "FX3")]:
    print(v.describe())


# ── INTERFACE-LIKE PATTERN ──────────────────────────────────
# Python has no 'interface' keyword, but ABC achieves the same thing
# A class can "implement" multiple ABCs
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


class User(Serializable, Printable):
    """User implements both Serializable and Printable interfaces."""

    def __init__(self, name, email):
        self.name  = name
        self.email = email

    def to_dict(self):
        return {"name": self.name, "email": self.email}

    def to_json(self):
        import json
        return json.dumps(self.to_dict(), indent=2)

    def print_info(self):
        print(f"User: {self.name} <{self.email}>")


u = User("Alice", "alice@example.com")
u.print_info()
print(u.to_json())


# ── REAL EXAMPLE: Database Abstraction Layer ─────────────────
# The app code works with the abstract Database interface
# Swap InMemoryDatabase for a real DB without changing app code
class Database(ABC):
    """Abstract interface — defines what a database must support."""

    @abstractmethod
    def connect(self) -> bool: pass

    @abstractmethod
    def disconnect(self): pass

    @abstractmethod
    def insert(self, table: str, data: dict) -> int: pass

    @abstractmethod
    def find(self, table: str, query: dict) -> list: pass

    @abstractmethod
    def delete(self, table: str, record_id: int) -> bool: pass


class InMemoryDatabase(Database):
    """Concrete implementation — stores data in a dict (great for testing)."""

    def __init__(self):
        self._data = {}
        self._next_id = 1

    def connect(self):
        print("Connected to in-memory DB")
        return True

    def disconnect(self):
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


# App code only knows about Database — not InMemoryDatabase
def run_app(db: Database):
    db.connect()
    db.insert("users", {"name": "Alice", "email": "alice@example.com"})
    db.insert("users", {"name": "Bob",   "email": "bob@example.com"})
    results = db.find("users", {"name": "Alice"})
    print(results)
    db.delete("users", 1)
    db.disconnect()

run_app(InMemoryDatabase())


# ── PRACTICE ────────────────────────────────────────────────
# 1. Create abstract Animal with abstract speak() and move(). Implement Dog, Bird, Fish
# 2. Build abstract Logger with log(message). Implement FileLogger and ConsoleLogger
# 3. Design abstract PaymentGateway with charge(), refund(), get_status()
# 4. Create abstract Sorter and implement BubbleSorter and SelectionSorter

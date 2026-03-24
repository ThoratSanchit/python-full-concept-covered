# 06 - Magic Methods (Dunder Methods)

## What are Magic Methods?

Magic methods (also called **dunder methods** — double underscore) are special methods Python calls automatically in certain situations. They let your objects behave like built-in types.

```python
v1 + v2       # calls v1.__add__(v2)
print(obj)    # calls obj.__str__()
len(obj)      # calls obj.__len__()
obj[key]      # calls obj.__getitem__(key)
```

---

## Object Representation

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        """Human-readable — used by print() and str()"""
        return f'"{self.title}" by {self.author}'

    def __repr__(self):
        """Developer-readable — used in REPL and repr()"""
        return f"Book(title={self.title!r}, author={self.author!r}, pages={self.pages})"

b = Book("Clean Code", "Robert Martin", 431)
print(b)        # "Clean Code" by Robert Martin
print(repr(b))  # Book(title='Clean Code', author='Robert Martin', pages=431)
```

---

## Comparison Methods

```python
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __eq__(self, other):
        return self.gpa == other.gpa

    def __lt__(self, other):
        return self.gpa < other.gpa

    def __le__(self, other):
        return self.gpa <= other.gpa

    def __gt__(self, other):
        return self.gpa > other.gpa

    def __ge__(self, other):
        return self.gpa >= other.gpa

    def __ne__(self, other):
        return self.gpa != other.gpa

    def __str__(self):
        return f"{self.name} ({self.gpa})"

s1 = Student("Alice", 3.9)
s2 = Student("Bob", 3.5)

print(s1 > s2)   # True
print(s1 == s2)  # False

students = [Student("Charlie", 3.7), s2, s1]
print(sorted(students))  # Sorted by GPA (uses __lt__)
```

### Shortcut: `@total_ordering`

Define only `__eq__` and one comparison, get the rest for free.

```python
from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __eq__(self, other):
        return self.gpa == other.gpa

    def __lt__(self, other):
        return self.gpa < other.gpa

    # __le__, __gt__, __ge__ are auto-generated
```

---

## Arithmetic Operators

```python
class Money:
    def __init__(self, amount, currency="USD"):
        self.amount = round(amount, 2)
        self.currency = currency

    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot add different currencies")
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot subtract different currencies")
        return Money(self.amount - other.amount, self.currency)

    def __mul__(self, factor):
        return Money(self.amount * factor, self.currency)

    def __rmul__(self, factor):
        return self.__mul__(factor)  # Handles: 3 * money

    def __truediv__(self, divisor):
        return Money(self.amount / divisor, self.currency)

    def __neg__(self):
        return Money(-self.amount, self.currency)

    def __abs__(self):
        return Money(abs(self.amount), self.currency)

    def __str__(self):
        return f"{self.currency} {self.amount:.2f}"

    def __repr__(self):
        return f"Money({self.amount}, '{self.currency}')"

price = Money(10.00)
tax = Money(1.50)

print(price + tax)    # USD 11.50
print(price * 3)      # USD 30.00
print(3 * price)      # USD 30.00
print(abs(Money(-5))) # USD 5.00
```

---

## Container Methods

Make your class behave like a list or dict.

```python
class Playlist:
    def __init__(self, name):
        self.name = name
        self._songs = []

    def __len__(self):
        return len(self._songs)

    def __getitem__(self, index):
        return self._songs[index]

    def __setitem__(self, index, value):
        self._songs[index] = value

    def __delitem__(self, index):
        del self._songs[index]

    def __contains__(self, song):
        return song in self._songs

    def __iter__(self):
        return iter(self._songs)

    def append(self, song):
        self._songs.append(song)

    def __str__(self):
        return f"Playlist '{self.name}' ({len(self)} songs)"

p = Playlist("Favorites")
p.append("Bohemian Rhapsody")
p.append("Stairway to Heaven")
p.append("Hotel California")

print(len(p))                        # 3
print(p[0])                          # Bohemian Rhapsody
print("Hotel California" in p)       # True

for song in p:
    print(f"  - {song}")
```

---

## Context Manager Methods

```python
class DatabaseConnection:
    def __init__(self, host, db_name):
        self.host = host
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        print(f"Connecting to {self.db_name} at {self.host}")
        self.connection = f"conn:{self.db_name}"  # Simulated
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing connection to {self.db_name}")
        self.connection = None
        # Return False to propagate exceptions, True to suppress
        return False

with DatabaseConnection("localhost", "mydb") as conn:
    print(f"Using {conn}")
    # Connection auto-closes after block
```

---

## Callable Objects

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

double = Multiplier(2)
triple = Multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15
print(callable(double))  # True
```

---

## `__hash__` — Using Objects as Dict Keys

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        # Must be consistent with __eq__
        return hash((self.x, self.y))

p1 = Point(1, 2)
p2 = Point(1, 2)

# Can use as dict key or in set
locations = {p1: "Home", Point(3, 4): "Work"}
print(locations[p2])  # "Home" (p1 == p2, same hash)

point_set = {p1, p2, Point(3, 4)}
print(len(point_set))  # 2 (p1 and p2 are equal)
```

---

## Quick Reference

| Method | Triggered by |
|--------|-------------|
| `__init__` | `MyClass()` |
| `__str__` | `print(obj)`, `str(obj)` |
| `__repr__` | `repr(obj)`, REPL |
| `__len__` | `len(obj)` |
| `__add__` | `obj + other` |
| `__sub__` | `obj - other` |
| `__mul__` | `obj * other` |
| `__rmul__` | `other * obj` |
| `__eq__` | `obj == other` |
| `__lt__` | `obj < other` |
| `__contains__` | `item in obj` |
| `__getitem__` | `obj[key]` |
| `__setitem__` | `obj[key] = val` |
| `__delitem__` | `del obj[key]` |
| `__iter__` | `for x in obj` |
| `__next__` | `next(obj)` |
| `__call__` | `obj()` |
| `__enter__` | `with obj:` |
| `__exit__` | end of `with` block |
| `__hash__` | `hash(obj)`, dict key |
| `__bool__` | `bool(obj)`, `if obj:` |

---

## Practice Questions

1. Build a `Matrix` class with `__add__`, `__mul__`, `__str__`, and `__getitem__`
2. Create a `Stack` class with `__len__`, `__contains__`, `__iter__`, and `__bool__`
3. Implement a `Duration` class (hours, minutes, seconds) with `__add__`, `__sub__`, `__str__`, and comparison methods
4. Make a `Config` class that behaves like a dict using `__getitem__`, `__setitem__`, `__contains__`

---

## Summary

Magic methods let your objects integrate naturally with Python's syntax. Instead of calling `obj.get_length()`, users can just write `len(obj)`. Instead of `obj.add(other)`, they write `obj + other`.

The goal: make your classes feel like they belong in Python.

---

Previous → [05 - Abstraction](./05_abstraction.md) | Next → [07 - Real World Project](./07_real_world_project.md)

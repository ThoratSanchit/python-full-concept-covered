# 11 - Advanced Python

## What's in This Section?

This covers Python features that separate intermediate from advanced developers:
- Iterators and Generators
- Context Managers
- Decorators (advanced)
- Type Hints
- Dataclasses
- Comprehensions (advanced)
- `*args`, `**kwargs` patterns
- `functools` and `itertools`

---

## Iterators

An iterator is any object with `__iter__` and `__next__` methods.

```python
# Lists, strings, dicts are all iterables
nums = [1, 2, 3]
it = iter(nums)

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# next(it)  → StopIteration

# Custom iterator
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

for n in Countdown(5):
    print(n)  # 5, 4, 3, 2, 1
```

---

## Generators

Generators are functions that `yield` values one at a time — memory efficient.

```python
# Generator function
def count_up(start, end):
    current = start
    while current <= end:
        yield current
        current += 1

gen = count_up(1, 5)
print(next(gen))  # 1
print(next(gen))  # 2

for n in count_up(1, 5):
    print(n)

# Generator expression
squares = (x**2 for x in range(10))

# Infinite generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
first_10 = [next(fib) for _ in range(10)]
print(first_10)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### Generator vs List

```python
import sys

# List - all in memory
squares_list = [x**2 for x in range(1_000_000)]
print(sys.getsizeof(squares_list))  # ~8MB

# Generator - lazy, one at a time
squares_gen = (x**2 for x in range(1_000_000))
print(sys.getsizeof(squares_gen))   # ~120 bytes
```

### `yield from`

```python
def chain(*iterables):
    for it in iterables:
        yield from it

list(chain([1, 2], [3, 4], [5]))  # [1, 2, 3, 4, 5]
```

---

## Context Managers

Manage resources (files, connections, locks) safely.

```python
# Using 'with' statement
with open("file.txt") as f:
    data = f.read()
# File is closed here automatically

# Custom context manager using class
class Timer:
    import time

    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.elapsed = time.time() - self.start
        print(f"Elapsed: {self.elapsed:.4f}s")
        return False  # Don't suppress exceptions

with Timer() as t:
    sum(range(1_000_000))

# Custom context manager using @contextmanager
from contextlib import contextmanager

@contextmanager
def db_transaction(connection):
    try:
        yield connection
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()
```

---

## Type Hints

Make code self-documenting and catch bugs early.

```python
# Basic type hints
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

# Complex types
from typing import List, Dict, Tuple, Optional, Union, Callable

def process(items: List[int]) -> Dict[str, int]:
    return {"sum": sum(items), "count": len(items)}

def find_user(user_id: int) -> Optional[str]:
    # Returns str or None
    ...

def transform(value: Union[int, float]) -> float:
    return float(value)

# Python 3.10+ syntax (cleaner)
def find(user_id: int) -> str | None:
    ...

# Callable type hint
def apply(func: Callable[[int], int], value: int) -> int:
    return func(value)
```

---

## Dataclasses

Reduce boilerplate for data-holding classes.

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Point:
    x: float
    y: float

    def distance_from_origin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

p = Point(3.0, 4.0)
print(p)                        # Point(x=3.0, y=4.0)
print(p.distance_from_origin()) # 5.0
print(p == Point(3.0, 4.0))    # True (auto __eq__)

@dataclass
class Student:
    name: str
    age: int
    grades: List[float] = field(default_factory=list)
    is_active: bool = True

    @property
    def average(self) -> float:
        return sum(self.grades) / len(self.grades) if self.grades else 0.0

s = Student("Alice", 20, [85.0, 92.0, 78.0])
print(s.average)  # 85.0

# Frozen (immutable) dataclass
@dataclass(frozen=True)
class Color:
    r: int
    g: int
    b: int

red = Color(255, 0, 0)
# red.r = 100  → FrozenInstanceError
```

---

## Advanced Decorators

```python
import functools

# Decorator with arguments
def repeat(n: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hi(name):
    print(f"Hi, {name}!")

say_hi("Alice")  # Prints 3 times

# Class-based decorator
class Memoize:
    def __init__(self, func):
        self.func = func
        self.cache = {}
        functools.update_wrapper(self, func)

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]

@Memoize
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# Built-in lru_cache
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_calc(n):
    return sum(range(n))
```

---

## `functools` Module

```python
from functools import reduce, partial, wraps, lru_cache, total_ordering

# partial - fix some arguments
def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
cube = partial(power, exp=3)
print(square(5))  # 25

# reduce
from functools import reduce
product = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])  # 120

# total_ordering - define only __eq__ and one comparison
@total_ordering
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __eq__(self, other):
        return self.gpa == other.gpa

    def __lt__(self, other):
        return self.gpa < other.gpa

# Now <, <=, >, >= all work automatically
```

---

## `itertools` Module

```python
import itertools

# Infinite iterators
counter = itertools.count(10, 2)       # 10, 12, 14, ...
cycler = itertools.cycle([1, 2, 3])    # 1, 2, 3, 1, 2, 3, ...
repeater = itertools.repeat("x", 3)   # 'x', 'x', 'x'

# Combinatorics
list(itertools.combinations("ABC", 2))     # [('A','B'),('A','C'),('B','C')]
list(itertools.permutations("ABC", 2))     # [('A','B'),('A','C'),...]
list(itertools.product([0,1], repeat=3))   # All 3-bit binary numbers

# Grouping
data = [("A", 1), ("A", 2), ("B", 3), ("B", 4)]
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(key, list(group))

# Chaining
list(itertools.chain([1,2], [3,4], [5]))   # [1,2,3,4,5]
list(itertools.chain.from_iterable([[1,2],[3,4]]))  # [1,2,3,4]

# Slicing
list(itertools.islice(counter, 5))  # First 5 from infinite counter
```

---

## Walrus Operator `:=` (Python 3.8+)

Assign and use a value in the same expression.

```python
# Without walrus
data = get_data()
if data:
    process(data)

# With walrus
if data := get_data():
    process(data)

# Useful in while loops
while chunk := file.read(8192):
    process(chunk)

# In list comprehensions
results = [y for x in data if (y := transform(x)) > 0]
```

---

## Structural Pattern Matching (Python 3.10+)

```python
def handle_command(command):
    match command.split():
        case ["quit"]:
            return "Quitting"
        case ["go", direction]:
            return f"Going {direction}"
        case ["go", direction, speed]:
            return f"Going {direction} at {speed}"
        case ["pick", "up", item]:
            return f"Picking up {item}"
        case _:
            return f"Unknown command: {command}"

print(handle_command("go north"))        # Going north
print(handle_command("pick up sword"))   # Picking up sword
```

---

## Code Examples

### Example 1: Lazy Pipeline
```python
def read_lines(filename):
    with open(filename) as f:
        yield from f

def filter_lines(lines, keyword):
    for line in lines:
        if keyword in line:
            yield line

def transform_lines(lines):
    for line in lines:
        yield line.strip().upper()

# Chain generators — no memory overhead
pipeline = transform_lines(
    filter_lines(
        read_lines("log.txt"),
        "ERROR"
    )
)

for line in pipeline:
    print(line)
```

### Example 2: Typed Dataclass with Validation
```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Product:
    name: str
    price: float
    tags: List[str] = field(default_factory=list)

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")
        self.name = self.name.strip()

    @property
    def discounted_price(self, discount: float = 0.1) -> float:
        return self.price * (1 - discount)

p = Product("  Laptop  ", 999.99, ["electronics", "computers"])
print(p.name)   # "Laptop" (stripped)
```

---

## Practice Questions

1. Write a generator that yields prime numbers infinitely
2. Create a context manager that suppresses a specific exception type
3. Use `itertools.groupby` to group a list of dicts by a key
4. Write a typed function using `Optional` and `Union`
5. Convert a regular class to a `@dataclass` and add `__post_init__` validation

---

## Mini Task

Build a lazy data processing pipeline:
1. Generator that reads a large CSV file line by line
2. Generator that filters rows by a condition
3. Generator that transforms/maps each row
4. Context manager that handles file errors
5. Type hints throughout

---

## Summary

| Feature | Use Case |
|---------|---------|
| Generators | Memory-efficient iteration |
| Context managers | Resource management |
| Type hints | Documentation + static analysis |
| Dataclasses | Clean data containers |
| `lru_cache` | Memoization |
| `partial` | Pre-fill function arguments |
| `itertools` | Advanced iteration patterns |
| Walrus `:=` | Assign in expressions |

---

## Next Steps

Move to [12 - Standard Libraries](../12_Standard_Libraries/) to explore Python's powerful built-in modules.

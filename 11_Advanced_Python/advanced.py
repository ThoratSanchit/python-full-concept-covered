# ============================================================
# 11 - Advanced Python
# ============================================================
# Run this file: python advanced.py
# ============================================================

import sys
import time
from functools import lru_cache, partial, reduce, wraps
from dataclasses import dataclass, field
from typing import List, Optional, Generator
from contextlib import contextmanager
import itertools


# ── ITERATORS ───────────────────────────────────────────────
# An iterator is any object with __iter__ and __next__
# Lists, strings, dicts are all iterables — iter() makes them iterators
nums = [1, 2, 3]
it   = iter(nums)

print(next(it))     # 1
print(next(it))     # 2
print(next(it))     # 3
# next(it)  → StopIteration — no more items

# Custom iterator — useful when you need lazy, stateful iteration
class Countdown:
    """Counts down from start to 1."""
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self     # The iterator IS the object itself

    def __next__(self):
        if self.current <= 0:
            raise StopIteration     # Signal that iteration is done
        value = self.current
        self.current -= 1
        return value

for n in Countdown(5):
    print(n, end=" ")   # 5 4 3 2 1
print()


# ── GENERATORS ──────────────────────────────────────────────
# Generator functions use 'yield' — they pause and resume execution
# Much simpler than writing a full iterator class
def count_up(start: int, end: int) -> Generator[int, None, None]:
    """Yield integers from start to end, one at a time."""
    current = start
    while current <= end:
        yield current       # Pause here, return value, resume on next()
        current += 1

gen = count_up(1, 5)
print(next(gen))    # 1
print(next(gen))    # 2

for n in count_up(1, 5):
    print(n, end=" ")
print()

# Infinite generator — only computes what you ask for
def fibonacci():
    """Yield Fibonacci numbers forever."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
first_10 = [next(fib) for _ in range(10)]
print(first_10)     # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# yield from — delegate to another iterable
def chain_lists(*lists):
    for lst in lists:
        yield from lst  # Yields each item from lst one by one

print(list(chain_lists([1, 2], [3, 4], [5])))   # [1, 2, 3, 4, 5]


# ── GENERATOR EXPRESSIONS ───────────────────────────────────
# Like list comprehensions but lazy — use () instead of []
list_comp = [x**2 for x in range(1_000_000)]   # All in memory at once
gen_expr  = (x**2 for x in range(1_000_000))   # Lazy — almost no memory

print(f"List: {sys.getsizeof(list_comp):,} bytes")
print(f"Generator: {sys.getsizeof(gen_expr)} bytes")

# Generators work directly with sum(), max(), any(), all()
total = sum(x**2 for x in range(100))   # No list() needed
print(f"Sum of squares: {total}")


# ── CONTEXT MANAGERS ────────────────────────────────────────
# Manage resources safely — guarantee cleanup even if exceptions occur

# Class-based context manager
class Timer:
    """Measure execution time of a code block."""
    def __enter__(self):
        self._start = time.time()
        return self     # Value assigned to 'as' variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.time() - self._start
        print(f"Elapsed: {self.elapsed:.4f}s")
        return False    # False = don't suppress exceptions

with Timer() as t:
    total = sum(range(1_000_000))
# t.elapsed is available here

# Function-based context manager using @contextmanager
@contextmanager
def managed_file(filename, mode="r"):
    """Open a file and guarantee it's closed, even on error."""
    f = open(filename, mode)
    try:
        yield f         # Code inside 'with' block runs here
    finally:
        f.close()       # Always runs — cleanup guaranteed

# Write then read using our context manager
with managed_file("temp.txt", "w") as f:
    f.write("Hello from context manager!\n")

with managed_file("temp.txt", "r") as f:
    print(f.read().strip())

import os
os.remove("temp.txt")


# ── TYPE HINTS ──────────────────────────────────────────────
# Type hints don't enforce types at runtime — they're for documentation
# and static analysis tools (mypy, pyright, IDE autocomplete)

def greet(name: str, times: int = 1) -> str:
    """Greet someone a given number of times."""
    return (f"Hello, {name}! " * times).strip()

def process(items: List[int]) -> dict:
    return {"sum": sum(items), "avg": sum(items) / len(items)}

def find_user(user_id: int) -> Optional[str]:
    """Returns a username or None if not found."""
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)   # Returns str or None

print(greet("Alice", 3))
print(process([1, 2, 3, 4, 5]))
print(find_user(1))     # Alice
print(find_user(99))    # None


# ── DATACLASSES ─────────────────────────────────────────────
# @dataclass auto-generates __init__, __repr__, __eq__ — less boilerplate
@dataclass
class Point:
    x: float
    y: float

    def distance_from_origin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

p1 = Point(3.0, 4.0)
p2 = Point(3.0, 4.0)

print(p1)               # Point(x=3.0, y=4.0)  — auto __repr__
print(p1 == p2)         # True  — auto __eq__ compares fields
print(p1.distance_from_origin())    # 5.0

# field() for mutable defaults and post-init validation
@dataclass
class Student:
    name:     str
    age:      int
    grades:   List[float] = field(default_factory=list)  # Mutable default — use field()
    is_active: bool = True

    def __post_init__(self):
        """Called after __init__ — great for validation."""
        if self.age < 0:
            raise ValueError("Age cannot be negative")
        self.name = self.name.strip()   # Auto-clean name

    @property
    def average(self) -> float:
        return sum(self.grades) / len(self.grades) if self.grades else 0.0

s = Student("  Alice  ", 20, [85.0, 92.0, 78.0])
print(s.name)       # "Alice"  — stripped by __post_init__
print(s.average)    # 85.0

# Frozen dataclass — immutable (like a named tuple but with methods)
@dataclass(frozen=True)
class Color:
    r: int
    g: int
    b: int

    def to_hex(self) -> str:
        return f"#{self.r:02x}{self.g:02x}{self.b:02x}"

red = Color(255, 0, 0)
print(red.to_hex())     # #ff0000
# red.r = 100  → FrozenInstanceError


# ── LRU CACHE ───────────────────────────────────────────────
# Cache function results — avoid recomputing expensive calls
@lru_cache(maxsize=128)
def fib(n: int) -> int:
    """Fibonacci with memoization — fast even for large n."""
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(40))                  # Fast — results are cached
print(fib.cache_info())         # CacheInfo(hits=38, misses=41, ...)


# ── PARTIAL FUNCTIONS ───────────────────────────────────────
# Pre-fill some arguments of a function to create a specialized version
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)     # Fix exponent=2
cube   = partial(power, exponent=3)     # Fix exponent=3

print(square(5))    # 25
print(cube(3))      # 27

# Useful for callbacks and configuration
def send_email(to, subject, body, from_addr="noreply@example.com"):
    return f"From: {from_addr} | To: {to} | {subject}"

send_welcome = partial(send_email, subject="Welcome!", body="Thanks for joining")
print(send_welcome("alice@example.com"))


# ── ITERTOOLS ───────────────────────────────────────────────
# Efficient tools for working with iterables

# chain — combine multiple iterables
combined = list(itertools.chain([1, 2], [3, 4], [5]))
print(combined)     # [1, 2, 3, 4, 5]

# combinations — unique pairs (order doesn't matter)
pairs = list(itertools.combinations("ABCD", 2))
print(pairs)        # [('A','B'), ('A','C'), ...]

# groupby — group consecutive items by a key
data = [("Alice", "Eng"), ("Bob", "Eng"), ("Carol", "HR"), ("Dave", "HR")]
for dept, group in itertools.groupby(data, key=lambda x: x[1]):
    members = [name for name, _ in group]
    print(f"{dept}: {members}")

# islice — take first N items from any iterable (including infinite ones)
counter = itertools.count(start=10, step=5)     # 10, 15, 20, 25, ...
first_5 = list(itertools.islice(counter, 5))
print(first_5)      # [10, 15, 20, 25, 30]


# ── WALRUS OPERATOR := (Python 3.8+) ────────────────────────
# Assign AND use a value in the same expression
numbers = [1, -2, 3, -4, 5]

# Without walrus — compute twice
positives = [n for n in numbers if n > 0]

# With walrus — compute once, use in condition and expression
# Here: transform n, keep only if result > 5
results = [y for n in numbers if (y := n * 3) > 5]
print(results)      # [9, 15]


# ── PRACTICE ────────────────────────────────────────────────
# 1. Write a generator that yields prime numbers infinitely
# 2. Create a @contextmanager that suppresses a specific exception type
# 3. Convert a regular class to @dataclass with __post_init__ validation
# 4. Use itertools.groupby to group a list of dicts by a key
# 5. Write a typed function using Optional and List, run mypy on it

# ============================================================
# 05 - Functional Programming
# ============================================================
# Run this file: python functional.py
# ============================================================

from functools import reduce, partial, lru_cache


# ── MAP ─────────────────────────────────────────────────────
# Apply a function to EVERY item in an iterable
# Returns a lazy iterator — wrap in list() to see results
numbers = [1, 2, 3, 4, 5]

squared  = list(map(lambda x: x**2, numbers))
doubled  = list(map(lambda x: x * 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]
print(doubled)  # [2, 4, 6, 8, 10]

# map() with a named function
def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

temps_c = [0, 20, 37, 100]
temps_f = list(map(celsius_to_fahrenheit, temps_c))
print(temps_f)  # [32.0, 68.0, 98.6, 212.0]


# ── FILTER ──────────────────────────────────────────────────
# Keep only items where the function returns True
evens    = list(filter(lambda x: x % 2 == 0, numbers))
positives = list(filter(lambda x: x > 0, [-3, -1, 0, 2, 5]))
print(evens)        # [2, 4]
print(positives)    # [2, 5]

# filter(None, iterable) removes all falsy values (0, "", None, [], etc.)
mixed = [0, 1, "", "hello", None, [], [1, 2], False, True]
truthy = list(filter(None, mixed))
print(truthy)   # [1, 'hello', [1, 2], True]


# ── REDUCE ──────────────────────────────────────────────────
# Cumulatively apply a function to reduce a list to a single value
# reduce(f, [a, b, c]) → f(f(a, b), c)
total   = reduce(lambda x, y: x + y, numbers)       # 15
product = reduce(lambda x, y: x * y, numbers)       # 120
maximum = reduce(lambda x, y: x if x > y else y, numbers)  # 5

print(total, product, maximum)

# With an initial value (useful for empty lists)
total_with_start = reduce(lambda x, y: x + y, numbers, 100)  # 115
print(total_with_start)


# ── LIST COMPREHENSIONS ─────────────────────────────────────
# More readable than map/filter for most cases — prefer these
squares  = [x**2 for x in range(10)]
evens    = [x for x in range(20) if x % 2 == 0]
labels   = ["even" if x % 2 == 0 else "odd" for x in range(6)]

print(squares)
print(evens)
print(labels)

# Nested comprehension — flatten a 2D matrix
matrix  = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat    = [item for row in matrix for item in row]
print(flat)     # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Dict comprehension
word_len = {word: len(word) for word in ["apple", "banana", "cherry"]}
print(word_len)

# Set comprehension — automatically removes duplicates
unique_lengths = {len(word) for word in ["hi", "hello", "hey", "world"]}
print(unique_lengths)   # {2, 5}


# ── GENERATOR EXPRESSIONS ───────────────────────────────────
# Like list comprehensions but LAZY — compute one item at a time
# Use when you don't need all values at once (saves memory)
import sys

list_comp = [x**2 for x in range(1_000_000)]   # All in memory
gen_expr  = (x**2 for x in range(1_000_000))   # Lazy — almost no memory

print(f"List size: {sys.getsizeof(list_comp):,} bytes")
print(f"Generator size: {sys.getsizeof(gen_expr)} bytes")

# Generators work great with sum(), max(), any(), all()
total = sum(x**2 for x in range(100))   # No need for list()
print(total)


# ── GENERATOR FUNCTIONS ─────────────────────────────────────
# Use 'yield' instead of 'return' — pauses and resumes execution
def fibonacci():
    """Infinite Fibonacci sequence — only computes what you ask for."""
    a, b = 0, 1
    while True:
        yield a         # Pause here, return a, resume next time
        a, b = b, a + b

fib = fibonacci()
first_10 = [next(fib) for _ in range(10)]
print(first_10)     # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def count_up(start, end):
    """Yield numbers from start to end."""
    while start <= end:
        yield start
        start += 1

for n in count_up(1, 5):
    print(n, end=" ")
print()


# ── CLOSURES ────────────────────────────────────────────────
# A function that captures variables from its enclosing scope
def make_adder(n):
    """Returns a function that adds n to its argument."""
    def adder(x):
        return x + n    # 'n' is captured from the outer scope
    return adder

add5  = make_adder(5)
add10 = make_adder(10)
print(add5(3))      # 8
print(add10(3))     # 13


# ── PARTIAL FUNCTIONS ───────────────────────────────────────
# Pre-fill some arguments of a function
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)     # Fix exponent=2
cube   = partial(power, exponent=3)     # Fix exponent=3

print(square(5))    # 25
print(cube(3))      # 27


# ── LRU CACHE (MEMOIZATION) ─────────────────────────────────
# Cache results of expensive function calls — avoid recomputing
@lru_cache(maxsize=128)
def fib_cached(n):
    """Fibonacci with caching — much faster than naive recursion."""
    if n < 2:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)

print(fib_cached(40))   # Fast — results are cached
print(fib_cached.cache_info())  # See cache hits/misses


# ── REAL EXAMPLE: Functional Data Pipeline ──────────────────
employees = [
    {"name": "Alice", "dept": "Engineering", "salary": 95000},
    {"name": "Bob",   "dept": "Marketing",   "salary": 72000},
    {"name": "Carol", "dept": "Engineering", "salary": 105000},
    {"name": "Dave",  "dept": "Marketing",   "salary": 68000},
    {"name": "Eve",   "dept": "Engineering", "salary": 88000},
]

# Get average salary of Engineering department — functional style
eng_salaries = list(map(
    lambda e: e["salary"],
    filter(lambda e: e["dept"] == "Engineering", employees)
))
avg = reduce(lambda x, y: x + y, eng_salaries) / len(eng_salaries)
print(f"\nEngineering avg salary: ${avg:,.0f}")

# Same thing with comprehensions (more readable)
eng_avg = sum(e["salary"] for e in employees if e["dept"] == "Engineering") / \
          sum(1 for e in employees if e["dept"] == "Engineering")
print(f"Engineering avg salary: ${eng_avg:,.0f}")


# ── PRACTICE ────────────────────────────────────────────────
# 1. Use map() to convert ["1","2","3","4"] to [1, 2, 3, 4]
# 2. Use filter() to get words longer than 4 chars from a list
# 3. Write a generator that yields square numbers: 1, 4, 9, 16, ...
# 4. Create a compose(f, g) function where compose(f,g)(x) = f(g(x))

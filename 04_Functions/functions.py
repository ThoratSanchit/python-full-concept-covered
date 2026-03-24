# ============================================================
# 04 - Functions
# ============================================================
# Run this file: python functions.py
# ============================================================


# ── BASIC FUNCTION ──────────────────────────────────────────
# def keyword, function name, parameters in parentheses
def greet(name):
    """Docstring: describes what the function does.
    Always write one — it shows up in help() and IDEs."""
    return f"Hello, {name}!"

print(greet("Alice"))   # Hello, Alice!


# ── DEFAULT PARAMETERS ──────────────────────────────────────
# Default values make parameters optional
# Rule: defaults must come AFTER required parameters
def greet_with_title(name, greeting="Hello", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"

print(greet_with_title("Bob"))                      # Hello, Bob!
print(greet_with_title("Bob", "Hi"))                # Hi, Bob!
print(greet_with_title("Bob", punctuation="..."))   # Hello, Bob...


# ── KEYWORD ARGUMENTS ───────────────────────────────────────
# Pass by name — order doesn't matter, makes calls more readable
def create_user(name, age, role="user"):
    return {"name": name, "age": age, "role": role}

user = create_user(age=25, name="Alice", role="admin")
print(user)


# ── *args — VARIABLE POSITIONAL ARGUMENTS ───────────────────
# *args collects extra positional args into a TUPLE
def sum_all(*args):
    """Accept any number of numbers and return their sum."""
    return sum(args)    # args is a tuple: (1, 2, 3, ...)

print(sum_all(1, 2, 3))         # 6
print(sum_all(1, 2, 3, 4, 5))   # 15
print(sum_all())                 # 0


# ── **kwargs — VARIABLE KEYWORD ARGUMENTS ───────────────────
# **kwargs collects extra keyword args into a DICT
def print_profile(**kwargs):
    """Print any key-value pairs passed in."""
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print_profile(name="Alice", age=30, city="NYC", hobby="coding")


# ── COMBINING ALL PARAMETER TYPES ───────────────────────────
# Order must be: regular → *args → keyword-only → **kwargs
def flexible(required, *args, keyword_only="default", **kwargs):
    print(f"required: {required}")
    print(f"args: {args}")
    print(f"keyword_only: {keyword_only}")
    print(f"kwargs: {kwargs}")

flexible("hello", 1, 2, 3, keyword_only="custom", x=10, y=20)


# ── MULTIPLE RETURN VALUES ──────────────────────────────────
# Python returns a tuple — unpack it on the calling side
def min_max(numbers):
    return min(numbers), max(numbers)   # Returns a tuple

low, high = min_max([3, 1, 4, 1, 5, 9])
print(f"Min: {low}, Max: {high}")


# ── LAMBDA FUNCTIONS ────────────────────────────────────────
# Anonymous one-liner functions — best for simple, short operations
square = lambda x: x ** 2
add    = lambda x, y: x + y

print(square(5))    # 25
print(add(3, 4))    # 7

# Most common use: as a key for sorting
students = [("Alice", 3.9), ("Bob", 3.5), ("Charlie", 3.7)]
students.sort(key=lambda s: s[1])   # Sort by GPA (index 1)
print(students)


# ── RECURSION ───────────────────────────────────────────────
# A function that calls itself — needs a BASE CASE to stop
def factorial(n):
    """n! = n × (n-1) × ... × 1"""
    if n <= 1:          # Base case — stops the recursion
        return 1
    return n * factorial(n - 1)   # Recursive case

print(factorial(5))     # 120
# How it works: factorial(5) → 5 * factorial(4) → 5 * 4 * factorial(3) → ...


# ── SCOPE — LEGB RULE ───────────────────────────────────────
# Python looks for variables in: Local → Enclosing → Global → Built-in
total = 0   # Global variable

def add_to_total(amount):
    global total        # Declare we want to modify the global
    total += amount

add_to_total(10)
add_to_total(5)
print(f"Total: {total}")    # 15


# ── CLOSURES ────────────────────────────────────────────────
# A function that "remembers" variables from its enclosing scope
def make_multiplier(factor):
    """Returns a new function that multiplies by factor."""
    def multiply(x):
        return x * factor   # 'factor' is remembered from outer scope
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))    # 10
print(triple(5))    # 15


# ── DECORATORS ──────────────────────────────────────────────
# A function that wraps another function to add behavior
import time
from functools import wraps

def timer(func):
    """Decorator: measures how long a function takes to run."""
    @wraps(func)    # Preserves the original function's name and docstring
    def wrapper(*args, **kwargs):
        start  = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

@timer  # Same as: slow_sum = timer(slow_sum)
def slow_sum(n):
    """Sum numbers 0 to n."""
    return sum(range(n))

print(slow_sum(1_000_000))


# ── REAL EXAMPLE: Data Processing Pipeline ──────────────────
def clean(data):
    """Strip whitespace and remove empty strings."""
    return [item.strip() for item in data if item.strip()]

def normalize(data):
    """Convert all strings to lowercase."""
    return [item.lower() for item in data]

def deduplicate(data):
    """Remove duplicates while preserving order."""
    seen = set()
    return [x for x in data if not (x in seen or seen.add(x))]

def process(data):
    """Chain all steps together."""
    return deduplicate(normalize(clean(data)))

raw = ["  Python  ", "java", "", "PYTHON", "  ", "Java", "Go"]
print(process(raw))     # ['python', 'java', 'go']


# ── PRACTICE ────────────────────────────────────────────────
# 1. Write is_palindrome(s) that returns True if s reads the same backwards
# 2. Write find_max(*args) that returns the largest value without using max()
# 3. Create a memoize(func) decorator that caches results

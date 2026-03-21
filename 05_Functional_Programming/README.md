# 05 - Functional Programming

## What is Functional Programming?

Functional Programming (FP) is a programming paradigm where programs are constructed by applying and composing functions. It emphasizes:

- **Pure Functions**: Same input always produces same output, no side effects
- **Immutability**: Data doesn't change after creation
- **First-Class Functions**: Functions can be passed as arguments, returned from functions
- **Higher-Order Functions**: Functions that operate on other functions

---

## Deep Explanation

### Imperative vs Functional

```python
# Imperative (How to do it)
numbers = [1, 2, 3, 4, 5]
squared = []
for n in numbers:
    squared.append(n ** 2)

# Functional (What to do)
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
```

### Benefits of FP

1. **Easier to test**: Pure functions have no hidden dependencies
2. **Easier to debug**: Output depends only on input
3. **Easier to parallelize**: No shared state means no race conditions
4. **More readable**: Declarative code describes intent

---

## map()

Apply a function to every item in an iterable.

```python
# Syntax: map(function, iterable)

numbers = [1, 2, 3, 4, 5]

# Using lambda
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Using named function
def double(x):
    return x * 2

doubled = list(map(double, numbers))
print(doubled)  # [2, 4, 6, 8, 10]

# Multiple iterables
list1 = [1, 2, 3]
list2 = [4, 5, 6]
sums = list(map(lambda x, y: x + y, list1, list2))
print(sums)  # [5, 7, 9]

# With strings
words = ["hello", "world", "python"]
lengths = list(map(len, words))
print(lengths)  # [5, 5, 6]
```

### map() returns an iterator

```python
numbers = [1, 2, 3]
result = map(lambda x: x ** 2, numbers)

print(result)  # <map object at 0x...>
print(list(result))  # [1, 4, 9]

# Can only iterate once
print(list(result))  # [] - empty!
```

---

## filter()

Select items that satisfy a condition.

```python
# Syntax: filter(function, iterable)
# function should return True/False

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Numbers greater than 5
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(greater_than_5)  # [6, 7, 8, 9, 10]

# Filter strings
words = ["apple", "banana", "cherry", "date"]
long_words = list(filter(lambda w: len(w) > 5, words))
print(long_words)  # ['banana', 'cherry']

# Filter None values
mixed = [1, None, 2, None, 3, None]
valid = list(filter(None, mixed))
print(valid)  # [1, 2, 3]
```

### filter() with None

When function is `None`, filter uses truthiness:

```python
values = [0, 1, "", "hello", [], [1, 2], None, True]
truthy = list(filter(None, values))
print(truthy)  # [1, 'hello', [1, 2], True]
```

---

## reduce()

Apply function cumulatively to reduce iterable to single value.

```python
from functools import reduce

# Syntax: reduce(function, iterable, initial)

numbers = [1, 2, 3, 4, 5]

# Sum all numbers
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 15

# With initial value
total = reduce(lambda x, y: x + y, numbers, 10)
print(total)  # 25 (10 + 1 + 2 + 3 + 4 + 5)

# Product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120

# Find maximum
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)  # 5

# String concatenation
words = ["Hello", " ", "World", "!"]
sentence = reduce(lambda x, y: x + y, words)
print(sentence)  # "Hello World!"
```

### How reduce() Works

```python
# reduce(f, [a, b, c, d])
# Step 1: f(a, b) → result1
# Step 2: f(result1, c) → result2
# Step 3: f(result2, d) → final_result

numbers = [1, 2, 3, 4]
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
```

---

## List Comprehensions

Concise way to create lists.

```python
# Syntax: [expression for item in iterable if condition]

# Basic
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With condition
evens = [x for x in range(20) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# With if-else
labels = ["even" if x % 2 == 0 else "odd" for x in range(10)]
print(labels)  # ['even', 'odd', 'even', 'odd', ...]

# Nested loops
pairs = [(x, y) for x in range(3) for y in range(3)]
print(pairs)  # [(0,0), (0,1), (0,2), (1,0), ...]

# Flatten matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [item for row in matrix for item in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Set comprehension
squares_set = {x**2 for x in range(20)}
print(squares_set)  # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, ...}
```

### List Comprehension vs map/filter

```python
numbers = [1, 2, 3, 4, 5]

# map()
squares_map = list(map(lambda x: x**2, numbers))

# List comprehension
squares_comp = [x**2 for x in numbers]

# filter()
evens_filter = list(filter(lambda x: x % 2 == 0, numbers))

# List comprehension
evens_comp = [x for x in numbers if x % 2 == 0]

# Both produce same result, but comprehensions are often more readable
```

---

## Generator Expressions

Memory-efficient lazy evaluation.

```python
# List comprehension - creates entire list in memory
squares_list = [x**2 for x in range(1000000)]  # Uses lots of memory

# Generator expression - yields one item at a time
squares_gen = (x**2 for x in range(1000000))  # Almost no memory

# Use generators with iteration
for square in squares_gen:
    if square > 100:
        break

# Convert to list when needed
first_10 = list(x**2 for x in range(10))

# Generator functions
def infinite_counter(start=0):
    """Generate infinite sequence"""
    while True:
        yield start
        start += 1

counter = infinite_counter()
print(next(counter))  # 0
print(next(counter))  # 1
print(next(counter))  # 2
```

---

## Closures

Function that remembers values from enclosing scope.

```python
def make_multiplier(n):
    """Returns a function that multiplies by n"""
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15

# Another example
def make_power(exponent):
    def power(base):
        return base ** exponent
    return power

square = make_power(2)
cube = make_power(3)

print(square(4))   # 16
print(cube(3))     # 27
```

### Closure with Mutable State

```python
def make_counter():
    count = 0
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter

counter1 = make_counter()
counter2 = make_counter()

print(counter1())  # 1
print(counter1())  # 2
print(counter2())  # 1 (independent)
print(counter1())  # 3
```

---

## Decorators

Modify or enhance functions without changing their code.

### Basic Decorator

```python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function call
# Hello!
# After function call
```

### Decorator with Arguments

```python
def repeat(n):
    """Repeat function call n times"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# Output:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!
```

### Practical Decorators

```python
import time
from functools import wraps

def timing(func):
    """Measure execution time"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

def memoize(func):
    """Cache function results"""
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

def retry(max_attempts=3):
    """Retry function on failure"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
            raise Exception("All attempts failed")
        return wrapper
    return decorator

# Usage
@timing
@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(30))  # Fast due to memoization
```

### Preserving Function Metadata

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # Preserves __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        """Wrapper docstring"""
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def my_function():
    """Original docstring"""
    pass

print(my_function.__name__)  # my_function (not wrapper)
print(my_function.__doc__)   # Original docstring
```

---

## Code Examples

### Example 1: Data Pipeline
```python
from functools import reduce

def pipeline(data, *functions):
    """Apply series of functions to data"""
    return reduce(lambda x, f: f(x), functions, data)

# Processing functions
def clean(data):
    return [x.strip() for x in data if x.strip()]

def normalize(data):
    return [x.lower() for x in data]

def filter_short(data, min_len=3):
    return [x for x in data if len(x) >= min_len]

def count_words(data):
    from collections import Counter
    return Counter(data)

# Usage
raw_data = ["  Hello  ", "", "hello", "WORLD", "hi", "world", "  "]
result = pipeline(
    raw_data,
    clean,
    normalize,
    lambda x: filter_short(x, 4),
    count_words
)
print(result)  # Counter({'hello': 2, 'world': 2})
```

### Example 2: Function Composition
```python
from functools import reduce

def compose(*functions):
    """Compose functions right to left"""
    def composed(x):
        return reduce(lambda v, f: f(v), reversed(functions), x)
    return composed

# Individual functions
def add_one(x):
    return x + 1

def double(x):
    return x * 2

def square(x):
    return x ** 2

# Compose: square(double(add_one(x)))
transform = compose(square, double, add_one)

print(transform(3))  # (3+1)*2 squared = 64

# Another composition
def format_currency(x):
    return f"${x:.2f}"

def add_tax(x, rate=0.1):
    return x * (1 + rate)

price_pipeline = compose(format_currency, lambda x: add_tax(x, 0.2))
print(price_pipeline(100))  # $120.00
```

### Example 3: Lazy Evaluation with Generators
```python
def read_large_file(filename):
    """Lazy file reading"""
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()

def filter_lines(lines, pattern):
    """Lazy filtering"""
    for line in lines:
        if pattern in line:
            yield line

def process_lines(lines):
    """Lazy processing"""
    for line in lines:
        yield line.upper()

# Chain generators (no memory overhead)
lines = read_large_file("huge_file.txt")
filtered = filter_lines(lines, "ERROR")
processed = process_lines(filtered)

# Process one line at a time
for line in processed:
    print(line)
    # Can break early without reading entire file
```

### Example 4: Curry Function
```python
from functools import partial

def curry(func):
    """Convert function to curried form"""
    def curried(*args):
        if len(args) >= func.__code__.co_argcount:
            return func(*args)
        return lambda x: curried(*(args + (x,)))
    return curried

@curry
def add(a, b, c):
    return a + b + c

# Usage
add_5 = add(5)
add_5_3 = add_5(3)
result = add_5_3(2)  # 10

# Or all at once
print(add(1)(2)(3))  # 6

# Using functools.partial
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(5))  # 25
print(cube(3))    # 27
```

### Example 5: Event System with Decorators
```python
class EventManager:
    def __init__(self):
        self.handlers = {}
    
    def on(self, event):
        """Decorator to register event handlers"""
        def decorator(func):
            if event not in self.handlers:
                self.handlers[event] = []
            self.handlers[event].append(func)
            return func
        return decorator
    
    def emit(self, event, *args, **kwargs):
        """Trigger all handlers for an event"""
        for handler in self.handlers.get(event, []):
            handler(*args, **kwargs)

# Usage
events = EventManager()

@events.on("user_login")
def log_login(username):
    print(f"User logged in: {username}")

@events.on("user_login")
def send_welcome(username):
    print(f"Welcome email sent to: {username}")

@events.on("error")
def log_error(message):
    print(f"ERROR: {message}")

# Trigger events
events.emit("user_login", "john_doe")
# Output:
# User logged in: john_doe
# Welcome email sent to: john_doe

events.emit("error", "Connection failed")
# Output:
# ERROR: Connection failed
```

---

## Real-World Use Cases

1. **Data Processing Pipelines**: ETL operations, data transformations
2. **Event Systems**: Callback registration, pub/sub patterns
3. **API Rate Limiting**: Decorator-based throttling
4. **Caching**: Memoization for expensive computations
5. **Logging**: Decorators for automatic logging
6. **Validation**: Function composition for data validation

---

## Common Mistakes / Pitfalls

| Mistake | Example | Solution |
|---------|---------|----------|
| Using list comp when generator needed | `[x for x in huge_data]` | Use `(x for x in huge_data)` |
| Forgetting to convert map/filter | `map(...)` without `list()` | Use `list()` or iterate |
| Mutable default in closure | Closure capturing loop variable | Use default argument |
| Not using @wraps | Losing function metadata | Always use `@wraps` |
| Over-engineering | Simple loop vs complex FP | Use simplest solution |

```python
# Error 1: Closure capturing loop variable
functions = []
for i in range(5):
    functions.append(lambda: i)  # All return 4!

print([f() for f in functions])  # [4, 4, 4, 4, 4]

# Fix: Default argument captures value
functions = []
for i in range(5):
    functions.append(lambda x=i: x)

print([f() for f in functions])  # [0, 1, 2, 3, 4]

# Error 2: Not using @wraps
def bad_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@bad_decorator
def my_func():
    """My function"""
    pass

print(my_func.__name__)  # wrapper (wrong!)

# Fix: Use @wraps
from functools import wraps

def good_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

---

## Best Practices

1. **Prefer comprehensions over map/filter**
   ```python
   # More readable
   squares = [x**2 for x in numbers]
   
   # Less readable
   squares = list(map(lambda x: x**2, numbers))
   ```

2. **Use generators for large datasets**
   ```python
   # Memory efficient
   def process_large_file(filename):
       with open(filename) as f:
           for line in f:
               yield process_line(line)
   ```

3. **Keep decorators simple**
   ```python
   # Good - single responsibility
   @timing
   @memoize
   def calculate():
       ...
   
   # Bad - too complex
   @complex_decorator_with_many_responsibilities
   def calculate():
       ...
   ```

4. **Use functools for common patterns**
   ```python
   from functools import partial, reduce, wraps, lru_cache
   
   @lru_cache(maxsize=128)  # Built-in memoization
   def fibonacci(n):
       if n < 2:
           return n
       return fibonacci(n-1) + fibonacci(n-2)
   ```

5. **Document closures and decorators**
   ```python
   def make_counter():
       """
       Create an independent counter.
       
       Each call returns a new counter starting at 0.
       Counters are independent of each other.
       """
       count = 0
       def counter():
           nonlocal count
           count += 1
           return count
       return counter
   ```

---

## Practice Questions

### Question 1 (Easy)
Use `map()` to convert a list of strings to uppercase.

### Question 2 (Easy)
Use `filter()` to get all numbers divisible by 3 from a list.

### Question 3 (Medium)
Write a list comprehension that creates a list of tuples (number, square, cube) for numbers 1-10.

### Question 4 (Medium)
Create a decorator `@count_calls` that counts how many times a function is called.

### Question 5 (Hard)
Implement a `pipe()` function that chains multiple functions together (left to right composition).

**Example:** `pipe(add_one, double, square)(3)` → `((3+1)*2)^2` = 64

---

## Mini Task / Assignment

### Task: Build a Functional Data Processing Library

Create a module with functional utilities for data processing:

1. **Transformation Functions**
   - `map_values(func, dict)` - Apply function to all dict values
   - `filter_keys(predicate, dict)` - Filter dict by keys
   - `pluck(key, list_of_dicts)` - Extract values by key

2. **Composition Utilities**
   - `compose(*functions)` - Right-to-left composition
   - `pipe(*functions)` - Left-to-right composition
   - `curry(func)` - Convert to curried function

3. **Higher-Order Functions**
   - `throttle(func, delay)` - Limit execution rate
   - `debounce(func, delay)` - Delay execution until pause
   - `once(func)` - Execute only once

4. **Collection Utilities**
   - `group_by(key_func, items)` - Group items by key
   - `partition(predicate, items)` - Split into two lists
   - `flatten(nested_list)` - Flatten nested lists

5. **Decorator Collection**
   - `@retry(max_attempts, delay)` - Retry on failure
   - `@cache(timeout)` - Cache with expiration
   - `@validate(schema)` - Validate arguments

**Requirements:**
- All functions must be pure (no side effects)
- Use type hints
- Include comprehensive docstrings
- Write unit tests

**Bonus:**
- Add async versions of utilities
- Implement lazy evaluation for all operations
- Add function to visualize function composition

---

## Summary

| Concept | Syntax | Use Case |
|---------|--------|----------|
| map() | `map(func, iterable)` | Transform each item |
| filter() | `filter(func, iterable)` | Select items |
| reduce() | `reduce(func, iterable)` | Aggregate to single value |
| List comp | `[x for x in items]` | Create lists |
| Generator | `(x for x in items)` | Lazy evaluation |
| Closure | Nested function + nonlocal | Remember state |
| Decorator | `@decorator` | Modify functions |

**Key Takeaways:**
- FP emphasizes pure functions and immutability
- List comprehensions are often more readable than map/filter
- Generators save memory for large datasets
- Decorators add functionality without modifying code
- Closures create functions with remembered state
- Compose small functions for complex operations

---

## Next Steps

Move to [06 - Strings](../06_Strings/) to learn advanced string manipulation techniques.

---

**Congratulations!** You've completed the foundation phase of Python programming. You now know:
- Python basics and syntax
- Control flow (conditions and loops)
- Data structures (lists, tuples, sets, dicts)
- Functions and functional programming

Keep practicing and building projects to solidify these concepts!

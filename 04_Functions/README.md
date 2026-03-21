# 04 - Functions

## What are Functions?

Functions are reusable blocks of code that perform a specific task. They help organize code, reduce repetition, and make programs more modular.

**Key Benefits:**
- **Reusability**: Write once, use many times
- **Organization**: Break complex problems into smaller parts
- **Maintainability**: Easier to update and debug
- **Abstraction**: Hide complex logic behind simple interfaces

---

## Deep Explanation

### How Functions Work

```
Function Definition          Function Call
┌─────────────────┐         ┌─────────────────┐
│ def greet(name):│         │ greet("John")   │
│     return ...  │◄────────│                 │
└─────────────────┘         └─────────────────┘
         │                           │
         ▼                           ▼
┌─────────────────┐         ┌─────────────────┐
│ 1. name = "John"│         │ Return Value    │
│ 2. Execute body │────────►│ "Hello, John!"  │
│ 3. Return result│         │                 │
└─────────────────┘         └─────────────────┘
```

### Function Lifecycle

1. **Definition**: Code is stored, not executed
2. **Call**: Function is invoked with arguments
3. **Execution**: Parameters receive values, body runs
4. **Return**: Result sent back to caller (or `None`)

---

## Defining Functions

### Basic Syntax

```python
def function_name(parameters):
    """Docstring - describes what function does"""
    # Function body
    return value  # Optional
```

### Simple Function

```python
def greet():
    """Prints a greeting message"""
    print("Hello, World!")

greet()  # Output: Hello, World!
```

### Function with Parameters

```python
def greet(name):
    """Greets a person by name"""
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
greet("Bob")    # Output: Hello, Bob!
```

### Function with Return Value

```python
def add(a, b):
    """Returns the sum of two numbers"""
    return a + b

result = add(3, 5)
print(result)  # Output: 8
```

---

## Parameters and Arguments

### Positional Arguments

Arguments matched by position.

```python
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

describe_pet("dog", "Buddy")  # I have a dog named Buddy.
describe_pet("Buddy", "dog")  # I have a Buddy named dog. (Wrong!)
```

### Keyword Arguments

Arguments matched by name (order doesn't matter).

```python
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

describe_pet(name="Buddy", animal="dog")  # I have a dog named Buddy.
describe_pet(animal="cat", name="Whiskers")  # I have a cat named Whiskers.
```

### Default Parameters

Parameters with default values.

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")                    # Hello, Alice!
greet("Bob", "Hi")               # Hi, Bob!
greet("Carol", greeting="Hey")   # Hey, Carol!
```

**Important**: Default parameters must come after required parameters.

```python
# Correct
def func(a, b, c=3, d=4):
    pass

# Incorrect - SyntaxError
def func(a=1, b, c=3):
    pass
```

### Mutable Default Parameters (Gotcha!)

```python
# WRONG - Don't do this!
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] - Surprise! List persists

# CORRECT
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item(1))  # [1]
print(add_item(2))  # [2] - As expected
```

---

## *args and **kwargs

### *args - Variable Positional Arguments

Accept any number of positional arguments.

```python
def sum_all(*args):
    """Sum all arguments"""
    total = 0
    for num in args:
        total += num
    return total

# Usage
print(sum_all(1, 2, 3))      # 6
print(sum_all(1, 2, 3, 4, 5))  # 15
print(sum_all())              # 0

# args is a tuple
print(type(args))  # <class 'tuple'>
```

### **kwargs - Variable Keyword Arguments

Accept any number of keyword arguments.

```python
def print_info(**kwargs):
    """Print key-value pairs"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Usage
print_info(name="John", age=30, city="NYC")
# Output:
# name: John
# age: 30
# city: NYC

# kwargs is a dictionary
print(type(kwargs))  # <class 'dict'>
```

### Combined Usage

```python
def flexible(*args, **kwargs):
    print(f"Positional: {args}")
    print(f"Keyword: {kwargs}")

flexible(1, 2, 3, name="John", age=30)
# Output:
# Positional: (1, 2, 3)
# Keyword: {'name': 'John', 'age': 30}
```

### Unpacking Arguments

```python
def add(a, b, c):
    return a + b + c

# Unpack list/tuple
numbers = [1, 2, 3]
print(add(*numbers))  # 6

# Unpack dictionary
data = {"a": 1, "b": 2, "c": 3}
print(add(**data))    # 6
```

---

## Return Values

### Single Return Value

```python
def square(x):
    return x ** 2

result = square(5)  # 25
```

### Multiple Return Values

```python
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([3, 1, 4, 1, 5, 9])
print(minimum)  # 1
print(maximum)  # 9
```

### Early Return

```python
def divide(a, b):
    if b == 0:
        return None  # Early exit
    return a / b

print(divide(10, 2))  # 5.0
print(divide(10, 0))  # None
```

### No Return Statement

```python
def print_greeting(name):
    print(f"Hello, {name}!")
    # No return statement

result = print_greeting("Alice")
print(result)  # None
```

---

## Lambda Functions

Anonymous (nameless) functions for simple operations.

```python
# Regular function
def square(x):
    return x ** 2

# Equivalent lambda
square = lambda x: x ** 2

print(square(5))  # 25
```

### Common Use Cases

```python
# Sorting
students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
students.sort(key=lambda x: x[1])  # Sort by age
print(students)  # [('Bob', 20), ('Charlie', 23), ('Alice', 25)]

# With map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# With filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]
```

### Limitations

- Single expression only
- No statements (no assignments, loops)
- Harder to debug

---

## Recursion

Function calling itself to solve problems.

### Basic Recursion

```python
def factorial(n):
    """Calculate n! = n * (n-1) * (n-2) * ... * 1"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

### How Recursion Works

```
factorial(5)
├── 5 * factorial(4)
│   ├── 4 * factorial(3)
│   │   ├── 3 * factorial(2)
│   │   │   ├── 2 * factorial(1)
│   │   │   │   └── 1 (base case)
│   │   │   └── 2 * 1 = 2
│   │   └── 3 * 2 = 6
│   └── 4 * 6 = 24
└── 5 * 24 = 120
```

### Fibonacci Sequence

```python
def fibonacci(n):
    """Return nth Fibonacci number"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # 55
```

### Recursion vs Iteration

```python
# Recursive (elegant but slower for large n)
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# Iterative (faster, no stack overflow risk)
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

---

## Scope and Lifetime

### Local vs Global Variables

```python
count = 0  # Global variable

def increment():
    count = 1  # Local variable (different from global!)
    print(f"Local: {count}")

increment()      # Local: 1
print(count)     # 0 (global unchanged)
```

### Modifying Global Variables

```python
count = 0

def increment():
    global count  # Declare we're using global
    count += 1
    print(f"Count: {count}")

increment()  # Count: 1
increment()  # Count: 2
print(count)  # 2
```

### Nonlocal (Nested Functions)

```python
def outer():
    x = 10
    
    def inner():
        nonlocal x  # Use outer's x, not global
        x += 5
        print(f"Inner: {x}")
    
    inner()
    print(f"Outer: {x}")

outer()
# Inner: 15
# Outer: 15
```

### LEGB Rule (Scope Resolution)

Python looks for variables in this order:
1. **L**ocal
2. **E**nclosing
3. **G**lobal
4. **B**uilt-in

---

## Code Examples

### Example 1: Calculator Function
```python
def calculator(a, b, operation="add"):
    """Perform arithmetic operations"""
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Error: Unknown operation"

# Usage
print(calculator(10, 5, "add"))       # 15
print(calculator(10, 5, "multiply"))  # 50
print(calculator(10, 0, "divide"))    # Error: Division by zero
```

### Example 2: Validate Password
```python
def validate_password(password):
    """Check if password meets criteria"""
    if len(password) < 8:
        return False, "Password must be at least 8 characters"
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*" for c in password)
    
    checks = [
        (has_upper, "Must contain uppercase letter"),
        (has_lower, "Must contain lowercase letter"),
        (has_digit, "Must contain digit"),
        (has_special, "Must contain special character")
    ]
    
    for passed, message in checks:
        if not passed:
            return False, message
    
    return True, "Password is strong"

# Usage
is_valid, message = validate_password("Hello1!")
print(message)  # Password must be at least 8 characters

is_valid, message = validate_password("HelloWorld1!")
print(message)  # Password is strong
```

### Example 3: Data Processing Pipeline
```python
def clean_data(data):
    """Remove empty values and strip whitespace"""
    return [item.strip() for item in data if item.strip()]

def transform_data(data):
    """Convert to uppercase"""
    return [item.upper() for item in data]

def filter_data(data, min_length=3):
    """Filter by minimum length"""
    return [item for item in data if len(item) >= min_length]

def process_data(data, min_length=3):
    """Complete pipeline"""
    cleaned = clean_data(data)
    transformed = transform_data(cleaned)
    filtered = filter_data(transformed, min_length)
    return filtered

# Usage
raw_data = ["  hello  ", "", "  ", "hi", "world", "  python  "]
result = process_data(raw_data, min_length=4)
print(result)  # ['HELLO', 'WORLD', 'PYTHON']
```

### Example 4: Decorator Function
```python
import time

def timer(func):
    """Decorator to measure function execution time"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"

@timer
def fast_function(n):
    return sum(range(n))

# Usage
slow_function()        # slow_function took 1.0012 seconds
fast_function(1000000)  # fast_function took 0.0234 seconds
```

### Example 5: Higher-Order Function
```python
def apply_operation(numbers, operation):
    """Apply a function to each number"""
    return [operation(n) for n in numbers]

def double(x):
    return x * 2

def square(x):
    return x ** 2

# Usage
nums = [1, 2, 3, 4, 5]

print(apply_operation(nums, double))   # [2, 4, 6, 8, 10]
print(apply_operation(nums, square))   # [1, 4, 9, 16, 25]
print(apply_operation(nums, lambda x: x + 10))  # [11, 12, 13, 14, 15]
```

---

## Real-World Use Cases

1. **API Endpoints**: Each endpoint is a function
2. **Data Validation**: Reusable validation functions
3. **Utility Functions**: Common operations (formatting, parsing)
4. **Event Handlers**: Functions responding to user actions
5. **Middleware**: Functions processing requests/responses
6. **Mathematical Operations**: Scientific calculations

---

## Common Mistakes / Pitfalls

| Mistake | Example | Solution |
|---------|---------|----------|
| Mutable default arguments | `def f(lst=[])` | Use `None` and check |
| Forgetting return | Function without return | Add `return` or handle `None` |
| Name collision | Local shadows global | Use different names or `global` |
| Wrong argument order | `func(a, b)` vs `func(b, a)` | Use keyword arguments |
| Infinite recursion | No base case | Always define base case |

```python
# Error 1: Mutable default
def add_item(item, items=[]):
    items.append(item)
    return items

# Fix:
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

# Error 2: Forgetting return
def calculate_area(radius):
    3.14 * radius ** 2  # No return!

area = calculate_area(5)
print(area)  # None

# Fix:
def calculate_area(radius):
    return 3.14 * radius ** 2

# Error 3: Infinite recursion
def factorial(n):
    return n * factorial(n - 1)  # No base case!

# Fix:
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

---

## Best Practices

1. **Single Responsibility**: One function, one job
   ```python
   # Bad - does too much
   def process_user(data):
       validate(data)
       save_to_db(data)
       send_email(data)
       log_activity(data)
   
   # Good - separate concerns
   def validate_user(data): ...
   def save_user(data): ...
   def notify_user(data): ...
   ```

2. **Descriptive Names**: Use verbs for functions
   ```python
   # Bad
   def calc(a, b): ...
   
   # Good
   def calculate_area(length, width): ...
   ```

3. **Docstrings**: Document what function does
   ```python
   def calculate_bmi(weight, height):
       """
       Calculate Body Mass Index.
       
       Args:
           weight (float): Weight in kilograms
           height (float): Height in meters
       
       Returns:
           float: BMI value
       """
       return weight / (height ** 2)
   ```

4. **Type Hints**: Make code self-documenting
   ```python
   from typing import List, Dict
   
   def process_users(users: List[Dict]) -> Dict:
       ...
   ```

5. **Avoid side effects**: Functions should be predictable
   ```python
   # Bad - modifies input
   def add_item(lst, item):
       lst.append(item)
   
   # Good - returns new list
   def add_item(lst, item):
       return lst + [item]
   ```

---

## Practice Questions

### Question 1 (Easy)
Write a function `is_even(n)` that returns `True` if a number is even, `False` otherwise.

### Question 2 (Easy)
Create a function `greet_user(name, greeting="Hello")` that prints a greeting. If no greeting is provided, use "Hello".

### Question 3 (Medium)
Write a function `find_max(*args)` that accepts any number of arguments and returns the maximum value.

### Question 4 (Medium)
Create a recursive function to calculate the sum of all numbers from 1 to n.

### Question 5 (Hard)
Write a function `memoize(func)` that creates a memoized version of any function. The memoized function should cache results to avoid redundant calculations.

---

## Mini Task / Assignment

### Task: Build a Math Utilities Library

Create a module with the following mathematical functions:

1. **Basic Operations**
   - `add`, `subtract`, `multiply`, `divide` (with error handling)
   - `power(base, exponent)`
   - `root(n, degree=2)` - nth root

2. **Statistical Functions**
   - `mean(numbers)` - arithmetic mean
   - `median(numbers)` - middle value
   - `mode(numbers)` - most frequent value
   - `standard_deviation(numbers)`

3. **Geometric Functions**
   - `circle_area(radius)`
   - `rectangle_area(length, width)`
   - `triangle_area(base, height)`
   - `sphere_volume(radius)`

4. **Utility Functions**
   - `is_prime(n)` - check if prime
   - `gcd(a, b)` - greatest common divisor
   - `lcm(a, b)` - least common multiple
   - `factorial(n)` - with memoization

**Requirements:**
- All functions must have docstrings
- Handle edge cases (negative numbers, zero, etc.)
- Include type hints
- Write test cases for each function

**Bonus:**
- Add a command-line interface
- Support for complex numbers
- Plotting functions using matplotlib

---

## Summary

| Concept | Syntax | Use Case |
|---------|--------|----------|
| Basic function | `def func():` | Reusable code block |
| Parameters | `def func(a, b):` | Pass data to function |
| Default args | `def func(a=1):` | Optional parameters |
| *args | `def func(*args):` | Variable positional args |
| **kwargs | `def func(**kwargs):` | Variable keyword args |
| Return | `return value` | Send data back |
| Lambda | `lambda x: x**2` | Simple anonymous functions |
| Recursion | `func()` calls itself | Divide and conquer problems |

**Key Takeaways:**
- Functions make code reusable and organized
- Use clear, descriptive names
- Document with docstrings
- Handle edge cases gracefully
- Avoid mutable default arguments
- Prefer pure functions (no side effects)

---

## Next Steps

Move to [05 - Functional Programming](../05_Functional_Programming/) to learn advanced function techniques.

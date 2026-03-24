# 09 - Exception Handling

## What are Exceptions?

Exceptions are errors that occur during program execution. Instead of crashing, Python lets you catch and handle them gracefully.

---

## Common Built-in Exceptions

| Exception | When it occurs |
|-----------|---------------|
| `ValueError` | Wrong value type (e.g., `int("abc")`) |
| `TypeError` | Wrong type (e.g., `"a" + 1`) |
| `KeyError` | Dict key doesn't exist |
| `IndexError` | List index out of range |
| `FileNotFoundError` | File doesn't exist |
| `ZeroDivisionError` | Division by zero |
| `AttributeError` | Object has no such attribute |
| `ImportError` | Module not found |
| `NameError` | Variable not defined |
| `OverflowError` | Number too large |

---

## try / except

```python
# Basic structure
try:
    # Code that might fail
    result = 10 / 0
except ZeroDivisionError:
    # Handle the error
    print("Cannot divide by zero!")

# Catch multiple exceptions
try:
    value = int(input("Enter a number: "))
    result = 100 / value
except ValueError:
    print("That's not a number!")
except ZeroDivisionError:
    print("Can't divide by zero!")

# Catch multiple in one line
try:
    ...
except (ValueError, TypeError) as e:
    print(f"Error: {e}")

# Catch any exception (use sparingly)
try:
    ...
except Exception as e:
    print(f"Something went wrong: {e}")
```

---

## else and finally

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division error!")
else:
    # Runs only if NO exception occurred
    print(f"Result: {result}")
finally:
    # ALWAYS runs, exception or not
    print("Done.")
```

### When to use each:
- `except` — handle the error
- `else` — code that should run only on success
- `finally` — cleanup (close files, DB connections, etc.)

---

## Raising Exceptions

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return age

# Re-raise an exception
try:
    set_age(-5)
except ValueError as e:
    print(f"Caught: {e}")
    raise  # Re-raises the same exception
```

---

## Custom Exceptions

```python
# Define custom exception
class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        super().__init__(f"Cannot withdraw ${amount}. Balance: ${balance}")

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(amount, self.balance)
        self.balance -= amount
        return self.balance

# Usage
account = BankAccount(100)
try:
    account.withdraw(200)
except InsufficientFundsError as e:
    print(e)  # Cannot withdraw $200. Balance: $100
```

---

## Exception Hierarchy

```
BaseException
├── SystemExit
├── KeyboardInterrupt
└── Exception
    ├── ValueError
    ├── TypeError
    ├── RuntimeError
    ├── OSError
    │   ├── FileNotFoundError
    │   └── PermissionError
    ├── LookupError
    │   ├── KeyError
    │   └── IndexError
    └── ArithmeticError
        └── ZeroDivisionError
```

Catching a parent class catches all its children:
```python
except LookupError:  # catches both KeyError and IndexError
    ...
```

---

## Context Managers and Exception Safety

```python
# 'with' ensures cleanup even if exception occurs
with open("file.txt") as f:
    data = f.read()
# File is always closed here, even if read() fails

# Custom context manager
from contextlib import contextmanager

@contextmanager
def managed_resource():
    print("Acquiring resource")
    try:
        yield "resource"
    finally:
        print("Releasing resource")

with managed_resource() as r:
    print(f"Using {r}")
```

---

## Code Examples

### Example 1: Safe Input Handler
```python
def get_integer(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Value must be at least {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be at most {max_val}")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer.")

age = get_integer("Enter your age: ", min_val=0, max_val=120)
```

### Example 2: Retry Decorator
```python
import time

def retry(max_attempts=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")
                    if attempt < max_attempts:
                        time.sleep(delay)
            raise Exception(f"All {max_attempts} attempts failed")
        return wrapper
    return decorator

@retry(max_attempts=3, delay=2)
def fetch_data(url):
    # Simulated network call
    import random
    if random.random() < 0.7:
        raise ConnectionError("Network error")
    return "data"
```

### Example 3: Validation with Custom Exceptions
```python
class ValidationError(Exception):
    pass

class EmailError(ValidationError):
    pass

class AgeError(ValidationError):
    pass

def validate_user(name, email, age):
    if not name or not name.strip():
        raise ValidationError("Name cannot be empty")
    if "@" not in email or "." not in email.split("@")[-1]:
        raise EmailError(f"Invalid email: {email}")
    if not isinstance(age, int) or age < 0 or age > 120:
        raise AgeError(f"Invalid age: {age}")
    return True

try:
    validate_user("Alice", "alice@example.com", 30)
    print("User is valid")
except EmailError as e:
    print(f"Email problem: {e}")
except AgeError as e:
    print(f"Age problem: {e}")
except ValidationError as e:
    print(f"Validation failed: {e}")
```

---

## Best Practices

1. Catch specific exceptions, not bare `except:`
2. Don't silence exceptions without logging
3. Use `finally` for cleanup
4. Create custom exceptions for your domain
5. Include helpful messages in exceptions

```python
# Bad
try:
    do_something()
except:
    pass  # Silently ignores ALL errors

# Good
try:
    do_something()
except ValueError as e:
    logger.error(f"Invalid value: {e}")
    raise
```

---

## Practice Questions

1. Write a function that safely converts a string to a float, returning `None` on failure
2. Create a custom `TemperatureError` exception for invalid temperature values
3. Write a program that reads a file and handles all possible file-related errors
4. Implement a `safe_divide(a, b)` function that handles division by zero

---

## Mini Task

Build a robust user registration system that:
1. Validates name, email, password, and age
2. Uses custom exceptions for each validation type
3. Logs all errors to a file
4. Returns meaningful error messages to the user

---

## Summary

| Keyword | Purpose |
|---------|---------|
| `try` | Code that might fail |
| `except` | Handle specific errors |
| `else` | Run if no error |
| `finally` | Always runs |
| `raise` | Throw an exception |
| Custom exception | `class MyError(Exception)` |

---

## Next Steps

Move to [10 - OOP](../10_OOP/) to learn Object-Oriented Programming.

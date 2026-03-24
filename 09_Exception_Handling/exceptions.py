# ============================================================
# 09 - Exception Handling
# ============================================================
# Run this file: python exceptions.py
# ============================================================


# ── WHY EXCEPTIONS? ─────────────────────────────────────────
# Without handling, errors crash your program entirely.
# With handling, you can recover gracefully and give useful feedback.

# This would crash without a try/except:
# result = 10 / 0   → ZeroDivisionError


# ── BASIC TRY / EXCEPT ──────────────────────────────────────
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")     # Program continues


# ── CATCHING MULTIPLE EXCEPTIONS ────────────────────────────
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: division by zero")
        return None
    except TypeError:
        print("Error: both arguments must be numbers")
        return None

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # Error: division by zero → None
print(safe_divide(10, "x")) # Error: both arguments must be numbers → None


# ── ACCESSING THE EXCEPTION OBJECT ──────────────────────────
# 'as e' gives you the exception object with its message
try:
    numbers = [1, 2, 3]
    print(numbers[10])          # Index out of range
except IndexError as e:
    print(f"Caught: {e}")       # list index out of range


# ── CATCH MULTIPLE IN ONE LINE ──────────────────────────────
try:
    value = int("not a number")
except (ValueError, TypeError) as e:
    print(f"Conversion error: {e}")


# ── ELSE — runs only if NO exception occurred ────────────────
def read_number(s):
    try:
        n = int(s)
    except ValueError:
        print(f"'{s}' is not a valid integer")
    else:
        # Only runs if try succeeded
        print(f"Successfully parsed: {n}")
        return n

read_number("42")       # Successfully parsed: 42
read_number("hello")    # 'hello' is not a valid integer


# ── FINALLY — ALWAYS runs, exception or not ─────────────────
# Use for cleanup: closing files, DB connections, releasing locks
def process_file(filename):
    f = None
    try:
        f = open(filename, "r")
        data = f.read()
        return data
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return None
    finally:
        # This runs whether or not an exception occurred
        if f:
            f.close()
            print("File closed.")

process_file("nonexistent.txt")


# ── RAISING EXCEPTIONS ──────────────────────────────────────
# Use 'raise' to signal that something went wrong in your code
def set_age(age):
    if not isinstance(age, int):
        raise TypeError(f"Age must be an integer, got {type(age).__name__}")
    if age < 0 or age > 150:
        raise ValueError(f"Age {age} is out of realistic range (0-150)")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(f"ValueError: {e}")

try:
    set_age("twenty")
except TypeError as e:
    print(f"TypeError: {e}")


# ── CUSTOM EXCEPTIONS ───────────────────────────────────────
# Create your own exception classes for domain-specific errors
# Always inherit from Exception (or a more specific built-in)

class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the account balance."""
    def __init__(self, amount, balance):
        self.amount  = amount
        self.balance = balance
        # Call parent with a descriptive message
        super().__init__(
            f"Cannot withdraw ${amount:.2f}. Available balance: ${balance:.2f}"
        )

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner   = owner
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise InsufficientFundsError(amount, self._balance)
        self._balance -= amount
        return amount

    @property
    def balance(self):
        return self._balance

account = BankAccount("Alice", 100)
account.deposit(50)

try:
    account.withdraw(200)
except InsufficientFundsError as e:
    print(e)    # Cannot withdraw $200.00. Available balance: $150.00


# ── EXCEPTION HIERARCHY ─────────────────────────────────────
# Catching a parent class catches all its children
# LookupError is parent of both KeyError and IndexError
data = {"key": "value"}
try:
    _ = data["missing"]
except LookupError as e:
    # Catches KeyError, IndexError, and any other LookupError
    print(f"Lookup failed: {type(e).__name__}: {e}")


# ── REAL EXAMPLE: Safe Input Handler ────────────────────────
def get_integer(prompt, min_val=None, max_val=None):
    """Keep asking until the user enters a valid integer in range."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("  Please enter a whole number.")
            continue

        if min_val is not None and value < min_val:
            print(f"  Must be at least {min_val}.")
            continue
        if max_val is not None and value > max_val:
            print(f"  Must be at most {max_val}.")
            continue

        return value    # Valid input — exit the loop

# Uncomment to try interactively:
# age = get_integer("Enter your age: ", min_val=0, max_val=120)
# print(f"Age: {age}")


# ── REAL EXAMPLE: Retry Decorator ───────────────────────────
import time
from functools import wraps

def retry(max_attempts=3, delay=0.5, exceptions=(Exception,)):
    """Decorator: retry a function up to max_attempts times on failure."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    print(f"  Attempt {attempt}/{max_attempts} failed: {e}")
                    if attempt < max_attempts:
                        time.sleep(delay)
            raise RuntimeError(f"All {max_attempts} attempts failed")
        return wrapper
    return decorator

import random

@retry(max_attempts=3, delay=0.1, exceptions=(ValueError,))
def flaky_function():
    """Simulates a function that sometimes fails."""
    if random.random() < 0.6:
        raise ValueError("Random failure!")
    return "Success!"

try:
    result = flaky_function()
    print(result)
except RuntimeError as e:
    print(f"Gave up: {e}")


# ── PRACTICE ────────────────────────────────────────────────
# 1. Write safe_int(s) that converts a string to int, returns None on failure
# 2. Create a custom TemperatureError for values below -273.15°C
# 3. Write a function that reads a file and handles FileNotFoundError,
#    PermissionError, and UnicodeDecodeError separately
# 4. Add a retry decorator that only retries on ConnectionError

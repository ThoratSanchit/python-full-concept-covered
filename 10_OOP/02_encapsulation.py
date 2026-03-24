# ============================================================
# 10 OOP — 02: Encapsulation
# ============================================================
# Run this file: python 02_encapsulation.py
# ============================================================


# ── ACCESS LEVELS ───────────────────────────────────────────
# Python uses naming conventions — there's no strict enforcement like Java
class Demo:
    def __init__(self):
        self.public    = "Anyone can access this"
        self._protected = "Convention: internal use only"
        self.__private  = "Name-mangled — hard to access outside"

d = Demo()
print(d.public)         # Works fine
print(d._protected)     # Works, but signals "don't touch this"
# print(d.__private)    # AttributeError!

# Python name-mangles __private to _ClassName__private
# This is intentional — it prevents accidental access, not malicious access
print(d._Demo__private) # Works, but NEVER do this in real code


# ── @PROPERTY — CONTROLLED ACCESS ──────────────────────────
# Properties let you add validation/logic to attribute access
# From the outside, it looks like a plain attribute — clean API
class BankAccount:
    def __init__(self, owner, balance):
        self.owner    = owner
        self.__balance = balance    # Private — only accessible via property

    @property
    def balance(self):
        """Getter — called when you read account.balance"""
        return self.__balance

    @balance.setter
    def balance(self, amount):
        """Setter — called when you write account.balance = x"""
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        return self.__balance

    def __str__(self):
        return f"Account({self.owner}, balance=${self.__balance:.2f})"

account = BankAccount("Alice", 1000)
print(account.balance)      # 1000  — calls getter
account.deposit(500)
print(account.balance)      # 1500

try:
    account.balance = -100  # Calls setter → raises ValueError
except ValueError as e:
    print(f"Error: {e}")


# ── READ-ONLY PROPERTIES ────────────────────────────────────
# A property with no setter is read-only
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius  # Goes through the setter below

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self.__celsius = value

    @property
    def fahrenheit(self):
        """Read-only — computed from celsius, no setter needed."""
        return self.__celsius * 9/5 + 32

    @property
    def kelvin(self):
        """Read-only — computed from celsius."""
        return self.__celsius + 273.15

    def __str__(self):
        return f"{self.__celsius}°C | {self.fahrenheit:.1f}°F | {self.kelvin:.2f}K"

t = Temperature(100)
print(t)                # 100°C | 212.0°F | 373.15K

t.celsius = 0
print(t.fahrenheit)     # 32.0

# t.fahrenheit = 50   # AttributeError — no setter defined


# ── REAL EXAMPLE: Product with Validation ───────────────────
class Product:
    def __init__(self, name, price, quantity):
        # These all go through their setters — validation happens immediately
        self.name     = name
        self.price    = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty")
        self.__name = value.strip()     # Auto-strip whitespace

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = round(value, 2)  # Always store with 2 decimal places

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Quantity must be a non-negative integer")
        self.__quantity = value

    @property
    def total_value(self):
        """Read-only: price × quantity."""
        return self.__price * self.__quantity

    def sell(self, amount):
        if amount > self.__quantity:
            raise ValueError(f"Only {self.__quantity} in stock")
        self.__quantity -= amount

    def __str__(self):
        return f"{self.name} | ${self.price:.2f} × {self.quantity} = ${self.total_value:.2f}"

laptop = Product("  Laptop  ", 999.99, 10)
print(laptop)           # Laptop | $999.99 × 10 = $9999.90

laptop.sell(3)
print(laptop.quantity)  # 7

try:
    laptop.price = -50
except ValueError as e:
    print(f"Error: {e}")


# ── PRACTICE ────────────────────────────────────────────────
# 1. Create a Circle class where radius rejects negative values via @property
# 2. Add read-only area and circumference properties to Circle
# 3. Build a Person class where age must be 0-120 and name cannot be empty
# 4. Create a Rectangle where setting width or height auto-updates area

# 02 - Encapsulation

## What is Encapsulation?

Encapsulation means **bundling data and methods together** inside a class, and **controlling access** to that data. It protects the internal state of an object from being accidentally modified.

---

## Access Levels in Python

Python uses naming conventions (not strict enforcement like Java/C++).

```python
class Example:
    def __init__(self):
        self.public = "Anyone can access"        # public
        self._protected = "Convention: internal" # protected
        self.__private = "Name-mangled, hidden"  # private
```

| Prefix | Access Level | Convention |
|--------|-------------|------------|
| `name` | Public | Accessible everywhere |
| `_name` | Protected | Internal use (convention only) |
| `__name` | Private | Name-mangled, hard to access outside |

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner              # public
        self._account_type = "savings"  # protected
        self.__balance = balance        # private

account = BankAccount("Alice", 1000)

print(account.owner)           # Alice ✓
print(account._account_type)   # savings ✓ (works but shouldn't)
# print(account.__balance)     # AttributeError ✗

# Python name-mangles __balance to _BankAccount__balance
print(account._BankAccount__balance)  # 1000 (works but NEVER do this)
```

---

## Properties — The Right Way

Use `@property` to create controlled getters and setters.

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        """Getter — read the balance"""
        return self.__balance

    @balance.setter
    def balance(self, amount):
        """Setter — validate before setting"""
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = amount

    @balance.deleter
    def balance(self):
        """Deleter — called when del obj.balance"""
        print("Deleting balance...")
        del self.__balance

# Usage
account = BankAccount("Alice", 1000)

print(account.balance)    # 1000  (calls getter)
account.balance = 1500    # calls setter
print(account.balance)    # 1500

account.balance = -100    # ValueError: Balance cannot be negative
```

---

## Full Encapsulation Example

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius  # Uses the setter

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
        """Read-only computed property"""
        return self.__celsius * 9/5 + 32

    @property
    def kelvin(self):
        """Read-only computed property"""
        return self.__celsius + 273.15

    def __str__(self):
        return f"{self.__celsius}°C | {self.fahrenheit}°F | {self.kelvin}K"

t = Temperature(100)
print(t)              # 100°C | 212.0°F | 373.15K

t.celsius = 0
print(t.fahrenheit)   # 32.0

t.celsius = -300      # ValueError: Temperature below absolute zero!
```

---

## Why Encapsulation Matters

```python
# WITHOUT encapsulation — dangerous
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("Alice", 25)
user.age = -5       # No validation — silently broken
user.age = "hello"  # No type check — will crash later

# WITH encapsulation — safe
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age  # Goes through setter

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        if value < 0 or value > 150:
            raise ValueError(f"Invalid age: {value}")
        self.__age = value

user = User("Alice", 25)
user.age = -5       # ValueError: Invalid age: -5
user.age = "hello"  # TypeError: Age must be an integer
```

---

## Code Example: Product Inventory

```python
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price        # Uses setter
        self.quantity = quantity  # Uses setter

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = round(value, 2)

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
        """Read-only: computed from price and quantity"""
        return self.__price * self.__quantity

    def restock(self, amount):
        if amount <= 0:
            raise ValueError("Restock amount must be positive")
        self.__quantity += amount

    def sell(self, amount):
        if amount > self.__quantity:
            raise ValueError("Not enough stock")
        self.__quantity -= amount

    def __str__(self):
        return f"{self.name} | ${self.price:.2f} x {self.quantity} = ${self.total_value:.2f}"

# Usage
laptop = Product("Laptop", 999.99, 10)
print(laptop)           # Laptop | $999.99 x 10 = $9999.90

laptop.sell(3)
print(laptop.quantity)  # 7

laptop.restock(5)
print(laptop)           # Laptop | $999.99 x 12 = $11999.88

laptop.price = -50      # ValueError: Price cannot be negative
```

---

## Practice Questions

1. Create a `Circle` class where `radius` is a property that rejects negative values
2. Add a read-only `area` and `circumference` property to the Circle
3. Build a `Password` class that stores a hashed password and never exposes the raw value
4. Create a `Rectangle` class where setting `width` or `height` automatically updates a `area` property

---

## Summary

| Concept | Syntax |
|---------|--------|
| Public attribute | `self.name` |
| Protected attribute | `self._name` |
| Private attribute | `self.__name` |
| Getter | `@property` |
| Setter | `@name.setter` |
| Read-only property | `@property` with no setter |

---

Previous → [01 - Classes and Objects](./01_classes_and_objects.md) | Next → [03 - Inheritance](./03_inheritance.md)

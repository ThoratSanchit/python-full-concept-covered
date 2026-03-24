# 04 - Polymorphism

## What is Polymorphism?

Polymorphism means **"many forms"**. The same method name behaves differently depending on the object calling it.

One interface → multiple implementations.

---

## Method Overriding (Runtime Polymorphism)

```python
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area()")

    def describe(self):
        return f"I am a {self.__class__.__name__} with area {self.area():.2f}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Polymorphism in action — same call, different behavior
shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]

for shape in shapes:
    print(shape.describe())
# I am a Circle with area 78.54
# I am a Rectangle with area 24.00
# I am a Triangle with area 12.00
```

---

## Duck Typing

"If it walks like a duck and quacks like a duck, it's a duck."

Python doesn't care about the type — only whether the object has the method.

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Robot:
    def speak(self):
        return "Beep boop."

class Person:
    def speak(self):
        return "Hello!"

# These classes don't share a parent — but all have speak()
def make_noise(thing):
    print(thing.speak())  # Works on anything with speak()

for obj in [Dog(), Cat(), Robot(), Person()]:
    make_noise(obj)
# Woof!
# Meow!
# Beep boop.
# Hello!
```

---

## Operator Overloading

Define how operators (`+`, `-`, `*`, `==`, etc.) work on your objects.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)  # Handles: 3 * vector

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __abs__(self):
        return (self.x**2 + self.y**2) ** 0.5

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1 + v2)    # Vector(4, 6)
print(v2 - v1)    # Vector(2, 2)
print(v1 * 3)     # Vector(3, 6)
print(3 * v1)     # Vector(3, 6)
print(abs(v2))    # 5.0
print(v1 == v1)   # True
```

---

## Polymorphism with Functions

```python
# Same function works on different types
def total_area(shapes):
    return sum(shape.area() for shape in shapes)

shapes = [Circle(3), Rectangle(4, 5), Triangle(6, 7)]
print(f"Total area: {total_area(shapes):.2f}")  # Total area: 69.27
```

---

## Method Overloading (Python style)

Python doesn't support true overloading, but you can simulate it with default args or `*args`.

```python
class Calculator:
    def add(self, *args):
        return sum(args)

    def multiply(self, a, b, c=1):
        return a * b * c

calc = Calculator()
print(calc.add(1, 2))        # 3
print(calc.add(1, 2, 3, 4))  # 10
print(calc.multiply(2, 3))   # 6
print(calc.multiply(2, 3, 4)) # 24
```

---

## Code Example: Payment System

```python
class PaymentMethod:
    def __init__(self, amount):
        self.amount = amount

    def process(self):
        raise NotImplementedError

    def receipt(self):
        return f"Payment of ${self.amount:.2f} via {self.__class__.__name__}"

class CreditCard(PaymentMethod):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = f"****{card_number[-4:]}"

    def process(self):
        return f"Charging ${self.amount:.2f} to card {self.card_number}"

class PayPal(PaymentMethod):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email

    def process(self):
        return f"Sending ${self.amount:.2f} via PayPal to {self.email}"

class Crypto(PaymentMethod):
    def __init__(self, amount, wallet):
        super().__init__(amount)
        self.wallet = wallet

    def process(self):
        return f"Transferring ${self.amount:.2f} to wallet {self.wallet[:8]}..."

def checkout(payment: PaymentMethod):
    print(payment.process())
    print(payment.receipt())
    print("---")

# Same checkout() function works for all payment types
checkout(CreditCard(99.99, "1234567890123456"))
checkout(PayPal(49.99, "user@example.com"))
checkout(Crypto(199.99, "0xABCDEF1234567890"))
```

---

## Practice Questions

1. Create `Animal` subclasses (`Dog`, `Cat`, `Bird`) each with a different `speak()` and `move()` method. Write a function that calls both on any animal.
2. Build a `Notification` class with `Email`, `SMS`, `PushNotification` subclasses, each implementing `send(message)`
3. Implement operator overloading for a `Fraction` class (`+`, `-`, `*`, `/`, `==`, `__str__`)
4. Use duck typing to write a `serialize(obj)` function that works on any object with a `to_dict()` method

---

## Summary

| Type | Description |
|------|-------------|
| Method overriding | Child redefines parent method |
| Duck typing | Works if object has the right method |
| Operator overloading | Custom behavior for `+`, `==`, etc. |
| Method overloading | Simulated with default args / `*args` |

Key idea: write code that works on the **interface**, not the **type**.

---

Previous → [03 - Inheritance](./03_inheritance.md) | Next → [05 - Abstraction](./05_abstraction.md)

# ============================================================
# 10 OOP — 04: Polymorphism
# ============================================================
# Run this file: python 04_polymorphism.py
# ============================================================


# ── METHOD OVERRIDING ───────────────────────────────────────
# Same method name, different behavior per class
# The correct version is chosen at runtime based on the object's type
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area()")

    def describe(self):
        # This method works for ALL shapes — it calls the right area() automatically
        return f"I am a {self.__class__.__name__} with area {self.area():.2f}"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width  = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base   = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Polymorphism in action — same loop, same method call, different results
shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]
for shape in shapes:
    print(shape.describe())     # Each calls its own area()

# Works in functions too
def total_area(shapes):
    return sum(shape.area() for shape in shapes)

print(f"Total area: {total_area(shapes):.2f}")


# ── DUCK TYPING ─────────────────────────────────────────────
# "If it walks like a duck and quacks like a duck, it's a duck."
# Python doesn't care about the TYPE — only whether the object has the method.
class Dog:
    def speak(self): return "Woof!"

class Cat:
    def speak(self): return "Meow!"

class Robot:
    def speak(self): return "Beep boop."

# These classes share NO parent — but all have speak()
# Python doesn't require a common base class
def make_noise(thing):
    print(thing.speak())    # Works on anything with a speak() method

for obj in [Dog(), Cat(), Robot()]:
    make_noise(obj)


# ── OPERATOR OVERLOADING ────────────────────────────────────
# Define how operators (+, -, *, ==, etc.) work on your objects
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Called when you write: v1 + v2
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        # Called when you write: v1 - v2
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        # Called when you write: v1 * 3
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        # Called when you write: 3 * v1 (scalar on the LEFT)
        return self.__mul__(scalar)

    def __eq__(self, other):
        # Called when you write: v1 == v2
        return self.x == other.x and self.y == other.y

    def __abs__(self):
        # Called when you write: abs(v1) — returns the magnitude
        return (self.x**2 + self.y**2) ** 0.5

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1 + v2)      # Vector(4, 6)
print(v2 - v1)      # Vector(2, 2)
print(v1 * 3)       # Vector(3, 6)
print(3 * v1)       # Vector(3, 6)  — uses __rmul__
print(abs(v2))      # 5.0
print(v1 == v1)     # True
print(v1 == v2)     # False


# ── REAL EXAMPLE: Payment System ────────────────────────────
# Same checkout() function works for ANY payment method — that's polymorphism
class PaymentMethod:
    def __init__(self, amount):
        self.amount = amount

    def process(self):
        raise NotImplementedError

    def receipt(self):
        return f"Paid ${self.amount:.2f} via {self.__class__.__name__}"


class CreditCard(PaymentMethod):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        # Only store last 4 digits — never store full card numbers!
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
    """Works with ANY PaymentMethod subclass — polymorphism."""
    print(payment.process())
    print(payment.receipt())
    print()

checkout(CreditCard(99.99, "1234567890123456"))
checkout(PayPal(49.99, "user@example.com"))
checkout(Crypto(199.99, "0xABCDEF1234567890"))


# ── PRACTICE ────────────────────────────────────────────────
# 1. Create Animal subclasses (Dog, Cat, Bird) each with speak() and move()
#    Write a function that calls both on any animal
# 2. Build Notification subclasses (Email, SMS, Push) each with send(message)
# 3. Implement a Fraction class with +, -, *, /, ==, and __str__
# 4. Write serialize(obj) that works on any object with a to_dict() method

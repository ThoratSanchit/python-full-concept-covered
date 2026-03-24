# ============================================================
# 10 OOP — 01: Classes and Objects
# ============================================================
# Run this file: python 01_classes_and_objects.py
# ============================================================


# ── DEFINING A CLASS ────────────────────────────────────────
# A class is a blueprint. An object is an instance of that blueprint.
class Dog:
    # Class attribute — shared by ALL instances of Dog
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance attributes — unique to each object
        # 'self' refers to the specific object being created
        self.name = name
        self.age  = age

    def bark(self):
        # Instance method — has access to self (the object)
        return f"{self.name} says: Woof!"

    def describe(self):
        return f"{self.name} is {self.age} years old"


# ── CREATING OBJECTS ────────────────────────────────────────
dog1 = Dog("Buddy", 3)  # __init__ is called automatically
dog2 = Dog("Max", 5)

print(dog1.bark())          # Buddy says: Woof!
print(dog2.describe())      # Max is 5 years old

# Class attribute is the same for all instances
print(dog1.species)         # Canis familiaris
print(dog2.species)         # Canis familiaris
print(Dog.species)          # Also accessible from the class itself


# ── __STR__ AND __REPR__ ────────────────────────────────────
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def __str__(self):
        """Called by print() — meant for end users."""
        return f"{self.name} (age {self.age})"

    def __repr__(self):
        """Called in REPL and repr() — meant for developers/debugging."""
        return f"Person(name='{self.name}', age={self.age})"

p = Person("Alice", 30)
print(p)        # Alice (age 30)       — uses __str__
print(repr(p))  # Person(name='Alice', age=30) — uses __repr__


# ── INSTANCE vs CLASS vs STATIC METHODS ─────────────────────
class Circle:
    pi = 3.14159    # Class attribute

    def __init__(self, radius):
        self.radius = radius    # Instance attribute

    # Instance method — needs 'self', works with instance data
    def area(self):
        return Circle.pi * self.radius ** 2

    def circumference(self):
        return 2 * Circle.pi * self.radius

    # Class method — needs 'cls', works with class-level data
    # Common use: alternative constructors
    @classmethod
    def from_diameter(cls, diameter):
        """Create a Circle from a diameter instead of radius."""
        return cls(diameter / 2)    # cls is the Circle class itself

    # Static method — no 'self' or 'cls', just a utility function
    # Use when the logic is related to the class but doesn't need instance/class data
    @staticmethod
    def is_valid_radius(radius):
        return radius > 0

c1 = Circle(5)
print(f"Area: {c1.area():.2f}")             # 78.54
print(f"Circumference: {c1.circumference():.2f}")  # 31.42

c2 = Circle.from_diameter(10)               # Alternative constructor
print(f"Radius from diameter: {c2.radius}") # 5.0

print(Circle.is_valid_radius(3))    # True
print(Circle.is_valid_radius(-1))   # False


# ── CLASS vs INSTANCE ATTRIBUTES ────────────────────────────
class Counter:
    # Class attribute — shared, tracks total across all instances
    total_created = 0

    def __init__(self, name):
        self.name  = name       # Instance attribute — unique per object
        self.count = 0          # Instance attribute
        Counter.total_created += 1  # Modify class attribute

    def increment(self):
        self.count += 1

c1 = Counter("A")
c2 = Counter("B")
c3 = Counter("C")

c1.increment()
c1.increment()
c2.increment()

print(f"c1 count: {c1.count}")          # 2
print(f"c2 count: {c2.count}")          # 1
print(f"Total counters: {Counter.total_created}")  # 3


# ── REAL EXAMPLE: Student Report Card ───────────────────────
class Student:
    def __init__(self, name, student_id):
        self.name       = name
        self.student_id = student_id
        self.grades     = {}    # subject → score

    def add_grade(self, subject, score):
        if not 0 <= score <= 100:
            raise ValueError(f"Score must be 0-100, got {score}")
        self.grades[subject] = score

    def average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)

    def letter_grade(self):
        avg = self.average()
        if avg >= 90: return "A"
        if avg >= 80: return "B"
        if avg >= 70: return "C"
        if avg >= 60: return "D"
        return "F"

    def __str__(self):
        return (f"Student: {self.name} (ID: {self.student_id})\n"
                f"  Grades: {self.grades}\n"
                f"  Average: {self.average():.1f} → {self.letter_grade()}")

alice = Student("Alice", "S001")
alice.add_grade("Math", 92)
alice.add_grade("Science", 88)
alice.add_grade("English", 95)
print(alice)


# ── PRACTICE ────────────────────────────────────────────────
# 1. Create a Car class with brand, model, year and a description() method
# 2. Add a class attribute 'total_cars' that increments each time a Car is created
# 3. Add @classmethod from_string("Toyota,Camry,2022") as an alternative constructor
# 4. Add @staticmethod is_vintage(year) → True if car is 25+ years old

# 01 - Classes and Objects

## What is a Class?

A **class** is a blueprint. An **object** is an instance created from that blueprint.

Think of a class like a cookie cutter — the cutter is the class, each cookie is an object.

---

## Defining a Class

```python
class Dog:
    # Class attribute — shared by ALL instances
    species = "Canis familiaris"

    # Constructor — runs when object is created
    def __init__(self, name, age):
        # Instance attributes — unique to each object
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        return f"{self.name} says: Woof!"

    def describe(self):
        return f"{self.name} is {self.age} years old"
```

---

## Creating Objects

```python
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.bark())       # Buddy says: Woof!
print(dog2.describe())   # Max is 5 years old

# Class attribute accessible from instance or class
print(dog1.species)      # Canis familiaris
print(Dog.species)       # Canis familiaris
```

---

## `self` Explained

`self` refers to the current instance. Python passes it automatically.

```python
class Counter:
    def __init__(self):
        self.count = 0       # Each instance has its own count

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

c1 = Counter()
c2 = Counter()

c1.increment()
c1.increment()
c2.increment()

print(c1.count)  # 2
print(c2.count)  # 1  (independent)
```

---

## `__str__` and `__repr__`

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        """Human-readable — used by print()"""
        return f"{self.name} (age {self.age})"

    def __repr__(self):
        """Developer-readable — used in REPL/debugging"""
        return f"Person(name='{self.name}', age={self.age})"

p = Person("Alice", 30)
print(p)       # Alice (age 30)
print(repr(p)) # Person(name='Alice', age=30)
```

---

## Instance vs Class vs Static Methods

```python
class Circle:
    pi = 3.14159  # Class attribute

    def __init__(self, radius):
        self.radius = radius

    # Instance method — has access to self (instance data)
    def area(self):
        return Circle.pi * self.radius ** 2

    def circumference(self):
        return 2 * Circle.pi * self.radius

    # Class method — has access to cls (class itself), not instance
    @classmethod
    def from_diameter(cls, diameter):
        """Alternative constructor"""
        return cls(diameter / 2)

    # Static method — no access to instance or class
    @staticmethod
    def is_valid_radius(radius):
        return radius > 0

# Usage
c1 = Circle(5)
print(c1.area())                     # 78.53975
print(c1.circumference())            # 31.4159

c2 = Circle.from_diameter(10)        # Alternative constructor
print(c2.radius)                     # 5.0

print(Circle.is_valid_radius(3))     # True
print(Circle.is_valid_radius(-1))    # False
```

### When to use each:

| Method type | Use when |
|-------------|---------|
| Instance method | Needs to access/modify instance data (`self`) |
| Class method | Alternative constructors, factory methods |
| Static method | Utility/helper that doesn't need instance or class |

---

## Class vs Instance Attributes

```python
class Student:
    school = "Python Academy"   # Class attribute

    def __init__(self, name, grade):
        self.name = name        # Instance attribute
        self.grade = grade      # Instance attribute

s1 = Student("Alice", "A")
s2 = Student("Bob", "B")

# Class attribute — same for all
print(s1.school)  # Python Academy
print(s2.school)  # Python Academy

# Change class attribute
Student.school = "Code School"
print(s1.school)  # Code School (changed for all)

# Instance attribute — unique per object
print(s1.name)    # Alice
print(s2.name)    # Bob
```

---

## Deleting Attributes and Objects

```python
p = Person("Alice", 30)

# Delete an attribute
del p.age
# print(p.age)  → AttributeError

# Delete the object
del p
# print(p)  → NameError
```

---

## Code Example: Student Report Card

```python
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}

    def add_grade(self, subject, score):
        self.grades[subject] = score

    def average(self):
        if not self.grades:
            return 0
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
                f"Average: {self.average():.1f} | Grade: {self.letter_grade()}")

# Usage
alice = Student("Alice", "S001")
alice.add_grade("Math", 92)
alice.add_grade("Science", 88)
alice.add_grade("English", 95)

print(alice)
# Student: Alice (ID: S001)
# Average: 91.7 | Grade: A
```

---

## Practice Questions

1. Create a `Car` class with `brand`, `model`, `year` attributes and a `description()` method
2. Add a class attribute `total_cars` that tracks how many Car objects have been created
3. Add a `@classmethod` called `from_string` that creates a Car from a string like `"Toyota,Camry,2022"`
4. Add a `@staticmethod` called `is_vintage(year)` that returns `True` if the car is older than 25 years

---

## Summary

| Concept | Syntax |
|---------|--------|
| Define class | `class MyClass:` |
| Constructor | `def __init__(self, ...):` |
| Instance attribute | `self.name = value` |
| Class attribute | `name = value` (outside `__init__`) |
| Instance method | `def method(self):` |
| Class method | `@classmethod` + `def method(cls):` |
| Static method | `@staticmethod` + `def method():` |

---

Next → [02 - Encapsulation](./02_encapsulation.md)

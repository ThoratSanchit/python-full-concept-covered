# ============================================================
# 10 OOP — 06: Magic / Dunder Methods
# ============================================================
# Run this file: python 06_magic_methods.py
# ============================================================
# Dunder = Double UNDERscore (__method__)
# Python calls these automatically in specific situations


# ── REPRESENTATION ──────────────────────────────────────────
class Book:
    def __init__(self, title, author, pages):
        self.title  = title
        self.author = author
        self.pages  = pages

    def __str__(self):
        """Called by print() and str() — for end users."""
        return f'"{self.title}" by {self.author}'

    def __repr__(self):
        """Called in REPL and repr() — for developers/debugging.
        Should ideally be a valid Python expression to recreate the object."""
        return f"Book(title={self.title!r}, author={self.author!r}, pages={self.pages})"

b = Book("Clean Code", "Robert Martin", 431)
print(b)            # "Clean Code" by Robert Martin
print(repr(b))      # Book(title='Clean Code', author='Robert Martin', pages=431)


# ── COMPARISON OPERATORS ────────────────────────────────────
from functools import total_ordering

# @total_ordering: define __eq__ + ONE comparison, get the rest for free
@total_ordering
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa  = gpa

    def __eq__(self, other):
        # Called when you write: s1 == s2
        return self.gpa == other.gpa

    def __lt__(self, other):
        # Called when you write: s1 < s2
        # @total_ordering generates __le__, __gt__, __ge__ from these two
        return self.gpa < other.gpa

    def __str__(self):
        return f"{self.name} ({self.gpa})"

s1 = Student("Alice", 3.9)
s2 = Student("Bob",   3.5)
s3 = Student("Carol", 3.7)

print(s1 > s2)      # True
print(s2 < s3)      # True
print(s1 == s1)     # True

# sorted() uses __lt__ automatically
students = [s1, s2, s3]
print(sorted(students))     # Sorted by GPA ascending


# ── ARITHMETIC OPERATORS ────────────────────────────────────
class Money:
    def __init__(self, amount, currency="USD"):
        self.amount   = round(amount, 2)
        self.currency = currency

    def _check_currency(self, other):
        if self.currency != other.currency:
            raise ValueError(f"Cannot operate on {self.currency} and {other.currency}")

    def __add__(self, other):
        # Called when you write: m1 + m2
        self._check_currency(other)
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other):
        # Called when you write: m1 - m2
        self._check_currency(other)
        return Money(self.amount - other.amount, self.currency)

    def __mul__(self, factor):
        # Called when you write: m1 * 3
        return Money(self.amount * factor, self.currency)

    def __rmul__(self, factor):
        # Called when you write: 3 * m1  (scalar on the LEFT side)
        return self.__mul__(factor)

    def __truediv__(self, divisor):
        # Called when you write: m1 / 2
        return Money(self.amount / divisor, self.currency)

    def __neg__(self):
        # Called when you write: -m1
        return Money(-self.amount, self.currency)

    def __abs__(self):
        # Called when you write: abs(m1)
        return Money(abs(self.amount), self.currency)

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

    def __str__(self):
        return f"{self.currency} {self.amount:.2f}"

price = Money(10.00)
tax   = Money(1.50)

print(price + tax)      # USD 11.50
print(price * 3)        # USD 30.00
print(3 * price)        # USD 30.00  — uses __rmul__
print(abs(Money(-5)))   # USD 5.00


# ── CONTAINER METHODS ───────────────────────────────────────
# Make your class behave like a list or dict
class Playlist:
    def __init__(self, name):
        self.name   = name
        self._songs = []

    def add(self, song):
        self._songs.append(song)

    def __len__(self):
        # Called when you write: len(playlist)
        return len(self._songs)

    def __getitem__(self, index):
        # Called when you write: playlist[0]
        return self._songs[index]

    def __setitem__(self, index, value):
        # Called when you write: playlist[0] = "new song"
        self._songs[index] = value

    def __delitem__(self, index):
        # Called when you write: del playlist[0]
        del self._songs[index]

    def __contains__(self, song):
        # Called when you write: "song" in playlist
        return song in self._songs

    def __iter__(self):
        # Called when you write: for song in playlist
        return iter(self._songs)

    def __bool__(self):
        # Called when you write: if playlist:
        return len(self._songs) > 0

    def __str__(self):
        return f"Playlist '{self.name}' ({len(self)} songs)"

p = Playlist("Favorites")
p.add("Bohemian Rhapsody")
p.add("Stairway to Heaven")
p.add("Hotel California")

print(len(p))                           # 3
print(p[0])                             # Bohemian Rhapsody
print("Hotel California" in p)          # True
print(bool(p))                          # True

for song in p:
    print(f"  ♪ {song}")


# ── CALLABLE OBJECTS ────────────────────────────────────────
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        # Called when you write: multiplier(5)  — object used like a function
        return value * self.factor

double = Multiplier(2)
triple = Multiplier(3)

print(double(5))        # 10
print(triple(5))        # 15
print(callable(double)) # True — has __call__


# ── CONTEXT MANAGER ─────────────────────────────────────────
class Timer:
    """Use as: with Timer() as t: ..."""
    import time as _time

    def __enter__(self):
        # Called at the start of 'with' block — return value goes to 'as' variable
        import time
        self._start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Called at the end of 'with' block — always, even if exception occurred
        import time
        self.elapsed = time.time() - self._start
        print(f"Elapsed: {self.elapsed:.4f}s")
        return False    # False = don't suppress exceptions

with Timer():
    total = sum(range(1_000_000))


# ── HASHING — USE OBJECTS AS DICT KEYS ──────────────────────
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        # Must be consistent with __eq__: equal objects must have equal hashes
        # tuple hash is a good pattern for immutable-like objects
        return hash((self.x, self.y))

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(1, 2)    # Equal to p1

# Can use as dict key because __hash__ is defined
locations = {p1: "Home", Point(3, 4): "Work"}
print(locations[p2])    # "Home" — p1 == p2, same hash

# Can use in sets
point_set = {p1, p2, Point(3, 4)}
print(len(point_set))   # 2 — p1 and p2 are equal, counted once


# ── PRACTICE ────────────────────────────────────────────────
# 1. Build a Matrix class with __add__, __mul__ (scalar), __str__, __getitem__
# 2. Create a Stack class with __len__, __contains__, __iter__, __bool__
# 3. Implement Duration (hours, minutes, seconds) with __add__, __str__, comparisons
# 4. Make a Config class that behaves like a dict using __getitem__, __setitem__, __contains__

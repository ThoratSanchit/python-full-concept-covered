# ============================================================
# 03 - Data Structures
# ============================================================
# Run this file: python data_structures.py
# ============================================================


# ── LISTS ───────────────────────────────────────────────────
# Ordered, mutable — use when order matters and you need to modify the collection
fruits = ["apple", "banana", "cherry"]

# Indexing — 0-based, negative counts from end
print(fruits[0])    # apple
print(fruits[-1])   # cherry

# Slicing [start:stop:step] — stop is exclusive
print(fruits[0:2])  # ['apple', 'banana']
print(fruits[::-1]) # ['cherry', 'banana', 'apple']  — reversed

# Common list methods
fruits.append("date")           # Add to end
fruits.insert(1, "blueberry")   # Insert at index 1
fruits.remove("banana")         # Remove by value (first occurrence)
popped = fruits.pop()           # Remove and return last item
print(fruits)
print(f"Popped: {popped}")

# Sorting
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()                  # Sort in place (modifies original)
print(numbers)
sorted_copy = sorted([3, 1, 2]) # Returns new sorted list (original unchanged)

# List comprehension — concise way to build lists
squares = [x**2 for x in range(1, 6)]          # [1, 4, 9, 16, 25]
evens   = [x for x in range(20) if x % 2 == 0] # [0, 2, 4, ...]
print(squares)
print(evens)


# ── TUPLES ──────────────────────────────────────────────────
# Ordered, IMMUTABLE — use for fixed data (coordinates, RGB, DB records)
point = (3, 4)
rgb   = (255, 128, 0)

print(point[0])     # 3

# Tuple unpacking — clean way to extract values
x, y = point
r, g, b = rgb
print(f"x={x}, y={y}")

# Extended unpacking
first, *rest = (1, 2, 3, 4, 5)
print(first)    # 1
print(rest)     # [2, 3, 4, 5]

# Tuples can be dict keys (lists cannot — they're not hashable)
locations = {(40.7, -74.0): "New York", (51.5, -0.1): "London"}
print(locations[(40.7, -74.0)])


# ── SETS ────────────────────────────────────────────────────
# Unordered, unique items — use for membership testing and removing duplicates
tags = {"python", "coding", "python", "tutorial"}  # Duplicate removed
print(tags)     # {'python', 'coding', 'tutorial'}

# IMPORTANT: empty set must use set(), not {} (that creates a dict!)
empty_set = set()

# Set operations — great for comparing collections
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)    # Union:        {1, 2, 3, 4, 5, 6}
print(a & b)    # Intersection: {3, 4}
print(a - b)    # Difference:   {1, 2}
print(a ^ b)    # Symmetric diff (in one but not both): {1, 2, 5, 6}

# Fast membership test — O(1) vs O(n) for lists
print(3 in a)   # True


# ── DICTIONARIES ────────────────────────────────────────────
# Key-value pairs — use for fast lookups and structured data
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Access — use .get() to avoid KeyError on missing keys
print(person["name"])               # Alice
print(person.get("salary", 0))      # 0 — default if key missing

# Add / update
person["email"] = "alice@example.com"   # Add new key
person["age"] = 31                       # Update existing key

# Remove
del person["city"]                  # Delete key
removed = person.pop("email")       # Remove and return value

# Iterate
for key, value in person.items():
    print(f"  {key}: {value}")

# Dictionary comprehension
word_lengths = {word: len(word) for word in ["apple", "banana", "cherry"]}
print(word_lengths)     # {'apple': 5, 'banana': 6, 'cherry': 6}


# ── NESTED DATA STRUCTURES ──────────────────────────────────
# Real-world data is often nested — dicts inside lists, etc.
students = [
    {"name": "Alice", "grades": [90, 85, 92]},
    {"name": "Bob",   "grades": [78, 88, 80]},
]

for student in students:
    avg = sum(student["grades"]) / len(student["grades"])
    print(f"{student['name']}: avg = {avg:.1f}")


# ── MUTABILITY GOTCHA ───────────────────────────────────────
# Lists are mutable — assignment copies the REFERENCE, not the data
list1 = [1, 2, 3]
list2 = list1           # Both point to the same list!
list2.append(4)
print(list1)            # [1, 2, 3, 4]  — list1 changed too!

# Fix: use .copy() for a shallow copy
list3 = list1.copy()
list3.append(99)
print(list1)            # [1, 2, 3, 4]  — unchanged


# ── REAL EXAMPLE: Word Frequency Counter ────────────────────
text = "the quick brown fox jumps over the lazy dog the fox"
words = text.split()

frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

# Sort by frequency (highest first)
sorted_freq = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
print("\n--- Word Frequency ---")
for word, count in sorted_freq[:5]:
    print(f"  '{word}': {count}")


# ── PRACTICE ────────────────────────────────────────────────
# 1. Given [1,2,2,3,3,3,4], remove duplicates while preserving order
# 2. Count character frequency in "hello world" using a dict
# 3. Find common elements between [1,2,3,4] and [3,4,5,6] using sets

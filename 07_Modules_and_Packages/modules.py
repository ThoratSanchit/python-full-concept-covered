# ============================================================
# 07 - Modules and Packages
# ============================================================
# Run this file: python modules.py
# ============================================================


# ── IMPORTING MODULES ───────────────────────────────────────

# Import the whole module — access with dot notation
import math
print(math.pi)          # 3.141592653589793
print(math.sqrt(16))    # 4.0
print(math.ceil(4.2))   # 5
print(math.floor(4.9))  # 4

# Import specific items — no dot notation needed
from math import pi, sqrt, factorial
print(pi)           # 3.14159...
print(sqrt(25))     # 5.0
print(factorial(5)) # 120

# Import with alias — useful for long module names
import datetime as dt
now = dt.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M"))


# ── OS MODULE — File System Operations ──────────────────────
import os

print(os.getcwd())                          # Current working directory
print(os.path.exists("modules.py"))         # True — file exists
print(os.path.basename("/path/to/file.txt"))# file.txt
print(os.path.dirname("/path/to/file.txt")) # /path/to
print(os.path.splitext("script.py"))        # ('script', '.py')

# Build paths safely — works on Windows AND Mac/Linux
path = os.path.join("folder", "subfolder", "file.txt")
print(path)     # folder/subfolder/file.txt  (or folder\subfolder\file.txt on Windows)

# Environment variables
home = os.environ.get("HOME", "unknown")    # Use .get() to avoid KeyError
print(f"Home: {home}")


# ── DATETIME MODULE ─────────────────────────────────────────
from datetime import datetime, date, timedelta

# Current date and time
now   = datetime.now()
today = date.today()
print(now.strftime("%Y-%m-%d %H:%M:%S"))    # 2024-03-15 14:30:00
print(today)                                 # 2024-03-15

# Date arithmetic
tomorrow    = today + timedelta(days=1)
last_week   = today - timedelta(weeks=1)
print(f"Tomorrow: {tomorrow}")
print(f"Last week: {last_week}")

# Days between two dates
new_year = date(today.year + 1, 1, 1)
days_left = (new_year - today).days
print(f"Days until New Year: {days_left}")

# Parse a date string
birthday = datetime.strptime("1995-06-15", "%Y-%m-%d")
print(f"Birthday: {birthday.strftime('%B %d, %Y')}")   # June 15, 1995


# ── RANDOM MODULE ───────────────────────────────────────────
import random

# Random float between 0 and 1
print(random.random())

# Random integer (inclusive on both ends)
dice = random.randint(1, 6)
print(f"Dice roll: {dice}")

# Random choice from a list
colors = ["red", "green", "blue", "yellow"]
print(random.choice(colors))

# Multiple unique random choices
sample = random.sample(range(1, 50), 6)     # Like a lottery
print(f"Lottery numbers: {sorted(sample)}")

# Shuffle a list in place
deck = list(range(1, 14))
random.shuffle(deck)
print(f"Shuffled deck: {deck}")

# Reproducible randomness — set a seed for testing
random.seed(42)
print(random.randint(1, 100))   # Always 82 with seed=42


# ── JSON MODULE ─────────────────────────────────────────────
import json

# Python dict → JSON string
data = {
    "name": "Alice",
    "age": 30,
    "scores": [95, 87, 92],
    "active": True
}
json_str = json.dumps(data, indent=2)   # indent makes it readable
print(json_str)

# JSON string → Python dict
parsed = json.loads(json_str)
print(parsed["name"])   # Alice
print(type(parsed))     # <class 'dict'>

# Write JSON to file
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# Read JSON from file
with open("data.json", "r") as f:
    loaded = json.load(f)
print(loaded["scores"])     # [95, 87, 92]

# Cleanup
os.remove("data.json")


# ── COLLECTIONS MODULE ──────────────────────────────────────
from collections import Counter, defaultdict, deque

# Counter — count occurrences of items
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count = Counter(words)
print(count)                        # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
print(count.most_common(2))         # [('apple', 3), ('banana', 2)]

# Counter works on strings too
letter_count = Counter("mississippi")
print(letter_count)

# defaultdict — dict that creates a default value for missing keys
# No more KeyError when accessing a key that doesn't exist yet
groups = defaultdict(list)
students = [("Alice", "Math"), ("Bob", "Science"), ("Carol", "Math")]
for name, subject in students:
    groups[subject].append(name)    # No need to check if key exists
print(dict(groups))     # {'Math': ['Alice', 'Carol'], 'Science': ['Bob']}

# deque — double-ended queue, fast append/pop from both ends
# Much faster than list for prepend operations
dq = deque([1, 2, 3])
dq.appendleft(0)    # Add to front — O(1) vs O(n) for list
dq.append(4)        # Add to back
print(dq)           # deque([0, 1, 2, 3, 4])
dq.popleft()        # Remove from front
print(dq)           # deque([1, 2, 3, 4])

# deque with maxlen — automatically discards old items (useful for logs)
recent = deque(maxlen=3)
for i in range(6):
    recent.append(i)
print(recent)   # deque([3, 4, 5], maxlen=3)


# ── ITERTOOLS MODULE ────────────────────────────────────────
import itertools

# chain — combine multiple iterables into one
combined = list(itertools.chain([1, 2], [3, 4], [5]))
print(combined)     # [1, 2, 3, 4, 5]

# combinations — all unique pairs (order doesn't matter)
pairs = list(itertools.combinations(["A", "B", "C", "D"], 2))
print(pairs)        # [('A','B'), ('A','C'), ('A','D'), ('B','C'), ...]

# permutations — all ordered arrangements
perms = list(itertools.permutations([1, 2, 3], 2))
print(perms)        # [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]

# islice — slice a lazy iterator without converting to list
counter = itertools.count(start=1)      # Infinite counter: 1, 2, 3, ...
first_5 = list(itertools.islice(counter, 5))
print(first_5)      # [1, 2, 3, 4, 5]


# ── PRACTICE ────────────────────────────────────────────────
# 1. Use datetime to find what day of the week you were born
# 2. Use Counter to find the 3 most common words in a paragraph
# 3. Use random to simulate rolling two dice 1000 times, count each sum
# 4. Use os.path to check if a file exists before trying to open it

# 07 - Modules and Packages

## What are Modules?

A module is a Python file (`.py`) containing functions, classes, and variables that you can reuse in other files. Packages are directories of modules.

---

## Importing Modules

```python
# Import entire module
import math
print(math.pi)        # 3.141592653589793
print(math.sqrt(16))  # 4.0

# Import specific items
from math import pi, sqrt
print(pi)       # 3.141592653589793
print(sqrt(16)) # 4.0

# Import with alias
import numpy as np
from datetime import datetime as dt

# Import everything (avoid in production)
from math import *
```

---

## Creating Your Own Module

Create `utils.py`:
```python
# utils.py

def greet(name):
    """Return a greeting message"""
    return f"Hello, {name}!"

def add(a, b):
    return a + b

PI = 3.14159
```

Use it in `main.py`:
```python
# main.py
import utils

print(utils.greet("Alice"))  # Hello, Alice!
print(utils.add(3, 4))       # 7
print(utils.PI)               # 3.14159
```

---

## The `__name__` Variable

```python
# mymodule.py

def main():
    print("Running as main script")

if __name__ == "__main__":
    # This only runs when file is executed directly
    # NOT when imported as a module
    main()
```

---

## Packages

A package is a folder with an `__init__.py` file.

```
mypackage/
├── __init__.py
├── math_utils.py
├── string_utils.py
└── file_utils.py
```

```python
# __init__.py
from .math_utils import add, subtract
from .string_utils import greet

# Usage
from mypackage import add, greet
```

---

## Standard Library Highlights

### os — Operating System
```python
import os

os.getcwd()                    # Current directory
os.listdir(".")                # List files
os.path.exists("file.txt")     # Check if exists
os.path.join("folder", "file") # Build paths safely
os.makedirs("new/folder", exist_ok=True)
os.environ.get("HOME")         # Environment variables
```

### sys — System
```python
import sys

sys.argv          # Command-line arguments
sys.path          # Module search paths
sys.version       # Python version
sys.exit(0)       # Exit program
```

### datetime — Dates and Times
```python
from datetime import datetime, date, timedelta

now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

today = date.today()
birthday = date(1995, 6, 15)
age_days = (today - birthday).days

tomorrow = today + timedelta(days=1)
```

### random — Random Numbers
```python
import random

random.random()              # Float between 0 and 1
random.randint(1, 10)        # Integer between 1 and 10
random.choice([1, 2, 3])     # Random item from list
random.shuffle([1, 2, 3])    # Shuffle list in place
random.sample([1,2,3,4,5], 3) # 3 unique random items
```

### json — JSON Data
```python
import json

# Python → JSON string
data = {"name": "Alice", "age": 30}
json_str = json.dumps(data, indent=2)

# JSON string → Python
parsed = json.loads(json_str)

# File operations
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

with open("data.json", "r") as f:
    loaded = json.load(f)
```

### collections — Specialized Containers
```python
from collections import Counter, defaultdict, OrderedDict, deque

# Counter - count occurrences
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count = Counter(words)
print(count.most_common(2))  # [('apple', 3), ('banana', 2)]

# defaultdict - dict with default value
dd = defaultdict(list)
dd["fruits"].append("apple")  # No KeyError

# deque - fast append/pop from both ends
dq = deque([1, 2, 3])
dq.appendleft(0)   # [0, 1, 2, 3]
dq.popleft()       # 0
```

### itertools — Iterator Tools
```python
import itertools

# Combinations and permutations
list(itertools.combinations([1,2,3], 2))   # [(1,2),(1,3),(2,3)]
list(itertools.permutations([1,2,3], 2))   # [(1,2),(1,3),(2,1),...]

# Chain iterables
list(itertools.chain([1,2], [3,4], [5]))   # [1,2,3,4,5]

# Infinite counter
counter = itertools.count(start=1, step=2)
[next(counter) for _ in range(5)]          # [1, 3, 5, 7, 9]
```

---

## Installing Third-Party Packages

```bash
# Install a package
pip install requests

# Install specific version
pip install requests==2.28.0

# Install from requirements file
pip install -r requirements.txt

# List installed packages
pip list

# Save dependencies
pip freeze > requirements.txt
```

### Popular Third-Party Packages

| Package | Purpose |
|---------|---------|
| `requests` | HTTP requests |
| `numpy` | Numerical computing |
| `pandas` | Data analysis |
| `flask` | Web framework |
| `sqlalchemy` | Database ORM |
| `pytest` | Testing |
| `pillow` | Image processing |

---

## Virtual Environments

Isolate project dependencies.

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Deactivate
deactivate
```

---

## Practice Questions

1. Create a module `calculator.py` with add, subtract, multiply, divide functions
2. Use `datetime` to calculate how many days until New Year
3. Use `Counter` to find the 3 most common words in a text
4. Create a package with two modules and import from both

---

## Mini Task

Build a `file_organizer` package that:
1. Scans a directory
2. Groups files by extension
3. Moves files into subfolders by type (images, docs, videos, etc.)
4. Generates a report of what was moved

---

## Summary

| Concept | Example |
|---------|---------|
| Import module | `import math` |
| Import specific | `from math import sqrt` |
| Alias | `import numpy as np` |
| Create module | Save as `.py` file |
| Package | Folder with `__init__.py` |
| Install package | `pip install name` |

---

## Next Steps

Move to [08 - File Handling](../08_File_Handling/) to learn how to read and write files.

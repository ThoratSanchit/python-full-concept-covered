# 03 - Data Structures

## What are Data Structures?

Data structures are containers that organize and store data efficiently. Python provides built-in data structures that are powerful and easy to use.

**Main Data Structures in Python:**
- **List**: Ordered, mutable collection
- **Tuple**: Ordered, immutable collection
- **Set**: Unordered, unique items
- **Dictionary**: Key-value pairs

---

## Deep Explanation

### Memory and Performance

| Structure | Lookup | Insert | Delete | Memory |
|-----------|--------|--------|--------|--------|
| List | O(n) | O(1)* | O(n) | Medium |
| Tuple | O(n) | - | - | Low |
| Set | O(1) | O(1) | O(1) | High |
| Dict | O(1) | O(1) | O(1) | High |

*Amortized - occasionally needs to resize

### What These Mean

`O(1)` = **Constant Time**

No matter how much data you have, the time stays the **same**.

Examples:
- Accessing the last item of a list: `my_list[-1]`
- Looking up a value in a dictionary by key: `my_dict["name"]`

`O(n)` = **Linear Time**

If the data gets bigger, the time also grows.
If you have 10 items, it checks about 10 items.
If you have 1000 items, it may check about 1000 items.

Examples:
- Searching for an item in a list
- Deleting an item from the middle of a list

`O(log n)` = **Logarithmic Time**

As the data grows, the time grows very slowly.
Instead of checking every item one by one, it keeps reducing the problem size.

Examples:
- Binary search in a sorted list
- Finding something by repeatedly dividing the data in half

`O(1)*` = **Amortized Constant Time**

Most of the time, the operation takes the **same** amount of time.
But sometimes Python needs to resize the list, so one operation can take longer.

Example:
- `list.append()` is usually `O(1)`, but sometimes resizing happens

### When to Use What?

- **List**: Ordered data, frequent modifications
- **Tuple**: Fixed data, faster than lists, dictionary keys
- **Set**: Membership testing, removing duplicates
- **Dictionary**: Fast lookups by key, structured data

---

## Lists

Ordered, mutable collection of items.

### Creating Lists
```python
# Empty list
my_list = []
my_list = list()

# With values
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]

# Nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

### Indexing and Slicing
```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Indexing (0-based)
fruits[0]     # "apple"
fruits[-1]    # "elderberry" (last item)
fruits[2]     # "cherry"

# Slicing [start:stop:step]
fruits[1:4]   # ["banana", "cherry", "date"]
fruits[:3]    # ["apple", "banana", "cherry"]
fruits[2:]    # ["cherry", "date", "elderberry"]
fruits[::2]   # ["apple", "cherry", "elderberry"]
fruits[::-1]  # Reverse list
```

### List Methods
```python
fruits = ["apple", "banana"]

# Adding items
fruits.append("cherry")        # Add to end
fruits.insert(1, "blueberry")  # Insert at index
fruits.extend(["date", "fig"]) # Add multiple items

# Removing items
fruits.remove("banana")        # Remove by value
popped = fruits.pop()          # Remove and return last
popped = fruits.pop(0)         # Remove and return at index
del fruits[0]                  # Delete by index
fruits.clear()                 # Remove all items

# Other operations
fruits.sort()                  # Sort in place
fruits.sort(reverse=True)      # Sort descending
fruits.reverse()               # Reverse in place
index = fruits.index("apple")  # Find index
count = fruits.count("apple")  # Count occurrences
```

### List Operations
```python
a = [1, 2, 3]
b = [4, 5, 6]

# Concatenation
c = a + b          # [1, 2, 3, 4, 5, 6]

# Repetition
d = a * 3          # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Membership
2 in a             # True
5 in a             # False

# Length
len(a)             # 3

# Min/Max/Sum
min(a)             # 1
max(a)             # 3
sum(a)             # 6
```

---

## Tuples

Ordered, immutable collection.

### Creating Tuples
```python
# Empty tuple
empty = ()
empty = tuple()

# With values
point = (3, 4)
single = (5,)      # Note the comma!

# Without parentheses
coordinates = 10, 20, 30

# Nested tuples
nested = ((1, 2), (3, 4), (5, 6))
```

### Tuple Operations
```python
coords = (10, 20, 30, 40, 50)

# Indexing and slicing (same as lists)
coords[0]          # 10
coords[-1]         # 50
coords[1:4]        # (20, 30, 40)

# Unpacking
x, y = (10, 20)    # x=10, y=20
a, b, *rest = (1, 2, 3, 4, 5)  # a=1, b=2, rest=[3,4,5]

# Tuple methods
count = coords.count(10)       # 1
index = coords.index(30)       # 2

# Immutable - can't modify
coords[0] = 100    # TypeError!
```

### Why Use Tuples?
- Faster than lists
- Can be dictionary keys (hashable)
- Protects data from accidental modification
- Used for fixed data like coordinates, RGB values

---

## Sets

Unordered collection of unique items.

### Creating Sets
```python
# Empty set
empty = set()      # NOT {} - that's an empty dict!

# With values
fruits = {"apple", "banana", "cherry"}
numbers = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3} - duplicates removed
```

### Set Methods
```python
s = {1, 2, 3}

# Adding/Removing
s.add(4)               # Add single item
s.update([5, 6])       # Add multiple items
s.remove(3)            # Remove (error if not exists)
s.discard(10)          # Remove (no error if not exists)
popped = s.pop()       # Remove and return arbitrary item
s.clear()              # Remove all

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a.union(b)             # {1, 2, 3, 4, 5, 6}
a | b                  # Same as union

a.intersection(b)      # {3, 4}
a & b                  # Same as intersection

a.difference(b)        # {1, 2}
a - b                  # Same as difference

a.symmetric_difference(b)  # {1, 2, 5, 6}
a ^ b                  # Same as symmetric_difference

# Subset/Superset
a.issubset(b)          # False
a.issuperset({1, 2})   # True
a.isdisjoint({5, 6})   # False (they share 3,4)
```

---

## Dictionaries

Key-value pairs for fast lookups.

### Creating Dictionaries
```python
# Empty dict
empty = {}
empty = dict()

# With values
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# From sequences
pairs = [("a", 1), ("b", 2)]
d = dict(pairs)        # {"a": 1, "b": 2}

# Using dict()
d = dict(name="John", age=30)
```

### Accessing and Modifying
```python
person = {"name": "John", "age": 30}

# Access
person["name"]         # "John"
person.get("age")      # 30
person.get("salary", 0)  # 0 (default if key not found)

# Modify/Add
person["age"] = 31     # Update
person["city"] = "NYC" # Add new key

# Remove
del person["age"]      # Delete key
age = person.pop("age")  # Remove and return
person.popitem()       # Remove and return arbitrary item
person.clear()         # Remove all

# Check existence
"name" in person       # True
"salary" in person     # False
```

### Dictionary Methods
```python
person = {"name": "John", "age": 30, "city": "NYC"}

# Get all keys, values, items
keys = person.keys()       # dict_keys(['name', 'age', 'city'])
values = person.values()   # dict_values(['John', 30, 'NYC'])
items = person.items()     # dict_items([('name', 'John'), ...])

# Iteration
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(f"{key}: {value}")

# Update
person.update({"age": 31, "country": "USA"})

# Set default (only if key doesn't exist)
person.setdefault("salary", 50000)
```

### Nested Dictionaries
```python
company = {
    "name": "TechCorp",
    "employees": {
        "john": {"age": 30, "role": "Developer"},
        "jane": {"age": 28, "role": "Designer"}
    },
    "departments": ["Engineering", "Design", "Marketing"]
}

# Access nested data
company["employees"]["john"]["role"]  # "Developer"
```

---

## Mutability vs Immutability

| Mutable | Immutable |
|---------|-----------|
| Can be changed after creation | Cannot be changed after creation |
| List, Set, Dictionary | int, float, str, bool, Tuple |

```python
# Mutable example
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1)  # [1, 2, 3, 4] - both changed!

# Immutable example
a = "hello"
b = a
b = b + " world"
print(a)  # "hello" - unchanged
print(b)  # "hello world"

# Copying mutable objects
import copy
list_copy = list1.copy()      # Shallow copy
deep_copy = copy.deepcopy(nested_list)  # Deep copy
```

---

## Code Examples

### Example 1: Student Grade Manager
```python
# Store student grades
students = {
    "Alice": [85, 90, 78],
    "Bob": [92, 88, 95],
    "Charlie": [78, 85, 80]
}

# Calculate average grades
for name, grades in students.items():
    average = sum(grades) / len(grades)
    print(f"{name}: Average = {average:.2f}")
```

### Example 2: Remove Duplicates
```python
# Using set
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = list(set(numbers))
print(unique)  # [1, 2, 3, 4] (order not guaranteed)

# Preserving order
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(remove_duplicates(numbers))  # [1, 2, 3, 4]
```

### Example 3: Word Frequency Counter
```python
text = "apple banana apple cherry banana apple"
words = text.split()

frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)  # {'apple': 3, 'banana': 2, 'cherry': 1}

# Sort by frequency
sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
print(sorted_words)  # [('apple', 3), ('banana', 2), ('cherry', 1)]
```

### Example 4: Matrix Operations
```python
# Matrix transpose
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Using list comprehension
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transpose)
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Flatten matrix
flattened = [item for row in matrix for item in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Example 5: Inventory System
```python
inventory = {
    "apple": {"quantity": 50, "price": 0.5},
    "banana": {"quantity": 30, "price": 0.3},
    "cherry": {"quantity": 100, "price": 0.1}
}

def add_item(name, quantity, price):
    if name in inventory:
        inventory[name]["quantity"] += quantity
    else:
        inventory[name] = {"quantity": quantity, "price": price}

def sell_item(name, quantity):
    if name not in inventory:
        return "Item not found"
    if inventory[name]["quantity"] < quantity:
        return "Not enough stock"
    
    inventory[name]["quantity"] -= quantity
    total = quantity * inventory[name]["price"]
    return f"Sold {quantity} {name}(s) for ${total:.2f}"

def get_inventory_value():
    total = sum(item["quantity"] * item["price"] for item in inventory.values())
    return f"Total inventory value: ${total:.2f}"

# Usage
add_item("apple", 20, 0.5)
print(sell_item("apple", 10))
print(get_inventory_value())
```

---

## Real-World Use Cases

1. **Lists**: Shopping carts, to-do lists, timelines
2. **Tuples**: GPS coordinates, RGB colors, database records
3. **Sets**: Unique tags, user permissions, finding common friends
4. **Dictionaries**: User profiles, configuration settings, JSON data

---

## Common Mistakes / Pitfalls

| Mistake | Example | Solution |
|---------|---------|----------|
| Modifying list while iterating | `for x in lst: lst.remove(x)` | Iterate over copy or use list comprehension |
| Using `[]` for empty set | `s = {}` creates dict! | Use `s = set()` |
| Mutable default arguments | `def func(lst=[])` | Use `None` and check |
| Shallow vs deep copy | Nested lists share references | Use `copy.deepcopy()` |
| KeyError | `dict['missing_key']` | Use `.get()` or check with `in` |

```python
# Error 1: Modifying while iterating
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Skips elements!

# Fix: Create new list
evens = [n for n in numbers if n % 2 == 0]

# Error 2: Empty set
data = {}  # This is a dictionary!
print(type(data))  # <class 'dict'>

# Fix:
data = set()

# Error 3: Mutable default argument
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] - Surprise!

# Fix:
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

---

## Best Practices

1. **Choose the right data structure**
   ```python
   # Need fast lookup? Use dict
   users = {"john": {...}, "jane": {...}}
   
   # Need uniqueness? Use set
   tags = {"python", "coding", "tutorial"}
   
   # Fixed data? Use tuple
   coordinates = (40.7128, -74.0060)
   ```

2. **Use list comprehensions for simple transformations**
   ```python
   # Good
   squares = [x**2 for x in range(10)]
   
   # Avoid for simple cases
   squares = []
   for x in range(10):
       squares.append(x**2)
   ```

3. **Use `.get()` for dictionaries**
   ```python
   # Safer
   value = config.get("timeout", 30)
   
   # Risky
   value = config["timeout"]  # KeyError if missing
   ```

4. **Use tuple unpacking**
   ```python
   # Good
   name, age = ("John", 30)
   
   # Avoid
   data = ("John", 30)
   name = data[0]
   age = data[1]
   ```

5. **Document complex structures**
   ```python
   # Type hints help
   from typing import Dict, List, Tuple
   
   def process_users(users: Dict[str, Dict[str, any]]) -> List[Tuple[str, int]]:
       ...
   ```

---

## Practice Questions

### Question 1 (Easy)
Create a list of 5 fruits and print the 2nd and 4th items using indexing.

### Question 2 (Easy)
Given a list `[1, 2, 2, 3, 3, 3, 4, 4, 4, 4]`, create a new list with only unique elements (preserve order).

### Question 3 (Medium)
Write a program to count the frequency of each character in a string using a dictionary.

**Example:** `"hello"` → `{'h': 1, 'e': 1, 'l': 2, 'o': 1}`

### Question 4 (Medium)
Create a nested dictionary to store student information (name, grades for 3 subjects). Calculate and store the average grade for each student.

### Question 5 (Hard)
Write a function that finds the intersection of two lists without using set operations.

**Example:** `[1, 2, 3, 4]` and `[3, 4, 5, 6]` → `[3, 4]`

---

## Mini Task / Assignment

### Task: Build a Contact Management System

Create a contact manager with the following features:

1. **Add Contact**: Name, phone, email, address
2. **Search Contact**: By name or phone number
3. **Update Contact**: Modify existing contact
4. **Delete Contact**: Remove a contact
5. **List All Contacts**: Display all contacts sorted by name
6. **Export/Import**: Save to/load from JSON file

**Data Structure:**
```python
contacts = {
    "john_doe": {
        "name": "John Doe",
        "phone": "123-456-7890",
        "email": "john@example.com",
        "address": "123 Main St"
    },
    ...
}
```

**Requirements:**
- Use appropriate data structures
- Handle edge cases (duplicate names, invalid input)
- Include a menu-driven interface
- Validate phone numbers and emails

**Bonus Features:**
- Group contacts (Family, Friends, Work)
- Search by partial name match
- Favorite contacts
- Recent contacts list

---

## Summary

| Structure | Ordered | Mutable | Duplicates | Use Case |
|-----------|---------|---------|------------|----------|
| List | Yes | Yes | Allowed | Dynamic collections |
| Tuple | Yes | No | Allowed | Fixed data, keys |
| Set | No | Yes | No | Uniqueness, math ops |
| Dict | No* | Yes | No (keys) | Key-value mapping |

*Python 3.7+ maintains insertion order

**Key Takeaways:**
- Lists for ordered, changeable data
- Tuples for fixed, hashable data
- Sets for uniqueness and fast membership testing
- Dictionaries for key-based lookups
- Choose based on your use case, not habit

---

## Next Steps

Move to [04 - Functions](../04_Functions/) to learn about creating reusable code blocks.

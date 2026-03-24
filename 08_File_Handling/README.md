# 08 - File Handling

## What is File Handling?

File handling lets you read from and write to files on disk — essential for storing data, reading configs, processing logs, and more.

---

## Opening Files

```python
# Basic syntax
file = open("filename.txt", mode)
# Always close after use
file.close()

# Better: use 'with' statement (auto-closes)
with open("filename.txt", "r") as file:
    content = file.read()
```

### File Modes

| Mode | Description |
|------|-------------|
| `"r"` | Read (default) — error if file doesn't exist |
| `"w"` | Write — creates file, overwrites if exists |
| `"a"` | Append — adds to end of file |
| `"x"` | Create — error if file already exists |
| `"r+"` | Read and write |
| `"rb"` | Read binary |
| `"wb"` | Write binary |

---

## Reading Files

```python
# Read entire file as string
with open("file.txt", "r") as f:
    content = f.read()

# Read line by line (memory efficient)
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())

# Read all lines into a list
with open("file.txt", "r") as f:
    lines = f.readlines()

# Read single line
with open("file.txt", "r") as f:
    first_line = f.readline()
```

---

## Writing Files

```python
# Write (overwrites existing content)
with open("output.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("Second line\n")

# Write multiple lines at once
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)

# Append to existing file
with open("log.txt", "a") as f:
    f.write("New log entry\n")
```

---

## Working with File Paths

```python
import os

# Build paths safely (works on all OS)
path = os.path.join("folder", "subfolder", "file.txt")

# Check if file/folder exists
os.path.exists("file.txt")    # True/False
os.path.isfile("file.txt")    # Is it a file?
os.path.isdir("folder")       # Is it a directory?

# Get file info
os.path.basename("/path/to/file.txt")  # "file.txt"
os.path.dirname("/path/to/file.txt")   # "/path/to"
os.path.splitext("file.txt")           # ("file", ".txt")
os.path.getsize("file.txt")            # Size in bytes

# Using pathlib (modern approach)
from pathlib import Path

p = Path("folder") / "subfolder" / "file.txt"
p.exists()
p.read_text()
p.write_text("content")
p.suffix    # ".txt"
p.stem      # "file"
p.parent    # Path("folder/subfolder")
```

---

## Working with CSV Files

```python
import csv

# Read CSV
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)  # Skip header row
    for row in reader:
        print(row)

# Read CSV as dictionaries
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])

# Write CSV
data = [["Name", "Age"], ["Alice", 30], ["Bob", 25]]
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Write CSV from dicts
people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
with open("output.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerows(people)
```

---

## Working with JSON Files

```python
import json

# Read JSON
with open("data.json", "r") as f:
    data = json.load(f)

# Write JSON
data = {"name": "Alice", "scores": [95, 87, 92]}
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
```

---

## Error Handling with Files

```python
try:
    with open("missing.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("No permission to read file!")
except IOError as e:
    print(f"IO Error: {e}")
```

---

## Code Examples

### Example 1: Log File Writer
```python
from datetime import datetime

def log(message, level="INFO", filename="app.log"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] [{level}] {message}\n"
    with open(filename, "a") as f:
        f.write(entry)

log("Application started")
log("User logged in", "INFO")
log("Database connection failed", "ERROR")
```

### Example 2: CSV Data Processor
```python
import csv

def read_students(filename):
    students = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            students.append({
                "name": row["name"],
                "grade": float(row["grade"])
            })
    return students

def get_top_students(students, n=3):
    return sorted(students, key=lambda s: s["grade"], reverse=True)[:n]
```

### Example 3: Config File Reader
```python
import json
from pathlib import Path

def load_config(path="config.json"):
    config_file = Path(path)
    if not config_file.exists():
        # Return defaults if no config file
        return {"debug": False, "port": 8080, "host": "localhost"}
    with open(config_file) as f:
        return json.load(f)

def save_config(config, path="config.json"):
    with open(path, "w") as f:
        json.dump(config, f, indent=2)
```

---

## Practice Questions

1. Write a program that counts the number of lines, words, and characters in a text file
2. Read a CSV file and calculate the average of a numeric column
3. Write a program that merges two text files into one
4. Create a simple note-taking app that saves notes to a file

---

## Mini Task

Build a student grade manager that:
1. Reads student data from a CSV file
2. Calculates average, highest, and lowest grades
3. Adds new students
4. Saves updated data back to CSV
5. Exports a summary report as a text file

---

## Summary

| Operation | Code |
|-----------|------|
| Read file | `open("f", "r")` |
| Write file | `open("f", "w")` |
| Append file | `open("f", "a")` |
| Safe open | `with open(...) as f:` |
| Read CSV | `csv.reader(f)` |
| Read JSON | `json.load(f)` |

---

## Next Steps

Move to [09 - Exception Handling](../09_Exception_Handling/) to learn how to handle errors gracefully.

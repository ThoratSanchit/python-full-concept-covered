# ============================================================
# 08 - File Handling
# ============================================================
# Run this file: python file_handling.py
# ============================================================

import os
import csv
import json
from pathlib import Path


# ── WRITING A FILE ──────────────────────────────────────────
# Always use 'with' — it automatically closes the file even if an error occurs
with open("sample.txt", "w") as f:
    f.write("Line 1: Hello, World!\n")
    f.write("Line 2: Python file handling\n")
    f.write("Line 3: Reading and writing files\n")

print("File written.")


# ── READING A FILE ──────────────────────────────────────────

# Read entire file as one string
with open("sample.txt", "r") as f:
    content = f.read()
print("--- Full content ---")
print(content)

# Read line by line — memory efficient for large files
print("--- Line by line ---")
with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())     # strip() removes the trailing \n

# Read all lines into a list
with open("sample.txt", "r") as f:
    lines = f.readlines()       # Returns ['Line 1...\n', 'Line 2...\n', ...]
print(f"Total lines: {len(lines)}")


# ── APPENDING TO A FILE ─────────────────────────────────────
# "a" mode adds to the end — does NOT overwrite existing content
with open("sample.txt", "a") as f:
    f.write("Line 4: Appended line\n")

print("Line appended.")


# ── FILE MODES SUMMARY ──────────────────────────────────────
# "r"  — read only (default), error if file doesn't exist
# "w"  — write, creates file, OVERWRITES if exists
# "a"  — append, creates file, adds to end if exists
# "x"  — create new file, error if already exists
# "rb" — read binary (images, PDFs, etc.)
# "wb" — write binary


# ── PATHLIB — MODERN FILE PATH HANDLING ─────────────────────
# pathlib.Path is cleaner than os.path for most operations
p = Path("sample.txt")

print(p.exists())       # True
print(p.suffix)         # .txt
print(p.stem)           # sample
print(p.name)           # sample.txt
print(p.parent)         # . (current directory)
print(p.stat().st_size) # File size in bytes

# Read/write with pathlib
text = p.read_text()            # Read entire file
p.write_text("New content\n")   # Write (overwrites)

# Build paths safely — works on all operating systems
config_path = Path("config") / "settings" / "app.json"
print(config_path)  # config/settings/app.json


# ── CSV FILES ───────────────────────────────────────────────
# CSV = Comma-Separated Values — common format for tabular data

# Write CSV
students = [
    ["Name", "Age", "Grade"],   # Header row
    ["Alice", 20, "A"],
    ["Bob", 22, "B"],
    ["Carol", 21, "A"],
]

with open("students.csv", "w", newline="") as f:
    # newline="" prevents extra blank lines on Windows
    writer = csv.writer(f)
    writer.writerows(students)

print("CSV written.")

# Read CSV as lists
print("--- CSV as lists ---")
with open("students.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)       # Skip the header row
    for row in reader:
        print(row)

# Read CSV as dictionaries — much more readable
print("--- CSV as dicts ---")
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)  # Uses first row as keys
    for row in reader:
        print(f"{row['Name']} is {row['Age']} years old, grade: {row['Grade']}")

# Write CSV from dicts
people = [
    {"name": "Dave", "city": "NYC", "score": 88},
    {"name": "Eve",  "city": "LA",  "score": 95},
]
with open("people.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "city", "score"])
    writer.writeheader()        # Write the header row
    writer.writerows(people)


# ── JSON FILES ──────────────────────────────────────────────
# JSON = JavaScript Object Notation — standard format for structured data

config = {
    "app_name": "MyApp",
    "version": "1.0.0",
    "debug": False,
    "database": {
        "host": "localhost",
        "port": 5432
    },
    "allowed_hosts": ["localhost", "127.0.0.1"]
}

# Write JSON
with open("config.json", "w") as f:
    json.dump(config, f, indent=2)  # indent=2 makes it human-readable

# Read JSON
with open("config.json", "r") as f:
    loaded = json.load(f)

print(f"App: {loaded['app_name']} v{loaded['version']}")
print(f"DB host: {loaded['database']['host']}")


# ── REAL EXAMPLE: Simple Logger ─────────────────────────────
from datetime import datetime

def log(message, level="INFO", filename="app.log"):
    """Append a timestamped log entry to a file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] [{level}] {message}\n"
    with open(filename, "a") as f:
        f.write(entry)

log("Application started")
log("User logged in: alice")
log("Database connection failed", level="ERROR")

# Read and display the log
print("\n--- App Log ---")
with open("app.log", "r") as f:
    print(f.read())


# ── CLEANUP — remove files created during this demo ─────────
for filename in ["sample.txt", "students.csv", "people.csv", "config.json", "app.log"]:
    if os.path.exists(filename):
        os.remove(filename)

print("Cleanup done.")


# ── PRACTICE ────────────────────────────────────────────────
# 1. Write a program that counts lines, words, and characters in a text file
# 2. Read a CSV of products (name, price, quantity) and find the most expensive
# 3. Build a simple note-taking app: save notes to a file, load them on startup
# 4. Write a function that merges two CSV files with the same columns

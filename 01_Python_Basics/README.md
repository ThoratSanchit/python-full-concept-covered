# 01 - Python Basics

## What is Python?

Python is a high-level, interpreted programming language known for its simplicity and readability. It was created by Guido van Rossum in 1991.

**Key Characteristics:**
- Easy to learn and read (English-like syntax)
- Interpreted (no compilation needed)
- Dynamically typed (no need to declare variable types)
- Cross-platform (works on Windows, Mac, Linux)
- Huge community and extensive libraries

---

## Deep Explanation

### How Python Works

1. **Source Code** (.py file) → **Bytecode** (.pyc file) → **Python Virtual Machine (PVM)** executes it
2. Python is both **compiled** (to bytecode) and **interpreted** (by PVM)
3. This makes Python slower than C/C++ but much faster to develop with

### Why Python is Popular

- **Rapid Development**: Write less code, do more
- **Versatility**: Web, AI, Data Science, Automation, Scripting
- **Community**: Millions of developers, endless resources
- **Libraries**: 400,000+ packages available via PyPI

---

## Installation

### Windows
1. Download from [python.org](https://python.org)
2. Run installer
3. **Important**: Check "Add Python to PATH"

### Verify Installation
```bash
python --version
```

---

## Running Python

### Method 1: Interactive Shell (REPL)
```bash
python
```
```python
>>> print("Hello, World!")
Hello, World!
```

### Method 2: Python File
Create `hello.py`:
```python
print("Hello, World!")
```

Run it:
```bash
python hello.py
```

---

## Syntax and Indentation

Python uses **indentation** (whitespace) to define code blocks, not curly braces.

```python
# Correct
if True:
    print("This is indented")
    print("Same block")

# Incorrect (will cause error)
if True:
print("Not indented")  # IndentationError!
```

**Rule**: Use 4 spaces per indentation level (PEP 8 standard)

---

## Comments

```python
# This is a single-line comment

"""
This is a 
multi-line comment
(or docstring)
"""

# Inline comment
x = 5  # This is a variable
```

---

## Variables

Variables are containers for storing data. No declaration needed!

```python
# Creating variables
name = "John"      # String
age = 25           # Integer
height = 5.9       # Float
is_student = True  # Boolean

# Multiple assignment
x, y, z = 1, 2, 3

# Same value to multiple variables
a = b = c = 0
```

**Variable Naming Rules:**
- Must start with letter or underscore
- Can contain letters, numbers, underscores
- Case-sensitive (`Name` != `name`)
- Cannot use reserved keywords

---

## Data Types

| Type | Description | Example |
|------|-------------|---------|
| `int` | Integer | `42`, `-7` |
| `float` | Decimal number | `3.14`, `-0.5` |
| `str` | Text/String | `"Hello"`, `'World'` |
| `bool` | Boolean | `True`, `False` |
| `list` | Ordered collection | `[1, 2, 3]` |
| `tuple` | Immutable ordered collection | `(1, 2, 3)` |
| `dict` | Key-value pairs | `{"name": "John"}` |
| `set` | Unordered unique items | `{1, 2, 3}` |

### Check Type
```python
type(42)        # <class 'int'>
type("hello")   # <class 'str'>
type(3.14)      # <class 'float'>
```

---

## Type Casting

Convert one data type to another:

```python
# String to int
age_str = "25"
age_int = int(age_str)      # 25

# Int to string
num = 42
num_str = str(num)          # "42"

# Int to float
x = 5
x_float = float(x)          # 5.0

# Float to int (truncates decimal)
y = 3.9
y_int = int(y)              # 3 (not 4!)
```

---

## Input and Output

### Output - print()
```python
print("Hello, World!")
print("Name:", "John", "Age:", 25)  # Multiple values
print(f"Name: {name}, Age: {age}")  # f-string (recommended)
```

### Input - input()
```python
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Input always returns string
age = int(input("Enter age: "))  # Convert to int
```

---

## Operators

### Arithmetic Operators
```python
a = 10
b = 3

print(a + b)   # 13 (Addition)
print(a - b)   # 7 (Subtraction)
print(a * b)   # 30 (Multiplication)
print(a / b)   # 3.333... (Division)
print(a // b)  # 3 (Floor division)
print(a % b)   # 1 (Modulo/Remainder)
print(a ** b)  # 1000 (Exponent/Power)
```

### Comparison Operators
```python
a = 5
b = 10

print(a == b)  # False (Equal)
print(a != b)  # True (Not equal)
print(a > b)   # False (Greater than)
print(a < b)   # True (Less than)
print(a >= b)  # False (Greater or equal)
print(a <= b)  # True (Less or equal)
```

### Logical Operators
```python
x = True
y = False

print(x and y)  # False (Both must be True)
print(x or y)   # True (At least one True)
print(not x)    # False (Negation)
```

### Assignment Operators
```python
x = 10
x += 5   # x = x + 5 → 15
x -= 3   # x = x - 3 → 12
x *= 2   # x = x * 2 → 24
x /= 4   # x = x / 4 → 6.0
x //= 2  # x = x // 2 → 3.0
x **= 2  # x = x ** 2 → 9.0
```

---

## Code Examples

### Example 1: Simple Calculator
```python
# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform operations
sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2
quot_result = num1 / num2

# Display results
print(f"Sum: {sum_result}")
print(f"Difference: {diff_result}")
print(f"Product: {prod_result}")
print(f"Quotient: {quot_result}")
```

### Example 2: Temperature Converter
```python
# Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")
```

### Example 3: BMI Calculator
```python
# Get user details
name = input("Enter your name: ")
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display result
print(f"\nHello {name}!")
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")
```

---

## Real-World Use Cases

1. **Simple Scripts**: Automate repetitive tasks
2. **Data Entry Forms**: Collect and process user input
3. **Calculators**: Financial, scientific, health calculators
4. **Configuration Files**: Read and parse settings
5. **Prototyping**: Quickly test ideas before full implementation

---

## Common Mistakes / Pitfalls

| Mistake | Why It Happens | Solution |
|---------|---------------|----------|
| `IndentationError` | Wrong/mixed spaces and tabs | Use 4 spaces consistently |
| `NameError` | Using variable before defining | Define variables before use |
| `TypeError` | Operating on incompatible types | Check types or cast properly |
| `ValueError` | Invalid conversion | Validate input before casting |
| `SyntaxError` | Missing colon, quotes, brackets | Check syntax carefully |

### Common Errors
```python
# Error 1: Division by zero
result = 10 / 0  # ZeroDivisionError

# Error 2: Wrong indentation
if True:
print("Wrong")  # IndentationError

# Error 3: Type mismatch
age = "25"
print(age + 5)  # TypeError - can't add str and int

# Fix: Convert first
print(int(age) + 5)  # 30
```

---

## Best Practices

1. **Use meaningful variable names**
   ```python
   # Bad
   x = 25
   
   # Good
   user_age = 25
   ```

2. **Follow PEP 8 naming conventions**
   - Variables/functions: `snake_case`
   - Constants: `UPPER_CASE`
   - Classes: `PascalCase`

3. **Use f-strings for formatting**
   ```python
   # Good
   print(f"Hello, {name}!")
   
   # Avoid
   print("Hello, " + name + "!")
   ```

4. **Add comments for complex logic**
   ```python
   # Calculate compound interest
   amount = principal * (1 + rate/n) ** (n * time)
   ```

5. **Validate user input**
   ```python
   try:
       age = int(input("Enter age: "))
   except ValueError:
       print("Please enter a valid number")
   ```

---

## Practice Questions

### Question 1 (Easy)
Write a program that takes a user's name and age, then prints a greeting message.

### Question 2 (Easy)
Create variables for length and width of a rectangle. Calculate and print its area and perimeter.

### Question 3 (Medium)
Write a program to swap two variables without using a third variable.

### Question 4 (Medium)
Create a program that converts kilometers to miles (1 km = 0.621371 miles).

### Question 5 (Hard)
Write a program that takes a 3-digit number and prints the sum of its digits.

**Example:** Input: 123 → Output: 6 (1+2+3)

---

## Mini Task / Assignment

### Task: Create a Simple Banking System

Create a Python program that:
1. Takes user's name and initial balance
2. Allows deposit and withdrawal operations
3. Displays final balance with a summary

**Requirements:**
- Use appropriate variable names
- Include comments
- Handle basic input validation
- Format output nicely

**Bonus:** Add interest calculation (5% per year)

---

## Summary

| Concept | Key Point |
|---------|-----------|
| Python | High-level, interpreted, easy to read |
| Variables | No declaration needed, dynamic typing |
| Data Types | int, float, str, bool, list, dict, etc. |
| Type Casting | int(), float(), str() for conversion |
| Input/Output | input() returns string, print() for output |
| Operators | Arithmetic, Comparison, Logical, Assignment |
| Indentation | 4 spaces, mandatory for code blocks |

**Remember**: Python is all about readability and simplicity. Write code that humans can understand!

---

## Next Steps

Move to [02 - Control Flow](../02_Control_Flow/) to learn about conditions and loops.

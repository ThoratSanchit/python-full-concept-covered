# ============================================================
# 01 - Python Basics
# ============================================================
# Run this file: python basics.py
# ============================================================


# ── VARIABLES ───────────────────────────────────────────────
# Variables store data. No need to declare a type — Python figures it out.
name = "Alice"
age = 25
height = 5.7
is_student = True

print(name, age, height, is_student)
print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>


# ── MULTIPLE ASSIGNMENT ─────────────────────────────────────
x, y, z = 1, 2, 3          # Assign multiple variables at once
a = b = c = 0               # Same value to multiple variables
print(x, y, z)
print(a, b, c)


# ── DATA TYPES ──────────────────────────────────────────────
integer_val = 42
float_val   = 3.14
string_val  = "Hello"
bool_val    = True
none_val    = None          # Represents "no value"

print(type(none_val))       # <class 'NoneType'>


# ── TYPE CASTING ────────────────────────────────────────────
# Convert between types when needed
age_str  = "25"
age_int  = int(age_str)     # str → int
num      = 42
num_str  = str(num)         # int → str
x_float  = float(5)         # int → float
y_int    = int(3.9)         # float → int  (truncates, NOT rounds → 3)

print(age_int + 5)          # 30
print(y_int)                # 3


# ── INPUT / OUTPUT ──────────────────────────────────────────
# input() always returns a string — cast if you need a number
# Uncomment to try interactively:
# user_name = input("Enter your name: ")
# print(f"Hello, {user_name}!")

# f-strings are the cleanest way to format output
city = "New York"
temp = 22.5
print(f"{city} temperature: {temp}°C")


# ── ARITHMETIC OPERATORS ────────────────────────────────────
a, b = 10, 3

print(a + b)    # 13  — addition
print(a - b)    # 7   — subtraction
print(a * b)    # 30  — multiplication
print(a / b)    # 3.333... — true division (always float)
print(a // b)   # 3   — floor division (drops decimal)
print(a % b)    # 1   — modulo (remainder)
print(a ** b)   # 1000 — exponentiation


# ── COMPARISON OPERATORS ────────────────────────────────────
# These return True or False
print(10 == 10)   # True
print(10 != 5)    # True
print(10 > 5)     # True
print(10 < 5)     # False
print(10 >= 10)   # True
print(10 <= 9)    # False


# ── LOGICAL OPERATORS ───────────────────────────────────────
print(True and False)   # False — both must be True
print(True or False)    # True  — at least one must be True
print(not True)         # False — flips the value


# ── ASSIGNMENT OPERATORS ────────────────────────────────────
score = 100
score += 10     # score = score + 10  → 110
score -= 5      # score = score - 5   → 105
score *= 2      # score = score * 2   → 210
score //= 3     # score = score // 3  → 70
print(score)


# ── REAL EXAMPLE: BMI CALCULATOR ────────────────────────────
weight = 70     # kg
height = 1.75   # meters

bmi = weight / (height ** 2)
print(f"\nBMI: {bmi:.2f}")   # :.2f = 2 decimal places

# Classify BMI
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"Category: {category}")


# ── PRACTICE ────────────────────────────────────────────────
# Try these yourself:
# 1. Create variables for a rectangle's length and width, print area and perimeter
# 2. Convert 100 kilometers to miles (1 km = 0.621371 miles)
# 3. Swap two variables without using a third variable: x, y = y, x

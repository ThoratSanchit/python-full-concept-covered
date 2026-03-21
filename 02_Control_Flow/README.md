# 02 - Control Flow

## What is Control Flow?

Control flow determines the order in which your code executes. It allows your program to make decisions and repeat actions based on conditions.

**Key Concepts:**
- **Conditional Statements**: Execute code based on conditions (if/else)
- **Loops**: Repeat code multiple times (for/while)
- **Control Keywords**: Modify loop behavior (break/continue/pass)

---

## Deep Explanation

### How Control Flow Works

Python executes code **sequentially** (top to bottom) by default. Control flow statements change this order:

```
Sequential Flow:     Controlled Flow:
    A                    A
    B                   / \
    C              condition?
    D                 /   \
                    True   False
                    /       \
                   B         C
                    \       /
                     \     /
                       D
```

### Truthiness in Python

Values that evaluate to `False`:
- `False`, `None`, `0`, `0.0`, `""`, `[]`, `{}`, `()`

Everything else is `True`.

---

## Conditional Statements

### if Statement

Execute code only if condition is True.

```python
age = 18

if age >= 18:
    print("You are an adult")
```

### if-else Statement

Choose between two paths.

```python
age = 16

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

### if-elif-else Statement

Handle multiple conditions.

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")
```

### Nested Conditions

Conditions inside conditions.

```python
age = 25
has_id = True

if age >= 18:
    if has_id:
        print("You can enter")
    else:
        print("Please show ID")
else:
    print("You are too young")

# Cleaner version using 'and'
if age >= 18 and has_id:
    print("You can enter")
elif age >= 18:
    print("Please show ID")
else:
    print("You are too young")
```

### Ternary Operator (One-liner if-else)

```python
age = 20
status = "adult" if age >= 18 else "minor"
print(status)  # adult
```

---

## Loops

### for Loop

Iterate over a sequence (list, string, range, etc.).

```python
# Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterate over a string
for char in "Hello":
    print(char)

# Using range()
for i in range(5):      # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):   # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8 (step=2)
    print(i)
```

### while Loop

Repeat while condition is True.

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### Loop Control Statements

#### break
Exit the loop immediately.

```python
for i in range(10):
    if i == 5:
        break  # Exit loop when i is 5
    print(i)   # Prints 0, 1, 2, 3, 4
```

#### continue
Skip current iteration, continue to next.

```python
for i in range(5):
    if i == 2:
        continue  # Skip when i is 2
    print(i)      # Prints 0, 1, 3, 4
```

#### pass
Do nothing (placeholder).

```python
for i in range(5):
    if i == 2:
        pass  # TODO: implement later
    print(i)
```

---

## range() Function

Generate a sequence of numbers.

```python
# Syntax: range(start, stop, step)

range(5)        # 0, 1, 2, 3, 4
range(1, 5)     # 1, 2, 3, 4
range(0, 10, 2) # 0, 2, 4, 6, 8
range(10, 0, -1) # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

# Convert to list
numbers = list(range(5))  # [0, 1, 2, 3, 4]
```

---

## Code Examples

### Example 1: Number Guessing Game
```python
import random

secret = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess the number (1-100): "))
    attempts += 1
    
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
```

### Example 2: Multiplication Table
```python
number = int(input("Enter a number: "))

print(f"Multiplication table for {number}:")
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
```

### Example 3: Password Validator
```python
password = input("Enter password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char in "!@#$%^&*":
        has_special = True

if len(password) < 8:
    print("Password must be at least 8 characters")
elif not has_upper:
    print("Password must contain uppercase letter")
elif not has_lower:
    print("Password must contain lowercase letter")
elif not has_digit:
    print("Password must contain a digit")
elif not has_special:
    print("Password must contain special character (!@#$%^&*)")
else:
    print("Password is strong!")
```

### Example 4: FizzBuzz (Classic Interview Question)
```python
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

### Example 5: ATM Simulation
```python
balance = 1000

while True:
    print("\n=== ATM Menu ===")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Enter choice (1-4): ")
    
    if choice == "1":
        print(f"Balance: ${balance}")
    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"Deposited ${amount}")
        else:
            print("Invalid amount")
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds")
        elif amount <= 0:
            print("Invalid amount")
        else:
            balance -= amount
            print(f"Withdrew ${amount}")
    elif choice == "4":
        print("Thank you for using our ATM!")
        break
    else:
        print("Invalid choice")
```

---

## Real-World Use Cases

1. **Form Validation**: Check if user input meets criteria
2. **Game Logic**: Determine win/lose conditions
3. **Data Processing**: Iterate through datasets
4. **Menu Systems**: Handle user choices
5. **Automation**: Repeat tasks until condition met
6. **Search Algorithms**: Find items in collections

---

## Common Mistakes / Pitfalls

| Mistake | Example | Solution |
|---------|---------|----------|
| Infinite loop | `while True:` without break | Always ensure condition becomes False |
| Off-by-one error | `range(1, 10)` vs `range(10)` | Remember: stop is exclusive |
| Modifying list while iterating | `for x in lst: lst.remove(x)` | Iterate over a copy or use list comprehension |
| Indentation errors | Missing colon or wrong indent | Check syntax carefully |
| Using `=` instead of `==` | `if x = 5:` | Use `==` for comparison |

### Common Errors
```python
# Error 1: Infinite loop
count = 0
while count < 5:
    print(count)
    # Forgot: count += 1

# Error 2: Wrong comparison
if x = 5:  # SyntaxError - assignment in condition
    pass

# Error 3: Modifying list during iteration
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Dangerous!

# Fix: Create new list
evens = [n for n in numbers if n % 2 == 0]
```

---

## Best Practices

1. **Use meaningful loop variables**
   ```python
   # Bad
   for x in students:
       print(x)
   
   # Good
   for student in students:
       print(student)
   ```

2. **Avoid deep nesting (max 3 levels)**
   ```python
   # Bad - too nested
   if condition1:
       if condition2:
           if condition3:
               do_something()
   
   # Good - flatten with logical operators
   if condition1 and condition2 and condition3:
       do_something()
   ```

3. **Use `for` loops for known iterations, `while` for unknown**
   ```python
   # Known count - use for
   for i in range(10):
       print(i)
   
   # Unknown count - use while
   while user_input != "quit":
       user_input = input("> ")
   ```

4. **Always handle the `else` case**
   ```python
   if condition:
       do_something()
   else:
       handle_other_case()  # Don't forget this!
   ```

5. **Use `enumerate()` when you need index and value**
   ```python
   fruits = ["apple", "banana", "cherry"]
   for index, fruit in enumerate(fruits):
       print(f"{index}: {fruit}")
   ```

---

## Practice Questions

### Question 1 (Easy)
Write a program that checks if a number is positive, negative, or zero.

### Question 2 (Easy)
Print all even numbers from 1 to 50 using a for loop.

### Question 3 (Medium)
Write a program to calculate the factorial of a number using a while loop.

**Example:** 5! = 5 × 4 × 3 × 2 × 1 = 120

### Question 4 (Medium)
Create a program that prints a pattern:
```
*
**
***
****
*****
```

### Question 5 (Hard)
Write a program to check if a number is prime. A prime number is only divisible by 1 and itself.

**Example:** 2, 3, 5, 7, 11 are prime numbers.

---

## Mini Task / Assignment

### Task: Build a Quiz Game

Create a multiple-choice quiz with the following features:

1. **At least 5 questions** with 4 options each
2. **Scoring system**: +10 for correct, -5 for wrong
3. **Categories**: Easy, Medium, Hard (different point values)
4. **Final report**: Show score, percentage, and grade

**Requirements:**
- Use loops to iterate through questions
- Use conditionals to check answers
- Validate user input (1-4 only)
- Show progress (Question 1/5, etc.)

**Bonus Features:**
- Timer for each question
- Hint system (costs points)
- Save high scores to file
- Different question categories

---

## Summary

| Concept | Syntax | Use Case |
|---------|--------|----------|
| if | `if condition:` | Single condition |
| if-else | `if condition: else:` | Two-way decision |
| if-elif-else | `if...elif...else:` | Multiple conditions |
| for loop | `for item in sequence:` | Iterate known items |
| while loop | `while condition:` | Iterate until condition |
| break | `break` | Exit loop early |
| continue | `continue` | Skip iteration |
| range() | `range(start, stop, step)` | Generate number sequence |

**Key Takeaways:**
- Use `if` for decisions, loops for repetition
- `for` = known iterations, `while` = unknown iterations
- Always ensure loops can terminate
- Keep nesting shallow (max 3 levels)

---

## Next Steps

Move to [03 - Data Structures](../03_Data_Structures/) to learn about lists, tuples, dictionaries, and sets.

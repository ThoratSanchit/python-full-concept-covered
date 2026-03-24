# ============================================================
# 02 - Control Flow
# ============================================================
# Run this file: python control_flow.py
# ============================================================


# ── IF / ELIF / ELSE ────────────────────────────────────────
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"     # This branch runs — score is 85
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Score: {score} → Grade: {grade}")


# ── TERNARY (ONE-LINE IF-ELSE) ──────────────────────────────
# Useful for simple conditions — don't overuse for complex logic
age = 20
status = "adult" if age >= 18 else "minor"
print(status)   # adult


# ── NESTED CONDITIONS ───────────────────────────────────────
age = 25
has_id = True

# Cleaner to use 'and' instead of nesting when possible
if age >= 18 and has_id:
    print("Entry allowed")
elif age >= 18:
    print("Show your ID")
else:
    print("Too young")


# ── FOR LOOP ────────────────────────────────────────────────
# Use 'for' when you know how many times to iterate
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# range(start, stop, step) — stop is EXCLUSIVE
for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i, end=" ")
print()

# Iterate with index using enumerate()
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")


# ── WHILE LOOP ──────────────────────────────────────────────
# Use 'while' when you don't know how many iterations you need
count = 0
while count < 5:
    print(count, end=" ")
    count += 1              # IMPORTANT: always update the condition variable
print()


# ── BREAK — exit the loop early ─────────────────────────────
for i in range(10):
    if i == 5:
        break               # Stop as soon as i hits 5
    print(i, end=" ")
print()                     # Prints: 0 1 2 3 4


# ── CONTINUE — skip current iteration ──────────────────────
for i in range(6):
    if i == 3:
        continue            # Skip 3, keep going
    print(i, end=" ")
print()                     # Prints: 0 1 2 4 5


# ── PASS — placeholder (do nothing) ─────────────────────────
for i in range(3):
    if i == 1:
        pass                # TODO: handle this case later
    print(i)


# ── REAL EXAMPLE 1: FizzBuzz ────────────────────────────────
# Classic interview question — divisible by 3 → Fizz, by 5 → Buzz, both → FizzBuzz
print("\n--- FizzBuzz (1-20) ---")
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
print()


# ── REAL EXAMPLE 2: Multiplication Table ────────────────────
number = 7
print(f"\n--- {number}x Table ---")
for i in range(1, 11):
    print(f"{number} x {i:2} = {number * i}")


# ── REAL EXAMPLE 3: Find First Prime ────────────────────────
def is_prime(n):
    # A prime is only divisible by 1 and itself
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Only check up to √n
        if n % i == 0:
            return False
    return True

print("\n--- Primes up to 30 ---")
primes = [n for n in range(2, 31) if is_prime(n)]
print(primes)


# ── PRACTICE ────────────────────────────────────────────────
# 1. Print all even numbers from 1 to 50
# 2. Calculate factorial of 6 using a while loop (6! = 720)
# 3. Print a right-angle triangle pattern using nested loops:
#    *
#    **
#    ***

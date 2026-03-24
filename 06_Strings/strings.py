# ============================================================
# 06 - Strings
# ============================================================
# Run this file: python strings.py
# ============================================================


# ── CREATING STRINGS ────────────────────────────────────────
single  = 'Hello'
double  = "World"
multi   = """This spans
multiple lines"""

# Raw string — backslashes are treated literally (great for file paths)
path    = r"C:\Users\name\Documents"
print(path)     # C:\Users\name\Documents  (no escape interpretation)


# ── INDEXING AND SLICING ────────────────────────────────────
text = "Python"

print(text[0])      # P  — first character
print(text[-1])     # n  — last character (negative = count from end)
print(text[1:4])    # yth — slice [start:stop] (stop is exclusive)
print(text[::2])    # Pto — every 2nd character
print(text[::-1])   # nohtyP — reversed (step=-1)


# ── STRINGS ARE IMMUTABLE ───────────────────────────────────
# You cannot change a character in place — you must create a new string
s = "hello"
# s[0] = "H"  → TypeError!
s = "H" + s[1:]    # Create a new string instead
print(s)    # Hello


# ── CASE METHODS ────────────────────────────────────────────
s = "hello world"
print(s.upper())        # HELLO WORLD
print(s.lower())        # hello world
print(s.title())        # Hello World  — capitalizes each word
print(s.capitalize())   # Hello world  — only first letter
print(s.swapcase())     # HELLO WORLD → hello world


# ── WHITESPACE METHODS ──────────────────────────────────────
s = "   hello   "
print(s.strip())    # "hello"   — removes both sides
print(s.lstrip())   # "hello   " — removes left only
print(s.rstrip())   # "   hello" — removes right only


# ── SEARCH METHODS ──────────────────────────────────────────
s = "Hello, World!"
print(s.find("World"))      # 7  — index of first match (-1 if not found)
print(s.count("l"))         # 3  — how many times "l" appears
print(s.startswith("Hello"))# True
print(s.endswith("!"))      # True
print("World" in s)         # True — membership test (preferred over find)


# ── REPLACE AND SPLIT ───────────────────────────────────────
s = "I love Python. Python is great."
print(s.replace("Python", "coding"))   # Replace all occurrences

csv_line = "Alice,30,New York,Engineer"
parts = csv_line.split(",")             # Split into list by delimiter
print(parts)    # ['Alice', '30', 'New York', 'Engineer']

# join() is the reverse of split() — combine a list into a string
words = ["Python", "is", "awesome"]
print(" ".join(words))      # Python is awesome
print("-".join(words))      # Python-is-awesome


# ── CHECK METHODS ───────────────────────────────────────────
print("hello".isalpha())    # True  — only letters
print("123".isdigit())      # True  — only digits
print("abc123".isalnum())   # True  — letters and digits
print("  ".isspace())       # True  — only whitespace
print("Hello".islower())    # False
print("HELLO".isupper())    # True


# ── F-STRINGS (RECOMMENDED) ─────────────────────────────────
name  = "Alice"
score = 95.678
items = 1234567

# Basic interpolation
print(f"Name: {name}, Score: {score}")

# Format specifiers
print(f"Score: {score:.2f}")        # 95.68  — 2 decimal places
print(f"Items: {items:,}")          # 1,234,567 — thousands separator
print(f"Hex: {255:#x}")             # 0xff
print(f"Binary: {10:08b}")          # 00001010 — 8-bit binary

# Alignment and padding
print(f"{'left':<10}|")             # left       |
print(f"{'right':>10}|")            # "     right|"
print(f"{'center':^10}|")           # "  center  |"
print(f"{'fill':*^10}|")            # "***fill***|"

# Debug shortcut (Python 3.8+) — prints variable name AND value
x = 42
print(f"{x=}")      # x=42


# ── ESCAPE CHARACTERS ───────────────────────────────────────
print("Line 1\nLine 2")     # \n = newline
print("Col1\tCol2")         # \t = tab
print("She said \"hi\"")    # \" = escaped quote
print("Back\\slash")        # \\ = literal backslash


# ── USEFUL STRING PATTERNS ──────────────────────────────────

# Palindrome check
def is_palindrome(s):
    """Returns True if s reads the same forwards and backwards."""
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

print(is_palindrome("racecar"))                         # True
print(is_palindrome("A man a plan a canal Panama"))     # True
print(is_palindrome("hello"))                           # False


# Count vowels
def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")

print(count_vowels("Hello World"))  # 3


# Truncate long text with ellipsis
def truncate(s, max_len=30):
    """Shorten string to max_len, adding '...' if truncated."""
    return s[:max_len - 3] + "..." if len(s) > max_len else s

print(truncate("This is a very long sentence that needs truncating", 30))


# ── REAL EXAMPLE: Caesar Cipher ─────────────────────────────
def caesar_cipher(text, shift):
    """Encrypt/decrypt text by shifting each letter by 'shift' positions."""
    result = ""
    for char in text:
        if char.isalpha():
            # Determine base: 'A' for uppercase, 'a' for lowercase
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around using modulo 26
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Non-letters stay unchanged
    return result

encrypted = caesar_cipher("Hello, World!", 3)
decrypted = caesar_cipher(encrypted, -3)
print(f"Encrypted: {encrypted}")    # Khoor, Zruog!
print(f"Decrypted: {decrypted}")    # Hello, World!


# ── PRACTICE ────────────────────────────────────────────────
# 1. Check if two strings are anagrams (same letters, different order)
# 2. Count words in a sentence (split on spaces, handle multiple spaces)
# 3. Remove all duplicate characters from "programming" → "progamin"
# 4. Find the longest word in "The quick brown fox jumps"

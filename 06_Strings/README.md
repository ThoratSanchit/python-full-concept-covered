# 06 - Strings

## What are Strings?

Strings are sequences of characters used to represent text. In Python, strings are immutable — once created, they can't be changed.

---

## Creating Strings

```python
single = 'Hello'
double = "World"
triple = """This is a
multi-line string"""

# Raw string (ignores escape characters)
path = r"C:\Users\name\file.txt"

# Byte string
data = b"binary data"
```

---

## String Indexing and Slicing

```python
text = "Python"

# Indexing
text[0]    # 'P'
text[-1]   # 'n'

# Slicing [start:stop:step]
text[0:3]  # 'Pyt'
text[::2]  # 'Pto'
text[::-1] # 'nohtyP' (reverse)
```

---

## String Methods

```python
s = "  Hello, World!  "

# Case
s.upper()          # '  HELLO, WORLD!  '
s.lower()          # '  hello, world!  '
s.title()          # '  Hello, World!  '
s.swapcase()       # '  hELLO, wORLD!  '

# Whitespace
s.strip()          # 'Hello, World!'
s.lstrip()         # 'Hello, World!  '
s.rstrip()         # '  Hello, World!'

# Search
s.find("World")    # 9
s.count("l")       # 3
s.startswith("  Hello")  # True
s.endswith("!  ")        # True

# Replace
s.replace("World", "Python")  # '  Hello, Python!  '

# Split / Join
"a,b,c".split(",")         # ['a', 'b', 'c']
",".join(["a", "b", "c"])  # 'a,b,c'

# Check
"hello".isalpha()   # True
"123".isdigit()     # True
"abc123".isalnum()  # True
"  ".isspace()      # True
```

---

## String Formatting

```python
name = "Alice"
age = 30

# f-strings (recommended, Python 3.6+)
print(f"Name: {name}, Age: {age}")
print(f"Pi is approximately {3.14159:.2f}")
print(f"{'centered':^20}")   # centered with padding

# format()
print("Name: {}, Age: {}".format(name, age))
print("Name: {name}, Age: {age}".format(name=name, age=age))

# % formatting (old style)
print("Name: %s, Age: %d" % (name, age))
```

### f-string Tricks

```python
value = 1234567.89

# Number formatting
f"{value:,.2f}"     # '1,234,567.89'
f"{value:.2e}"      # '1.23e+06'
f"{255:08b}"        # '11111111' (binary)
f"{255:#x}"         # '0xff' (hex)

# Alignment
f"{'left':<10}"     # 'left      '
f"{'right':>10}"    # '     right'
f"{'center':^10}"   # '  center  '
f"{'fill':*^10}"    # '**fill****'

# Debug (Python 3.8+)
x = 42
f"{x=}"             # 'x=42'
```

---

## Escape Characters

```python
print("Line 1\nLine 2")   # newline
print("Tab\there")        # tab
print("Quote: \"hello\"") # escaped quote
print("Backslash: \\")    # backslash
print("\u2764")            # Unicode heart ❤
```

---

## String Operations

```python
# Concatenation
"Hello" + " " + "World"   # 'Hello World'

# Repetition
"ha" * 3                  # 'hahaha'

# Membership
"ell" in "Hello"          # True

# Length
len("Python")             # 6

# Iteration
for char in "abc":
    print(char)
```

---

## Useful String Patterns

```python
# Palindrome check
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

is_palindrome("racecar")  # True
is_palindrome("A man a plan a canal Panama")  # True

# Count vowels
def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")

# Title case without title()
def to_title(s):
    return " ".join(word.capitalize() for word in s.split())

# Truncate with ellipsis
def truncate(s, max_len=50):
    return s[:max_len - 3] + "..." if len(s) > max_len else s
```

---

## Code Examples

### Example 1: Caesar Cipher
```python
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

print(caesar_cipher("Hello, World!", 3))  # Khoor, Zruog!
print(caesar_cipher("Khoor, Zruog!", -3)) # Hello, World!
```

### Example 2: Word Frequency
```python
def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        word = word.strip(".,!?")
        freq[word] = freq.get(word, 0) + 1
    return sorted(freq.items(), key=lambda x: x[1], reverse=True)

text = "the quick brown fox jumps over the lazy dog the fox"
print(word_frequency(text))
```

### Example 3: Email Validator (basic)
```python
def is_valid_email(email):
    if "@" not in email:
        return False
    parts = email.split("@")
    if len(parts) != 2:
        return False
    local, domain = parts
    if not local or not domain:
        return False
    if "." not in domain:
        return False
    return True
```

---

## Practice Questions

1. Reverse a string without using `[::-1]`
2. Check if two strings are anagrams
3. Count the number of words in a sentence
4. Remove all duplicate characters from a string
5. Find the longest word in a sentence

---

## Mini Task

Build a text analyzer that takes a paragraph and outputs:
- Word count
- Character count (with and without spaces)
- Most frequent word
- Average word length
- Number of sentences

---

## Summary

| Method | Purpose |
|--------|---------|
| `upper/lower` | Change case |
| `strip` | Remove whitespace |
| `split/join` | Split/join strings |
| `find/replace` | Search and replace |
| `format/f-string` | String formatting |
| `startswith/endswith` | Check prefix/suffix |

---

## Next Steps

Move to [07 - Modules and Packages](../07_Modules_and_Packages/) to learn how to organize and reuse code.

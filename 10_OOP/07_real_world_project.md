# 07 - Real World Project: Library Management System

This project uses **all 4 OOP pillars** together in one realistic system.

---

## What We're Building

A library system where:
- Books can be added and searched
- Members can borrow and return books
- Fines are calculated for late returns
- All OOP concepts are applied naturally

---

## Design Overview

```
LibraryItem (Abstract)
├── Book
└── Magazine

Person (Abstract)
├── Member
└── Librarian

Library
└── manages Books, Members, Borrowing records
```

---

## The Code

```python
from abc import ABC, abstractmethod
from datetime import date, timedelta
from typing import List, Optional


# ─── ABSTRACTION ──────────────────────────────────────────────

class LibraryItem(ABC):
    """Abstract base for anything that can be borrowed"""

    def __init__(self, item_id: str, title: str, year: int):
        self.item_id = item_id
        self.title = title
        self.year = year
        self._available = True

    @property
    @abstractmethod
    def item_type(self) -> str:
        pass

    @property
    @abstractmethod
    def borrow_duration_days(self) -> int:
        pass

    # ENCAPSULATION — availability controlled via property
    @property
    def available(self) -> bool:
        return self._available

    def checkout(self):
        if not self._available:
            raise ValueError(f'"{self.title}" is already checked out')
        self._available = False

    def checkin(self):
        self._available = True

    def __str__(self):
        status = "Available" if self._available else "Checked out"
        return f"[{self.item_type}] {self.title} ({self.year}) — {status}"

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.item_id!r}, title={self.title!r})"


# ─── INHERITANCE ──────────────────────────────────────────────

class Book(LibraryItem):
    def __init__(self, item_id, title, author, year, isbn):
        super().__init__(item_id, title, year)
        self.author = author
        self.isbn = isbn

    @property
    def item_type(self):
        return "Book"

    @property
    def borrow_duration_days(self):
        return 14  # 2 weeks

    def __str__(self):
        return f"{super().__str__()} | by {self.author}"


class Magazine(LibraryItem):
    def __init__(self, item_id, title, issue, year):
        super().__init__(item_id, title, year)
        self.issue = issue

    @property
    def item_type(self):
        return "Magazine"

    @property
    def borrow_duration_days(self):
        return 7  # 1 week

    def __str__(self):
        return f"{super().__str__()} | Issue #{self.issue}"


# ─── ENCAPSULATION ────────────────────────────────────────────

class BorrowRecord:
    FINE_PER_DAY = 0.50

    def __init__(self, member_id: str, item: LibraryItem):
        self.member_id = member_id
        self.item = item
        self.borrow_date = date.today()
        self.due_date = date.today() + timedelta(days=item.borrow_duration_days)
        self._return_date: Optional[date] = None

    @property
    def is_returned(self) -> bool:
        return self._return_date is not None

    @property
    def fine(self) -> float:
        if not self.is_returned:
            overdue = (date.today() - self.due_date).days
        else:
            overdue = (self._return_date - self.due_date).days
        return max(0, overdue * self.FINE_PER_DAY)

    def complete_return(self):
        self._return_date = date.today()
        self.item.checkin()

    def __str__(self):
        status = f"Returned {self._return_date}" if self.is_returned else f"Due {self.due_date}"
        fine_str = f" | Fine: ${self.fine:.2f}" if self.fine > 0 else ""
        return f"{self.item.title} — {status}{fine_str}"


# ─── INHERITANCE + POLYMORPHISM ───────────────────────────────

class Person(ABC):
    def __init__(self, person_id: str, name: str, email: str):
        self.person_id = person_id
        self.name = name
        self._email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email")
        self._email = value

    @abstractmethod
    def role(self) -> str:
        pass

    def __str__(self):
        return f"{self.role()}: {self.name} <{self._email}>"


class Member(Person):
    MAX_BORROWS = 5

    def __init__(self, person_id, name, email):
        super().__init__(person_id, name, email)
        self._records: List[BorrowRecord] = []

    def role(self):
        return "Member"

    @property
    def active_borrows(self) -> List[BorrowRecord]:
        return [r for r in self._records if not r.is_returned]

    @property
    def total_fine(self) -> float:
        return sum(r.fine for r in self._records)

    def can_borrow(self) -> bool:
        return len(self.active_borrows) < self.MAX_BORROWS

    def borrow(self, item: LibraryItem) -> BorrowRecord:
        if not self.can_borrow():
            raise ValueError(f"Borrow limit ({self.MAX_BORROWS}) reached")
        item.checkout()
        record = BorrowRecord(self.person_id, item)
        self._records.append(record)
        return record

    def return_item(self, item: LibraryItem) -> BorrowRecord:
        for record in self.active_borrows:
            if record.item == item:
                record.complete_return()
                return record
        raise ValueError(f"No active borrow found for '{item.title}'")

    def borrow_history(self):
        for r in self._records:
            print(f"  {r}")


class Librarian(Person):
    def __init__(self, person_id, name, email, employee_id):
        super().__init__(person_id, name, email)
        self.employee_id = employee_id

    def role(self):
        return "Librarian"


# ─── MAGIC METHODS ────────────────────────────────────────────

class Library:
    def __init__(self, name: str):
        self.name = name
        self._items: List[LibraryItem] = []
        self._members: List[Member] = []

    def add_item(self, item: LibraryItem):
        self._items.append(item)

    def register_member(self, member: Member):
        self._members.append(member)

    def search(self, query: str) -> List[LibraryItem]:
        query = query.lower()
        return [item for item in self._items
                if query in item.title.lower()
                or (isinstance(item, Book) and query in item.author.lower())]

    def available_items(self) -> List[LibraryItem]:
        return [item for item in self._items if item.available]

    # Magic methods
    def __len__(self):
        return len(self._items)

    def __contains__(self, item):
        return item in self._items

    def __str__(self):
        return f"Library '{self.name}' | {len(self)} items | {len(self._members)} members"

    def __repr__(self):
        return f"Library(name={self.name!r})"
```

---

## Using the System

```python
# Setup
library = Library("City Public Library")

# Add items
b1 = Book("B001", "Python Crash Course", "Eric Matthes", 2019, "978-1593279288")
b2 = Book("B002", "Clean Code", "Robert Martin", 2008, "978-0132350884")
b3 = Book("B003", "The Pragmatic Programmer", "David Thomas", 2019, "978-0135957059")
m1 = Magazine("M001", "Python Weekly", 42, 2024)

for item in [b1, b2, b3, m1]:
    library.add_item(item)

# Register members
alice = Member("M001", "Alice Johnson", "alice@example.com")
bob = Member("M002", "Bob Smith", "bob@example.com")

library.register_member(alice)
library.register_member(bob)

print(library)
# Library 'City Public Library' | 4 items | 2 members

# Borrow
record = alice.borrow(b1)
print(f"Due: {record.due_date}")
print(b1)  # [Book] Python Crash Course (2019) — Checked out | by Eric Matthes

# Search
results = library.search("python")
for r in results:
    print(r)

# Return
returned = alice.return_item(b1)
print(f"Fine: ${returned.fine:.2f}")

# Borrow history
print(f"\n{alice.name}'s history:")
alice.borrow_history()

# Magic methods
print(len(library))          # 4
print(b2 in library)         # True
print(library.available_items())
```

---

## OOP Concepts Used

| Concept | Where |
|---------|-------|
| Abstraction | `LibraryItem`, `Person` are abstract |
| Encapsulation | `_available`, `_email`, `_records` with properties |
| Inheritance | `Book`/`Magazine` from `LibraryItem`, `Member`/`Librarian` from `Person` |
| Polymorphism | `item_type`, `borrow_duration_days`, `role()` differ per subclass |
| Magic methods | `__len__`, `__contains__`, `__str__`, `__repr__` on `Library` |

---

## Extension Ideas

1. Add a `Reservation` system for unavailable books
2. Implement `__iter__` on `Library` to loop over items
3. Add `save_to_json()` / `load_from_json()` for persistence
4. Create a `Librarian` method to generate overdue reports
5. Add a `Genre` enum and filter search by genre

---

Previous → [06 - Magic Methods](./06_magic_methods.md) | Back to [OOP Overview](./README.md)

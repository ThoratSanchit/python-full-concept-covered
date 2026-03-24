# ============================================================
# 10 OOP — 07: Real World Project — Library Management System
# ============================================================
# Run this file: python 07_real_world_project.py
#
# Concepts used:
#   Abstraction   — LibraryItem and Person are abstract base classes
#   Encapsulation — private attributes with @property validation
#   Inheritance   — Book/Magazine from LibraryItem, Member/Librarian from Person
#   Polymorphism  — item_type, borrow_duration_days, role() differ per subclass
#   Magic methods — __len__, __contains__, __str__, __repr__ on Library
# ============================================================

from abc import ABC, abstractmethod
from datetime import date, timedelta
from typing import List, Optional


# ── ABSTRACTION: LibraryItem ────────────────────────────────
class LibraryItem(ABC):
    """Abstract base for anything that can be borrowed from the library."""

    def __init__(self, item_id: str, title: str, year: int):
        self.item_id   = item_id
        self.title     = title
        self.year      = year
        self._available = True  # Protected — use property below

    @property
    @abstractmethod
    def item_type(self) -> str:
        """Subclass must declare what type of item this is."""
        pass

    @property
    @abstractmethod
    def borrow_duration_days(self) -> int:
        """Subclass must declare how long it can be borrowed."""
        pass

    # ENCAPSULATION: availability controlled via property
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


# ── INHERITANCE: Book and Magazine ──────────────────────────
class Book(LibraryItem):
    def __init__(self, item_id, title, author, year, isbn):
        super().__init__(item_id, title, year)
        self.author = author
        self.isbn   = isbn

    @property
    def item_type(self):
        return "Book"   # POLYMORPHISM: each subclass returns its own type

    @property
    def borrow_duration_days(self):
        return 14       # Books: 2 weeks

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
        return 7        # Magazines: 1 week

    def __str__(self):
        return f"{super().__str__()} | Issue #{self.issue}"


# ── ENCAPSULATION: BorrowRecord ─────────────────────────────
class BorrowRecord:
    FINE_PER_DAY = 0.50     # $0.50 per day overdue

    def __init__(self, member_id: str, item: LibraryItem):
        self.member_id  = member_id
        self.item       = item
        self.borrow_date = date.today()
        # Due date depends on the item type — polymorphism at work
        self.due_date   = date.today() + timedelta(days=item.borrow_duration_days)
        self._return_date: Optional[date] = None   # None until returned

    @property
    def is_returned(self) -> bool:
        return self._return_date is not None

    @property
    def fine(self) -> float:
        """Calculate overdue fine. 0 if returned on time."""
        check_date = self._return_date if self.is_returned else date.today()
        overdue_days = (check_date - self.due_date).days
        return max(0.0, overdue_days * self.FINE_PER_DAY)

    def complete_return(self):
        """Mark item as returned and update availability."""
        self._return_date = date.today()
        self.item.checkin()

    def __str__(self):
        status   = f"Returned {self._return_date}" if self.is_returned else f"Due {self.due_date}"
        fine_str = f" | Fine: ${self.fine:.2f}" if self.fine > 0 else ""
        return f"{self.item.title} — {status}{fine_str}"


# ── ABSTRACTION: Person ─────────────────────────────────────
class Person(ABC):
    def __init__(self, person_id: str, name: str, email: str):
        self.person_id = person_id
        self.name      = name
        self.email     = email  # Goes through setter

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        # Basic validation — real apps would use regex
        if "@" not in value or "." not in value.split("@")[-1]:
            raise ValueError(f"Invalid email: {value}")
        self._email = value

    @abstractmethod
    def role(self) -> str:
        """Subclass must declare the person's role."""
        pass

    def __str__(self):
        return f"{self.role()}: {self.name} <{self._email}>"


# ── INHERITANCE: Member and Librarian ───────────────────────
class Member(Person):
    MAX_BORROWS = 5     # Maximum items a member can borrow at once

    def __init__(self, person_id, name, email):
        super().__init__(person_id, name, email)
        self._records: List[BorrowRecord] = []

    def role(self):
        return "Member"     # POLYMORPHISM

    @property
    def active_borrows(self) -> List[BorrowRecord]:
        """Items currently borrowed (not yet returned)."""
        return [r for r in self._records if not r.is_returned]

    @property
    def total_fine(self) -> float:
        return sum(r.fine for r in self._records)

    def can_borrow(self) -> bool:
        return len(self.active_borrows) < self.MAX_BORROWS

    def borrow(self, item: LibraryItem) -> BorrowRecord:
        if not self.can_borrow():
            raise ValueError(f"Borrow limit ({self.MAX_BORROWS}) reached")
        item.checkout()     # Marks item as unavailable
        record = BorrowRecord(self.person_id, item)
        self._records.append(record)
        return record

    def return_item(self, item: LibraryItem) -> BorrowRecord:
        for record in self.active_borrows:
            if record.item == item:
                record.complete_return()    # Marks item as available again
                return record
        raise ValueError(f"No active borrow found for '{item.title}'")

    def print_history(self):
        print(f"\n{self.name}'s borrow history:")
        for r in self._records:
            print(f"  {r}")


class Librarian(Person):
    def __init__(self, person_id, name, email, employee_id):
        super().__init__(person_id, name, email)
        self.employee_id = employee_id

    def role(self):
        return "Librarian"  # POLYMORPHISM


# ── MAGIC METHODS: Library ──────────────────────────────────
class Library:
    def __init__(self, name: str):
        self.name     = name
        self._items:   List[LibraryItem] = []
        self._members: List[Member]      = []

    def add_item(self, item: LibraryItem):
        self._items.append(item)

    def register_member(self, member: Member):
        self._members.append(member)

    def search(self, query: str) -> List[LibraryItem]:
        """Search by title or author (case-insensitive)."""
        q = query.lower()
        return [item for item in self._items
                if q in item.title.lower()
                or (isinstance(item, Book) and q in item.author.lower())]

    def available_items(self) -> List[LibraryItem]:
        return [item for item in self._items if item.available]

    def __len__(self):
        # len(library) → total number of items
        return len(self._items)

    def __contains__(self, item):
        # 'book in library' → True/False
        return item in self._items

    def __str__(self):
        return f"Library '{self.name}' | {len(self)} items | {len(self._members)} members"

    def __repr__(self):
        return f"Library(name={self.name!r})"


# ── DEMO ────────────────────────────────────────────────────
if __name__ == "__main__":
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
    bob   = Member("M002", "Bob Smith",     "bob@example.com")
    library.register_member(alice)
    library.register_member(bob)

    print(library)      # Library 'City Public Library' | 4 items | 2 members
    print()

    # Borrow
    record = alice.borrow(b1)
    print(f"Alice borrowed: {b1.title}")
    print(f"Due date: {record.due_date}")
    print(b1)           # Shows "Checked out"
    print()

    # Search
    print("Search 'python':")
    for result in library.search("python"):
        print(f"  {result}")
    print()

    # Return
    returned = alice.return_item(b1)
    print(f"Alice returned: {b1.title}")
    print(f"Fine: ${returned.fine:.2f}")
    print(b1)           # Shows "Available" again
    print()

    # Borrow history
    alice.print_history()

    # Magic methods
    print(f"\nTotal items in library: {len(library)}")
    print(f"Is b2 in library? {b2 in library}")
    print(f"Available items: {len(library.available_items())}")

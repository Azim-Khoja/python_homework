# 1. Circle Class
# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


# Foydalanuvchidan radiusni olish
r = float(input("Doiraning radiusini kiriting: "))

circle = Circle(r)
print(f"Doira yuzi: {circle.area():.2f}")
print(f"Doira aylana uzunligi: {circle.perimeter():.2f}")

# 2. Person Class
# Write a Python program to create a Person class. Include attributes like name, country, and date of birth. Implement a method to determine the person's age.

class Person:
    def __init__(self, name, gender, country, birth_date, is_married):
        self.name = name
        self._gender = gender
        self.country = country
        self.birth_date = birth_date
        self._is_married = is_married

    def get_gender(self):
        if self._gender:
            return f"he"
        else:
            return f"she"

    def get_name(self):
        return self.name

    def get_country(self):
        return self.country

    def get_birth_date(self):
        return self.birth_date

    def is_married_status(self):
        if self._is_married:
            return f"is married."
        else:
            return f"is not married."

    def get_info(self):
        return (f"{self.name} was born in the year {self.birth_date} in the country {self.country}. "
                f"{self.get_gender().title()} {self.is_married_status()}")


Jack = Person("Jack", True, "USA", "05-10-1994", True)
Amelia = Person("Amelia", False, "Netherlands", "12-01-1998", False)
print(Jack.get_info())
print(Amelia.get_info())

# 3. Calculator Class
# Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.

class Calculator:
    def __repr__(self):
        return f"This is a program for performing arithmetic operations"

    def add(self, x, y):
        """This function adds y to x"""
        result = x + y
        return f"{x} + {y} = {result}"

    def subtract(self, x, y):
        """This function subtracts y from x"""
        result = x - y
        return f"{x} - {y} = {result}"

    def multiple(self, x, y):
        """This function multiplies x by y"""
        result = x * y
        return f"{x} x {y} = {result}"

    def division(self, x, y):
        """This function divides x by x"""
        try:
            result = x / y
            return f"{x} ÷ {y} = {result}"
        except ZeroDivisionError:
            return f"Error: You cannot be divided by 0!"


calc = Calculator()
print(calc.add(5, 4))
print(calc.subtract(-4, 10))
print(calc.multiple(0, 4))
print(calc.division(10, 0))

# 4. Shape and Subclasses
# Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like Circle, Triangle, and Square.

import math

# Bazaviy klass
class Shape:
    def area(self):
        raise NotImplementedError("Area method must be implemented by subclass")

    def perimeter(self):
        raise NotImplementedError("Perimeter method must be implemented by subclass")


# Doira klassi
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Kvadrat klassi
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


# Uchburchak klassi (uchta tomoni berilgan)
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2  # yarim perimetr
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))  # Geron formulasi

    def perimeter(self):
        return self.a + self.b + self.c


# --- Test qismi ---
circle = Circle(5)
square = Square(4)
triangle = Triangle(3, 4, 5)

print("CIRCLE:")
print(f"  Area: {circle.area():.2f}")
print(f"  Perimeter: {circle.perimeter():.2f}")

print("\nSQUARE:")
print(f"  Area: {square.area():.2f}")
print(f"  Perimeter: {square.perimeter():.2f}")

print("\nTRIANGLE:")
print(f"  Area: {triangle.area():.2f}")
print(f"  Perimeter: {triangle.perimeter():.2f}")


# 5. Binary Search Tree Class
# Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Yangi tugun qo‘shish"""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(current_node.right, value)
        else:
            print(f"{value} qiymati allaqachon mavjud (dublikat kiritilmaydi).")

    def search(self, value):
        """Qiymatni qidirish"""
        return self._search(self.root, value)

    def _search(self, current_node, value):
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        elif value < current_node.value:
            return self._search(current_node.left, value)
        else:
            return self._search(current_node.right, value)

    def inorder(self):
        """Daraxtni tartib bilan (chap - ildiz - o‘ng) chiqarish"""
        return self._inorder(self.root)

    def _inorder(self, node):
        elements = []
        if node:
            elements += self._inorder(node.left)
            elements.append(node.value)
            elements += self._inorder(node.right)
        return elements


# --- Test qismi ---
bst = BinarySearchTree()
values = [50, 30, 70, 20, 40, 60, 80]
for v in values:
    bst.insert(v)

print("Inorder traversal:", bst.inorder())

# Qidiruv testlari
print("60 mavjudmi?", bst.search(60))
print("25 mavjudmi?", bst.search(25))


# 6. Stack Data Structure
# Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Stack bo‘shligini tekshiradi"""
        return len(self.items) == 0

    def push(self, item):
        """Elementni stackning ustiga qo‘shadi"""
        self.items.append(item)
        print(f"{item} stackka qo‘shildi.")

    def pop(self):
        """Eng yuqoridagi elementni stackdan oladi"""
        if self.is_empty():
            return "Stack bo‘sh, element yo‘q."
        removed = self.items.pop()
        return f"{removed} stackdan olindi."

    def peek(self):
        """Stackning eng yuqori elementini qaytaradi"""
        if self.is_empty():
            return "Stack bo‘sh."
        return self.items[-1]

    def size(self):
        """Stackdagi elementlar sonini qaytaradi"""
        return len(self.items)


# --- Test qismi ---
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Eng yuqoridagi element:", stack.peek())
print(stack.pop())
print("Hozirgi stack:", stack.items)
print("Stack hajmi:", stack.size())


# 7. Linked List Data Structure
# Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting, and deleting nodes.

class Node:
    """Har bir tugun (node) qiymat va keyingi tugunga ishorani saqlaydi"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Linked list ma'lumot tuzilmasi"""
    def __init__(self):
        self.head = None

    def display(self):
        """Bog‘langan ro‘yxatdagi barcha qiymatlarni chiqaradi"""
        if self.head is None:
            print("Linked list bo‘sh.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert(self, data):
        """Yangi tugunni ro‘yxat oxiriga qo‘shadi"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, key):
        """Berilgan qiymatli tugunni o‘chiradi"""
        current = self.head

        # Agar bosh tugun o‘chirilsa
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            print(f"{key} qiymati topilmadi.")
            return

        prev.next = current.next
        current = None


# --- Test qismi ---
ll = LinkedList()

# Tugunlar qo‘shish
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)

print("Boshlang‘ich linked list:")
ll.display()

# Tugun o‘chirish
ll.delete(20)
print("\n20 o‘chirildi:")
ll.display()

# Tugun o‘chirish (mavjud bo‘lmagan)
ll.delete(100)

# Yangi tugun qo‘shish
ll.insert(50)
print("\n50 qo‘shildi:")
ll.display()


# 8. Shopping Cart Class
# Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.

class ShoppingCart:
    def __init__(self):
        # Cart will store items as a dictionary: {item_name: (price, quantity)}
        self.cart = {}

    def add_item(self, item_name, price, quantity=1):
        """Add an item to the cart or update quantity if it already exists."""
        if item_name in self.cart:
            old_quantity = self.cart[item_name][1]
            self.cart[item_name] = (price, old_quantity + quantity)
        else:
            self.cart[item_name] = (price, quantity)
        print(f"{quantity} x '{item_name}' added to cart.")

    def remove_item(self, item_name, quantity=1):
        """Remove an item or decrease its quantity."""
        if item_name in self.cart:
            price, current_quantity = self.cart[item_name]
            if quantity >= current_quantity:
                del self.cart[item_name]
                print(f"'{item_name}' removed from cart.")
            else:
                self.cart[item_name] = (price, current_quantity - quantity)
                print(f"{quantity} x '{item_name}' removed from cart.")
        else:
            print(f"'{item_name}' not found in cart.")

    def calculate_total(self):
        """Calculate the total cost of all items in the cart."""
        total = sum(price * quantity for price, quantity in self.cart.values())
        return total

    def display_cart(self):
        """Display all items in the cart with prices and quantities."""
        if not self.cart:
            print("🛒 Your cart is empty.")
            return
        print("\n--- Shopping Cart ---")
        for item, (price, quantity) in self.cart.items():
            print(f"{item}: ${price:.2f} x {quantity} = ${price * quantity:.2f}")
        print("---------------------")
        print(f"Total: ${self.calculate_total():.2f}")
        print("---------------------\n")


# --- Example usage ---
cart = ShoppingCart()

cart.add_item("Apple", 1.5, 4)
cart.add_item("Banana", 0.8, 6)
cart.add_item("Milk", 2.0, 2)

cart.display_cart()

cart.remove_item("Banana", 3)
cart.display_cart()

cart.remove_item("Milk", 2)
cart.display_cart()


# 9. Stack with Display
# Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping, and displaying elements

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Add an element to the top of the stack"""
        self.stack.append(item)
        print(f"'{item}' pushed to stack.")

    def pop(self):
        """Remove and return the top element of the stack"""
        if not self.is_empty():
            removed_item = self.stack.pop()
            print(f"'{removed_item}' popped from stack.")
        else:
            print("Stack is empty! Nothing to pop.")

    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.stack) == 0

    def display(self):
        """Display all elements in the stack"""
        if self.is_empty():
            print("Stack is empty!")
        else:
            print("\nCurrent Stack:")
            for item in reversed(self.stack):
                print(item)
            print("---------------")


# --- Example usage ---
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()

stack.pop()
stack.display()

stack.pop()
stack.pop()
stack.pop()  # Extra pop to test empty stack


# 10. Queue Data Structure
# Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """Add an element to the end of the queue"""
        self.queue.append(item)
        print(f"'{item}' added to queue.")

    def dequeue(self):
        """Remove and return the first element from the queue"""
        if not self.is_empty():
            removed_item = self.queue.pop(0)
            print(f"'{removed_item}' removed from queue.")
        else:
            print("Queue is empty! Nothing to dequeue.")

    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.queue) == 0

    def display(self):
        """Display all elements in the queue"""
        if self.is_empty():
            print("Queue is empty!")
        else:
            print("\nCurrent Queue:")
            for item in self.queue:
                print(item)
            print("---------------")


# --- Example usage ---
queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

queue.display()

queue.dequeue()
queue.display()

queue.dequeue()
queue.dequeue()
queue.dequeue()  # Test empty queue


# 11. Bank Class
# Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.

class BankAccount:
    def __init__(self, account_number, owner_name, balance=0.0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        """Add money to the account"""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount <= 0:
            print("Withdrawal amount must be positive!")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def get_balance(self):
        """Return the current balance"""
        return f"Current balance for {self.owner_name}: ${self.balance:.2f}"

    def __repr__(self):
        return f"Account({self.account_number}, Owner: {self.owner_name}, Balance: ${self.balance:.2f})"


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, account_number, owner_name, initial_balance=0.0):
        """Create a new bank account"""
        if account_number in self.accounts:
            print("Account number already exists!")
        else:
            account = BankAccount(account_number, owner_name, initial_balance)
            self.accounts[account_number] = account
            print(f"Account created for {owner_name} with number {account_number}.")

    def get_account(self, account_number):
        """Retrieve account by number"""
        return self.accounts.get(account_number, None)

    def show_all_accounts(self):
        """Display all accounts in the bank"""
        if not self.accounts:
            print("No accounts in the bank yet.")
        else:
            print(f"\nList of all accounts in {self.name}:")
            for acc in self.accounts.values():
                print(acc)


# --- Example usage ---
bank = Bank("Python Bank")

bank.create_account(1001, "Azim", 500)
bank.create_account(1002, "Sasha", 1000)

acc1 = bank.get_account(1001)
acc2 = bank.get_account(1002)

acc1.deposit(200)
acc1.withdraw(100)
print(acc1.get_balance())

acc2.withdraw(1500)  # will show insufficient balance
acc2.deposit(400)

bank.show_all_accounts()

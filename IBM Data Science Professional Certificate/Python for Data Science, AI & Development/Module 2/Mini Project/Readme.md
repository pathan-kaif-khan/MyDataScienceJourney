# ☕ Cafe Ordering System

A simple Python-based cafe ordering system designed to practice and demonstrate core Python data structures and concepts.

## 📌 Overview

This project simulates a basic cafe system that manages menu items, inventory, customer orders, and daily customers. It uses Python's built-in **lists, tuples, dictionaries, and sets** to organize and process data.

## 🚀 Features

- 📋 Store cafe menu items and prices using tuples and lists
- 📦 Track inventory using dictionaries
- 🛒 Manage customer orders using a list-based order queue
- 👥 Track unique daily customers using a set
- 💰 Calculate total daily revenue from customer orders
- 🔄 Convert menu data from a list of tuples into a dictionary for faster price lookup

## 🧠 Python Concepts Practiced

- Lists
- Tuples
- Dictionaries
- Sets
- `for` loops
- `if` statements
- Dictionary key/value access
- List methods such as `append()`
- Set methods such as `add()`
- Type conversion using `dict()`
- Basic arithmetic and data processing

## 💻 Example

```python
menu = [
    ("espresso", 2.99),
    ("cappuccino", 2.50),
    ("latte", 1.99)
]

menu_dict = dict(menu)

order_queue = ["espresso", "latte", "cappuccino"]

total_revenue = 0

for order in order_queue:
    total_revenue += menu_dict[order]

print(total_revenue)

# 🛒 Python Order Management System

A beginner-friendly Python project created as part of **GenAI Assignment 2**. This project demonstrates the use of Python fundamentals including conditional statements, loops, lists, user input, `break`, and `continue`.

---

## 📌 Project Overview

This project simulates a simple order management system where discounts are applied based on order amount. It also includes processing multiple orders, a menu-driven application, and loop control using `break` and `continue`.

---

# 📋 Tasks Completed

## ✅ Task 1: Discount Calculator (if-elif-else)

### Objective
Calculate the discount on a customer's order based on predefined rules.

### Discount Rules

| Order Amount | Discount |
|--------------|-----------|
| ₹3000 and above | 20% |
| ₹2000 – ₹2999 | 15% |
| ₹1000 – ₹1999 | 10% |
| Below ₹1000 | 0% |

### Features
- Accepts user input.
- Converts input into a numeric value.
- Handles invalid (non-numeric) input using exception handling.
- Calculates discount amount.
- Displays the final payable amount.
- *(Optional)* Calculates 5% tax after discount.

### Python Concepts Used
- Variables
- Input/Output
- Type Casting
- if-elif-else
- Arithmetic Operators
- Exception Handling (`try-except`)

---

## ✅ Task 2: Process Multiple Orders (for loop)

### Objective
Apply discount rules to multiple orders using a `for` loop.

### Given Orders

```python
orders = [1200, 2500, 800, 1750, 3000]
```

### Features
- Applies discounts to every order.
- Prints a summary table.
- Calculates total revenue after discounts.
- Counts how many orders received discounts.

### Output Includes
- Order Amount
- Discount Percentage
- Final Amount
- Total Revenue
- Number of Discounted Orders

### Python Concepts Used
- Lists
- for Loop
- Conditional Statements
- Accumulator Variables

---

## ✅ Task 3: User Menu (while loop + break + continue)

### Objective
Create a menu-driven program using a `while` loop.

### Menu Options

```
1 → Add Order
2 → Show Orders & Totals
q → Quit
```

### Features
- Add new order amounts.
- Display all orders after discount calculation.
- Calculate total revenue.
- Uses `continue` for invalid choices.
- Uses `break` to exit the program.

### Python Concepts Used
- while Loop
- Lists
- User Input
- break
- continue
- Conditional Statements

---

## ✅ Task 4: Loop Control (break & continue)

### Objective

Process daily sales while demonstrating loop control statements.

### Given Data

```python
daily = [200, 150, 0, 400, 50, -1, 300]
```

### Rules
- If value is **-1**
  - Treat as corrupted data.
  - Stop processing using `break`.

- If value is **0**
  - Treat as no sales.
  - Skip using `continue`.

- Otherwise
  - Add sale to total.
  - Display running total.

### Output Includes
- Running Total
- Final Total Sales

### Python Concepts Used
- for Loop
- break
- continue
- Lists
- Conditional Statements

---

# 🛠️ Technologies Used

- Python 3
- VS Code

---

# 📂 Project Structure

```
GenAI-Assignment-2/
│
├── task1_discount_calculator.py
├── task2_multiple_orders.py
├── task3_user_menu.py
├── task5_loop_control.py
└── README.md
```

---

# 🎯 Learning Outcomes

By completing this assignment, I learned:

- Working with variables and user input
- Conditional statements (`if-elif-else`)
- Using lists
- Iterating with `for` and `while` loops
- Menu-driven programming
- Using `break` and `continue`
- Exception handling
- Writing clean and structured Python code

---


# 👩‍💻 Author

**Tanu Patel**

- BE Computer Science Engineering Student
- Learning Python, AI/ML and GenAI

---

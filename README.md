# 🧾 ABCInventory

**ABCInventory** is a **command-line inventory management system** built specifically for **ABC Traders**. Designed to run in a terminal environment, it provides a lightweight yet powerful solution to manage product stock, user access, and inventory data without relying on complex databases or graphical interfaces.

---

## 📋 Overview

ABCInventory empowers small businesses to:

- Maintain a clean, searchable inventory
- Securely manage multiple user accounts
- Track stock levels and inventory value
- Present data in a clear and visually enhanced terminal interface

This project is ideal for those who want a **simple**, **secure**, and **portable** inventory tool with zero external server dependencies.

---

## ✅ Key Features

### 📦 Inventory Management
- Add new items with name, quantity, price, and description
- Update or remove existing products
- View complete inventory in table format
- Low-stock alerts and filters (optional)

### 👤 User Management
- Create, update, or delete user accounts
- Assign roles (e.g., admin, staff) with permission levels
- Authenticate users via terminal login

### 🧮 Reporting
- Display total inventory value (e.g., total cost or retail price)
- Generate itemized summaries
- Styled tables for quick readability using the `tabulate` library

---

## 🔐 Security

ABCInventory prioritizes **user data protection** and **access control** with the following measures:

### 🔑 Password Protection
- All user passwords are **hashed with bcrypt**
- No plain-text passwords are stored

### 🔍 Authentication & Validation
- Passwords are validated securely with hash comparisons during login and password changes
- Strong password enforcement (optional feature)

### 🛡️ Registration Key
- Only users with a valid **secret registration key** can create new accounts
- Prevents unauthorized signups

---

## 🛠️ Tech Stack

| Tech                      | Purpose                                      |
|---------------------------|----------------------------------------------|
| 🐍 Python 3               | Core programming language                    |
| 🔐 bcrypt                 | Password hashing and verification            |
| 📁 Text Files             | Lightweight file-based "database" storage    |
| 📊 tabulate               | Stylish table generation for inventory views |
| 🎨 colorama & termcolor   | Styled, color-coded terminal output          |

---

## 🚀 Setup & Usage

```bash
# Clone the repository
git clone https://github.com/mabrikado/abcInventory.git
cd abc-inventory

# (Optional) Create a virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python CLI.py

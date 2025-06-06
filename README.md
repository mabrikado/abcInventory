🧾 ABCInventory


📋 Description

ABCInventory is a command-line inventory management system designed for ABC Traders. It allows users to efficiently manage products, track inventory, and control user access—all through a simple terminal interface.
✅ Features

    📦 Add, update, delete, and view items in the inventory

    👤 Create, update, and delete user accounts

    🧮 View total inventory value and itemized summaries in a styled table

🔐 Security

    🔑 Passwords are securely stored using bcrypt hashing

    🔍 Passwords are verified using hash comparison on login or password change

    🛡️ A secret registration key is required for new users to sign up

🛠️ Tech Stack

    🐍 Python 3

    🔐 bcrypt – password hashing and verification

    📁 Text files – used as a lightweight, file-based database

    📊 tabulate – display inventory in styled table formats

    🎨 colorama, termcolor – color-coded and styled terminal output
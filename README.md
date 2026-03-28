# AIML-PROJECT 

🛒 OneCart – CLI-Based E-Commerce System


📌 Overview

OneCart is a simple command-line based e-commerce application developed in Python.


It simulates the core functionality of an online shopping system, including:

User authentication

Product browsing

Cart management

Order placement

This project is designed to provide a strong foundational understanding of backend logic, file handling, and data persistence using JSON.


🎯 Objective


The main goal of this project is to:

Understand how real-world e-commerce systems work at a basic level

Practice file handling using JSON

Implement object-oriented programming (OOP) concepts

Build a modular and scalable CLI application



🧠 Core Concepts Used


1. File Handling (Persistent Storage)

The system uses JSON files as a lightweight database:

users.json → stores user credentials

products.json → stores product catalog

orders.json → stores order history

2. Object-Oriented Programming (OOP)
The application is divided into logical classes:


User → handles registration and login

Product → displays available products

Cart → manages user cart operations

Order → processes and stores orders


3. Data Flow Architecture

User Input → Business Logic → JSON Storage → Output Display







📂 Project Structure



OneCart/
│
├── main.py            # Main application logic
├── users.json         # User database
├── products.json      # Product catalog
├── orders.json        # Order history
└── README.md          # Project documentation







⚙️ Features
🔐 User Management


Register new users


Login with credentials


Prevent duplicate usernames

📦 Product Management
Display product list with ID, name, and price


Reads data dynamically from JSON

🛒 Cart System
Add products using product ID


View cart items


Calculate total cost

📑 Order System
Place orders from cart


Store order history


Clear cart after order

▶️ How to Run
Step 1: Install Python


Make sure Python is installed on your system.


Step 2: Run the program


python main.py


Step 3: Follow menu options
1 register

2 login

3 products

4 add to cart

5 view cart

6 order

7 exit

🧩 Design Analysis (Deep Understanding)


✔ Why JSON Instead of Database?

Lightweight and easy to use

No external dependencies

Perfect for beginner-level backend projects



✔ Why CLI Instead of GUI?


Focus on logic rather than UI complexity

Helps understand program flow clearly

Faster development and testing



✔ Data Integrity Handling

Files are auto-created if missing

Error handling for corrupted JSON

Input validation for product IDs



✔ Limitations

No password encryption (plain text storage)

No multi-user session handling

No concurrency support

No real database integration



🚀 Future Enhancements


Add graphical user interface (GUI)

Integrate database (MySQL / MongoDB)

Implement password hashing for security

Add admin panel for product management

Add payment gateway simulation

Improve input validation and error handling


📚 Learning Outcomes


Through this project, you will understand:

How backend systems store and retrieve data


How authentication systems work


How e-commerce logic is structured


Importance of modular programming


Real-world application of Python fundamentals


🏁 Conclusion


OneCart serves as a beginner-friendly e-commerce simulation that builds strong fundamentals in backend development. While simple in design, it reflects real-world system logic and provides a solid base for developing advanced applications



# Banking Database Management System

A MySQL-based Banking Database Management System created for SQL and database management practice.

## 📁 Project Structure

```text
Banking-Database-Management-System/
│
├── README.md
│
├── documentation/
│   ├── Banking_SQL_Practice_Questions.pdf
│   └── MySQL_Project.pdf
│
└── terminal/
    ├── MySQL terminal.txt
    ├── MySQL_Actual_Terminal_Run_Notes.pdf
    └── MySQL_Terminal_Complete_Notes.pdf
```

## 🗄️ Database

**Database:** `banking_db`

### Main Tables

- `branches`
- `customers`
- `employees`
- `accounts`
- `transactions`
- `cards`
- `card_transactions`
- `beneficiaries`
- `transfers`

## 🧠 SQL Concepts Practiced

- SELECT and filtering with `WHERE`
- `AND`, `OR`, `IN`, `BETWEEN`
- `LIKE`
- `IS NULL` / `IS NOT NULL`
- `ORDER BY` and `LIMIT`
- INSERT, UPDATE and DELETE
- Aggregate functions: `COUNT()`, `SUM()`, `AVG()`, `MAX()`, `MIN()`
- `GROUP BY` and `HAVING`
- Joins
- Subqueries
- Window functions and ranking

## 📚 SQL Practice

`documentation/Banking_SQL_Practice_Questions.pdf` contains **28 SQL practice questions**, including:

1. Active customers
2. Savings accounts
3. Accounts with balance above ₹1 lakh
4. ATM transactions
5. Customers from Delhi
6. Total balance by branch
7. Average balance by account type
8. Number of accounts per customer
9. Total transaction amount per customer
10. Total transactions by mode
11. Customer + Account details
12. Customer + Account + Branch
13. Customers having cards
14. Customers without cards
15. Customers having multiple accounts
16. Above-average balance customers
17. Second-highest balance
18. Customers above their branch average
19. Highest transaction customer
20. Branch with highest total balance
21. Customer-wise total balance
22. Customer-wise transaction volume
23. Branch-wise average balance
24. Above-average customers
25. Top customers per branch
26. Rank customers by balance
27. Top 3 customers per branch
28. Rank transactions per customer

## 💻 Terminal Work

The `terminal/` folder keeps the MySQL Shell work and notes.

- **`MySQL terminal.txt`** — original terminal record.
- **`MySQL_Actual_Terminal_Run_Notes.pdf`** — clean terminal-style record of commands and outputs.
- **`MySQL_Terminal_Complete_Notes.pdf`** — reference notes for MySQL Shell and SQL commands.

## 🚀 MySQL Shell Workflow

```text
mysqlsh
\sql
\connect root@localhost
\use banking_db
SELECT DATABASE();
SHOW TABLES;
DESC table_name;
```

Then execute the required SQL queries.

## 🛠️ Technology

- MySQL
- MySQL Shell
- SQL
- Windows

## 🎯 Objectives

- Understand relational database structure.
- Practice SQL queries in MySQL.
- Work with related banking tables.
- Perform filtering, aggregation and grouping.
- Practice joins, subqueries and ranking.
- Maintain a clean record of terminal execution.

---

**Project:** Banking Database Management System  
**Purpose:** SQL / Database Management Practice

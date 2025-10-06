# 🧮 CalcMate — Professional Command-Line Calculator

[![CI – Tests & Coverage](https://github.com/shanmukh1315/CalcMate/actions/workflows/python-app.yml/badge.svg)](https://github.com/shanmukh1315/CalcMate/actions)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

A **modular, professional-grade calculator** built with Python.  
CalcMate demonstrates clean architecture, error handling, and **100% automated test coverage** enforced via **GitHub Actions CI**.

---

## 🚀 Features

**REPL (Read–Eval–Print Loop)** for continuous user interaction  
**Arithmetic Operations:** Addition, Subtraction, Multiplication, Division  
**Special Commands:** `help`, `history`, `exit`  
**Comprehensive Error Handling:**  
- Invalid inputs  
- Unsupported operations  
- Division by zero  
**CalculationFactory Class:** Creates `Calculation` instances from user input  
**History Management:** Tracks all previous calculations during the session  
**Full Unit Testing:** 100% code coverage with `pytest`  
**Continuous Integration (CI):** GitHub Actions enforces coverage and testing

---

## 🧩 Project Structure


CalcMate/
├── app/
│   ├── calculator/
│   │   ├── __init__.py        # CLI logic (REPL, input parsing, history)
│   │   └── cli.py
│   ├── calculation/
│   │   └── __init__.py        # CalculationFactory + Calculation class
│   ├── operation/
│   │   └── __init__.py        # add(), subtract(), multiply(), divide()
│   └── __init__.py
│
├── tests/
│   ├── test_operations.py     # Parameterized tests for arithmetic ops
│   ├── test_calculations.py   # Factory and Calculation class tests
│   └── test_cli.py            # REPL and CLI flow tests
│
├── .github/
│   └── workflows/
│       └── python-app.yml     # GitHub Actions CI config
│
├── pyproject.toml             # Project + pytest configuration
├── .gitignore                 # Ignore venv, caches, coverage, etc.
└── README.md                  # Documentation


## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository

git clone https://github.com/shanmukh1315/CalcMate.git
cd CalcMate


### 2️⃣ Create & Activate Virtual Environment

python -m venv .venv
source .venv/bin/activate      # macOS / Linux

### 3️⃣ Install Dependencies

pip install -r requirements.txt
# OR (for this assignment)
pip install pytest pytest-cov


**Usage (Run the Calculator)**
python -m app.calculator.cli


**Example Session:**
Welcome to CalcMate! Type 'help' for instructions.
Enter operation (+, -, *, /) or command (help, history, exit): +
Enter numbers separated by spaces: 5 10 15
Result: 30.0
Enter operation (+, -, *, /) or command (help, history, exit): history
1: add [5.0, 10.0, 15.0] = 30.0
Enter operation (+, -, *, /) or command (help, history, exit): exit
Goodbye!


**Testing**

Run all tests with coverage:

pytest --cov=app --cov-report=term-missing


**Enforce 100% coverage:**

pytest --cov=app --cov-fail-under=100

**output:**
---------- coverage: platform darwin ----------
Name                          Stmts   Miss  Cover
-------------------------------------------------
app/__init__.py                   0      0   100%
app/calculation/__init__.py      25      0   100%
app/calculator/__init__.py       17      0   100%
app/calculator/cli.py            29      0   100%
app/operation/__init__.py        30      0   100%
-------------------------------------------------
TOTAL                           101      0   100%

from __future__ import annotations
from app.calculation import CalculationFactory
from app.calculator import Calculator

HELP_TEXT = """\
CalcMate — Commands & Usage
---------------------------
Commands:
  help       Show this message
  history    Show calculation history (op + operands)
  exit/quit  Leave the program

Operations:
  +  -  *  /
After choosing an operation, enter numbers separated by spaces.
"""

def main() -> None:
    calc = Calculator()
    print("Welcome to CalcMate! Type 'help' for instructions.")
    while True:
        op = input("Enter operation (+, -, *, /) or command (help, history, exit): ").strip().lower()
        if op in {"exit", "quit"}:
            print("Goodbye!")
            break
        if op == "help":
            print(HELP_TEXT); continue
        if op == "history":
            if not calc.history:
                print("No calculations yet.")
            else:
                for i, c in enumerate(calc.history, start=1):
                    print(f"{i}. {c.operation.__name__} {list(c.operands)} = {c.compute()}")
            continue
        numbers = input("Enter numbers separated by spaces: ")
        try:
            c = CalculationFactory.from_strings(op, numbers)
            result = calc.add_to_history(c)
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed. Try again.")
        except ValueError as ve:
            print(f"Error: {ve}")

if __name__ == "__main__":  # pragma: no cover
    main()

import ast
import math
import operator
import tkinter as tk
from tkinter import ttk


def calculate(first_number, operation, second_number):
    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    if operation not in operations:
        raise ValueError("Nieznane działanie. Wybierz +, -, * lub /.")
    if operation == "/" and second_number == 0:
        raise ZeroDivisionError("Nie można dzielić przez zero.")
    return operations[operation](first_number, second_number)


def _evaluate_node(node):
    if isinstance(node, ast.Expression):
        return _evaluate_node(node.body)

    if isinstance(node, ast.Constant) and type(node.value) in (int, float):
        value = float(node.value)
        if not math.isfinite(value):
            raise ValueError("Liczba jest poza obsługiwanym zakresem.")
        return value

    if isinstance(node, ast.BinOp):
        operations = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.Pow: operator.pow,
        }
        operation = operations.get(type(node.op))
        if operation is None:
            raise ValueError("Niedozwolone działanie.")
        result = operation(_evaluate_node(node.left), _evaluate_node(node.right))
        if type(result) not in (int, float):
            raise ValueError("Wynik musi być liczbą rzeczywistą.")
        if not math.isfinite(result):
            raise ValueError("Wynik jest poza obsługiwanym zakresem.")
        return result

    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        value = _evaluate_node(node.operand)
        return value if isinstance(node.op, ast.UAdd) else -value

    if (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "sqrt"
        and len(node.args) == 1
        and not node.keywords
    ):
        value = _evaluate_node(node.args[0])
        if value < 0:
            raise ValueError("Nie można obliczyć pierwiastka z liczby ujemnej.")
        return math.sqrt(value)

    raise ValueError("Niepoprawne wyrażenie.")


def evaluate_expression(expression):
    normalized = expression.replace(",", ".").replace("^", "**")
    try:
        tree = ast.parse(normalized, mode="eval")
    except SyntaxError as error:
        raise ValueError("Niepoprawne wyrażenie.") from error
    return _evaluate_node(tree)


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.expression = tk.StringVar()
        self.status = tk.StringVar()
        self.last_result = None
        self.showing_result = False

        root.title("Kalkulator")
        root.resizable(False, False)
        root.bind_all("<Key>", self._on_key)

        frame = ttk.Frame(root, padding=12)
        frame.grid()

        display = ttk.Entry(
            frame,
            textvariable=self.expression,
            justify="right",
            font=("TkDefaultFont", 20),
            width=22,
            state="readonly",
        )
        display.grid(row=0, column=0, columnspan=4, sticky="ew", pady=(0, 4))
        ttk.Label(frame, textvariable=self.status, anchor="w").grid(
            row=1, column=0, columnspan=4, sticky="ew", pady=(0, 6)
        )

        buttons = (
            ("C", "DEL", "(", ")"),
            ("7", "8", "9", "/"),
            ("4", "5", "6", "*"),
            ("1", "2", "3", "-"),
            ("0", ",", "^", "+"),
            ("sqrt", "=", "", ""),
        )
        for row_index, row in enumerate(buttons, start=2):
            for column_index, label in enumerate(row):
                if not label:
                    continue
                button = ttk.Button(
                    frame,
                    text=label,
                    command=lambda value=label: self._on_button(value),
                    width=7,
                )
                button.grid(
                    row=row_index,
                    column=column_index,
                    columnspan=3 if label == "=" else 1,
                    sticky="nsew",
                    padx=2,
                    pady=2,
                )

    def _on_button(self, value):
        if value == "C":
            self.expression.set("")
            self.status.set("")
            self.last_result = None
            self.showing_result = False
        elif value == "DEL":
            self.expression.set(self.expression.get()[:-1])
            self.status.set("")
            self.showing_result = False
        elif value == "=":
            self._calculate()
        else:
            self._append(value)

    def _append(self, value):
        if self.showing_result:
            if value[0].isdigit() or value in (",", "(", "sqrt"):
                self.expression.set("")
            elif self.last_result is not None:
                self.expression.set(repr(self.last_result))
            self.showing_result = False
        self.expression.set(self.expression.get() + ("sqrt(" if value == "sqrt" else value))
        self.status.set("")

    def _calculate(self):
        try:
            result = evaluate_expression(self.expression.get())
        except (ValueError, ZeroDivisionError, OverflowError) as error:
            self.status.set(f"Błąd: {error}")
            self.showing_result = False
            return
        self.last_result = result
        self.expression.set(format(result, ".15g").replace(".", ","))
        self.status.set("")
        self.showing_result = True

    def _on_key(self, event):
        if event.keysym in ("Return", "KP_Enter"):
            self._calculate()
            return "break"
        if event.keysym == "BackSpace":
            self._on_button("DEL")
            return "break"
        if event.keysym == "Escape":
            self._on_button("C")
            return "break"
        if event.char and event.char in "0123456789+-*/^(),.":
            self._append("," if event.char == "." else event.char)
            return "break"
        return None


def main():
    root = tk.Tk()
    CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

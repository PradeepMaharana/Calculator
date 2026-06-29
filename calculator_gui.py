#!/usr/bin/env python3
"""Calculator GUI Application using Tkinter"""

import tkinter as tk
from tkinter import font, messagebox
from calculator import add, subtract, multiply, divide, power, modulo, square_root, factorial, absolute_value, percentage

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("500x650")
        self.root.resizable(False, False)
        self.root.configure(bg="#2c3e50")

        self.expression = ""
        self.result_value = 0

        self.setup_ui()

    def setup_ui(self):
        # Title
        title_font = font.Font(family="Helvetica", size=16, weight="bold")
        title = tk.Label(
            self.root,
            text="Advanced Calculator",
            font=title_font,
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        title.pack(pady=10)

        # Display Frame
        display_frame = tk.Frame(self.root, bg="#34495e", relief=tk.SUNKEN, bd=2)
        display_frame.pack(pady=10, padx=10, fill=tk.BOTH)

        # Expression Display
        self.expr_label = tk.Label(
            display_frame,
            text=self.expression if self.expression else "0",
            font=("Helvetica", 12),
            bg="#34495e",
            fg="#3498db",
            anchor="e",
            padx=10,
            pady=5
        )
        self.expr_label.pack(fill=tk.BOTH)

        # Result Display
        result_font = font.Font(family="Helvetica", size=24, weight="bold")
        self.result_label = tk.Label(
            display_frame,
            text="0",
            font=result_font,
            bg="#34495e",
            fg="#2ecc71",
            anchor="e",
            padx=10,
            pady=10
        )
        self.result_label.pack(fill=tk.BOTH)

        # Button Frame
        button_frame = tk.Frame(self.root, bg="#2c3e50")
        button_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Button layout
        buttons = [
            ["C", "DEL", "(", ")", "√"],
            ["7", "8", "9", "/", "%"],
            ["4", "5", "6", "*", "^"],
            ["1", "2", "3", "-", "!"],
            ["0", ".", "+", "=", "|x|"],
            ["sin", "cos", "tan", "pct", "π"]
        ]

        self.button_widgets = {}
        for row_idx, row in enumerate(buttons):
            for col_idx, btn_text in enumerate(row):
                self.create_button(button_frame, btn_text, row_idx, col_idx)

    def create_button(self, parent, text, row, col):
        # Color scheme for different button types
        if text in ["C", "DEL"]:
            bg_color = "#e74c3c"
            fg_color = "white"
        elif text in ["=", "pct"]:
            bg_color = "#27ae60"
            fg_color = "white"
        elif text in ["+", "-", "*", "/", "%", "^", "!", "|x|", "√", "(", ")"]:
            bg_color = "#3498db"
            fg_color = "white"
        else:
            bg_color = "#95a5a6"
            fg_color = "black"

        button = tk.Button(
            parent,
            text=text,
            font=("Helvetica", 12, "bold"),
            bg=bg_color,
            fg=fg_color,
            activebackground="#34495e",
            activeforeground="white",
            relief=tk.RAISED,
            bd=1,
            command=lambda: self.on_button_click(text)
        )
        button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
        self.button_widgets[text] = button

        # Configure grid weight for responsive layout
        parent.grid_rowconfigure(row, weight=1)
        parent.grid_columnconfigure(col, weight=1)

    def on_button_click(self, char):
        if char == "C":
            self.clear()
        elif char == "DEL":
            self.delete()
        elif char == "=":
            self.calculate()
        elif char == "√":
            self.apply_single_op("sqrt")
        elif char == "!":
            self.apply_single_op("factorial")
        elif char == "|x|":
            self.apply_single_op("abs")
        elif char == "pct":
            self.show_percentage_dialog()
        elif char in ["sin", "cos", "tan", "π"]:
            messagebox.showinfo("Info", "Trigonometric functions coming soon!")
        else:
            self.append_to_expression(char)

    def append_to_expression(self, char):
        self.expression += str(char)
        self.update_display()

    def clear(self):
        self.expression = ""
        self.result_value = 0
        self.update_display()

    def delete(self):
        self.expression = self.expression[:-1]
        self.update_display()

    def update_display(self):
        display_text = self.expression if self.expression else "0"
        self.expr_label.config(text=display_text)
        self.result_label.config(text=display_text if self.expression else "0")

    def calculate(self):
        try:
            if not self.expression:
                return

            # Replace symbols for evaluation
            expr = self.expression.replace("^", "**")

            # Evaluate the expression
            result = eval(expr)
            self.result_value = result

            # Display result
            self.expr_label.config(text=self.expression)
            self.result_label.config(text=str(result), fg="#2ecc71")

            # Update expression for next calculation
            self.expression = str(result)

        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero!")
            self.clear()
        except Exception as e:
            messagebox.showerror("Error", f"Invalid expression: {str(e)}")
            self.clear()

    def apply_single_op(self, operation):
        try:
            if not self.expression:
                messagebox.showwarning("Warning", "Please enter a number first")
                return

            num = float(self.expression)

            if operation == "sqrt":
                result = square_root(num)
            elif operation == "factorial":
                result = factorial(num)
            elif operation == "abs":
                result = absolute_value(num)

            if isinstance(result, str):  # Error message
                messagebox.showerror("Error", result)
            else:
                self.expr_label.config(text=f"{operation}({num})")
                self.result_label.config(text=str(result), fg="#2ecc71")
                self.expression = str(result)

        except ValueError:
            messagebox.showerror("Error", "Invalid input for this operation")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def show_percentage_dialog(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Percentage Calculator")
        dialog.geometry("300x200")
        dialog.configure(bg="#2c3e50")

        # Labels and entries
        tk.Label(dialog, text="Percentage (%)", bg="#2c3e50", fg="#ecf0f1").pack(pady=5)
        pct_entry = tk.Entry(dialog, font=("Helvetica", 12), width=20)
        pct_entry.pack(pady=5)

        tk.Label(dialog, text="Of (Total)", bg="#2c3e50", fg="#ecf0f1").pack(pady=5)
        total_entry = tk.Entry(dialog, font=("Helvetica", 12), width=20)
        total_entry.pack(pady=5)

        def calculate_pct():
            try:
                pct = float(pct_entry.get())
                total = float(total_entry.get())
                result = percentage(pct, total)
                messagebox.showinfo("Result", f"{pct}% of {total} = {result}")
                self.expression = str(result)
                self.update_display()
                dialog.destroy()
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numbers")

        tk.Button(
            dialog,
            text="Calculate",
            bg="#27ae60",
            fg="white",
            font=("Helvetica", 12),
            command=calculate_pct
        ).pack(pady=10)


def main():
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
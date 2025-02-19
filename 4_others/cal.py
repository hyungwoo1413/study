import tkinter as tk
from tkinter import messagebox

from cal2 import calc_ver03  
class CalculatorGUI:
    def __init__(self, calculator):
        self.calculator = calculator
        self.root = tk.Tk()
        self.root.title("계산기")
        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self.root, font=("Arial", 24), justify='right')
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")
        self.display.insert(0, str(self.calculator.accum))

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3),
            ('<', 5, 0), ('>', 5, 2)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, font=("Arial", 18),
                               command=lambda t=text: self.on_button_click(t))
            if text == '<' or text == '>':
                button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2, columnspan=2)
            else:
                button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char.isdigit():
            current = self.display.get()
            if current == '0':
                self.display.delete(0, tk.END)
            self.display.insert(tk.END, char)

        elif char in '+-*/':
            self.display.insert(tk.END, f' {char} ')

        elif char == 'C':
            self.display.delete(0, tk.END)
            self.calculator.accum = 0
            self.display.insert(0, '0')

        elif char == '=':
            expression = self.display.get().split()
            if len(expression) == 3:
                operand1, operator, operand2 = expression
                self.calculator.accum = float(operand1)
                try:
                    operand2 = float(operand2)
                    if operator == '+':
                        self.calculator.add(operand2)
                    elif operator == '-':
                        self.calculator.sub(operand2)
                    elif operator == '*':
                        self.calculator.mul(operand2)
                    elif operator == '/':
                        if operand2 == 0:
                            messagebox.showerror("Error", "0으로 나눌 수 없습니다!")
                            return
                        self.calculator.div(operand2)

                    self.display.delete(0, tk.END)
                    self.display.insert(0, str(self.calculator.accum))
                except Exception as e:
                    messagebox.showerror("Error", f"잘못된 입력입니다: {e}")
            else:
                messagebox.showerror("Error", "잘못된 수식입니다!")

        elif char == '<':
            self.calculator.undo()
            self.display.delete(0, tk.END)
            self.display.insert(0, str(self.calculator.accum))

        elif char == '>':
            self.calculator.redo()
            self.display.delete(0, tk.END)
            self.display.insert(0, str(self.calculator.accum))

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    calc = calc_ver03(0)  # 초기값 0으로 계산기 인스턴스 생성
    gui = CalculatorGUI(calc)
    gui.run()
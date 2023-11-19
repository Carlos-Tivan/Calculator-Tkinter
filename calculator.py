import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, window):
        self.window = window
        self.window.title("Calculator")
        
        # Entry widget to display the calculations
        self.entry = ttk.Entry(window, width=20, font=('Courier New', 16))
        self.entry.grid(row=0, column=0, columnspan=6)

        # Buttons for digits and operations, including the "Clear" and "Del" buttons
        buttons = [

            '7','8','9','DEL','AC',
            '4','5','6','*','/',
            '1','2','3','+','-',
            '%','(',')','='

        ]

        # Create and place the buttons on the grid
        row_val = 1
        col_val = 0
        for button in buttons:
            ttk.Button(window, text=button, command=lambda btn=button: self.button_click(btn)).grid(row=row_val, column=col_val, ipadx=10, ipady=10)
            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1

    def button_click(self, button):
        current_entry_text = self.entry.get()

        if button == '=':
            try:
                result = eval(current_entry_text)
                self.entry.delete(0, tk.END)  # condition division by zero 
                self.entry.insert(tk.END, str(round(result, 3)))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Syntax Error")

        elif button == 'AC':
            self.entry.delete(0, tk.END)  # Clear the entry

        elif button == '%':
            # Implement the percentage calculation
            try:
                result = eval(current_entry_text) / 100
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Syntax Error")

        elif button == '(':
            # Add an open parenthesis to the entry
            self.entry.insert(tk.END, '(')

        elif button == ')':
            # Add a closing parenthesis to the entry
            self.entry.insert(tk.END, ')')

        elif button == 'DEL':
            # Implement the delete functionality
            if current_entry_text:
                self.entry.delete(len(current_entry_text) - 1, tk.END)  # Delete the last character
        else:
            self.entry.insert(tk.END, button)

# Create the main window
window = tk.Tk()
calculator = Calculator(window)
# Run the Tkinter event loop
window.mainloop()

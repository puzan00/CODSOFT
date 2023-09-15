import tkinter as tk
from tkinter import ttk

def button_click(number):
    current = input_field.get()
    input_field.delete(0, tk.END)
    input_field.insert(0, current + str(number))

def clear():
    input_field.delete(0, tk.END)

def evaluate_expression():
    try:
        expression = input_field.get()
        result = eval(expression)
        input_field.delete(0, tk.END)
        input_field.insert(0, result)
    except Exception as e:
        input_field.delete(0, tk.END)
        input_field.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")
root.geometry("450x530")
root.resizable(False, False)  # Make the window non-resizable

style = ttk.Style()
style.configure("TFrame", background="#333")

frame = ttk.Frame(root, style="TFrame")
frame.grid(row=0, column=0)

input_field = tk.Entry(frame, width=20, font=("Helvetica", 24), bd=10, insertbackground="white", justify="right")
input_field.grid(row=0, column=0, columnspan=4, padx=20, pady=20, ipadx=10, ipady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+',
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        command = evaluate_expression
        bg_color = "#ff9933"  # Highlight "=" button
        fg_color = "white"   # White text color for "="
    elif button == 'C':
        command = clear
        bg_color = "#ff5555"  # Red color for "C" button
        fg_color = "white"   # White text color for "C"
    elif button in ['+', '-', '*', '/']:
        command = lambda b=button: button_click(b)
        bg_color = "#ff9933"  # Operator buttons in #ff9933 color
        fg_color = "white"   # White text color for operators
    else:
        command = lambda b=button: button_click(b)
        bg_color = "#7fb3d5"  # Light blue color for other buttons
        fg_color = "white"   # White text color for digits

    tk.Button(frame, text=button, font=("Helvetica", 18), width=4, height=2,
              padx=10, pady=10, command=command, bg=bg_color, fg=fg_color).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the main application
root.mainloop()

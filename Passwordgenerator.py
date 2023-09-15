import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + '!@#$&%^'
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_button_click():
    try:
        password_length = int(length_entry.get())
        if password_length < 1:
            raise ValueError("Password length must be at least 1.")
        password = generate_password(password_length)
        password_label.config(text=f"Generated Password: {password}")
        length_label.config(foreground="black")  # Set the text color to black
    except ValueError as e:
        password_label.config(text=str("First Enter the Password Length!"))

app = tk.Tk()
app.title("Modern Password Generator")
app.geometry("500x200")  # Set the initial window size
app.resizable(False, False)  # Make the window non-resizable

style = ttk.Style()
style.configure("TFrame", background="#374785")  # Set background color

container_frame = ttk.Frame(app)
container_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

length_label = ttk.Label(container_frame, text="Password Length:", foreground="black", font=("Arial", 16))
length_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

length_entry = ttk.Entry(container_frame, font=("Arial", 14))
length_entry.grid(row=0, column=1, padx=5, pady=5)

generate_button = ttk.Button(container_frame, text="Generate Password", command=generate_button_click)
generate_button.grid(row=1, columnspan=2, padx=5, pady=10)

password_label = ttk.Label(container_frame, text="", font=("Arial", 16), foreground="white", background="#374785")
password_label.grid(row=2, columnspan=2, padx=5, pady=10)

# Start the application
app.mainloop()

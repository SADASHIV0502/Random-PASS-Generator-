#pass gen
import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_var.get())
    include_upper = upper_var.get()
    include_lower = lower_var.get()
    include_digits = digit_var.get()
    include_special = special_var.get()

    if not (include_upper or include_lower or include_digits or include_special):
        messagebox.showerror("Error", "Select at least one character type.")
        return

    if length < 4:
        messagebox.showerror("Error", "Length should be at least 4.")
        return

    char_pool = ""
    if include_upper:
        char_pool += string.ascii_uppercase
    if include_lower:
        char_pool += string.ascii_lowercase
    if include_digits:
        char_pool += string.digits
    if include_special:
        char_pool += string.punctuation

    password = ''.join(random.choice(char_pool) for _ in range(length))

    password_var.set(password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    root.update()  # Keeps the clipboard content even after the window is closed
    messagebox.showinfo("Info", "Password copied to clipboard.")

root = tk.Tk()
root.title("Advanced Password Generator")

# Variables
length_var = tk.StringVar(value='12')
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)
password_var = tk.StringVar()

# UI Layout
tk.Label(root, text="Password Length:").grid(row=0, column=0, sticky='w')
tk.Entry(root, textvariable=length_var).grid(row=0, column=1)

tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var).grid(row=1, column=0, columnspan=2, sticky='w')
tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var).grid(row=2, column=0, columnspan=2, sticky='w')
tk.Checkbutton(root, text="Include Digits", variable=digit_var).grid(row=3, column=0, columnspan=2, sticky='w')
tk.Checkbutton(root, text="Include Special Characters", variable=special_var).grid(row=4, column=0, columnspan=2, sticky='w')

tk.Button(root, text="Generate Password", command=generate_password).grid(row=5, column=0, columnspan=2)
tk.Entry(root, textvariable=password_var, state='readonly', width=40).grid(row=6, column=0, columnspan=2)
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).grid(row=7, column=0, columnspan=2)

root.mainloop()

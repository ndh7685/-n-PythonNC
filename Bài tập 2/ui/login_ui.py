import tkinter as tk
from tkinter import messagebox
from models import register_user, login_user
from ui.main_ui import show_main_window


def show_login_window():
    def login():
        username = entry_username.get()
        password = entry_password.get()
        user = login_user(username, password)
        if user:
            messagebox.showinfo("Success", "Login successful!")
            root.destroy()
            show_main_window()
            # Hiển thị giao diện chính (main_ui.py)
        else:
            messagebox.showerror("Error", "Invalid credentials!")

    def register():
        username = entry_username.get()
        password = entry_password.get()
        try:
            register_user(username, password)
            messagebox.showinfo("Success", "Registration successful!")
        except:
            messagebox.showerror("Error", "Username already exists!")

    root = tk.Tk()
    root.title("Login/Register")

    tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=10)
    entry_username = tk.Entry(root)
    entry_username.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10)
    entry_password = tk.Entry(root, show="*")
    entry_password.grid(row=1, column=1, padx=10, pady=10)

    tk.Button(root, text="Login", command=login).grid(row=2, column=0, padx=10, pady=10)
    tk.Button(root, text="Register", command=register).grid(row=2, column=1, padx=10, pady=10)

    root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox
from models import get_all_students, add_student, delete_student, update_student, search_students_by_name

def show_main_window():
    def refresh_table():
        """Làm mới bảng hiển thị học sinh."""
        for row in tree.get_children():
            tree.delete(row)
        for student in get_all_students():
            tree.insert("", "end", values=student)

    def add_new_student():
        """Thêm học sinh mới."""
        name = entry_name.get()
        age = entry_age.get()
        grade = entry_grade.get()
        address = entry_address.get()
        if not (name and age and grade and address):
            messagebox.showerror("Error", "All fields are required!")
            return
        try:
            add_student(name, int(age), grade, address)
            messagebox.showinfo("Success", "Student added successfully!")
            refresh_table()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_selected_student():
        """Xóa học sinh được chọn."""
        selected = tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a student to delete!")
            return
        student_id = tree.item(selected[0])["values"][0]
        try:
            delete_student(student_id)
            messagebox.showinfo("Success", "Student deleted successfully!")
            refresh_table()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_selected_student():
        """Cập nhật thông tin học sinh."""
        selected = tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a student to update!")
            return
        student_id = tree.item(selected[0])["values"][0]
        name = entry_name.get()
        age = entry_age.get()
        grade = entry_grade.get()
        address = entry_address.get()
        if not (name and age and grade and address):
            messagebox.showerror("Error", "All fields are required!")
            return
        try:
            update_student(student_id, name, int(age), grade, address)
            messagebox.showinfo("Success", "Student updated successfully!")
            refresh_table()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def search_student():
        """Tìm kiếm học sinh theo tên."""
        search_name = entry_search.get()
        if not search_name:
            messagebox.showerror("Error", "Please enter a name to search!")
            return
        students = search_students_by_name(search_name)
        for row in tree.get_children():
            tree.delete(row)
        for student in students:
            tree.insert("", "end", values=student)

    # Tạo cửa sổ chính
    root = tk.Tk()
    root.title("Student Management System")

    # Form thêm/sửa học sinh
    tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
    entry_name = tk.Entry(root)
    entry_name.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(root, text="Age:").grid(row=1, column=0, padx=5, pady=5)
    entry_age = tk.Entry(root)
    entry_age.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(root, text="Grade:").grid(row=2, column=0, padx=5, pady=5)
    entry_grade = tk.Entry(root)
    entry_grade.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(root, text="Address:").grid(row=3, column=0, padx=5, pady=5)
    entry_address = tk.Entry(root)
    entry_address.grid(row=3, column=1, padx=5, pady=5)

    tk.Button(root, text="Add", command=add_new_student).grid(row=4, column=0, padx=5, pady=5)
    tk.Button(root, text="Update", command=update_selected_student).grid(row=4, column=1, padx=5, pady=5)

    # Form tìm kiếm học sinh
    tk.Label(root, text="Search by Name:").grid(row=5, column=0, padx=5, pady=5)
    entry_search = tk.Entry(root)
    entry_search.grid(row=5, column=1, padx=5, pady=5)
    tk.Button(root, text="Search", command=search_student).grid(row=5, column=2, padx=5, pady=5)

    # Bảng hiển thị học sinh
    columns = ("ID", "Name", "Age", "Grade", "Address")
    tree = ttk.Treeview(root, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    tree.grid(row=6, column=0, columnspan=3, pady=10)

    tk.Button(root, text="Delete", command=delete_selected_student).grid(row=7, column=1, pady=5)

    # Hiển thị danh sách học sinh ban đầu
    refresh_table()

    root.mainloop()

import tkinter as tk
from tkinter import messagebox

students = {}

def calculate_grade(percentage):
    if percentage >= 80:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "Fail"

def add_student():
    roll = roll_entry.get()
    name = name_entry.get()
    marks = marks_entry.get()

    if roll in students:
        messagebox.showerror("Error", "Student already exists!")
        return

    try:
        marks_list = list(map(int, marks.split(",")))
        percentage = sum(marks_list) / len(marks_list)
        grade = calculate_grade(percentage)

        students[roll] = {
            "name": name,
            "marks": marks_list,
            "percentage": percentage,
            "grade": grade
        }

        messagebox.showinfo("Success", "Student Added Successfully!")
        clear_fields()

    except:
        messagebox.showerror("Error", "Enter marks like: 80,75,90")

def display_students():
    display_box.delete("1.0", tk.END)
    for roll, data in students.items():
        display_box.insert(tk.END,
            f"Roll: {roll}\n"
            f"Name: {data['name']}\n"
            f"Percentage: {round(data['percentage'],2)}%\n"
            f"Grade: {data['grade']}\n"
            "------------------------\n"
        )

def clear_fields():
    roll_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    marks_entry.delete(0, tk.END)

# Main Window
root = tk.Tk()
root.title("Smart Student Management System")
root.geometry("550x550")
root.configure(bg="#E3F2FD")   # Light blue background

# Heading
tk.Label(root,
         text="Smart Student Management System",
         font=("Arial", 16, "bold"),
         bg="#E3F2FD",
         fg="#0D47A1").pack(pady=15)

# Labels & Entries
tk.Label(root, text="Roll Number", bg="#E3F2FD").pack()
roll_entry = tk.Entry(root, bg="#FFFFFF")
roll_entry.pack(pady=5)

tk.Label(root, text="Name", bg="#E3F2FD").pack()
name_entry = tk.Entry(root, bg="#FFFFFF")
name_entry.pack(pady=5)

tk.Label(root, text="Marks (comma separated)", bg="#E3F2FD").pack()
marks_entry = tk.Entry(root, bg="#FFFFFF")
marks_entry.pack(pady=5)

# Buttons
tk.Button(root,
          text="Add Student",
          command=add_student,
          bg="#4CAF50",
          fg="white",
          width=20).pack(pady=8)

tk.Button(root,
          text="Display Students",
          command=display_students,
          bg="#2196F3",
          fg="white",
          width=20).pack(pady=5)

tk.Button(root,
          text="Clear Fields",
          command=clear_fields,
          bg="#FF9800",
          fg="white",
          width=20).pack(pady=5)

# Display Box
display_box = tk.Text(root,
                      height=10,
                      width=50,
                      bg="#FFFFFF",
                      fg="black")
display_box.pack(pady=15)

root.mainloop()
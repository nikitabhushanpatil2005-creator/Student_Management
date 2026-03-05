import tkinter as tk
from tkinter import messagebox

students = {}

# ---------------- FUNCTIONS ---------------- #

def calculate_grade(percentage):
    if percentage >= 80:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "Fail"

def show_frame(frame):
    frame.tkraise()

def add_student():
    roll = roll_entry.get()
    name = name_entry.get()

    try:
        m1 = int(sub1_entry.get())
        m2 = int(sub2_entry.get())
        m3 = int(sub3_entry.get())
        m4 = int(sub4_entry.get())
        m5 = int(sub5_entry.get())

        marks = [m1, m2, m3, m4, m5]
        percentage = sum(marks) / 5
        grade = calculate_grade(percentage)

        students[roll] = {
            "name": name,
            "marks": marks,
            "percentage": percentage,
            "grade": grade
        }

        messagebox.showinfo("Success", "Student Added Successfully!")

    except:
        messagebox.showerror("Error", "Enter valid marks!")

def display_students():
    display_box.delete("1.0", tk.END)

    for roll, data in students.items():
        display_box.insert(tk.END,
            f"Roll: {roll}\n"
            f"Name: {data['name']}\n"
            f"Percentage: {round(data['percentage'],2)}%\n"
            f"Grade: {data['grade']}\n"
            "----------------------\n"
        )

# ---------------- MAIN WINDOW ---------------- #

root = tk.Tk()
root.title("Smart Student Management System")
root.geometry("600x600")

# Container
container = tk.Frame(root)
container.pack(fill="both", expand=True)

# Create Pages
home_page = tk.Frame(container, bg="#E3F2FD")
add_page = tk.Frame(container, bg="#E8F5E9")
display_page = tk.Frame(container, bg="#FFF3E0")

for frame in (home_page, add_page, display_page):
    frame.place(relwidth=1, relheight=1)

# ---------------- HOME PAGE ---------------- #

tk.Label(home_page, text="Smart Student Management System",
         font=("Arial", 16, "bold"),
         bg="#E3F2FD").pack(pady=30)

tk.Button(home_page, text="Add Student",
          width=20,
          command=lambda: show_frame(add_page)).pack(pady=10)

tk.Button(home_page, text="Display Students",
          width=20,
          command=lambda: show_frame(display_page)).pack(pady=10)

tk.Button(home_page, text="Exit",
          width=20,
          command=root.destroy).pack(pady=10)

# ---------------- ADD STUDENT PAGE ---------------- #

tk.Label(add_page, text="Add Student",
         font=("Arial", 14, "bold"),
         bg="#E8F5E9").pack(pady=15)

tk.Label(add_page, text="Roll Number", bg="#E8F5E9").pack()
roll_entry = tk.Entry(add_page)
roll_entry.pack()

tk.Label(add_page, text="Name", bg="#E8F5E9").pack()
name_entry = tk.Entry(add_page)
name_entry.pack()

tk.Label(add_page, text="Subject 1").pack()
sub1_entry = tk.Entry(add_page)
sub1_entry.pack()

tk.Label(add_page, text="Subject 2").pack()
sub2_entry = tk.Entry(add_page)
sub2_entry.pack()

tk.Label(add_page, text="Subject 3").pack()
sub3_entry = tk.Entry(add_page)
sub3_entry.pack()

tk.Label(add_page, text="Subject 4").pack()
sub4_entry = tk.Entry(add_page)
sub4_entry.pack()

tk.Label(add_page, text="Subject 5").pack()
sub5_entry = tk.Entry(add_page)
sub5_entry.pack()

tk.Button(add_page, text="Save",
          bg="#4CAF50",
          fg="white",
          command=add_student).pack(pady=10)

tk.Button(add_page, text="Back",
          command=lambda: show_frame(home_page)).pack()

# ---------------- DISPLAY PAGE ---------------- #

tk.Label(display_page, text="Student Records",
         font=("Arial", 14, "bold"),
         bg="#FFF3E0").pack(pady=15)

display_box = tk.Text(display_page, width=60, height=15)
display_box.pack(pady=10)

tk.Button(display_page, text="Refresh",
          command=display_students).pack(pady=5)

tk.Button(display_page, text="Back",
          command=lambda: show_frame(home_page)).pack()

# Show Home Page First
show_frame(home_page)

root.mainloop()
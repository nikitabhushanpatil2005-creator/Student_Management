import tkinter as tk
from tkinter import ttk, messagebox
import csv

students = []

# ---------- FUNCTIONS ----------

def calculate_total_avg(m1, m2, m3):
    total = m1 + m2 + m3
    avg = round(total/3, 2)
    return total, avg


def add_student():
    roll = roll_entry.get()
    name = name_entry.get()

    if roll == "" or name == "":
        messagebox.showerror("Error", "Enter Roll and Name")
        return

    try:
        m1 = int(sub1_entry.get())
        m2 = int(sub2_entry.get())
        m3 = int(sub3_entry.get())
    except:
        messagebox.showerror("Error", "Enter valid marks")
        return

    total, avg = calculate_total_avg(m1, m2, m3)

    data = [roll, name, m1, m2, m3, total, avg]
    students.append(data)

    tree.insert("", tk.END, values=data)

    clear_fields()


def delete_student():

    selected = tree.selection()

    if not selected:
        messagebox.showwarning("Warning", "Select a student first")
        return

    for item in selected:
        values = tree.item(item)['values']
        students.remove(values)
        tree.delete(item)


def show_highest():

    if not students:
        return

    highest = max(students, key=lambda x: x[5])

    messagebox.showinfo(
        "Top Student",
        f"Name : {highest[1]}\nTotal Marks : {highest[5]}"
    )


def remove_lowest():

    if not students:
        return

    lowest = min(students, key=lambda x: x[5])

    for row in tree.get_children():
        if tree.item(row)['values'][0] == lowest[0]:
            tree.delete(row)

    students.remove(lowest)


def export_csv():

    with open("students.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Roll","Name","Subject1","Subject2","Subject3",
            "Total","Average"
        ])

        writer.writerows(students)

    messagebox.showinfo("Exported","Data exported to students.csv")


def search_student():

    keyword = search_entry.get().lower()

    for row in tree.get_children():
        tree.delete(row)

    for s in students:
        if keyword in s[1].lower():
            tree.insert("", tk.END, values=s)


def clear_fields():

    roll_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    sub1_entry.delete(0, tk.END)
    sub2_entry.delete(0, tk.END)
    sub3_entry.delete(0, tk.END)


# ---------- MAIN WINDOW ----------

root = tk.Tk()
root.title("Smart Student Management System")
root.geometry("900x550")
root.configure(bg="#F4F6F9")


# ---------- TITLE ----------

title = tk.Label(
    root,
    text="Smart Student Management Dashboard",
    font=("Segoe UI",18,"bold"),
    bg="#F4F6F9",
    fg="#2c3e50"
)

title.pack(pady=15)


# ---------- FORM ----------

form = tk.Frame(
    root,
    bg="#FFFFFF",
    padx=15,
    pady=15
)

form.pack(pady=10)


tk.Label(form,text="Roll No",bg="#FFFFFF").grid(row=0,column=0,padx=5)

roll_entry = tk.Entry(form,width=12)
roll_entry.grid(row=0,column=1)


tk.Label(form,text="Name",bg="#FFFFFF").grid(row=0,column=2)

name_entry = tk.Entry(form,width=18)
name_entry.grid(row=0,column=3)


tk.Label(form,text="Subject 1",bg="#FFFFFF").grid(row=1,column=0)

sub1_entry = tk.Entry(form,width=10)
sub1_entry.grid(row=1,column=1)


tk.Label(form,text="Subject 2",bg="#FFFFFF").grid(row=1,column=2)

sub2_entry = tk.Entry(form,width=10)
sub2_entry.grid(row=1,column=3)


tk.Label(form,text="Subject 3",bg="#FFFFFF").grid(row=1,column=4)

sub3_entry = tk.Entry(form,width=10)
sub3_entry.grid(row=1,column=5)


# ---------- BUTTONS ----------

button_frame = tk.Frame(root,bg="#F4F6F9")
button_frame.pack(pady=10)


tk.Button(
    button_frame,
    text="Add Student",
    bg="#2ecc71",
    fg="white",
    width=14,
    command=add_student
).grid(row=0,column=0,padx=6)


tk.Button(
    button_frame,
    text="Delete Student",
    bg="#e74c3c",
    fg="white",
    width=14,
    command=delete_student
).grid(row=0,column=1,padx=6)


tk.Button(
    button_frame,
    text="Highest Marks",
    bg="#3498db",
    fg="white",
    width=14,
    command=show_highest
).grid(row=0,column=2,padx=6)


tk.Button(
    button_frame,
    text="Remove Lowest",
    bg="#f39c12",
    fg="white",
    width=14,
    command=remove_lowest
).grid(row=0,column=3,padx=6)


tk.Button(
    button_frame,
    text="Export CSV",
    bg="#9b59b6",
    fg="white",
    width=14,
    command=export_csv
).grid(row=0,column=4,padx=6)


# ---------- SEARCH ----------

search_frame = tk.Frame(root,bg="#F4F6F9")
search_frame.pack(pady=5)


tk.Label(
    search_frame,
    text="Search Student:",
    bg="#F4F6F9"
).grid(row=0,column=0)


search_entry = tk.Entry(search_frame,width=20)
search_entry.grid(row=0,column=1,padx=5)


tk.Button(
    search_frame,
    text="Search",
    bg="#16a085",
    fg="white",
    command=search_student
).grid(row=0,column=2)


# ---------- TABLE ----------

columns = (
    "Roll",
    "Name",
    "Sub1",
    "Sub2",
    "Sub3",
    "Total",
    "Average"
)

style = ttk.Style()
style.configure("Treeview",
                background="white",
                fieldbackground="white",
                rowheight=25)

tree = ttk.Treeview(
    root,
    columns=columns,
    show="headings",
    height=10
)

for col in columns:

    tree.heading(col,text=col)
    tree.column(col,width=110,anchor="center")

tree.pack(pady=20)


root.mainloop()
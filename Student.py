# Enhanced Smart Student Management System

students = {}

# Grade Function
def calculate_grade(percentage):
    if percentage >= 80:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "Fail"

# Rank Function
def rank_students():
    if not students:
        print("No Records Available!")
        return
    
    sorted_students = sorted(students.items(),
                             key=lambda x: x[1]["percentage"],
                             reverse=True)
    
    print("\n--- Student Rankings ---")
    rank = 1
    for roll, data in sorted_students:
        print(f"Rank {rank}: {data['name']} - {round(data['percentage'],2)}%")
        rank += 1

while True:
    print("\n===== Smart Student Management System =====")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Display All Students")
    print("6. Rank Students")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        roll = input("Enter Roll Number: ")

        if roll in students:
            print("Student already exists!")
            continue

        name = input("Enter Name: ")

        marks = []
        for i in range(1, 6):
            while True:
                mark = int(input(f"Enter marks for Subject {i} (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Invalid marks! Enter between 0-100.")

        attendance = float(input("Enter Attendance Percentage: "))

        percentage = sum(marks) / len(marks)
        grade = calculate_grade(percentage)

        students[roll] = {
            "name": name,
            "marks": marks,
            "percentage": percentage,
            "grade": grade,
            "attendance": attendance
        }

        print("Student Added Successfully!")

    # Update Student
    elif choice == "2":
        roll = input("Enter Roll Number to Update: ")

        if roll in students:
            print("Enter new marks:")
            marks = []
            for i in range(1, 6):
                mark = int(input(f"Enter marks for Subject {i}: "))
                marks.append(mark)

            attendance = float(input("Enter new Attendance Percentage: "))

            percentage = sum(marks) / len(marks)
            grade = calculate_grade(percentage)

            students[roll]["marks"] = marks
            students[roll]["percentage"] = percentage
            students[roll]["grade"] = grade
            students[roll]["attendance"] = attendance

            print("Student Updated Successfully!")
        else:
            print("Student Not Found!")

    # Delete Student
    elif choice == "3":
        roll = input("Enter Roll Number to Delete: ")

        if roll in students:
            del students[roll]
            print("Student Deleted Successfully!")
        else:
            print("Student Not Found!")

    # Search Student
    elif choice == "4":
        roll = input("Enter Roll Number to Search: ")

        if roll in students:
            data = students[roll]
            print("\nStudent Details:")
            print("Name:", data["name"])
            print("Marks:", data["marks"])
            print("Percentage:", round(data["percentage"], 2))
            print("Grade:", data["grade"])
            print("Attendance:", data["attendance"], "%")

            if data["attendance"] < 75:
                print("⚠ Warning: Low Attendance!")

        else:
            print("Student Not Found!")

    # Display All
    elif choice == "5":
        if not students:
            print("No Records Found!")
        else:
            for roll, data in students.items():
                print("\nRoll:", roll)
                print("Name:", data["name"])
                print("Percentage:", round(data["percentage"], 2))
                print("Grade:", data["grade"])
                print("Attendance:", data["attendance"], "%")

    # Rank Students
    elif choice == "6":
        rank_students()

    # Exit
    elif choice == "7":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Try Again.")
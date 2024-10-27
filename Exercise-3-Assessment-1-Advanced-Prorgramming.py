import tkinter as tk
from tkinter import messagebox

# Function to load student data from the file
def load_student_data(filename):
    with open(filename, 'r') as file:
        num_students = int(file.readline().strip())  # First line is the number of students
        students = []
        for line in file:
            data = line.strip().split(',')
            student_id = int(data[0])
            student_name = data[1]
            coursework = list(map(int, data[2:5]))  # Three coursework marks
            exam = int(data[5])  # Exam mark
            students.append((student_id, student_name, coursework, exam))
        return students, num_students

# Function to calculate total marks, percentage, and grade
def calculate_stats(coursework, exam):
    total_coursework = sum(coursework)
    total_marks = total_coursework + exam
    percentage = (total_marks / 160) * 100  # Max total marks = 160
    grade = get_grade(percentage)
    return total_coursework, exam, percentage, grade

# Function to determine grade from percentage
def get_grade(percentage):
    if percentage >= 70:
        return 'A'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 50:
        return 'C'
    elif percentage >= 40:
        return 'D'
    else:
        return 'F'

# Function to view all student records
def view_all_students():
    total_percentage = 0
    output = ""
    for student in students:
        total_coursework, exam, percentage, grade = calculate_stats(student[2], student[3])
        output += (f"Name: {student[1]}, ID: {student[0]}\n"
                   f"Total Coursework: {total_coursework}, Exam: {exam}\n"
                   f"Percentage: {percentage:.2f}%, Grade: {grade}\n\n")
        total_percentage += percentage
    average_percentage = total_percentage / num_students
    output += f"Class Average Percentage: {average_percentage:.2f}%"
    messagebox.showinfo("All Student Records", output)

# Function to view individual student record
def view_single_student():
    selected_student = student_listbox.curselection()
    if not selected_student:
        messagebox.showerror("Selection Error", "Please select a student.")
        return
    student = students[selected_student[0]]
    total_coursework, exam, percentage, grade = calculate_stats(student[2], student[3])
    output = (f"Name: {student[1]}, ID: {student[0]}\n"
              f"Total Coursework: {total_coursework}, Exam: {exam}\n"
              f"Percentage: {percentage:.2f}%, Grade: {grade}")
    messagebox.showinfo("Student Record", output)

# Function to show student with the highest total score
def show_highest_student():
    highest_student = max(students, key=lambda s: sum(s[2]) + s[3])
    total_coursework, exam, percentage, grade = calculate_stats(highest_student[2], highest_student[3])
    output = (f"Name: {highest_student[1]}, ID: {highest_student[0]}\n"
              f"Total Coursework: {total_coursework}, Exam: {exam}\n"
              f"Percentage: {percentage:.2f}%, Grade: {grade}")
    messagebox.showinfo("Highest Scoring Student", output)

# Function to show student with the lowest total score
def show_lowest_student():
    lowest_student = min(students, key=lambda s: sum(s[2]) + s[3])
    total_coursework, exam, percentage, grade = calculate_stats(lowest_student[2], lowest_student[3])
    output = (f"Name: {lowest_student[1]}, ID: {lowest_student[0]}\n"
              f"Total Coursework: {total_coursework}, Exam: {exam}\n"
              f"Percentage: {percentage:.2f}%, Grade: {grade}")
    messagebox.showinfo("Lowest Scoring Student", output)

# Load student data from file
students, num_students = load_student_data("studentMarks.txt")

# Set up the main window
root = tk.Tk()
root.title("Student Manager")
root.geometry("500x400")

# Label
label = tk.Label(root, text="Select a student to view their record:")
label.pack(pady=10)

# Listbox to show student names
student_listbox = tk.Listbox(root, height=10, width=50)
for student in students:
    student_listbox.insert(tk.END, student[1])
student_listbox.pack(pady=10)

# Buttons for various functionalities
view_all_button = tk.Button(root, text="View All Student Records", command=view_all_students)
view_all_button.pack(pady=5)

view_single_button = tk.Button(root, text="View Selected Student Record", command=view_single_student)
view_single_button.pack(pady=5)

highest_button = tk.Button(root, text="Show Student with Highest Score", command=show_highest_student)
highest_button.pack(pady=5)

lowest_button = tk.Button(root, text="Show Student with Lowest Score", command=show_lowest_student)
lowest_button.pack(pady=5)

# Run the main loop
root.mainloop()

import tkinter as tk  # Import tkinter for GUI
from tkinter import messagebox, ttk  # Import messagebox for alerts and ttk for themed widgets

# Class to represent a student
class Student:
    def __init__(self, code, name, marks):
        # Initialize student attributes
        self.code = code  # Student ID
        self.name = name  # Student name
        self.coursework = sum(marks[:3])  # Total coursework marks (first three marks)
        self.exam = marks[3]  # Exam marks (fourth mark)
        self.total_score = self.coursework + self.exam  # Total score calculation
        self.overall_percentage = (self.total_score / 160) * 100  # Calculate percentage based on total score out of 160
        self.grade = self.calculate_grade()  # Determine the grade based on overall percentage

    # Method to calculate the student's grade based on their overall percentage
    def calculate_grade(self):
        if self.overall_percentage >= 70:
            return 'A'  # Grade A for 70% and above
        elif self.overall_percentage >= 60:
            return 'B'  # Grade B for 60% to 69%
        elif self.overall_percentage >= 50:
            return 'C'  # Grade C for 50% to 59%
        elif self.overall_percentage >= 40:
            return 'D'  # Grade D for 40% to 49%
        else:
            return 'F'  # Grade F for below 40%

# Class to create and manage the student management application
class StudentManagerApp:
    def __init__(self, root):
        self.root = root  # Store reference to the main window
        self.root.title("Student Manager")  # Set window title
        self.root.geometry("600x550")  # Set window size
        self.root.configure(bg="#fafafa")  # Set background color
        self.students = []  # Initialize an empty list to hold student objects
        self.load_data()  # Load student data from file
        
        self.create_widgets()  # Create the GUI components

    # Method to load student data from a file
    def load_data(self):
        try:
            # Open the student marks file in read mode
            with open("studentMarks.txt", "r") as file:
                num_students = int(file.readline().strip())  # Read the first line for the number of students
                for line in file:  # Read each subsequent line
                    parts = line.strip().split(',')  # Split the line by commas
                    code = int(parts[0])  # First part is the student ID
                    name = parts[1]  # Second part is the student name
                    marks = list(map(int, parts[2:]))  # Remaining parts are the marks (converted to integers)
                    self.students.append(Student(code, name, marks))  # Create a Student object and add to the list
        except FileNotFoundError:
            # Display an error message if the file is not found
            messagebox.showerror("Error", "studentMarks.txt file not found.")

    # Method to create the GUI widgets
    def create_widgets(self):
        # Add a title label for the application
        title_label = tk.Label(self.root, text="Student Manager", font=("Arial", 16, "bold"), bg="#fafafa")
        title_label.pack(pady=10)  # Pack the title label with some vertical padding

        # Create a tabbed interface using ttk.Notebook
        notebook = ttk.Notebook(self.root)
        notebook.pack(expand=True, fill='both')  # Pack the notebook to fill the available space

        # Create frames for each tab
        self.all_records_tab = ttk.Frame(notebook)
        self.individual_record_tab = ttk.Frame(notebook)
        self.highest_score_tab = ttk.Frame(notebook)
        self.lowest_score_tab = ttk.Frame(notebook)

        # Add tabs to the notebook
        notebook.add(self.all_records_tab, text="View All Student Records")
        notebook.add(self.individual_record_tab, text="View Individual Student Record")
        notebook.add(self.highest_score_tab, text="Show Highest Score")
        notebook.add(self.lowest_score_tab, text="Show Lowest Score")

        # Set up each tab with its specific widgets
        self.setup_all_records_tab()
        self.setup_individual_record_tab()
        self.setup_highest_score_tab()
        self.setup_lowest_score_tab()

    # Method to set up the All Records tab
    def setup_all_records_tab(self):
        label = ttk.Label(self.all_records_tab, text="All Student Records", font=("Arial", 14, "bold"))
        label.pack(pady=10)  # Pack the label with vertical padding

        # Text area to display all student records, initially disabled for editing
        self.all_records_text = tk.Text(self.all_records_tab, width=60, height=15, wrap="word", state="disabled", bg="#f8f8ff")
        self.all_records_text.pack(pady=10)  # Pack the text area

        # Button to view all records
        btn_view_all = ttk.Button(self.all_records_tab, text="View All Records", command=self.view_all_records)
        btn_view_all.pack()  # Pack the button

    # Method to view all student records in the text area
    def view_all_records(self):
        self.all_records_text.config(state="normal")  # Enable the text area for editing
        self.all_records_text.delete("1.0", tk.END)  # Clear any existing text

        # Calculate total and average percentage of students
        total_percentage = sum(student.overall_percentage for student in self.students)
        average_percentage = total_percentage / len(self.students) if self.students else 0

        records = ""  # Initialize an empty string to hold records
        for student in self.students:
            # Append each student's details to the records string
            records += (f"Name: {student.name}, ID: {student.code}\n"
                        f"  Coursework: {student.coursework}, Exam: {student.exam}, "
                        f"Percentage: {student.overall_percentage:.2f}%, Grade: {student.grade}\n\n")
        records += f"Total students: {len(self.students)}, Average percentage: {average_percentage:.2f}%"
        
        self.all_records_text.insert(tk.END, records)  # Insert records into the text area
        self.all_records_text.config(state="disabled")  # Disable editing again

    # Method to set up the Individual Record tab
    def setup_individual_record_tab(self):
        label = ttk.Label(self.individual_record_tab, text="View Individual Student Record:", font=("Arial", 14, "bold"))
        label.pack(pady=10)  # Pack the label with vertical padding

        # Combobox to select a student from the list
        self.student_list = ttk.Combobox(self.individual_record_tab, values=[f"{s.name} (ID: {s.code})" for s in self.students], state="readonly")
        self.student_list.pack(pady=5)  # Pack the combobox
        
        # Button to view the selected student's record
        btn_view_individual = ttk.Button(self.individual_record_tab, text="View Selected Record", command=self.view_individual_record)
        btn_view_individual.pack(pady=5)  # Pack the button

        # Text area to display individual student's record, initially disabled for editing
        self.individual_record_text = tk.Text(self.individual_record_tab, width=60, height=10, wrap="word", state="disabled", bg="#f8f8ff")
        self.individual_record_text.pack(pady=10)  # Pack the text area

    # Method to view the individual record of the selected student
    def view_individual_record(self):
        selected_idx = self.student_list.current()  # Get the index of the selected student
        if selected_idx >= 0:  # Ensure a valid selection
            student = self.students[selected_idx]  # Get the selected student object
            # Format the student's details into a string
            record = (f"Name: {student.name}, ID: {student.code}\n"
                      f"Coursework: {student.coursework}, Exam: {student.exam}, "
                      f"Percentage: {student.overall_percentage:.2f}%, Grade: {student.grade}")
            self.individual_record_text.config(state="normal")  # Enable the text area for editing
            self.individual_record_text.delete("1.0", tk.END)  # Clear existing text
            self.individual_record_text.insert(tk.END, record)  # Insert the student's record
            self.individual_record_text.config(state="disabled")  # Disable editing again

    # Method to set up the Highest Score tab
    def setup_highest_score_tab(self):
        label = ttk.Label(self.highest_score_tab, text="Top Scoring Student", font=("Arial", 14, "bold"))
        label.pack(pady=10)  # Pack the label with vertical padding

        # Text area to display the top-scoring student's record, initially disabled
        self.highest_score_text = tk.Text(self.highest_score_tab, width=60, height=10, wrap="word", state="disabled", bg="#f8f8ff")
        self.highest_score_text.pack(pady=10)  # Pack the text area

        # Button to show the highest scoring student
        btn_highest_score = ttk.Button(self.highest_score_tab, text="Show Highest Score", command=self.show_highest_score)
        btn_highest_score.pack()  # Pack the button

    # Method to show the highest scoring student in the text area
    def show_highest_score(self):
        if not self.students:  # Check if the student list is empty
            messagebox.showinfo("No Data", "No student data available.")  # Show info message if no data
            return

        # Find the student with the highest total score
        top_student = max(self.students, key=lambda s: s.total_score)
        # Format the student's details into a string
        record = (f"Name: {top_student.name}, ID: {top_student.code}\n"
                  f"Coursework: {top_student.coursework}, Exam: {top_student.exam}, "
                  f"Percentage: {top_student.overall_percentage:.2f}%, Grade: {top_student.grade}")
        self.highest_score_text.config(state="normal")  # Enable the text area for editing
        self.highest_score_text.delete("1.0", tk.END)  # Clear existing text
        self.highest_score_text.insert(tk.END, record)  # Insert the top student's record
        self.highest_score_text.config(state="disabled")  # Disable editing again

    # Method to set up the Lowest Score tab
    def setup_lowest_score_tab(self):
        label = ttk.Label(self.lowest_score_tab, text="Lowest Scoring Student", font=("Arial", 14, "bold"))
        label.pack(pady=10)  # Pack the label with vertical padding

        # Text area to display the lowest scoring student's record, initially disabled
        self.lowest_score_text = tk.Text(self.lowest_score_tab, width=60, height=10, wrap="word", state="disabled", bg="#f8f8ff")
        self.lowest_score_text.pack(pady=10)  # Pack the text area

        # Button to show the lowest scoring student
        btn_lowest_score = ttk.Button(self.lowest_score_tab, text="Show Lowest Score", command=self.show_lowest_score)
        btn_lowest_score.pack()  # Pack the button

    # Method to show the lowest scoring student in the text area
    def show_lowest_score(self):
        if not self.students:  # Check if the student list is empty
            messagebox.showinfo("No Data", "No student data available.")  # Show info message if no data
            return

        # Find the student with the lowest total score
        bottom_student = min(self.students, key=lambda s: s.total_score)
        # Format the student's details into a string
        record = (f"Name: {bottom_student.name}, ID: {bottom_student.code}\n"
                  f"Coursework: {bottom_student.coursework}, Exam: {bottom_student.exam}, "
                  f"Percentage: {bottom_student.overall_percentage:.2f}%, Grade: {bottom_student.grade}")
        self.lowest_score_text.config(state="normal")  # Enable the text area for editing
        self.lowest_score_text.delete("1.0", tk.END)  # Clear existing text
        self.lowest_score_text.insert(tk.END, record)  # Insert the lowest student's record
        self.lowest_score_text.config(state="disabled")  # Disable editing again

# Main function to run the application
if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    app = StudentManagerApp(root)  # Instantiate the StudentManagerApp class
    root.mainloop()  # Start the main event loop

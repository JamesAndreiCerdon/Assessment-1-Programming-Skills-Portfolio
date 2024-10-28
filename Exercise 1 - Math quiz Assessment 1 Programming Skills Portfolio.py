import tkinter as tk
import random

# Main class to handle the quiz
class MathsQuizApp:
    def __init__(self, root):
        self.root = root  # Store the root window
        self.root.title("Maths Quiz")  # Set the window title
        self.root.geometry("350x250")  # Set the initial window size
        self.score = 0  # Initialize the score
        self.questions_count = 0  # Initialize the question count
        self.level = 1  # Set the default difficulty level to easy
        self.create_widgets()  # Create the widgets in the GUI

    def create_widgets(self):
        self.frame = tk.Frame(self.root)  # Create a frame to hold all widgets
        self.frame.pack(expand=True)  # Pack the frame to expand in the window

        # Display the difficulty level menu
        self.displayMenu()

    def displayMenu(self):
        self.clear_frame()  # Clear any existing widgets from the frame
        
        # Simple title for title and difficulty selection
        tk.Label(self.frame, text="Math Quiz", font=("Helvetica", 14)).pack(pady=0)
        tk.Label(self.frame, text="Select Difficulty Level", font=("Helvetica", 14)).pack(pady=10)
        
        # Difficulty level buttons
        button_frame = tk.Frame(self.frame)  # Create a frame for buttons
        button_frame.pack(pady=10)  # Pack the button frame
        tk.Button(button_frame, text="1. Easy", command=lambda: self.start_quiz(1), width=15).pack(pady=5)
        tk.Button(button_frame, text="2. Moderate", command=lambda: self.start_quiz(2), width=15).pack(pady=5)
        tk.Button(button_frame, text="3. Advanced", command=lambda: self.start_quiz(3), width=15).pack(pady=5)

    def start_quiz(self, level):
        self.level = level  # Set the selected difficulty level
        self.score = 0  # Reset the score for the new quiz
        self.questions_count = 0  # Reset the question count
        self.next_question()  # Load the first question

    def randomInt(self):
        # Generate a random integer based on the selected difficulty level
        if self.level == 1:  # Easy level
            return random.randint(1, 9)
        elif self.level == 2:  # Moderate level
            return random.randint(10, 99)
        else:  # Advanced level
            return random.randint(1000, 9999)

    def decideOperation(self):
        # Randomly decide whether to perform addition or subtraction
        return random.choice(["+", "-"])

    def next_question(self):
        if self.questions_count < 10:  # Check if there are less than 10 questions answered
            self.questions_count += 1  # Increment the question count
            self.clear_frame()  # Clear the frame for the new question
            self.num1 = self.randomInt()  # Generate the first random number
            self.num2 = self.randomInt()  # Generate the second random number
            self.operation = self.decideOperation()  # Decide the operation
            self.answer = self.num1 + self.num2 if self.operation == "+" else self.num1 - self.num2  # Calculate the answer

            # Question prompt
            question_text = f"{self.num1} {self.operation} {self.num2} = "  # Format the question
            tk.Label(self.frame, text=f"Question {self.questions_count}", font=("Helvetica", 12)).pack(pady=5)
            tk.Label(self.frame, text=question_text, font=("Helvetica", 14)).pack(pady=5)

            # Answer entry
            self.answer_entry = tk.Entry(self.frame, justify="center")  # Entry field for user's answer
            self.answer_entry.pack(pady=5)

            # Submit button and feedback label
            self.submit_button = tk.Button(self.frame, text="Submit", command=self.check_answer)  # Button to submit answer
            self.submit_button.pack(pady=5)
            self.feedback_label = tk.Label(self.frame, text="", font=("Helvetica", 10))  # Label for feedback
            self.feedback_label.pack(pady=5)
        else:
            self.displayResults()  # Display results when quiz is complete

    def check_answer(self):
        user_answer = self.answer_entry.get()  # Get the user's input from the entry
        try:
            if int(user_answer) == self.answer:  # Check if the answer is correct
                self.feedback_label.config(text="Correct!", fg="green")  # Provide feedback
                self.score += 10  # Increment score for correct answer
                self.root.after(1000, self.next_question)  # Move to the next question after 1 second
            else:
                self.feedback_label.config(text="Incorrect! Try again.", fg="red")  # Incorrect feedback
                self.submit_button.config(command=self.check_answer_second_try)  # Change button command for second try
        except ValueError:
            self.feedback_label.config(text="Enter a valid number.", fg="red")  # Handle invalid input

    def check_answer_second_try(self):
        user_answer = self.answer_entry.get()  # Get user's answer again
        try:
            if int(user_answer) == self.answer:  # Check if the second attempt is correct
                self.feedback_label.config(text="Correct! (Second try)", fg="green")  # Feedback for correct answer
                self.score += 5  # Increment score for second try
            else:
                self.feedback_label.config(text=f"Incorrect! Correct answer was {self.answer}", fg="red")  # Feedback for wrong answer
            self.root.after(1000, self.next_question)  # Move to the next question after 1 second
        except ValueError:
            self.feedback_label.config(text="Enter a valid number.", fg="red")  # Handle invalid input

    def displayResults(self):
        self.clear_frame()  # Clear the frame for results display
        result_message = f"Your final score is {self.score}/100.\n"  # Show final score
        # Determine grade based on score
        grade = "A+" if self.score > 90 else "A" if self.score > 80 else "B" if self.score > 70 else "C" if self.score > 60 else "D"
        result_message += f"Your grade: {grade}"  # Append grade to result message

        # Result display and play again option
        tk.Label(self.frame, text="Quiz Complete!", font=("Helvetica", 14)).pack(pady=5)
        tk.Label(self.frame, text=result_message, font=("Helvetica", 12)).pack(pady=5)
        tk.Button(self.frame, text="Play Again", command=self.displayMenu).pack(pady=10)  # Button to play again

    def clear_frame(self):
        for widget in self.frame.winfo_children():  # Iterate through all widgets in the frame
            widget.destroy()  # Destroy each widget to clear the frame

# Run the application
if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    app = MathsQuizApp(root)  # Instantiate the MathsQuizApp class
    root.mainloop()  # Start the Tkinter event loop

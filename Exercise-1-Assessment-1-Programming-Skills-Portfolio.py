import tkinter as tk
import random

# Main class to handle the quiz
class MathsQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Maths Quiz")
        self.score = 0
        self.questions_count = 0
        self.level = 1
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        # Difficulty level menu
        self.displayMenu()

    def displayMenu(self):
        self.clear_frame()
        tk.Label(self.frame, text="DIFFICULTY LEVEL").pack()

        tk.Button(self.frame, text="1. Easy", command=lambda: self.start_quiz(1)).pack(pady=5)
        tk.Button(self.frame, text="2. Moderate", command=lambda: self.start_quiz(2)).pack(pady=5)
        tk.Button(self.frame, text="3. Advanced", command=lambda: self.start_quiz(3)).pack(pady=5)

    def start_quiz(self, level):
        self.level = level
        self.score = 0
        self.questions_count = 0
        self.next_question()

    def randomInt(self):
        if self.level == 1:
            return random.randint(1, 9)
        elif self.level == 2:
            return random.randint(10, 99)
        else:
            return random.randint(1000, 9999)

    def decideOperation(self):
        return random.choice(["+", "-"])

    def next_question(self):
        if self.questions_count < 10:
            self.questions_count += 1
            self.clear_frame()
            self.num1 = self.randomInt()
            self.num2 = self.randomInt()
            self.operation = self.decideOperation()
            self.answer = self.num1 + self.num2 if self.operation == "+" else self.num1 - self.num2

            question = f"{self.num1} {self.operation} {self.num2} = "
            tk.Label(self.frame, text=f"Question {self.questions_count}:").pack()
            self.problem_label = tk.Label(self.frame, text=question)
            self.problem_label.pack(pady=10)

            self.answer_entry = tk.Entry(self.frame)
            self.answer_entry.pack()

            self.submit_button = tk.Button(self.frame, text="Submit", command=self.check_answer)
            self.submit_button.pack(pady=10)

            self.feedback_label = tk.Label(self.frame, text="")
            self.feedback_label.pack(pady=10)
        else:
            self.displayResults()

    def check_answer(self):
        user_answer = self.answer_entry.get()
        try:
            if int(user_answer) == self.answer:
                self.feedback_label.config(text="Correct!", fg="green")
                self.score += 10
                self.root.after(1000, self.next_question)
            else:
                self.feedback_label.config(text="Incorrect! Try again.", fg="red")
                self.submit_button.config(command=self.check_answer_second_try)
        except ValueError:
            self.feedback_label.config(text="Please enter a valid number.", fg="red")

    def check_answer_second_try(self):
        user_answer = self.answer_entry.get()
        try:
            if int(user_answer) == self.answer:
                self.feedback_label.config(text="Correct! (on second attempt)", fg="green")
                self.score += 5
            else:
                self.feedback_label.config(text=f"Incorrect! The correct answer was {self.answer}", fg="red")
            self.root.after(1000, self.next_question)
        except ValueError:
            self.feedback_label.config(text="Please enter a valid number.", fg="red")

    def displayResults(self):
        self.clear_frame()
        result_message = f"Your final score is {self.score}/100.\n"
        if self.score > 90:
            grade = "A+"
        elif self.score > 80:
            grade = "A"
        elif self.score > 70:
            grade = "B"
        elif self.score > 60:
            grade = "C"
        else:
            grade = "D"
        result_message += f"Your grade: {grade}"

        tk.Label(self.frame, text=result_message).pack(pady=10)

        play_again_button = tk.Button(self.frame, text="Play Again", command=self.displayMenu)
        play_again_button.pack(pady=10)

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = MathsQuizApp(root)
    root.mainloop()

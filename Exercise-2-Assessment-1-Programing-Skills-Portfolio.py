import tkinter as tk
import random

# Function to load jokes from the file
def load_jokes(filename):
    with open(filename, "r", encoding="utf-8") as file:
        jokes = file.readlines()
    return [joke.strip().split("?") for joke in jokes if "?" in joke]


# Function to display a random joke
def show_setup():
    global current_joke
    current_joke = random.choice(jokes)
    setup_label.config(text=current_joke[0] + "?")
    punchline_label.config(text="")  # Clear punchline

# Function to display the punchline
def show_punchline():
    punchline_label.config(text=current_joke[1])

# Function to quit the program
def quit_program():
    root.quit()

# Load jokes from file
jokes = load_jokes("randomJokes.txt")
current_joke = None

# Set up the main tkinter window
root = tk.Tk()
root.title("Alexa, Tell Me a Joke")
root.geometry("400x200")

# Setup display
setup_label = tk.Label(root, text="", font=("Arial", 14), wraplength=380)
setup_label.pack(pady=20)

# Punchline display
punchline_label = tk.Label(root, text="", font=("Arial", 12), wraplength=380)
punchline_label.pack(pady=10)

# Button to show the joke setup
setup_button = tk.Button(root, text="Alexa, tell me a Joke", command=show_setup)
setup_button.pack(pady=5)

# Button to show the punchline
punchline_button = tk.Button(root, text="Show Punchline", command=show_punchline)
punchline_button.pack(pady=5)

# Button to quit the application
quit_button = tk.Button(root, text="Quit", command=quit_program)
quit_button.pack(pady=5)

# Run the tkinter event loop
root.mainloop()

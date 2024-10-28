import tkinter as tk
import random

# Function to load jokes from the file
def load_jokes(filename):
    # Open the specified file in read mode with UTF-8 encoding
    with open(filename, "r", encoding="utf-8") as file:
        # Read all lines from the file
        jokes = file.readlines()
    # Return a list of jokes, each joke split into setup and punchline at the '?'
    return [joke.strip().split("?") for joke in jokes if "?" in joke]

# Function to display a random joke setup
def show_setup():
    global current_joke  # Declare current_joke as global to access it outside the function
    # Select a random joke from the list of jokes
    current_joke = random.choice(jokes)
    # Display the setup part of the joke in the setup_label
    setup_label.config(text=current_joke[0] + "?")
    # Clear the punchline label
    punchline_label.config(text="")  # Clear punchline

# Function to display the punchline of the current joke
def show_punchline():
    # Set the text of the punchline label to the punchline part of the current joke
    punchline_label.config(text=current_joke[1])

# Function to quit the program
def quit_program():
    # Exit the Tkinter event loop and close the application
    root.quit()

# Load jokes from the specified text file
jokes = load_jokes("randomJokes.txt")
current_joke = None  # Initialize current_joke variable to store the joke being displayed

# Set up the main tkinter window
root = tk.Tk()  # Create a new Tkinter window
root.title("Exercise 2 - Alexa, Tell me a Joke")  # Set the window title
root.geometry("400x400")  # Set the window size
root.configure(bg="white")  # Set the background color of the window to white

# Title label for the application
title_label = tk.Label(root, text="Alexa, Tell me a Joke", font=("Arial", 18), bg="white")
title_label.pack(pady=10)  # Add the title label to the window with some vertical padding

# Setup display label for the joke setup
setup_label = tk.Label(root, text="", font=("Arial", 14), bg="white", wraplength=250)
setup_label.pack(pady=10)  # Add the setup label to the window with some vertical padding

# Punchline display label
punchline_label = tk.Label(root, text="", font=("Arial", 12), bg="white", wraplength=250)
punchline_label.pack(pady=5)  # Add the punchline label to the window with some vertical padding

# Create a frame to hold buttons, set the background to white
button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=20)  # Add the button frame to the window with some vertical padding

# Button to show the joke setup
setup_button = tk.Button(button_frame, text="Alexa, tell me a Joke", command=show_setup, width=15)
setup_button.pack(side=tk.LEFT, padx=5)  # Add the setup button to the button frame, aligned to the left with some horizontal padding

# Button to show the punchline of the joke
punchline_button = tk.Button(button_frame, text="Show Punchline", command=show_punchline, width=15)
punchline_button.pack(side=tk.LEFT, padx=5)  # Add the punchline button to the button frame, aligned to the left with some horizontal padding

# Run the tkinter event loop, waiting for user interactions
root.mainloop()

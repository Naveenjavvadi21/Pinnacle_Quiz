import tkinter as tk
from tkinter import messagebox

# Quiz Questions
quiz_data = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Chennai", "Kolkata"],
        "answer": "Delhi"
    },
    {
        "question": "Which language is used for Web Development?",
        "options": ["Python", "HTML", "C", "Java"],
        "answer": "HTML"
    },
    {
        "question": "Who developed Python?",
        "options": [
            "Dennis Ritchie",
            "James Gosling",
            "Guido van Rossum",
            "Bjarne Stroustrup"
        ],
        "answer": "Guido van Rossum"
    },
    {
        "question": "2 + 2 = ?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    }
]

# Variables
current_question = 0
score = 0

# Check Answer
def check_answer():

    global current_question
    global score

    selected = option_var.get()

    if selected == quiz_data[current_question]["answer"]:
        score += 1

    current_question += 1

    if current_question < len(quiz_data):
        display_question()
    else:
        show_result()

# Display Question
def display_question():

    question_label.config(
        text=quiz_data[current_question]["question"]
    )

    option_var.set(None)

    options = quiz_data[current_question]["options"]

    for i in range(4):
        radio_buttons[i].config(
            text=options[i],
            value=options[i]
        )

# Show Result
def show_result():

    result = (
        f"Quiz Completed!\n\n"
        f"Your Score: {score}/{len(quiz_data)}"
    )

    messagebox.showinfo("Result", result)

    root.destroy()

# GUI Window
root = tk.Tk()

root.title("Python Quiz Platform")
root.geometry("500x400")
root.config(bg="white")

# Heading
title = tk.Label(
    root,
    text="Quiz Application",
    font=("Arial", 20, "bold"),
    bg="white"
)

title.pack(pady=20)

# Question Label
question_label = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    wraplength=400,
    bg="white"
)

question_label.pack(pady=20)

# Option Variable
option_var = tk.StringVar()

# Radio Buttons
radio_buttons = []

for i in range(4):

    rb = tk.Radiobutton(
        root,
        text="",
        variable=option_var,
        value="",
        font=("Arial", 12),
        bg="white"
    )

    rb.pack(anchor="w", padx=50, pady=5)

    radio_buttons.append(rb)

# Next Button
next_button = tk.Button(
    root,
    text="Next",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    command=check_answer
)

next_button.pack(pady=20)

# Start Quiz
display_question()

# Run Application
root.mainloop()
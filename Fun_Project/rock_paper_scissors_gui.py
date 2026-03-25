import tkinter as tk
import random

# Main window
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("400x400")
root.config(bg="#1e1e2f")

choices = ["rock", "paper", "scissors"]

# Title
title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"), bg="#1e1e2f", fg="white")
title.pack(pady=20)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14), bg="#1e1e2f", fg="white")
result_label.pack(pady=20)

# Function to play
def play(user_choice):
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie! 🤝"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "You Win! 🎉"
    else:
        result = "Computer Wins! 🤖"

    result_label.config(
        text=f"You: {user_choice}\nComputer: {computer_choice}\n\n{result}"
    )

# Buttons
btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=20)

rock_btn = tk.Button(btn_frame, text="🪨 Rock", width=10, height=2, bg="#ff6b6b", fg="white",
                     command=lambda: play("rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(btn_frame, text="📄 Paper", width=10, height=2, bg="#4ecdc4", fg="white",
                      command=lambda: play("paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(btn_frame, text="✂️ Scissors", width=10, height=2, bg="#ffe66d", fg="black",
                         command=lambda: play("scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Exit button
exit_btn = tk.Button(root, text="Exit", bg="#ff4757", fg="white", command=root.quit)
exit_btn.pack(pady=20)

# Run app
root.mainloop()
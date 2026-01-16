import tkinter as tk
import random

user_point = 0
com_point = 0
current_theme = "dark"

EMOJI = {
    "rock": "🪨",
    "paper": "📄",
    "scissor": "✂️"
}

def player(user_choice):
    global user_point , com_point
    com_choice = random.choice(['rock','paper','scissor'])

    user_label.config(text=f"You: {EMOJI[user_choice]}")
    com_label.config(text=f"Computer: {EMOJI[com_choice]}")

    if user_choice == com_choice:
        result_label.config(text="Tie 🤝", fg="orange")
    elif (user_choice == "rock" and com_choice == "scissor") or \
         (user_choice == "paper" and com_choice == "rock") or \
         (user_choice == "scissor" and com_choice == "paper"):
        result_label.config(text="You Win 🏆", fg="green")
        user_point += 1
    else:
        result_label.config(text="Computer Wins 💀", fg="red")
        com_point += 1

    score_label.config(text=f"score -> you: {user_point} and computer: {com_point}")

#reset
def reset_game():
    global user_point, com_point
    user_point = 0
    com_point = 0

    user_label.config(text="You: ❔")
    com_label.config(text="Computer: ❔")
    result_label.config(text="")
    score_label.config(text="Score → You: 0 | Computer: 0")

def toggle_theme():
    global current_theme

    if current_theme == "dark":
        current_theme = "light"
        bg = "white"
        fg = "black"
    else:
        current_theme = "dark"
        bg = "#1e1e1e"
        fg = "white"

    # Apply theme to all widgets
    root.config(bg=bg)
    title.config(bg=bg, fg=fg)
    user_label.config(bg=bg, fg=fg)
    com_label.config(bg=bg, fg=fg)
    result_label.config(bg=bg, fg=fg)
    score_label.config(bg=bg, fg="cyan" if current_theme == "dark" else "blue")
    button_frame.config(bg=bg)




root = tk.Tk()
root.title("ROCK PAPER SCISSOR")
root.geometry("500x500")

title = tk.Label(
    root,
    text="ROCK-PAPER-SCISSORS",
    font=("Arial", 20, "bold italic"),
    fg="white",
    bg="#1e1e1e"
)
title.pack(pady=20)

user_label = tk.Label(root, text="You: ❔", font=("Arial", 18), fg="white", bg="#1e1e1e")
user_label.pack()

com_label = tk.Label(root, text="Computer: ❔", font=("Arial", 18), fg="white", bg="#1e1e1e")
com_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 22, "bold"), bg="#1e1e1e")
result_label.pack(pady=20)

score_label = tk.Label(root, text="Score → You: 0 | Computer: 0", font=("Arial", 16), fg="cyan", bg="#1e1e1e")
score_label.pack(pady=10)


button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=20)

tk.Button(button_frame, text="🪨 Rock", font=("Arial", 16), width=10,
          command=lambda: player("rock")).grid(row=0, column=0, padx=10)

tk.Button(button_frame, text="📄 Paper", font=("Arial", 16), width=10,
          command=lambda: player("paper")).grid(row=0, column=1, padx=10)

tk.Button(button_frame, text="✂️ Scissor", font=("Arial", 16), width=10,
          command=lambda: player("scissor")).grid(row=0, column=2, padx=10)
# RESET BUTTON
tk.Button(root, text="Reset Game", font=("Arial", 14),
          bg="red", fg="white", command=reset_game).pack(pady=10)

tk.Button(root, text="Toggle Theme", font=("Arial", 14),
          bg="gray", fg="white", command=toggle_theme).pack(pady=10)




root.mainloop()
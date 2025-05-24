import tkinter as tk
import random
import tkinter.messagebox as msgbox
import threading
import time
from playsound import playsound  # pip install playsound==1.2.2

# Messages and auto-type content
evil_texts = [
    "Can't touch this!",
    "Muahaha!",
    "Too slow!",
    "Run away!",
    "You wish!",
    "It’s watching you...",
    "The end is near...",
    "Don't click again...",
]

# Flash background color
def flash_background():
    while True:
        color = random.choice(["black", "darkred", "purple", "maroon"])
        root.configure(bg=color)
        time.sleep(0.2)

# Play scary sound
def play_sound():
    try:
        playsound("scary.mp3")
    except:
        pass

# Move button randomly
def move_button(event):
    new_x = random.randint(0, 300)
    new_y = random.randint(0, 300)
    evil_button.place(x=new_x, y=new_y)
    evil_button.config(text=random.choice(evil_texts))
    threading.Thread(target=play_sound, daemon=True).start()

# Endless popups
def infinite_popups():
    while True:
        msgbox.showerror("ERROR", "You shouldn't have clicked it...")

# Auto-type creepy message on screen
def auto_typing():
    messages = [
        "They're coming...",
        "Behind you!",
        "RUN NOW!",
        "It’s too late...",
        "You are not alone.",
        "System breach detected.",
    ]
    while True:
        msg = random.choice(messages)
        label = tk.Label(root, text=msg, fg="white", bg="black", font=("Courier", 10, "bold"))
        x = random.randint(0, 300)
        y = random.randint(0, 300)
        label.place(x=x, y=y)
        time.sleep(0.5)

# On click prank
def button_clicked():
    msgbox.showerror("FATAL ERROR", "Critical System Breach!")
    msgbox.showinfo("Joke's on you", "This will never end 😈")
    threading.Thread(target=infinite_popups, daemon=True).start()

# GUI setup
root = tk.Tk()
root.title("FINAL EVIL BUTTON 😈")
root.geometry("400x400")
root.configure(bg="black")

evil_button = tk.Button(root, text="Click me if you can!", bg="darkred", fg="white", font=("Helvetica", 12, "bold"))
evil_button.place(x=150, y=150)

# Bindings and events
evil_button.bind("<Enter>", move_button)
evil_button.config(command=button_clicked)

# Background threads for effects
threading.Thread(target=flash_background, daemon=True).start()
threading.Thread(target=auto_typing, daemon=True).start()

root.mainloop()

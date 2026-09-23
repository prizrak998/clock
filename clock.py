import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.title("Часы")
root.geometry("300x150")

def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.config(text=f"Время: {current_time}")
    time_label.after(1000, update_time)

time_label = tk.Label(root, font=("Arial", 28))
time_label.pack(pady=50)

update_time()
root.mainloop()
import tkinter as tk
import time

master_window = tk.Tk()
master_window.title("Racheal's Digital Clock")


def update_clock():
    clock_time = time.strftime('%I:%M:%S %p')
    clock_label.config(text=clock_time)
    clock_label.after(1000, update_clock)


clock_label = tk.Label(
    master_window, font="Helvetica 80 bold", foreground='black', bg='grey')
clock_label.pack()

update_clock()
master_window.mainloop()

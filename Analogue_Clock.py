import tkinter as tk
import time
import math

master_window = tk.Tk()
master_window.title("Racheal's Analogue Clock")
master_window.geometry("400x400")


def update_clock():
    hours = int(time.strftime("%I"))
    minutes = int(time.strftime("%M"))
    seconds = int(time.strftime("%S"))

    # Getting the seconds hand
    seconds_x = seconds_hand_len * \
        math.sin(math.radians(seconds * 6)) + center_x
    seconds_y = -1 * seconds_hand_len * \
        math.cos(math.radians(seconds * 6)) + center_y
    canvas.coords(seconds_hand, center_x, center_y, seconds_x, seconds_y)

    # Getting the minutes hand
    minutes_x = minutes_hand_len * \
        math.sin(math.radians(minutes * 6)) + center_x
    minutes_y = -1 * minutes_hand_len * \
        math.cos(math.radians(minutes * 6)) + center_y
    canvas.coords(minutes_hand, center_x, center_y, minutes_x, minutes_y)

    # Getting the hours hand
    hours_x = hours_hand_len * \
        math.sin(math.radians(hours * 30)) + center_x
    hours_y = -1 * hours_hand_len * \
        math.cos(math.radians(hours * 30)) + center_y
    canvas.coords(hours_hand, center_x, center_y, hours_x, hours_y)
    master_window.after(1000, update_clock)


canvas = tk.Canvas(master_window, width=400, height=400, bg="black")
canvas.pack(expand=True, fill="both")

# Background
bg = tk.PhotoImage(file="clock_face_grey.png")
canvas.create_image(200, 200, image=bg)

# Clock hands - lengths
center_x = 200
center_y = 200
seconds_hand_len = 160
minutes_hand_len = 80
hours_hand_len = 60

# Drawing hands
seconds_hand = canvas.create_line(
    200, 200, 200 + seconds_hand_len, 200 + seconds_hand_len, width=1.5, fill="blue")

minutes_hand = canvas.create_line(
    200, 200, 200 + minutes_hand_len, 200 + minutes_hand_len, width=3, fill="black")

hours_hand = canvas.create_line(
    200, 200, 200 + hours_hand_len, 200 + hours_hand_len, width=5, fill="black")

update_clock()
master_window.mainloop()

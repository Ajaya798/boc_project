from tkinter import Tk, Label
import time
import threading

master = Tk()
master.title("CLOCK")

def write_time_to_file(time_str):
    with open("present_time.txt", "a") as file:
        file.write(time_str + "\n")

def read_time_from_file():
    try:
        with open("present_time.txt", "r") as file:
            lines = file.readlines()
            return lines[-1].strip() if lines else "00:00:00 AM"
    except FileNotFoundError:
        return "00:00:00 AM"

def time_please():
    while True:
        timeVar = time.strftime("%I:%M:%S %p ")
        clock.config(text=timeVar)
        write_time_to_file(timeVar)

        if "AM" in timeVar:
            message = "Good morning!"
        else:
            message = "Good evening!"

        greeting.config(text=message)
        time.sleep(1)

def start_clock():
    thread = threading.Thread(target=time_please)
    thread.daemon = True
    thread.start()

clock = Label(master, font=("Algerian", 100), background="white", foreground="black")
clock.pack()

greeting = Label(master, font=("Algerian", 60), background="black", foreground="white")
greeting.pack()

initial_time = read_time_from_file()
clock.config(text=initial_time)

start_clock()

master.mainloop()

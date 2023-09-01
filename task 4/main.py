import sounddevice
from scipy.io.wavfile import write
import tkinter as tk
from tkinter import filedialog, ttk


def voice(seconds, file):
    print("Recording started")
    rec = sounddevice.rec((seconds * 44100), samplerate=44100, channels=2)
    sounddevice.wait()
    write(file, 44100, rec)
    print("Recording completed")


def start_recording():
    time = int(time_entry.get())
    name = name_entry.get() + ".File"
    voice(time, name)


root = tk.Tk()
root.geometry("400x400")
root.title("Sound Recorder")

bg = tk.PhotoImage(file=r"C:\Users\Akshada\PycharmProjects\task 4\back.jpeg")

background_label = tk.Label(root, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
time_label = tk.Label(root, text="Enter the time to record (in seconds):")

time_entry = tk.Entry(root)


name_label = tk.Label(root, text="Enter the name of the file:")

name_entry = tk.Entry(root)

record_button = tk.Button(root, text="Start Recording", command=start_recording)


root.configure(bg='lightgrey')
time_label.config(bg='pink', fg='black')
name_label.config(bg='pink', fg='black')
record_button.config(bg='pink', fg='black')

time_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')
time_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')

name_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')
name_entry.grid(row=1, column=1, padx=10, pady=10, sticky='w')

record_button.grid(row=2, columnspan=2, padx=10, pady=20)
style = ttk.Style()
style.theme_use("winnative")
root.mainloop()

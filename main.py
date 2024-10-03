import pyautogui
import time
import threading
import tkinter as tk

clicking_event = threading.Event()

window_title = "Auto Clicker"
clicker_interval = 3 # In Seconds
footer_text = "This text will be shown at the bottom of the window."

def click_mouse():
    while clicking_event.is_set():
        current_position = pyautogui.position()
        pyautogui.click(current_position)
        time.sleep(clicker_interval)

def start_clicking():
    if not clicking_event.is_set():  
        clicking_event.set() 
        status_label.config(text="Running")
        thread = threading.Thread(target=click_mouse)
        thread.start()

def stop_clicking():
    clicking_event.clear() 
    status_label.config(text="Stopped") 

# Create the GUI window
window = tk.Tk()
window.title(window_title)

# Create start and stop buttons
start_button = tk.Button(window, text="Start Clicking", command=start_clicking)
start_button.pack(pady=10)

stop_button = tk.Button(window, text="Stop Clicking", command=stop_clicking)
stop_button.pack(pady=10)

# Create a label to show the current status (Running or Stopped)
status_label = tk.Label(window, text="Stopped", font=("Helvetica", 12))
status_label.pack(pady=10)

info_label = tk.Label(window, text=footer_text, font=("Helvetica", 12))
info_label.pack(pady=10)

# Run the GUI loop
window.mainloop()

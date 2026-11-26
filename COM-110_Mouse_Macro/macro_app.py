# Using tkinter for UI interface and button interactions
# Using perf_counter for time, or determined sequence through comparison
import tkinter as tk
from time import perf_counter
is_recording = False

# function/action for toggle recording button
def toggle_recording():
    # local updates to var should update the global var
    global is_recording
    is_recording = not is_recording
    if is_recording:
        button.config(text="Stop Recording")
    else:
        button.config(text="Start Recording")

# function/ stores cursor positon of event only when recording, in the dict
actions:list[dict[str:int|float]] = []
def record_click(event):
    if is_recording:
        # stores pointers horizantal and vertical positon in pixels
        # relative to SCREENS top left corner
        # AND time
        actions.append({"x": event.x_root,"y": event.y_root, "time": perf_counter()})
        print(actions)

# funct/ A preivew screen display, both wating and finshed display
def show_preview():
    preview_button.config(text="Preview action happened!")

def start_preview():
    preview_button.config(text="Wating...")
    window.after(2300, show_preview)


#Establish window
window = tk.Tk()
window.title("Mouse Macro")


# create recording button
button = tk.Button(window, text="Start Recording",command=toggle_recording)
button.pack(padx=30,pady=30)

#create a label area in which actions will be recorded based on a watch conditon 
click_area = tk.Label(window, text="Click here to record", bg="lightblue",width=35,height=8)
click_area.pack(padx=10,pady=10)

# The label var is watching for the event: left mouse click (denoted by "<Button-1>")
# and will preform a callback to "record_click" when the event occurs
click_area.bind("<Button-1>", record_click)

#create Preview button
preview_button = tk.Button(window, text="Preview delay", command=start_preview)
preview_button.pack(padx=10, pady=10)

window.mainloop()
# Using tkinter for UI interface adn button interactions

import tkinter as tk
#*********************
#Example and Learning Module
#*********************

# function, what the button does upon interaction
def say_hello():
    # changes buttons text
    button.config(text="Hello!")

# Establishing/creating the window 
window = tk.Tk()
window.title("My Mouse Macro")

#**widget** an interface element, such as a button
#**callback** func privided for later execution

# create button, inside window, with displayed text, 
# and set action when interacted wiith
button = tk.Button(window, text="Click me", command=say_hello) # no () on say hello, handing over rather than calling immedatiely 

#pack() places the button in the window, 
# padx and pady add space arround it
button.pack(padx=500,pady=50)

# Starts event loop
# window.mainloop()

#**state** info the application remembers

#***********
#2) Practice stroreing actions only when recording is on
#***********
# Create list to store actions
actions: list[str] = []
bool = False
# create function that stores action ONLY when recording 
def record_practice_action():
    if bool:
        actions.append("Practice click")
        print(actions)

practice_button = tk.Button(window, text="Practice Action", command=record_practice_action)
practice_button.pack(padx=20 ,pady=20)

window.mainloop()

#***********
#3) Capture an actual click
#***********
#**event binding** connects an event, such as a mouse click, to callback
# recives event object containg info about what happened, rather than a func

#Create func/action to record mouse clicks,
# works by storing cursor pixel location, based on top left screen


# create click area, class: label, 
# calls record func whenever a specified event occurs within click area
# note, at this stage, recording only reocidng actions within a small area, 
# implement screen wide later

#***********
#4) Record WHEN each click happens (time aspect, accounts for record squences)
#***********
# Using perf_counter(), timer that returns seconds 
# starting point abriatry, compare two recorded times by subtracting
# gives elasped time between them, NOT time of day clock

# Currently, mouse postion is stored in actions: list[dict[str:int]]
# Upade so each dict also stores time, list[dict[str:int|float]]
# example of Stored click: [{"x": 200, "y": 200, "time": 21.45832 }]

#***********
#5) schedule action without freezing the interface
#***********
# Long waits inside event handlers prevent interface from proccessing other events
# add a preview button and display 

#**scheduling** arranging for a func/callback to run later 
# Exampe: window.after(2000, show_preivew), after 2000 milisecs or 2sec the callback occurs

# Imporantance, while playback is waiting to preform the next recored action, 
# the inferface is forze and cannot be interacted with, 
# therefore you cannot click a "stop playback button"
# Solution, rather then having a callback with a waiting period, use window.after()
# to preform the callback after elsaped time/ after the waiting periode




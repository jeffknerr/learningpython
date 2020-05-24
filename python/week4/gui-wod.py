"""
work out of the day (WOD) generator, with help 
from Aidan's tkinter gui programs

J. Knerr
Fall 2019
"""

import random
import tkinter as tk

# need a global variable for this???
wodtxt=None 

def wod():
    """pick workouts for the user"""
    global wodtxt
    exercises = ["burpees","pushups","box jumps","deadlifts",
                "pullups","situps","squats","curls","toes to bar"]
    numberOfExercises = 4
    rounds = random.randrange(3,10)
    workout = "Here's your workout: %s rounds of...\n" % (rounds)
    for i in range(numberOfExercises):
        exercise = random.choice(exercises)
        amt = random.randrange(8,16)
        what = "--> %2d %s" % (amt,exercise)
        workout += "%-30s\n" % (what)
    wodtxt.set(workout)

# Create the main window
root = tk.Tk()
root.title("WOD")
# Create label
wodtxt = tk.StringVar()
wod()
label = tk.Label(root, textvariable=wodtxt)
button = tk.Button(root, text="Pick Again...",command=wod)
quit = tk.Button(root, bg="red", text="quit", command=root.destroy)
# Lay out label
label.pack(padx=5,pady=5)
button.pack(padx=5,pady=5)
quit.pack(padx=5,pady=5)
# Run forever!
root.mainloop()

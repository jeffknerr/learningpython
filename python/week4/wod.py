"""
work out of the day (WOD) generator

J. Knerr
Fall 2019
"""

from random import *

def main():
    startday = 24     # day of month
    print("Here's your training week:")
    print("= "*20)
    for i in range(7):
        date = "May %d, 2020" % (startday + i)
        restday = choice([True, False])
        if restday:
            print("%s: REST DAY!!" % (date))
        else:
            print("%s: " % (date))
            wod()
        print("= "*20)

def wod():
    """pick and print workouts for the user"""
    exercises = ["burpees","pushups","box jumps","deadlifts",
                "pullups","situps","squats","curls","toes to bar"]
    numberOfExercises = 4
    print("Here's your WOD: 5 rounds of...")
    for i in range(numberOfExercises):
        workout = choice(exercises)
        amt = randrange(8,16)
        workout = str(amt) + " " + workout
        print("%d. %s" % (i+1, workout))

main()

# Basic damage calculations in Genshin inclusive of crit rate and crit damage uses the formula:
# damage = attack + (attack)(crit rate)(crit damage - 100%)
#
# To determine the best crit ratio with a given max crit value for the most damage,
# we just need to determine the maximum multiplier to a crit attack: (crit rate)(crit damage - 100%)
# this will be referred to as the "average crit multiplier"
from tkinter import *
from tkinter import ttk

# Input critValue takes standard CV 3 digit calculations
def calculateBestRatio(critValue, reasonablePercent):
    bestRatio = 1.0
    bestMultiplier = 0.0
    reasonableRatio = 1.0
    reasonableMultiplier = 0.0
    prevMultiplier = 0.0

    # Loop through every crit ratio from 1.0 to 5.0 in 0.1 increments
    for ratio in range(10, 51):
        ratio = round(ratio*0.1, 2)

        # Formula: 2(crit rate) + crit damage = crit value, crit damage = crit ratio(crit rate)
        critRate = (critValue/100)/(2 + ratio)

        # Formula: multiplier = (crit rate)(crit damage - 100%)
        # multiplier = (crit rate)((crit ratio)(crit rate) - 100%)
        # multiplier = (crit ratio)(crit rate)^2 - critRate
        damageMultiplier = round((ratio*(critRate**2) - critRate), 3)
        if damageMultiplier < 0:
            damageMultiplier = 0

        if damageMultiplier > bestMultiplier:
            bestMultiplier = damageMultiplier
            bestRatio = ratio

            # If the difference in multiplier between the current ratio and the previous ratio is 
            # less than the reasonable percent, it's not reasonable
            if abs(prevMultiplier - damageMultiplier)/((prevMultiplier + damageMultiplier)/2) > reasonablePercent/100:
                reasonableRatio = ratio
                reasonableMultiplier = damageMultiplier

        prevMultiplier = damageMultiplier
        print("Ratio: " + str(ratio) + " → Multiplier: " + str(damageMultiplier))

    print("For a CV of " + str(critValue) + ", the best ratio found is " + str(bestRatio) 
        + " with an average crit multiplier of " + str(bestMultiplier))
    print("A more reasonable ratio within " + str(reasonablePercent) + "% of the ratio ".format() + str(round((reasonableRatio + 0.1), 2)) + " is "
        + str(reasonableRatio) + " with a multiplier of " + str(reasonableMultiplier))

root = Tk()
root.title = "Crit Ratio Calculator"

frame = ttk.Frame(root, padding="3 3 12 12")
frame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

calculateBestRatio(325, 1)
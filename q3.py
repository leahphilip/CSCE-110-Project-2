#File: q3.py
#Author: Leah Philip
#Date: 02/07/2023
#Section: 506
#E-mail: leahephilip@tamu.edu
#Description: This program takes finds the difference in temperature between the user's inputted forecast from day 1 and day 2.
today = int(input ("Enter today's temperature in degrees: "))
tommorrow = int(input ("Enter Tomorrow's temperature in degrees: "))
if tommorrow>today:
    diff = tommorrow - today
    print("The temperature will rise by: ",diff ,"degrees.")
    change = (diff / today) * 100;
    print("The temperature's change is:",round(change) ,"%.")
else:
    diff = today - tommorrow
    print("The temperature will drop by: ", diff, "degrees.")
    change = (diff / today) * 100;
    print("The temperature's change is:-", round(change), "%.")

#File: q4.py
#Author: Leah Philip
#Date: 02/07/2023
#Section: 506
#E-mail: leahephilip@tamu.edu
#Description: This program prints the average of lunch cost based on user input.
input_str = input("Enter lunch costs for five working days:")
lunch_lengths_string = input_str.split()
lunch_lengths = [float(length) for length in lunch_lengths_string]
total= lunch_lengths[0]+lunch_lengths[1]+lunch_lengths[2]+lunch_lengths[3]+lunch_lengths[4]
average=total/5
print(f"The total cost of lunch this week is ${total:.0f}.")
print(f"On average, you spend ${average:.2f} daily for lunch.")

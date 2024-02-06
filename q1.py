#File: q1.py
#Author: Leah Philip
#Date: 2/07/2023
#Section: 506
#E-mail: leahephilip@tamu.edu
#Description: This program takes the dimensions of a box in feet from the user and calculates the sum of edges and volume of the box in meters.
input_str = input("Enter edge lengths of a box in feet (length, width, height):")
edge_lengths_string = input_str.split()
edge_lengths = [float(length) for length in edge_lengths_string]
sum_of_edges = (edge_lengths[0] + edge_lengths[1] + edge_lengths[2]) * 4*.3048
volume = edge_lengths[0] * edge_lengths[1] * edge_lengths[2]*.3048
print(f"Sum of all edges of the box is {sum_of_edges:.2f} m.")
print(f"Volume of the box is {volume:.2f} cubic m.")

#File: q5.py
#Author: Leah Philip
#Date: 02/07/2023
#Section: 506
#E-mail: leahephilip@tamu.edu
#Description: This program prints the total number of letters in the user's sentence input and the total number of occurrences of the first and last letter of the sentence.
sentence = input("Enter text (without punctuation, symbols, and/or numbers):")
letter_count = 0
# Iterate through each character in the sentence
for char in sentence:
    if char.isalpha():
        letter_count += 1
print(f"This sentence has {letter_count} letters.")

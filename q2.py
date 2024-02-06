#File: q2.py
#Author: Leah Philip
#Date: 02/07/2023
#Section: 506
#E-mail: leahephilip@tamu.edu
#Description: This program user for loan period (in years) and interest rate (in percentage) and prints out the total payoff amount.
def calculate_payoff(P, r, n):
    return P * (1 + r) ** n
loan_amount = 15000
interest_rate = float(input("Enter interest rate (in percentage): ")) / 100
loan_period = float(input("Enter loan period (in years): "))
total_payoff = calculate_payoff(loan_amount, interest_rate, loan_period)
print(f"At {interest_rate * 100:.2f}% interest, you need to pay ${total_payoff:.2f} after {loan_period} years.")

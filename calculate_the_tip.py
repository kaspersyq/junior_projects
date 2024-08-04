# Calculate the tip

from math import floor, ceil
print("What's the total bill for today, please?")
bill = float(input())
print(f'18% tip is ${ceil(bill * 0.18)}, which brings your total to ${floor(bill + (bill * 0.18))}')
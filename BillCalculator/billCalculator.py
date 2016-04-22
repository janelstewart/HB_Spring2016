# This is a comment and it not read by the interpreter
# These are useful for describing difficult code or adding reminders.
# TODO - fix this code :D
# (Part 1): Instead of using the hard coded ".18",
# Ask the user to input the percentage of tip they want to give. 
# Save the input to a variable. 
# Use the variable to calculate the tip.
# (Part 2): Fix any bugs and make it work!

bill = float(raw_input("How much was your bill? $"))
percent = float(raw_input("What percent tip do you want to leave? "))

tip = bill * (percent/100)

total_bill = bill + tip

print "The tip is %.2f and the total bill is %.2f." % (tip, total_bill)

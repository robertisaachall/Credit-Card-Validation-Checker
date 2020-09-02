# Credit Card Validation Checker
 Takes in a user input, and validates it according to a set rule-set.
Based on these three practices:

1. Starting at 0 and the rest of the numbers in  even index are doubled, and if their double is double digits, then remove 9 from it and add it, else add it together.
    Example:
    5 4 3 1
    Index 0 and 2 are doubled and subtracted since their addition results in double digits.
2. All odd numbered indexes are added together.

3. If the two numbers are divisible by 10, then the credit card is a good number. Else it is not.

# Vaidation and Testing
 Included errordetectiontester.py file is used for testing with inputs from files. Run with command line argument being a .txt file that is readable.
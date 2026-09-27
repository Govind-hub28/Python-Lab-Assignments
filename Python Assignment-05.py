# Python Assignment-05

# PAN Number Validation Using Regular Expression

import re


pan_number = input("Enter PAN Number: ")


# Regular expression for PAN number
pattern = r"^[A-Z]{5}[0-9]{4}[A-Z]$"


# Validate PAN number
if re.fullmatch(pattern, pan_number):
    print("Valid PAN Number")
else:
    print("Invalid PAN Number")
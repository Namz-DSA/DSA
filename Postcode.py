"""
1. ✅ Match a Valid PIN Code
Problem: Match exactly 4 or 6 digits (e.g., 1234, 987654)
✅ Must be numeric only.
❌ 12345 or 1234a is invalid.

Input: "1234" → Valid
Input: "1234a" → Invalid
"""
import re

pattern = r'^(\d{4}|\d{6})$'
# postcode = '12345a'

for code in ['1234', '123456', '123', '12345a', 'abcdef', '12345']:
    print(f"{code}: ", end='')
    print("Valid" if re.match(pattern, code) else "Invalid")

# matches = re.match(pattern , postcode)

# if matches:
#     print("Valid")
# else:
#     print("Invalid")
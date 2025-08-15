"""
Write a regex to validate Indian mobile numbers under these rules:

Must start with 7, 8, or 9

Must be exactly 10 digits

No extra characters, letters, or spaces
"""
import re

numbers = ["+919876543210", "08123456789", "9000000000","1234567890", "0987654321", "98765", "98765abcd1", "98765432101"]


pattern = r'^(?:\+91|0)?[789]\d{9}$'

matched_numbers = [number for number in numbers if re.match(pattern , number)]
print(matched_numbers)
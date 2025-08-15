"""
🎯 Extract full name + date of birth from text using named groups.
Input:
python
Copy
Edit
text = "Name: Alice Wonderland, DOB: 17-03-1997"
Your Task:
Use re.search and a named group pattern like (?P<name>...), (?P<day>...), etc.

Extract the full name and date parts

Print them like:

plaintext
Copy
Edit
Name: Alice Wonderland
Day: 17
Month: 03
Year: 1997
"""

import re

text = "Name: Alice Wonderland, DOB: 17-03-1997"

pattern = r'Name:\s(?P<name>[A-Za-z ]+),\sDOB:\s(?P<day>\d{2})-(?P<month>\d{2})-(?P<year>\d{4})'

match = re.search(pattern , text)

if match:
    print(match.group("name"))
    print(match.group("day"))   
    print(match.group("month"))  
    print(match.group("year")) 
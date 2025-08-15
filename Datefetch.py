"""
From a sentence, extract all valid dates in the following formats:

DD/MM/YYYY

DD-MM-YYYY

DD.MM.YYYY

The separator can be /, -, or . — but it must be consistent within a date.

🎯 Example Input:
python
Copy
Edit
text = "Important dates: 21/07/2025, 01-01-2024, and 31.12.2023 are all valid. Skip 12/31/2023 and 2025/07/21."
✅ Expected Output:
python
Copy
Edit
['21/07/2025', '01-01-2024', '31.12.2023']

"""
import re

from datetime import datetime

text = "Important dates: 21/07/2025, 01-01-2024, and 31.12.2023 are all valid. Skip 12/31/2023 and 2025/07/21."

pattern = r'\b(0[1-9]|[12][0-9]|3[01])(?:[/\.-])(0[1-9]|1[0-2])(?:[/\.-])(\d{4})\b'

matches = re.findall(pattern,text)

dates = ['-'.join(m) for m in matches]

leap_dates = []

for date in dates:
    try:
        dt = datetime.strptime(date, '%d-%m-%Y')
        year = dt.year
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            leap_dates.append(date)
    except ValueError:
        continue

print(leap_dates)
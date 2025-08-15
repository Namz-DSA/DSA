"""
🧠 Problem:
Extract all valid email addresses from a block of text.

🎯 Example Input:
python
Copy
Edit
text = "Reach us at info@example.com or support@my-domain.org. Avoid fake@mail, user@@domain.com and a@b.c"
✅ Expected Output:
python
Copy
Edit
['info@example.com', 'support@my-domain.org']
✅ Step-by-step Regex Plan:
We want to match:

username: letters, digits, ., _, %, +, -

an @ symbol

domain name: letters, digits, -, and .

TLD (like .com, .org) — 2 to 6 letters

"""
import re

text = "Reach us at info@example.com or support@my-domain.org. Avoid fake@mail, user@@domain.com and a@b.c"

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}\b'

print(re.findall(pattern,text))
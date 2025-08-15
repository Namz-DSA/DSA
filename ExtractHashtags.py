"""
🧠 Problem:
From a given text, extract all hashtags, such as:

#Python

#100DaysOfCode

#AI_ML

A hashtag:

Starts with #

Followed by letters, digits, or underscores

Cannot be just # alone

No punctuation (like !, ., ,, etc.) inside hashtags

🧪 Example Input:
python
Copy
Edit
text = "Loving the vibes of #Python, #MachineLearning, and #AI_2025! Avoid # and #bad-tag."
✅ Expected Output:
python
Copy
Edit
['#Python', '#MachineLearning', '#AI_2025']
"""

import re

text = "Loving the vibes of #Python, #MachineLearning, and #AI_2025! Avoid # and #bad-tag and energy#used."

pattern = r'(?<!\w)#([A-Za-z0-9_]+)(?![-\w])'

print(re.findall(pattern, text))
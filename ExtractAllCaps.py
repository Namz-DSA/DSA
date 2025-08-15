"""
Extract all words in a sentence that start with a capital letter (like names, places, proper nouns).

🎯 Example:
python
Copy
Edit
text = "Alice went to Wonderland with Bob and Charlie."
Expected Output:

python
Copy
Edit
['Alice', 'Wonderland', 'Bob', 'Charlie']
"""
import re

text = "Alice went to Wonderland with Bob and Charlie."

# pattern = r'^[A-Z][a-z]+$'

# caps = [char.strip('.,!?') for char in text.split() if re.match(pattern, char.strip('.,!?'))]

# print(caps)

pattern = r'\b[A-Z][a-z]+\b'

print(re.findall(pattern,text))
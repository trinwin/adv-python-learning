import re
result = 0
pattern = 'test'

pattern = r'([0-9]+)'
text = 'CS 122-Advanced Programming with Python, Fall 2019'
result = re.findall(pattern, text)
print(len(result))

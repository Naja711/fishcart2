import json

with open(r'd:\fishcart2\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# find the showDetails strings in the file
matches = re.findall(r'showDetails\([^)]+\)', html)
print('Total showDetails calls:', len(matches))
print('Unique:', set(matches))

# Find the hrefs
hrefs = re.findall(r'href="([^"]+)"', html)
print('Total hrefs:', len(hrefs))
print('Unique hrefs:', set(hrefs))

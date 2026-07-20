import re

# Extract NEW_STYLES from patch_index.py
with open('patch_index.py', 'r', encoding='utf-8') as f:
    patch = f.read()

# Find NEW_STYLES content - find the <style> block
start = patch.find('<style>')
end = patch.find('</style>')
new_css_inner = patch[start + len('<style>'):end]

# Now replace in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The existing style block is between the first <style> and first </style>
idx_s = content.find('<style>')
idx_e = content.find('</style>', idx_s)

if idx_s == -1 or idx_e == -1:
    print('ERROR: Could not find style block')
else:
    new_content = content[:idx_s + len('<style>')] + new_css_inner + content[idx_e:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('CSS successfully updated in index.html!')
    print(f'CSS inner length: {len(new_css_inner)} chars')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for i, line in enumerate(lines):
    if 'id="page-' in line:
        safe_line = line.encode('ascii', 'ignore').decode('ascii')
        print(f'{i+1}: {safe_line.strip()}')

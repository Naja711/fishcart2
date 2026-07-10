with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

if 'id="page-cook"' in text:
    print('Found page-cook')
else:
    print('No page cook')

if 'grid-template-columns: 1fr 1fr;' in text:
    print('Found mobile grid fix')
else:
    print('No mobile grid fix')

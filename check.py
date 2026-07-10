with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

if 'cook-grid-container' in text:
    print('cook-grid-container exists!')
else:
    print('cook-grid-container NOT FOUND. Let us check what page-cook is.')
    start = text.find('id="page-cook"')
    if start != -1:
        # Avoid unicode print errors
        print(text[start:start+200].encode('ascii', 'ignore').decode('ascii'))

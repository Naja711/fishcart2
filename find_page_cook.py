with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('id="page-cook"')
if start != -1:
    print('Found it around character:', start)
    # Be careful not to print unicode to console on windows
    snippet = text[max(0, start-100):start+200]
    safe_snippet = snippet.encode('ascii', 'ignore').decode('ascii')
    print('Snippet:')
    print(safe_snippet)
else:
    print('Not found!')

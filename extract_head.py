with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
end = html.find('</head>')
if end != -1:
    with open('temp_head.txt', 'w', encoding='utf-8') as f2:
        f2.write(html[:end])

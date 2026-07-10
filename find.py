with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()
    start = text.find('<div class="fp-card"')
    if start != -1:
        print(text[start:start+1000])

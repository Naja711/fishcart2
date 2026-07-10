favicon_html = '<link rel="icon" href="data:image/svg+xml,<svg xmlns=\\"http://www.w3.org/2000/svg\\" viewBox=\\"0 0 100 100\\"><text y=\\".9em\\" font-size=\\"90\\">🐟</text></svg>">'

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
if 'rel="icon"' not in html:
    html = html.replace('</title>', '</title>\n' + favicon_html)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

# Update product_template.html
with open('product_template.html', 'r', encoding='utf-8') as f:
    phtml = f.read()
if 'rel="icon"' not in phtml:
    phtml = phtml.replace('</title>', '</title>\n' + favicon_html)
    with open('product_template.html', 'w', encoding='utf-8') as f:
        f.write(phtml)

print('Added fish favicon to HTML files')

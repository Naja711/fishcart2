content = open('index.html', encoding='utf-8').read()
marker = 'id="page-home"'
replacement = 'id="page-home" style="overflow:hidden;"'
if replacement not in content:
    content = content.replace(marker, replacement, 1)
    open('index.html', 'w', encoding='utf-8').write(content)
    print('Fixed page-home overflow:hidden')
else:
    print('Already fixed')

import re

encoded_svg = '%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22%3E%3Ctext y=%22.9em%22 font-size=%2290%22%3E🐟%3C/text%3E%3C/svg%3E'
new_favicon = f'<link rel="icon" href="data:image/svg+xml,{encoded_svg}">'

def fix_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # We find the broken link tag and replace it
    # The broken tag looks like: <link rel="icon" href="data:image/svg+xml,<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 100 100\"><text y=\".9em\" font-size=\"90\">🐟</text></svg>">
    
    # Simple replace
    bad_string = '<link rel="icon" href="data:image/svg+xml,<svg xmlns=\\"http://www.w3.org/2000/svg\\" viewBox=\\"0 0 100 100\\"><text y=\\".9em\\" font-size=\\"90\\">🐟</text></svg>">'
    
    html = html.replace(bad_string, new_favicon)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

fix_file('index.html')
fix_file('product_template.html')
print('Fixed favicon parsing issue')

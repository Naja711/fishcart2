import re
from bs4 import BeautifulSoup

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

cards = soup.find_all('div', class_='fp-card')
for card in cards:
    # Try to find product ID from onclick or href
    prod_id = None
    onclick_el = card.find(lambda tag: tag.has_attr('onclick') and 'showDetails' in tag['onclick'])
    if onclick_el:
        m = re.search(r"showDetails\('([^']+)'\)", onclick_el['onclick'])
        if m:
            prod_id = m.group(1)
            
    # If not found, try to extract from old image src
    if not prod_id:
        img = card.find('img', class_='fp-cimg')
        if img and 'src' in img.attrs and 'assets/' in img['src']:
            m = re.search(r'assets/([^.]+)\.jpg', img['src'])
            if m:
                prod_id = m.group(1)
                
    if prod_id:
        # Wrap View Details with an A tag if not already wrapped
        clink = card.find('div', class_='fp-clink')
        if clink and 'View Details' in clink.text:
            parent = clink.parent
            if parent.name != 'a':
                a_tag = soup.new_tag('a', href=f"details_{prod_id}.html", style="text-decoration:none;")
                clink.wrap(a_tag)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(str(soup))

print('Updated links in index.html')

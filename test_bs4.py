import json
from bs4 import BeautifulSoup
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
cards = soup.find_all('div', class_='fp-card')
for card in cards:
    cbot = card.find('div', class_='fp-cbot')
    if cbot:
        onclick_div = cbot.find(lambda tag: tag.has_attr('onclick') and 'showDetails' in tag['onclick'])
        if onclick_div:
            m = re.search(r"showDetails\('([^']+)'\)", onclick_div['onclick'])
            if m:
                prod_id = m.group(1)
                img = card.find('img', class_='fp-cimg')
                if img:
                    print(f'Found card for {prod_id}, current img: {img["src"]}')

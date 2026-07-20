import os
import requests
import urllib.parse
from bs4 import BeautifulSoup

PROJECT_ID = 'v5b89tvp'
DATASET = 'production'
QUERY = '*[_type == \'product\' && defined(recipe_url)]'

recipe_html = ""

try:
    url = f'https://{PROJECT_ID}.api.sanity.io/v2021-10-21/data/query/{DATASET}?query={urllib.parse.quote(QUERY)}'
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        sanity_docs = response.json().get('result', [])
        for doc in sanity_docs:
            if doc.get('recipe_url'):
                title = doc.get('title', 'Delicious Recipe')
                recipe_url = doc.get('recipe_url')
                
                # Extract image URL
                img_url = ""
                img_obj = doc.get('image')
                if img_obj and isinstance(img_obj, dict) and 'asset' in img_obj:
                    ref = img_obj['asset']['_ref']
                    parts = ref.split('-')
                    if len(parts) >= 4:
                        img_url = f"https://cdn.sanity.io/images/{PROJECT_ID}/{DATASET}/{parts[1]}-{parts[2]}.{parts[3]}"
                
                if not img_url:
                    img_url = "https://images.unsplash.com/photo-1565557623262-b51c2513a641?auto=format&fit=crop&w=300&q=80"
                
                card = f'''
                <a href="{recipe_url}" target="_blank" class="cook-card" style="background: #fff; border-radius: 12px; overflow: hidden; display: flex; flex-direction: column; text-decoration: none; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                    <img src="{img_url}" class="cook-img" alt="{title}" style="width: 100%; height: 140px; object-fit: cover;">
                    <div class="cook-info" style="padding: 10px; flex: 1; display: flex; flex-direction: column;">
                        <div class="cook-title" style="font-size: 13px; font-weight: 700; color: #0A2848; margin-bottom: 8px;">{title} Recipe</div>
                        <div class="cook-btn" style="margin-top: auto; display: inline-flex; align-items: center; justify-content: center; background: #1565C0; color: #fff; border: none; padding: 6px 12px; border-radius: 6px; font-size: 11px; font-weight: 600; cursor: pointer; text-decoration: none;">Watch Recipe</div>
                    </div>
                </a>
                '''
                recipe_html += card
except Exception as e:
    print('Failed to fetch from Sanity for recipes', e)

if not recipe_html:
    recipe_html = '<div style="padding: 20px; color: #555;">No recipes found yet. Check back soon!</div>'

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
grid = soup.find('div', id='cook-grid-container')
if grid:
    # Clear existing content of the grid
    grid.clear()
    # Parse recipe_html and append to grid
    recipe_soup = BeautifulSoup(recipe_html, 'html.parser')
    grid.append(recipe_soup)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print("Injected recipe cards into index.html using BeautifulSoup")
else:
    print("Could not find cook-grid-container in index.html")

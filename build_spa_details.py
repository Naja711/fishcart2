import json
import re

data = {
    # FISH
    "prod_1_salmon": {
        "title": "Salmon", "subtitle": "Norway • Fillet", "price": "£14.99", "unit": "kg", "image": "assets/prod_1_salmon.jpg",
        "category": "Fish", "category_url": "index.html#fish", "origin_label": "Catch From",
        "origin": "Norway, North Atlantic Ocean. Wild Caught.", "best_for": "Curry, Grill, Baking.",
        "nutrition_protein": "20.4g", "nutrition_fat": "13.4g", "nutrition_calories": "208 kcal",
        "nutrition_extra_label": "Omega-3", "nutrition_extra_val": "3", "speciality": "Rich, buttery flavor and firm texture.",
        "famous_for": "Norwegian Cuisine, Japanese Sushi.", "allergy": "Contains Fish.",
        "how_to_cook": "Grill or pan-sear. Great with lemon and herbs.",
        "video1": "https://www.youtube.com/embed/jH-1gV1fH-s", "video2": "https://www.youtube.com/embed/9gN2lB5B9Qo",
        "instructions": "<li>Preheat pan on medium-high.</li><li>Season salmon with salt and pepper.</li><li>Sear skin-side down for 4 mins.</li><li>Flip and cook 2 mins.</li>"
    },
    "prod_2_seabass": {
        "title": "Sea Bass", "subtitle": "Local • Whole", "price": "£18.50", "unit": "kg", "image": "assets/prod_2_seabass.jpg",
        "category": "Fish", "category_url": "index.html#fish", "origin_label": "Catch From", "origin": "Mediterranean Sea.", "best_for": "Baking, Pan-frying.",
        "nutrition_protein": "18g", "nutrition_fat": "2.5g", "nutrition_calories": "97 kcal",
        "nutrition_extra_label": "B-Vitamins", "nutrition_extra_val": "High", "speciality": "Mild, delicate flavor.",
        "famous_for": "Mediterranean dishes.", "allergy": "Contains Fish.", "how_to_cook": "Bake whole with lemon and rosemary.",
        "video1": "", "video2": "", "instructions": "<li>Stuff with lemon.</li><li>Bake at 200C for 20 mins.</li>"
    },
    "prod_3_tuna": {
        "title": "Tuna Steak", "subtitle": "Pacific • Steak", "price": "£22.00", "unit": "kg", "image": "assets/prod_3_tuna.jpg",
        "category": "Fish", "category_url": "index.html#fish", "origin_label": "Catch From", "origin": "Pacific Ocean.", "best_for": "Searing, Sashimi.",
        "nutrition_protein": "24g", "nutrition_fat": "1g", "nutrition_calories": "109 kcal",
        "nutrition_extra_label": "Omega-3", "nutrition_extra_val": "Mod", "speciality": "Meaty texture.",
        "famous_for": "Sushi, Poke Bowls.", "allergy": "Contains Fish.", "how_to_cook": "Sear 1 min per side.",
        "video1": "", "video2": "", "instructions": "<li>Season well.</li><li>Sear on screaming hot pan for 1 min per side.</li>"
    },
    "prod_4_cod": {
        "title": "Cod Fillet", "subtitle": "Atlantic • Fillet", "price": "£12.99", "unit": "kg", "image": "assets/prod_4_cod.jpg",
        "category": "Fish", "category_url": "index.html#fish", "origin_label": "Catch From", "origin": "North Atlantic.", "best_for": "Fish & Chips, Baking.",
        "nutrition_protein": "17g", "nutrition_fat": "0.7g", "nutrition_calories": "82 kcal",
        "nutrition_extra_label": "Protein", "nutrition_extra_val": "High", "speciality": "Flaky white meat.",
        "famous_for": "British Fish & Chips.", "allergy": "Contains Fish.", "how_to_cook": "Batter and fry or bake.",
        "video1": "", "video2": "", "instructions": "<li>Batter lightly.</li><li>Deep fry until golden.</li>"
    },
    "prod_5_mackerel": {
        "title": "Mackerel", "subtitle": "Local • Whole", "price": "£9.50", "unit": "kg", "image": "assets/prod_5_mackerel.jpg",
        "category": "Fish", "category_url": "index.html#fish", "origin_label": "Catch From", "origin": "UK Coast.", "best_for": "Grilling, Smoking.",
        "nutrition_protein": "18g", "nutrition_fat": "13g", "nutrition_calories": "205 kcal",
        "nutrition_extra_label": "Omega-3", "nutrition_extra_val": "High", "speciality": "Rich, oily fish.",
        "famous_for": "Smoked dishes.", "allergy": "Contains Fish.", "how_to_cook": "Grill on high heat.",
        "video1": "", "video2": "", "instructions": "<li>Score skin.</li><li>Grill for 5 mins each side.</li>"
    },
    "prod_6_haddock": {
        "title": "Haddock", "subtitle": "Atlantic • Fillet", "price": "£14.00", "unit": "kg", "image": "assets/prod_6_haddock.jpg",
        "category": "Fish", "category_url": "index.html#fish", "origin_label": "Catch From", "origin": "North Atlantic.", "best_for": "Baking, Smoking.",
        "nutrition_protein": "19g", "nutrition_fat": "0.5g", "nutrition_calories": "90 kcal",
        "nutrition_extra_label": "B12", "nutrition_extra_val": "High", "speciality": "Slightly sweet taste.",
        "famous_for": "Scottish Cuisine.", "allergy": "Contains Fish.", "how_to_cook": "Poach in milk or bake.",
        "video1": "", "video2": "", "instructions": "<li>Bake with butter and herbs.</li>"
    },
    "prod_7_sardines": {
        "title": "Sardines", "subtitle": "Local • Fresh", "price": "£8.50", "unit": "kg", "image": "assets/prod_7_sardines.jpg",
        "category": "Fish", "category_url": "index.html#fish", "origin_label": "Catch From", "origin": "Cornwall Coast.", "best_for": "Grilling, BBQ.",
        "nutrition_protein": "20g", "nutrition_fat": "11g", "nutrition_calories": "190 kcal",
        "nutrition_extra_label": "Calcium", "nutrition_extra_val": "High", "speciality": "Nutrient dense.",
        "famous_for": "Mediterranean BBQ.", "allergy": "Contains Fish.", "how_to_cook": "Grill whole.",
        "video1": "", "video2": "", "instructions": "<li>Grill whole with olive oil and salt.</li>"
    },
    "prod_8_trout": {
        "title": "Trout", "subtitle": "Farm • Whole", "price": "£11.99", "unit": "kg", "image": "assets/prod_8_trout.jpg",
        "category": "Fish", "category_url": "index.html#fish", "origin_label": "Catch From", "origin": "UK Freshwater Farms.", "best_for": "Pan-frying, Baking.",
        "nutrition_protein": "19g", "nutrition_fat": "6g", "nutrition_calories": "140 kcal",
        "nutrition_extra_label": "Omega-3", "nutrition_extra_val": "Mod", "speciality": "Earthy flavor.",
        "famous_for": "European Freshwater Cuisine.", "allergy": "Contains Fish.", "how_to_cook": "Pan-fry with almonds.",
        "video1": "", "video2": "", "instructions": "<li>Pan fry with butter and almonds.</li>"
    },

    # MEAT
    "beef_chunks": {
        "title": "Beef Chunks", "subtitle": "Premium • Boneless", "price": "£10.99", "unit": "kg", "image": "assets/beef_chunks.jpg",
        "category": "Meat", "category_url": "index.html#meat", "origin_label": "Source", "origin": "UK Farms.", "best_for": "Stews, Curries.",
        "nutrition_protein": "26g", "nutrition_fat": "15g", "nutrition_calories": "250 kcal",
        "nutrition_extra_label": "Iron", "nutrition_extra_val": "High", "speciality": "Tender and flavorful.",
        "famous_for": "Slow-cooked stews.", "allergy": "No known allergens.", "how_to_cook": "Slow cook for 3 hours.",
        "video1": "", "video2": "", "instructions": "<li>Brown meat.</li><li>Slow cook in broth.</li>"
    },
    "boar_meat_bonless": {
        "title": "Boar Meat", "subtitle": "Exotic • Boneless", "price": "£18.50", "unit": "kg", "image": "assets/boar_meat_bonless.jpg",
        "category": "Meat", "category_url": "index.html#meat", "origin_label": "Source", "origin": "Wild Sourced.", "best_for": "Roasting, Stews.",
        "nutrition_protein": "28g", "nutrition_fat": "9g", "nutrition_calories": "210 kcal",
        "nutrition_extra_label": "Protein", "nutrition_extra_val": "High", "speciality": "Rich, gamey flavor.",
        "famous_for": "Exotic dishes.", "allergy": "No known allergens.", "how_to_cook": "Roast slowly.",
        "video1": "", "video2": "", "instructions": "<li>Marinate overnight.</li><li>Roast slow.</li>"
    },
    "boar_meat_with_bone": {
        "title": "Boar Bone-in", "subtitle": "Exotic • Bone-in", "price": "£15.50", "unit": "kg", "image": "assets/boar_meat_with_bone.jpg",
        "category": "Meat", "category_url": "index.html#meat", "origin_label": "Source", "origin": "Wild Sourced.", "best_for": "Broths, Slow Cook.",
        "nutrition_protein": "25g", "nutrition_fat": "11g", "nutrition_calories": "220 kcal",
        "nutrition_extra_label": "Flavor", "nutrition_extra_val": "High", "speciality": "Flavorful bone marrow.",
        "famous_for": "Rich broths.", "allergy": "No known allergens.", "how_to_cook": "Simmer for hours.",
        "video1": "", "video2": "", "instructions": "<li>Simmer for rich broth.</li>"
    },
    "buffalo": {
        "title": "Buffalo Meat", "subtitle": "Premium • Cuts", "price": "£9.50", "unit": "kg", "image": "assets/buffalo.jpg",
        "category": "Meat", "category_url": "index.html#meat", "origin_label": "Source", "origin": "Farmed.", "best_for": "Curries.",
        "nutrition_protein": "24g", "nutrition_fat": "8g", "nutrition_calories": "190 kcal",
        "nutrition_extra_label": "Iron", "nutrition_extra_val": "High", "speciality": "Leaner than beef.",
        "famous_for": "Spicy curries.", "allergy": "No known allergens.", "how_to_cook": "Pressure cook.",
        "video1": "", "video2": "", "instructions": "<li>Pressure cook for tenderness.</li>"
    },
    "deer_meat": {
        "title": "Venison", "subtitle": "Exotic • Cuts", "price": "£22.99", "unit": "kg", "image": "assets/deer_meat.jpg",
        "category": "Meat", "category_url": "index.html#meat", "origin_label": "Source", "origin": "Wild Sourced.", "best_for": "Steaks, Roasts.",
        "nutrition_protein": "30g", "nutrition_fat": "3g", "nutrition_calories": "150 kcal",
        "nutrition_extra_label": "Lean", "nutrition_extra_val": "Very High", "speciality": "Extremely lean, gamey.",
        "famous_for": "Gourmet dishes.", "allergy": "No known allergens.", "how_to_cook": "Sear quickly.",
        "video1": "", "video2": "", "instructions": "<li>Do not overcook. Sear quickly.</li>"
    },
    "lamb": {
        "title": "Lamb Meat", "subtitle": "Local • Mixed", "price": "£15.99", "unit": "kg", "image": "assets/lamb.jpg",
        "category": "Meat", "category_url": "index.html#meat", "origin_label": "Source", "origin": "UK Farms.", "best_for": "Roasting, Grilling.",
        "nutrition_protein": "25g", "nutrition_fat": "21g", "nutrition_calories": "290 kcal",
        "nutrition_extra_label": "Fat", "nutrition_extra_val": "High", "speciality": "Tender and sweet.",
        "famous_for": "Sunday Roasts.", "allergy": "No known allergens.", "how_to_cook": "Roast with rosemary.",
        "video1": "", "video2": "", "instructions": "<li>Roast with garlic and rosemary.</li>"
    },
    "mutton_leg": {
        "title": "Mutton Leg", "subtitle": "Local • Bone-in", "price": "£14.99", "unit": "kg", "image": "assets/mutton_leg.jpg",
        "category": "Meat", "category_url": "index.html#meat", "origin_label": "Source", "origin": "UK Farms.", "best_for": "Slow Roasting.",
        "nutrition_protein": "26g", "nutrition_fat": "18g", "nutrition_calories": "270 kcal",
        "nutrition_extra_label": "Iron", "nutrition_extra_val": "Mod", "speciality": "Rich, intense flavor.",
        "famous_for": "Traditional Roasts.", "allergy": "No known allergens.", "how_to_cook": "Slow roast.",
        "video1": "", "video2": "", "instructions": "<li>Slow roast for 4 hours.</li>"
    },
    "rabbit": {
        "title": "Rabbit Meat", "subtitle": "Farm • Whole", "price": "£12.50", "unit": "kg", "image": "assets/rabbit.jpg",
        "category": "Meat", "category_url": "index.html#meat", "origin_label": "Source", "origin": "UK Farms.", "best_for": "Stews, Braising.",
        "nutrition_protein": "28g", "nutrition_fat": "5g", "nutrition_calories": "160 kcal",
        "nutrition_extra_label": "Lean", "nutrition_extra_val": "High", "speciality": "Very lean white meat.",
        "famous_for": "French Cuisine.", "allergy": "No known allergens.", "how_to_cook": "Braise slowly.",
        "video1": "", "video2": "", "instructions": "<li>Braise in white wine.</li>"
    },

    # CHICKEN
    "chicken_full": {
        "title": "Whole Chicken", "subtitle": "Local Farm • Fresh", "price": "£5.99", "unit": "kg", "image": "assets/chicken_full.jpg",
        "category": "Chicken", "category_url": "index.html#chicken", "origin_label": "Source", "origin": "UK Free Range Farms.", "best_for": "Roasting.",
        "nutrition_protein": "27g", "nutrition_fat": "14g", "nutrition_calories": "239 kcal",
        "nutrition_extra_label": "Protein", "nutrition_extra_val": "High", "speciality": "Juicy and tender.",
        "famous_for": "Sunday Roasts.", "allergy": "No known allergens.", "how_to_cook": "Roast whole.",
        "video1": "", "video2": "", "instructions": "<li>Roast at 190C for 1h 20m.</li>"
    },
    "boneless_chicken": {
        "title": "Boneless Chicken", "subtitle": "Premium Cuts", "price": "£8.50", "unit": "kg", "image": "assets/boneless_chicken.jpg",
        "category": "Chicken", "category_url": "index.html#chicken", "origin_label": "Source", "origin": "UK Farms.", "best_for": "Curries, Stir-fry.",
        "nutrition_protein": "31g", "nutrition_fat": "3g", "nutrition_calories": "165 kcal",
        "nutrition_extra_label": "Lean", "nutrition_extra_val": "High", "speciality": "Very lean and versatile.",
        "famous_for": "Quick meals.", "allergy": "No known allergens.", "how_to_cook": "Pan fry or boil.",
        "video1": "", "video2": "", "instructions": "<li>Pan fry for 10-15 mins.</li>"
    },
    "chicken_liver": {
        "title": "Chicken Liver", "subtitle": "Fresh Offal", "price": "£3.99", "unit": "kg", "image": "assets/chicken_liver.jpg",
        "category": "Chicken", "category_url": "index.html#chicken", "origin_label": "Source", "origin": "UK Farms.", "best_for": "Pâté, Sauté.",
        "nutrition_protein": "24g", "nutrition_fat": "6g", "nutrition_calories": "167 kcal",
        "nutrition_extra_label": "Iron", "nutrition_extra_val": "Very High", "speciality": "Rich in iron and vitamins.",
        "famous_for": "Pâté.", "allergy": "No known allergens.", "how_to_cook": "Sauté quickly.",
        "video1": "", "video2": "", "instructions": "<li>Sauté with onions until brown.</li>"
    },

    # EGGS
    "chicken_egg": {
        "title": "Chicken Eggs", "subtitle": "Farm Fresh • Dozen", "price": "£2.99", "unit": "dozen", "image": "assets/chicken_egg.jpg",
        "category": "Eggs", "category_url": "index.html#eggs", "origin_label": "Source", "origin": "UK Free Range.", "best_for": "Boiling, Frying, Baking.",
        "nutrition_protein": "12g", "nutrition_fat": "10g", "nutrition_calories": "143 kcal",
        "nutrition_extra_label": "Vitamins", "nutrition_extra_val": "High", "speciality": "Daily essential.",
        "famous_for": "Breakfasts.", "allergy": "Contains Egg.", "how_to_cook": "Boil for 6 mins.",
        "video1": "", "video2": "", "instructions": "<li>Boil, fry, or scramble.</li>"
    },
    "duck_egg": {
        "title": "Duck Eggs", "subtitle": "Premium • Dozen", "price": "£4.50", "unit": "dozen", "image": "assets/duck_egg.jpg",
        "category": "Eggs", "category_url": "index.html#eggs", "origin_label": "Source", "origin": "UK Farms.", "best_for": "Baking, Custards.",
        "nutrition_protein": "13g", "nutrition_fat": "14g", "nutrition_calories": "185 kcal",
        "nutrition_extra_label": "Richness", "nutrition_extra_val": "High", "speciality": "Larger yolks, creamier.",
        "famous_for": "Baking fluffier cakes.", "allergy": "Contains Egg.", "how_to_cook": "Fry sunny side up.",
        "video1": "", "video2": "", "instructions": "<li>Fry on medium heat until white is set.</li>"
    },
    "quail_egg": {
        "title": "Quail Eggs", "subtitle": "Exotic • Pack", "price": "£3.99", "unit": "pack", "image": "assets/quail_egg.jpg",
        "category": "Eggs", "category_url": "index.html#eggs", "origin_label": "Source", "origin": "Specialty Farms.", "best_for": "Salads, Garnishes.",
        "nutrition_protein": "13g", "nutrition_fat": "11g", "nutrition_calories": "158 kcal",
        "nutrition_extra_label": "Vitamins", "nutrition_extra_val": "High", "speciality": "Small, speckled, nutrient dense.",
        "famous_for": "Gourmet dishes.", "allergy": "Contains Egg.", "how_to_cook": "Boil for 2.5 mins.",
        "video1": "", "video2": "", "instructions": "<li>Boil for 2.5 mins for soft boiled.</li>"
    }
}

import requests
import urllib.parse

PROJECT_ID = 'v5b89tvp'
DATASET = 'production'
QUERY = '*[_type == \'product\']'

try:
    url = f'https://{PROJECT_ID}.api.sanity.io/v2021-10-21/data/query/{DATASET}?query={urllib.parse.quote(QUERY)}'
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        sanity_docs = response.json().get('result', [])
        if len(sanity_docs) > 0:
            # Overwrite hardcoded data with sanity data
            for doc in sanity_docs:
                prod_id = doc.get('id')
                if prod_id and prod_id in data:
                    for k, v in doc.items():
                        if k == 'image' and v and isinstance(v, dict) and 'asset' in v:
                            ref = v['asset']['_ref']
                            parts = ref.split('-')
                            if len(parts) >= 4:
                                data[prod_id]['image'] = f"https://cdn.sanity.io/images/{PROJECT_ID}/{DATASET}/{parts[1]}-{parts[2]}.{parts[3]}"
                        elif k == 'gallery' and v and isinstance(v, list):
                            gallery_urls = []
                            for img_obj in v:
                                if img_obj and isinstance(img_obj, dict) and 'asset' in img_obj:
                                    ref = img_obj['asset']['_ref']
                                    parts = ref.split('-')
                                    if len(parts) >= 4:
                                        gallery_urls.append(f"https://cdn.sanity.io/images/{PROJECT_ID}/{DATASET}/{parts[1]}-{parts[2]}.{parts[3]}")
                            data[prod_id]['gallery'] = gallery_urls
                        else:
                            data[prod_id][k] = v
except Exception as e:
    print('Failed to fetch from Sanity, using local fallback.', e)


template_path = r"product_template.html"
with open(template_path, "r", encoding="utf-8") as f:
    template = f.read()

# Extract just the CSS from product_template.html
css_match = re.search(r'<style>(.*?)</style>', template, flags=re.DOTALL)
if css_match:
    css = css_match.group(1)
    # We remove body styles as they conflict with the SPA
    css = re.sub(r'body\s*{[^}]*}', '', css, flags=re.DOTALL)
    css = re.sub(r':root\s*{[^}]*}', '', css, flags=re.DOTALL)
    css = re.sub(r'\*\s*{[^}]*}', '', css, flags=re.DOTALL)
else:
    css = ""

# Extract just the HTML inside main-wrapper
html_match = re.search(r'<div class="top-section-row">.*?<!-- CONTACT US MODAL -->', template, flags=re.DOTALL)
if html_match:
    details_html = html_match.group(0)
    # Give elements specific IDs for JS updates
    details_html = details_html.replace('{{TITLE}}', '<span id="pd-title"></span>')
    details_html = details_html.replace('{{SUBTITLE}}', '<span id="pd-subtitle"></span>')
    details_html = details_html.replace('{{CATEGORY}}', '<span id="pd-category"></span>')
    details_html = details_html.replace('href="{{CATEGORY_URL}}"', 'href="#" id="pd-catlink" onclick="event.preventDefault();"')
    details_html = details_html.replace('{{PRICE}}', '<span id="pd-price"></span>')
    details_html = details_html.replace('{{UNIT}}', '<span id="pd-unit"></span>')
    details_html = details_html.replace('src="{{IMAGE}}"', 'src="" id="pd-img"')
    details_html = details_html.replace('{{ORIGIN_LABEL}}', '<span id="pd-origin-label"></span>')
    details_html = details_html.replace('{{ORIGIN}}', '<span id="pd-origin"></span>')
    details_html = details_html.replace('{{BEST_FOR}}', '<span id="pd-best-for"></span>')
    details_html = details_html.replace('{{NUTRITION_PROTEIN}}, {{NUTRITION_FAT}}, {{NUTRITION_CALORIES}}', '<span id="pd-nutr"></span>')
    details_html = details_html.replace('{{ALLERGY}}', '<span id="pd-allergy"></span>')
    details_html = details_html.replace('{{HOW_TO_COOK}}', '<span id="pd-how-cook"></span>')
    details_html = details_html.replace('{{SPECIALITY}}', '<span id="pd-speciality"></span>')
    details_html = details_html.replace('{{FAMOUS_FOR}}', '<span id="pd-famous-for"></span>')
    
    # Let's fix the thumbs
    details_html = details_html.replace('<div class="gallery-thumbnails">', '<div class="gallery-thumbnails" id="pd-thumbs">')
    # Let's fix the video
    details_html = details_html.replace('src="{{VIDEO1_URL}}"', 'src="" id="pd-vid1"')
    details_html = details_html.replace('src="{{VIDEO2_URL}}"', 'src="" id="pd-vid2"')
    details_html = details_html.replace('{{INSTRUCTIONS}}', '<div id="pd-instructions"></div>')
else:
    print("Could not find HTML in template")
    exit(1)

# Now we construct the JS block
js_block = f"""
<script>
const pdData = {json.dumps(data)};

function showDetails(id) {{
    const d = pdData[id];
    if(!d) return;
    
    document.getElementById('pd-title').innerText = d.title;
    document.getElementById('pd-subtitle').innerText = d.subtitle;
    document.getElementById('pd-category').innerText = d.category;
    document.getElementById('pd-price').innerText = d.price;
    document.getElementById('pd-unit').innerText = d.unit;
    
    const catLink = document.getElementById('pd-catlink');
    catLink.onclick = function(e) {{ e.preventDefault(); go(d.category.toLowerCase()); }};
    
    document.getElementById('pd-img').src = d.image;
    
    // Thumbs
    const thumbs = document.getElementById('pd-thumbs');
    if(thumbs) {{
        thumbs.innerHTML = '';
        if (d.gallery && d.gallery.length > 0) {{
            for(let i=0; i<d.gallery.length; i++) {{
                thumbs.innerHTML += `<img src="${{d.gallery[i]}}" class="thumb ${{i===0?'active':''}}" onclick="changeHeroImage(this.src, this)">`;
            }}
            document.getElementById('pd-img').src = d.gallery[0];
        }} else {{
            for(let i=0; i<6; i++) {{
                thumbs.innerHTML += `<img src="${{d.image}}" class="thumb ${{i===0?'active':''}}" onclick="changeHeroImage(this.src, this)">`;
            }}
        }}
    }}
    
    document.getElementById('pd-origin-label').innerText = d.origin_label;
    document.getElementById('pd-origin').innerText = d.origin;
    document.getElementById('pd-best-for').innerText = d.best_for;
    document.getElementById('pd-nutr').innerText = d.nutrition_protein + ", " + d.nutrition_fat + ", " + d.nutrition_calories;
    document.getElementById('pd-allergy').innerText = d.allergy;
    document.getElementById('pd-how-cook').innerText = d.how_to_cook;
    document.getElementById('pd-speciality').innerText = d.speciality;
    document.getElementById('pd-famous-for').innerText = d.famous_for;
    
    if(document.getElementById('pd-vid1')) document.getElementById('pd-vid1').src = d.video1;
    if(document.getElementById('pd-vid2')) document.getElementById('pd-vid2').src = d.video2;
    if(document.getElementById('pd-instructions')) document.getElementById('pd-instructions').innerHTML = d.instructions;
    
    go('details');
}}
</script>
"""

with open(r'.\index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

from bs4 import BeautifulSoup
soup = BeautifulSoup(index_html, 'html.parser')

cards = soup.find_all('div', class_='fp-card')
for card in cards:
    # We find the image src to extract product ID as a fallback, but the most reliable way 
    # since we cleaned up the tags is matching by filename if it's still local, or matching 
    # by the title text.
    prod_id = None
    
    # Try to find product ID from old image src
    img = card.find('img', class_='fp-cimg')
    if img and 'src' in img.attrs and 'assets/' in img['src']:
        m = re.search(r'assets/([^.]+)\.jpg', img['src'])
        if m:
            prod_id = m.group(1)
            
    # If not found from image, try matching the title with our Sanity data
    if not prod_id:
        title_div = card.find('div', class_='fp-ct')
        if title_div:
            for k, v in data.items():
                if v.get('title') == title_div.text.strip():
                    prod_id = k
                    break

    if prod_id:
        # Update image source if Sanity has it
        if prod_id in data and 'image' in data[prod_id]:
            img = card.find('img', class_='fp-cimg')
            if img:
                img['src'] = data[prod_id]['image']
                
        # Fix the SPA link
        cbot = card.find('div', class_='fp-cbot')
        if cbot:
            clink = cbot.find('div', class_='fp-clink')
            if clink:
                # Wrap it in a div with onclick for the SPA
                div_tag = soup.new_tag('div', style="cursor:pointer;")
                div_tag['onclick'] = f"showDetails('{prod_id}')"
                clink.wrap(div_tag)
                
index_html = str(soup)

# Insert the page-details block
if 'id="page-details"' not in index_html:
    page_details_div = f"""
<div id="page-details" class="page" style="background:#F8FAFC; overflow-y:auto; height:100%;">
  <style>{css}</style>
  <div style="padding: 16px 24px; padding-bottom:100px;">
    {details_html}
  </div>
</div>
"""
    # Insert before <div id="page-cook"
    index_html = index_html.replace('<div id="page-cook"', page_details_div + '\n<div id="page-cook"')

# Insert the JS block before </body>
if 'const pdData =' not in index_html:
    index_html = index_html.replace('</body>', js_block + '\n</body>')

with open(r'.\index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print('Updated index.html to inject SPA product details')

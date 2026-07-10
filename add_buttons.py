import re

with open(r'.\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replacer(card):
    # Extract image name
    img_match = re.search(r'assets/([^.]+)\.jpg', card)
    if img_match:
        img_name = img_match.group(1)
        
        # Determine the color based on the tag or category
        color = ""
        if 'C2185B' in card or 'beef' in img_name or 'meat' in img_name or 'lamb' in img_name or 'mutton' in img_name or 'rabbit' in img_name or 'buffalo' in img_name:
            color = 'color:#C2185B;' # Meat
        elif 'F57F17' in card or 'chicken' in img_name:
            color = 'color:#F57F17;' # Chicken
        elif '2E7D32' in card or 'egg' in img_name:
            color = 'color:#2E7D32;' # Eggs
        
        # Check if it already has showDetails
        if 'showDetails' not in card:
            # We need to inject it into fp-cbot
            # The cbot currently looks like: <div class="fp-cbot"><div><span class="fp-cprice">£5.99</span><span class="fp-cunit"> / kg</span></div></div>
            # We want: <div class="fp-cbot"><div>...</div><div onclick="showDetails('img_name')" style="cursor:pointer;"><div class="fp-clink" style="color">View Details &rarr;</div></div></div>
            
            # Find the inner div of cbot
            cbot_match = re.search(r'<div class="fp-cbot">(.*?)</div>\s*</div>', card, flags=re.DOTALL)
            if cbot_match:
                inner = cbot_match.group(1)
                new_cbot = f'<div class="fp-cbot">{inner}<div onclick="showDetails(\'{img_name}\')" style="cursor:pointer;"><div class="fp-clink" style="{color}">View Details →</div></div></div></div>'
                card = card.replace(cbot_match.group(0), new_cbot)
                
    return card

cards = html.split('<div class="fp-card">')
new_cards = [cards[0]]
for card in cards[1:]:
    fixed = replacer('<div class="fp-card">' + card)
    new_cards.append(fixed.replace('<div class="fp-card">', '', 1))

new_html = '<div class="fp-card">'.join(new_cards)

with open(r'.\index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print('Added missing View Details buttons')

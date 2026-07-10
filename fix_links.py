import re

with open(r'd:\fishcart2\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replacer(card):
    # Extract image name
    img_match = re.search(r'assets/([^.]+)\.jpg', card)
    if img_match:
        img_name = img_match.group(1)
        
        # Replace the entire view details wrapper that was botched
        # It currently looks like: <div onclick="showDetails(\'prod_1_salmon\')" style="cursor:pointer;"><div class="fp-clink">View Details →</div></div>
        # or <div onclick="showDetails('prod_1_salmon')" style="cursor:pointer;"><div class="fp-clink">View Details →</div></div>
        
        # Strip out any existing onclicks and View details completely in the cbot
        card_fixed = re.sub(r'<div onclick="showDetails.*?</div></div>', 
                            f'<div onclick="showDetails(\'{img_name}\')" style="cursor:pointer;"><div class="fp-clink">View Details →</div></div>', 
                            card, flags=re.DOTALL)
        
        # If it has the literal backslash:
        card_fixed = re.sub(r'<div onclick="showDetails\(\\\'prod_1_salmon\\\'\).*?</div></div>', 
                            f'<div onclick="showDetails(\'{img_name}\')" style="cursor:pointer;"><div class="fp-clink">View Details →</div></div>', 
                            card_fixed, flags=re.DOTALL)
                            
        # If it has the old fp-clink only:
        card_fixed = re.sub(r'<div><div class="fp-clink">View Details →</div></div>', 
                            f'<div onclick="showDetails(\'{img_name}\')" style="cursor:pointer;"><div class="fp-clink">View Details →</div></div>', 
                            card_fixed, flags=re.DOTALL)
        
        return card_fixed
    return card

# Split by fp-card to avoid dotall matching across multiple cards
cards = html.split('<div class="fp-card">')
new_cards = [cards[0]]
for card in cards[1:]:
    fixed = replacer('<div class="fp-card">' + card)
    new_cards.append(fixed.replace('<div class="fp-card">', '', 1))

new_html = '<div class="fp-card">'.join(new_cards)

with open(r'd:\fishcart2\index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print('Fixed links in index.html')

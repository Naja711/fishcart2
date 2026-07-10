import re

with open(r'd:\fishcart2\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replacer(match):
    full_card = match.group(0)
    img_name = match.group(1) # e.g. beef_chunks
    # find the View Details div in this card
    card_fixed = re.sub(r'<div class="fp-clink"[^>]*>View Details.*?</div>', 
                        f'<a href="details_{img_name}.html" style="text-decoration:none;">\g<0></a>', 
                        full_card)
    return card_fixed

new_html = re.sub(r'<div class="fp-card">.*?<img class="fp-cimg" src="assets/([^.]+)\.jpg".*?</div></div></div>', replacer, html, flags=re.DOTALL)

with open(r'd:\fishcart2\index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print('Updated links in index.html')

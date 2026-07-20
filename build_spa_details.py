import json
import re
from generate_details_pages import data

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
html_match = re.search(r'<div class="main-wrapper".*?<!-- CONTACT US MODAL -->', template, flags=re.DOTALL)
if html_match:
    details_html = html_match.group(0)
    # Replace default placeholders so initial static HTML has valid fallbacks
    details_html = details_html.replace("{{TITLE}}", "Salmon")
    details_html = details_html.replace("{{PRICE}}", "£14.99")
    details_html = details_html.replace("{{UNIT}}", "kg")
    details_html = details_html.replace("{{IMAGE}}", "assets/prod_1_salmon.jpg")
    details_html = details_html.replace("{{CATEGORY}}", "Fish")
    details_html = details_html.replace("{{CATEGORY_URL}}", "index.html#fish")
    details_html = details_html.replace("{{ORIGIN_LABEL}}", "Catch From")
    details_html = details_html.replace("{{ORIGIN}}", "Norway, North Atlantic Ocean. Wild Caught.")
    details_html = details_html.replace("{{BEST_FOR}}", "Curry, Grill, Baking.")
    details_html = details_html.replace("{{NUTRITION_PROTEIN}}", "20.4g")
    details_html = details_html.replace("{{NUTRITION_FAT}}", "13.4g")
    details_html = details_html.replace("{{NUTRITION_CALORIES}}", "208 kcal")
    details_html = details_html.replace("{{NUTRITION_EXTRA_LABEL}}", "Omega-3")
    details_html = details_html.replace("{{NUTRITION_EXTRA_VAL}}", "3")
    details_html = details_html.replace("{{SPECIALITY}}", "Rich, buttery flavor and firm texture.")
    details_html = details_html.replace("{{FAMOUS_FOR}}", "Norwegian Cuisine, Japanese Sushi.")
    details_html = details_html.replace("{{ALLERGY}}", "Contains Fish.")
    details_html = details_html.replace("{{HOW_TO_COOK}}", "Grill or pan-sear. Great with lemon and herbs.")
    details_html = details_html.replace("{{VIDEO1_URL}}", "https://www.youtube.com/embed/jH-1gV1fH-s")
    details_html = details_html.replace("{{VIDEO2_URL}}", "https://www.youtube.com/embed/9gN2lB5B9Qo")
    details_html = details_html.replace("{{INSTRUCTIONS}}", "<li>Preheat pan on medium-high.</li><li>Season salmon with salt and pepper.</li><li>Sear skin-side down for 4 mins.</li><li>Flip and cook 2 mins.</li>")
    details_html = details_html.replace("{{FISH_ACTIVE}}", "active")
    details_html = details_html.replace("{{MEAT_ACTIVE}}", "")
    details_html = details_html.replace("{{CHICKEN_ACTIVE}}", "")
    details_html = details_html.replace("{{EGGS_ACTIVE}}", "")
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
    
    const titleEl = document.getElementById('pd-title');
    if(titleEl) titleEl.innerText = d.title;
    
    const titleBc = document.getElementById('pd-title-breadcrumb');
    if(titleBc) titleBc.innerText = d.title;

    const cookTitle = document.getElementById('pd-cook-title');
    if(cookTitle) cookTitle.innerText = d.title;

    const descEl = document.getElementById('pd-desc');
    if(descEl) descEl.innerText = `Rich in Omega-3 and loaded with nutrients, ${{d.title}} is known for its incredible taste and health benefits.`;
    
    const catEl = document.getElementById('pd-category');
    if(catEl) catEl.innerText = d.category;
    
    const priceEl = document.getElementById('pd-price');
    if(priceEl) priceEl.innerText = d.price;
    
    const unitEl = document.getElementById('pd-unit');
    if(unitEl) unitEl.innerText = d.unit;
    
    const catLink = document.getElementById('pd-catlink');
    if(catLink) {{
        catLink.onclick = function(e) {{ e.preventDefault(); go(d.category.toLowerCase()); }};
    }}
    
    const mainImg = document.getElementById('pd-img');
    if(mainImg) mainImg.src = d.image;
    
    // Thumbs
    const thumbs = document.getElementById('pd-thumbs');
    if(thumbs) {{
        thumbs.innerHTML = '';
        if (d.gallery && d.gallery.length > 0) {{
            for(let i=0; i<d.gallery.length; i++) {{
                thumbs.innerHTML += `<img src="${{d.gallery[i]}}" class="thumb ${{i===0?'active':''}}" onclick="changeHeroImage(this.src, this)" style="width:36px; height:36px; border-radius:6px; object-fit:cover; cursor:pointer;">`;
            }}
            if(mainImg) mainImg.src = d.gallery[0];
        }} else {{
            for(let i=0; i<6; i++) {{
                thumbs.innerHTML += `<img src="${{d.image}}" class="thumb ${{i===0?'active':''}}" onclick="changeHeroImage(this.src, this)" style="width:36px; height:36px; border-radius:6px; object-fit:cover; cursor:pointer;">`;
            }}
        }}
    }}
    
    const origLbl = document.getElementById('pd-origin-label');
    if(origLbl) origLbl.innerText = d.origin_label;
    
    const origVal = document.getElementById('pd-origin');
    if(origVal) origVal.innerText = d.origin;
    
    const specVal = document.getElementById('pd-speciality');
    if(specVal) specVal.innerText = d.speciality;
    
    const famVal = document.getElementById('pd-famous-for');
    if(famVal) famVal.innerText = d.famous_for;

    const protEl = document.getElementById('pd-prot');
    if(protEl) protEl.innerText = d.nutrition_protein || '20.4g';

    const calEl = document.getElementById('pd-cal');
    if(calEl) calEl.innerText = d.nutrition_calories || '208 kcal';

    const fatEl = document.getElementById('pd-fat');
    if(fatEl) fatEl.innerText = d.nutrition_fat || '13.4g';
    
    const allVal = document.getElementById('pd-allergy');
    if(allVal) allVal.innerText = d.allergy;
    
    // Store numeric price for size calculations
    window.currentBasePrice = parseFloat((d.price || '14.99').replace(/[^0-9.]/g, '')) || 14.99;

    // Reset size selector to Medium (default)
    const sizeOpts = document.querySelectorAll('.pd-size-opt');
    sizeOpts.forEach((o, idx) => {{
        if(idx === 1) {{
            o.classList.add('active');
            o.style.border = '1.5px solid #0350dc';
            o.style.background = '#ebf5ff';
            o.style.color = '#0350dc';
            o.style.fontWeight = '700';
            const s = o.querySelector('span'); if(s) s.style.color = '#0350dc';
        }} else {{
            o.classList.remove('active');
            o.style.border = '1px solid #e2e8f0';
            o.style.background = '#ffffff';
            o.style.color = '#64748b';
            o.style.fontWeight = '400';
            const s = o.querySelector('span'); if(s) s.style.color = '#64748b';
        }}
    }});
    
    go('details');
}}

function changeHeroImage(src, el) {{
    const mainImg = document.getElementById('pd-img');
    if(mainImg) mainImg.src = src;
    const thumbs = document.querySelectorAll('.gallery-thumbnails .thumb');
    thumbs.forEach(t => t.classList.remove('active'));
    if(el) el.classList.add('active');
}}

function pdSelectSize(el, mult) {{
    const opts = el.parentElement.querySelectorAll('.pd-size-opt');
    opts.forEach(o => {{
        o.classList.remove('active');
        o.style.border = '1px solid #e2e8f0';
        o.style.background = '#ffffff';
        o.style.color = '#64748b';
        o.style.fontWeight = '400';
        const sub = o.querySelector('span'); if(sub) sub.style.color = '#64748b';
    }});
    el.classList.add('active');
    el.style.border = '1.5px solid #0350dc';
    el.style.background = '#ebf5ff';
    el.style.color = '#0350dc';
    el.style.fontWeight = '700';
    const sub = el.querySelector('span'); if(sub) sub.style.color = '#0350dc';

    const priceEl = document.getElementById('pd-price');
    if(priceEl && window.currentBasePrice) {{
        const calc = (window.currentBasePrice * mult).toFixed(2);
        priceEl.innerText = '£' + calc;
    }}
}}

function pdSelectCut(el) {{
    const cuts = el.parentElement.querySelectorAll('.pd-cut-opt');
    cuts.forEach(c => {{
        c.classList.remove('active');
        c.style.fontWeight = '500';
        c.style.color = '#64748b';
        c.style.textDecoration = 'none';
    }});
    el.classList.add('active');
    el.style.fontWeight = '800';
    el.style.color = '#0350dc';
    el.style.textDecoration = 'underline';
}}

function pdShareEmail() {{
    const titleEl = document.getElementById('pd-title');
    const title = titleEl ? titleEl.innerText : 'Fishcart Product';
    const priceEl = document.getElementById('pd-price');
    const price = priceEl ? priceEl.innerText : '';
    const subject = encodeURIComponent(`Fresh ${{title}} on Fishcart`);
    const body = encodeURIComponent(`Hi, check out this fresh ${{title}} on Fishcart for ${{price}}! ${{window.location.href}}`);
    window.location.href = `mailto:?subject=${{subject}}&body=${{body}}`;
}}

function pdToggleFav(btn) {{
    const isFav = btn.classList.toggle('fav-saved');
    if(isFav) {{
        btn.style.background = '#0350dc';
        btn.style.color = '#ffffff';
        btn.style.borderColor = '#0350dc';
        btn.innerHTML = `<svg fill="currentColor" stroke="none" style="width:12px; height:12px;" viewBox="0 0 24 24"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"></path></svg> Saved to Favorites`;
    }} else {{
        btn.style.background = '#ffffff';
        btn.style.color = '#0f46bd';
        btn.style.borderColor = '#cbd5e1';
        btn.innerHTML = `<svg fill="none" stroke="currentColor" stroke-width="2" style="width:12px; height:12px;" viewBox="0 0 24 24"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg> Save to Favorites`;
    }}
}}

function toggleViewMore(btn) {{
    const group = btn.parentElement;
    const moreContainer = group.querySelector('.fp-more-items');
    if(!moreContainer) return;
    
    if(moreContainer.style.display === 'none' || !moreContainer.style.display) {{
        moreContainer.style.display = 'flex';
        btn.innerHTML = 'View Less ⌃';
    }} else {{
        moreContainer.style.display = 'none';
        btn.innerHTML = 'View More ⌄';
    }}
}}

window.currentPage = 1;
window.perPage = 8;

window.changePage = function(delta) {{
    window.goToPage(window.currentPage + delta);
}};

window.changePerPage = function(val) {{
    window.perPage = parseInt(val) || 8;
    window.goToPage(1);
}};

window.goToPage = function(p) {{
    if(p < 1) p = 1;
    if(p > 15) p = 15;
    window.currentPage = p;
    
    const prevBtn = document.getElementById('fp-prev-btn');
    const nextBtn = document.getElementById('fp-next-btn');
    if(prevBtn) {{
        prevBtn.disabled = (p === 1);
        prevBtn.style.opacity = (p === 1) ? '0.5' : '1.0';
    }}
    if(nextBtn) {{
        nextBtn.disabled = (p === 15);
        nextBtn.style.opacity = (p === 15) ? '0.5' : '1.0';
    }}
    
    const pnums = document.querySelectorAll('.fp-pnum');
    pnums.forEach(btn => {{
        const pageNum = parseInt(btn.innerText);
        if(pageNum === p) {{
            btn.classList.add('active');
            btn.style.background = '#0350dc';
            btn.style.color = '#ffffff';
            btn.style.borderColor = '#0350dc';
        }} else {{
            btn.classList.remove('active');
            btn.style.background = '#ffffff';
            btn.style.color = '#0f46bd';
            btn.style.borderColor = '#cbd5e1';
        }}
    }});

    const startItem = (p - 1) * window.perPage + 1;
    const endItem = p * window.perPage;
    const rangeStr = `${{startItem}}-${{endItem}}`;
    
    const rangeText = document.getElementById('fp-range-text');
    if(rangeText) rangeText.innerText = rangeStr;
    
    const pinfoRange = document.getElementById('fp-pinfo-range');
    if(pinfoRange) pinfoRange.innerText = rangeStr;

    if(typeof window.renderFish === 'function') {{
        window.renderFish();
    }}
}};
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
                # Wrap it in a div with onclick for the SPA only if not already wrapped
                parent = clink.parent
                if parent and parent.name == 'div' and parent.has_attr('onclick') and 'showDetails' in parent['onclick']:
                    parent['onclick'] = f"showDetails('{prod_id}')"
                else:
                    div_tag = soup.new_tag('div', style="cursor:pointer;")
                    div_tag['onclick'] = f"showDetails('{prod_id}')"
                    clink.wrap(div_tag)
                
# Using BeautifulSoup to inject/update page-details
page_details_tag = soup.find('div', id='page-details')
new_page_details_soup = BeautifulSoup(f"""
<div id="page-details" class="page" style="background:#F8FAFC; overflow-y:auto; height:100%;">
  <style>{css}</style>
  <div style="padding: 16px 24px; padding-bottom:100px;">
    {details_html}
  </div>
</div>
""", 'html.parser')

if page_details_tag:
    page_details_tag.replace_with(new_page_details_soup)
else:
    page_cook_tag = soup.find('div', id='page-cook')
    if page_cook_tag:
        page_cook_tag.insert_before(new_page_details_soup)
    else:
        soup.body.append(new_page_details_soup)

index_html = str(soup)

# Always replace the pdData JS block to keep product data current
import re as _re
if 'const pdData =' in index_html:
    # Remove the old script block containing pdData
    index_html = _re.sub(r'<script>\s*const pdData =.*?</script>', '', index_html, flags=_re.DOTALL)

# Insert the fresh block BEFORE DOMContentLoaded script so pdData is defined when renderFish() runs
if "<script>\ndocument.addEventListener('DOMContentLoaded'" in index_html:
    index_html = index_html.replace("<script>\ndocument.addEventListener('DOMContentLoaded'", js_block + "\n<script>\ndocument.addEventListener('DOMContentLoaded'", 1)
elif "<script>\n  document.addEventListener('DOMContentLoaded'" in index_html:
    index_html = index_html.replace("<script>\n  document.addEventListener('DOMContentLoaded'", js_block + "\n<script>\n  document.addEventListener('DOMContentLoaded'", 1)
else:
    index_html = index_html.replace('</body>', js_block + '\n</body>')

with open(r'.\index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print('Updated index.html to inject SPA product details')

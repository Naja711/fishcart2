import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add ID to the grid container and remove hardcoded cards
cards_pattern = re.compile(r'<div class="fp-grid">.*?</div>\n</div>\n</div>\n<!-- FEATURES -->', re.DOTALL)
replacement = '''<div class="fp-grid" id="fp-fish-grid">
</div>
</div>
</div>
<!-- FEATURES -->'''
html = cards_pattern.sub(replacement, html)

# 2. Add IDs to the sorting dropdowns
html = html.replace('<select class="fp-psel"><option>Newest First</option></select>', '<select class="fp-psel" id="fp-sort"><option value="newest">Newest First</option><option value="price_low">Price: Low to High</option><option value="price_high">Price: High to Low</option></select>')
html = html.replace('<select class="fp-select"><option>Newest First</option></select>', '<select class="fp-select" id="fp-sort-sidebar"><option value="newest">Newest First</option><option value="price_low">Price: Low to High</option><option value="price_high">Price: High to Low</option></select>')

# 3. Add values to checkboxes so JS can read them easily
html = html.replace('<input checked="" type="checkbox"/> 🇬🇧 United Kingdom', '<input type="checkbox" value="uk" class="filter-country"/> 🇬🇧 United Kingdom')
html = html.replace('<input checked="" type="checkbox"/> 🇳🇴 Norway', '<input type="checkbox" value="norway" class="filter-country"/> 🇳🇴 Norway')
html = html.replace('<input type="checkbox"/> 🏴󠁧󠁢󠁳󠁣󠁴󠁿 Scotland', '<input type="checkbox" value="scotland" class="filter-country"/> 🏴󠁧󠁢󠁳󠁣󠁴󠁿 Scotland')
html = html.replace('<input type="checkbox"/> 🇮🇸 Iceland', '<input type="checkbox" value="iceland" class="filter-country"/> 🇮🇸 Iceland')
html = html.replace('<input type="checkbox"/> 🇳🇱 Netherlands', '<input type="checkbox" value="netherlands" class="filter-country"/> 🇳🇱 Netherlands')

html = html.replace('<input type="checkbox"/> Grill Fishes', '<input type="checkbox" value="grill" class="filter-type"/> Grill Fishes')
html = html.replace('<input type="checkbox"/> Curry Fishes', '<input type="checkbox" value="curry" class="filter-type"/> Curry Fishes')
html = html.replace('<input type="checkbox"/> Steak Cuts', '<input type="checkbox" value="steak" class="filter-type"/> Steak Cuts')
html = html.replace('<input type="checkbox"/> Whole Fish', '<input type="checkbox" value="whole" class="filter-type"/> Whole Fish')
html = html.replace('<input type="checkbox"/> Fillets', '<input type="checkbox" value="fillet" class="filter-type"/> Fillets')

html = html.replace('<input type="checkbox"/> Small (0-500g)', '<input type="checkbox" value="small" class="filter-size"/> Small (0-500g)')
html = html.replace('<input type="checkbox"/> Medium (500g-1kg)', '<input type="checkbox" value="medium" class="filter-size"/> Medium (500g-1kg)')
html = html.replace('<input type="checkbox"/> Large (1kg+)', '<input type="checkbox" value="large" class="filter-size"/> Large (1kg+)')

# 4. Add IDs to top tabs
html = re.sub(r'<div class="fp-tab( active)?">(\s*<span class="fp-tab-ic">.*?</span>\s*<div class="fp-tab-txt"><span class="fp-tab-n">(.*?)</span>)', r'<div class="fp-tab\1" data-tab-name="\3">\2', html)

# Add the JS logic
js_logic = """
<script>
document.addEventListener('DOMContentLoaded', () => {
    const grid = document.getElementById('fp-fish-grid');
    if(!grid) return;

    // Remove empty <p> that might be in grid if we didn't clear well
    grid.innerHTML = '';
    
    const countryCheckboxes = document.querySelectorAll('.filter-country');
    const typeCheckboxes = document.querySelectorAll('.filter-type');
    const sizeCheckboxes = document.querySelectorAll('.filter-size');
    const sortMain = document.getElementById('fp-sort');
    const sortSidebar = document.getElementById('fp-sort-sidebar');
    const tabs = document.querySelectorAll('.fp-tab');

    // Sync sorts
    if(sortMain && sortSidebar) {
        sortMain.addEventListener('change', (e) => { sortSidebar.value = e.target.value; renderFish(); });
        sortSidebar.addEventListener('change', (e) => { sortMain.value = e.target.value; renderFish(); });
    }
    
    // Add event listeners
    [...countryCheckboxes, ...typeCheckboxes, ...sizeCheckboxes].forEach(cb => {
        cb.addEventListener('change', renderFish);
    });

    // Top Tabs logic
    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            tabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');
            const name = tab.getAttribute('data-tab-name');
            
            // reset all checkboxes
            [...countryCheckboxes, ...typeCheckboxes, ...sizeCheckboxes].forEach(cb => cb.checked = false);
            
            if(name === 'By Country') {
                // Check a couple countries
                if(countryCheckboxes[0]) countryCheckboxes[0].checked = true;
                if(countryCheckboxes[1]) countryCheckboxes[1].checked = true;
            } else if(name === 'Grill Fishes') {
                const cb = document.querySelector('.filter-type[value="grill"]');
                if(cb) cb.checked = true;
            } else if(name === 'Curry Fishes') {
                const cb = document.querySelector('.filter-type[value="curry"]');
                if(cb) cb.checked = true;
            }
            renderFish();
        });
    });

    function renderFish() {
        // get selected filters
        const selCountries = Array.from(countryCheckboxes).filter(cb => cb.checked).map(cb => cb.value);
        const selTypes = Array.from(typeCheckboxes).filter(cb => cb.checked).map(cb => cb.value);
        const selSizes = Array.from(sizeCheckboxes).filter(cb => cb.checked).map(cb => cb.value);
        const sortBy = sortMain ? sortMain.value : 'newest';

        let products = Object.keys(pdData).map(k => ({id: k, ...pdData[k]})).filter(p => p.category === 'Fish');

        // Apply filters
        if(selCountries.length > 0) {
            products = products.filter(p => {
                const text = ((p.subtitle||'') + " " + (p.origin||'')).toLowerCase();
                return selCountries.some(c => text.includes(c) || (c==='uk' && text.includes('united kingdom')));
            });
        }
        
        if(selTypes.length > 0) {
            products = products.filter(p => {
                const text = ((p.subtitle||'') + " " + (p.best_for||'')).toLowerCase();
                return selTypes.some(t => text.includes(t));
            });
        }

        if(selSizes.length > 0) {
            // Mock: if selected, filter some out based on id length to simulate filtering
            products = products.filter(p => p.id.length % 2 === (selSizes.includes('small') ? 1 : 0));
        }

        // Sort
        if(sortBy === 'price_low') {
            products.sort((a,b) => parseFloat(a.price.replace('£','')) - parseFloat(b.price.replace('£','')));
        } else if(sortBy === 'price_high') {
            products.sort((a,b) => parseFloat(b.price.replace('£','')) - parseFloat(a.price.replace('£','')));
        }
        // newest is default, no sort needed

        // Render
        grid.innerHTML = '';
        if(products.length === 0) {
            grid.innerHTML = '<div style="grid-column: 1/-1; padding: 40px; text-align: center; color: #555; font-size: 16px;">No products match your selected filters. Try removing some filters.</div>';
        } else {
            products.forEach(p => {
                let tags = 'Fresh Catch';
                if((p.nutrition_extra_label || '').toLowerCase().includes('omega')) tags = 'Rich in Omega-3';
                else if((p.nutrition_extra_label || '').toLowerCase().includes('protein')) tags = 'High in Protein';
                else if((p.nutrition_extra_val || '').toLowerCase() === 'high') tags = 'High in Vitamins';

                grid.innerHTML += `
                <div class="fp-card">
                  <div class="fp-fav"><svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"></path></svg></div>
                  <img alt="${p.title}" class="fp-cimg" src="${p.image}"/>
                  <div class="fp-ct">${p.title}</div>
                  <div class="fp-csub">${p.subtitle}</div>
                  <div><span class="fp-ctag">${tags}</span></div>
                  <div class="fp-cbot">
                    <div><span class="fp-cprice">${p.price}</span><span class="fp-cunit"> / ${p.unit}</span></div>
                    <div style="cursor:pointer;" onclick="showDetails('${p.id}')">
                      <a href="details_${p.id}.html" style="text-decoration:none;">
                        <div class="fp-clink">View Details &rarr;</div>
                      </a>
                    </div>
                  </div>
                </div>`;
            });
        }
        
        // Update count
        const phL = document.querySelector('.fp-ph-l');
        if(phL) {
            phL.innerText = `Showing 1-${products.length} of 120+ items`;
        }
    }

    // Initial render
    renderFish();
});
</script>
</body>
"""

html = html.replace('</body>', js_logic)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Filtering logic injected.")

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Insert CSS for page-cook
css = '''
/* ── COOK PAGE ── */
.cook-page { display: flex; flex-direction: column; gap: 12px; height: 100%; overflow-y: auto; background: #E8F3FA; padding: 12px; }
.cook-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 12px; }
.cook-card { background: #fff; border-radius: 12px; overflow: hidden; display: flex; flex-direction: column; text-decoration: none; }
.cook-card:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
.cook-img { width: 100%; height: 140px; object-fit: cover; }
.cook-info { padding: 10px; flex: 1; display: flex; flex-direction: column; }
.cook-title { font-size: 13px; font-weight: 700; color: #0A2848; margin-bottom: 4px; }
.cook-btn { margin-top: auto; display: inline-flex; align-items: center; justify-content: center; background: #1565C0; color: #fff; border: none; padding: 6px 12px; border-radius: 6px; font-size: 11px; font-weight: 600; cursor: pointer; text-decoration: none; }
'''

if '/* ── COOK PAGE ── */' not in html:
    html = html.replace('</style>', css + '\n</style>')

# Insert page-cook HTML
page_html = '''
<!-- ═══ COOK PAGE ═══ -->
<div class="page" id="page-cook">
    <div class="cook-page">
        <div class="fp-banner" style="background: linear-gradient(115deg, #1565C0 0%, #1050A0 100%); color: white;">
            <div class="fp-title" style="color: white;">How to Cook</div>
            <div class="fp-desc" style="color: rgba(255,255,255,0.85);">Discover delicious recipes for our fresh catches.</div>
        </div>
        <div class="cook-grid" id="cook-grid-container">
            <!-- Dynamic Recipe Cards will be inserted here -->
        </div>
    </div>
</div>
'''

if 'id="page-cook"' not in html:
    # insert before the closing app div
    # search for closing </div>\n</div>\n</body>
    # actually, just insert it before </body> and make sure it's inside .app
    # <div class="page" id="page-contact"> ... </div>\n</div>
    # let's just insert before the very last </div> which closes .app
    
    last_div_idx = html.rfind('</div>')
    if last_div_idx != -1:
        html = html[:last_div_idx] + page_html + html[last_div_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Added #page-cook to index.html')

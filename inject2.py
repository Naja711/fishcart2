with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

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

if 'id="page-cook"' not in text:
    text = text.replace('<!-- ═══ PRODUCT DETAILS SPA MODAL ═══ -->', page_html + '\n<!-- ═══ PRODUCT DETAILS SPA MODAL ═══ -->')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Inserted page-cook before SPA modal')
else:
    print('page-cook already exists!')

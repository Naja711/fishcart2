with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

page_html = '''<div class="page" id="page-cook">
    <div class="cook-page">
        <div class="fp-banner" style="background: linear-gradient(115deg, #1565C0 0%, #1050A0 100%); color: white; padding: 20px; border-radius: 12px; margin-bottom: 12px;">
            <div class="fp-title" style="color: white; font-size: 20px; font-weight: 700;">How to Cook</div>
            <div class="fp-desc" style="color: rgba(255,255,255,0.85); font-size: 13px;">Discover delicious recipes for our fresh catches.</div>
        </div>
        <div class="cook-grid" id="cook-grid-container">
            <!-- Dynamic Recipe Cards will be inserted here -->
        </div>
    </div>
</div>'''

start = text.find('<div class="page" id="page-cook">')
if start != -1:
    end = text.find('<div class="page" id="page-benefits">', start)
    if end != -1:
        new_text = text[:start] + page_html + '\n' + text[end:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_text)
        print("Slice replaced successfully!")
    else:
        print("End not found")
else:
    print("Start not found")

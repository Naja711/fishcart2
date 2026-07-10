import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

page_html = '''<div class="page" id="page-cook">
    <div class="cook-page">
        <div class="fp-banner" style="background: linear-gradient(115deg, #1565C0 0%, #1050A0 100%); color: white; padding: 20px; border-radius: 12px;">
            <div class="fp-title" style="color: white; font-size: 20px; font-weight: 700;">How to Cook</div>
            <div class="fp-desc" style="color: rgba(255,255,255,0.85); font-size: 13px;">Discover delicious recipes for our fresh catches.</div>
        </div>
        <div class="cook-grid" id="cook-grid-container">
            <!-- Dynamic Recipe Cards will be inserted here -->
        </div>
    </div>
</div>'''

# Replace the existing placeholder page-cook
# The placeholder is: <div class="page" id="page-cook"><div class="ph"><div class="ph-ico"></div><div class="ph-title">How to Cook</div><div class="ph-sub">Send me the reference  ready to build!</div></div></div>
html = re.sub(r'<div class="page" id="page-cook">.*?</div></div></div>', page_html, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Replaced placeholder page-cook with new layout.')

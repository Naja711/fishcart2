with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

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
    start = html.find('<script>')
    if start != -1:
        idx = html.rfind('</div>', 0, start)
        if idx != -1:
            html = html[:idx] + page_html + '\n</div>\n' + html[idx+6:]
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(html)
            print('Injected page-cook correctly')
        else:
            print('Could not find closing div')
    else:
        print('Could not find script tag')
else:
    print('page-cook already exists')

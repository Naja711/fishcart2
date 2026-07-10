with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add the mobile filter button and overlay to the HTML body
button_html = '''
<div class="filter-overlay" id="filterOverlay" onclick="toggleFilters()"></div>
<div class="mobile-filter-btn" onclick="toggleFilters()">
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"></polygon></svg>
  Filter & Sort
</div>
<script>
function toggleFilters() {
    var sidebar = document.querySelector('.fp-sidebar');
    var overlay = document.getElementById('filterOverlay');
    if (sidebar) {
        sidebar.classList.toggle('filter-open');
        overlay.classList.toggle('active');
        if (sidebar.classList.contains('filter-open')) {
            document.body.style.overflow = 'hidden';
        } else {
            document.body.style.overflow = '';
        }
    }
}
</script>
'''

if 'mobile-filter-btn' not in html:
    html = html.replace('</body>', button_html + '\n</body>')

# 2. Add the CSS styles
desktop_css = '''
/* Filter Modal Styles */
.mobile-filter-btn { display: none; }
.filter-overlay { display: none; }
'''
if '/* Filter Modal Styles */' not in html:
    html = html.replace('/* ── MOBILE RESPONSIVENESS ── */', desktop_css + '\n/* ── MOBILE RESPONSIVENESS ── */')

mobile_css = '''
    /* Filter Modal Mobile */
    .fp-sidebar { 
        position: fixed !important; bottom: 0; left: 0; right: 0; 
        background: white; z-index: 1000; height: 85vh; 
        border-radius: 20px 20px 0 0; padding: 20px;
        box-shadow: 0 -5px 20px rgba(0,0,0,0.15);
        transform: translateY(100%); transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        visibility: hidden; margin-top: 0 !important; width: 100%;
    }
    .fp-sidebar.filter-open { transform: translateY(0); visibility: visible; }
    
    .mobile-filter-btn {
        display: flex; position: fixed; bottom: 30px; left: 50%; transform: translateX(-50%);
        background: #1565C0; color: white; border-radius: 30px; padding: 14px 28px;
        font-weight: 700; font-size: 14px; z-index: 900; box-shadow: 0 4px 15px rgba(21,101,192,0.4);
        cursor: pointer; align-items: center; gap: 8px;
    }
    .filter-overlay.active { display: block; position: fixed; inset: 0; background: rgba(0,0,0,0.5); z-index: 999; }
'''
if '/* Filter Modal Mobile */' not in html:
    html = html.replace('.fp-sidebar { order: 2; margin-top: 15px; }', mobile_css)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Updated index.html with mobile filter modal')

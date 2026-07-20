import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

with open('current_fp_styles.css', 'r', encoding='utf-8') as f:
    new_css = f.read()

# The old fish CSS block marker
old_marker = '/* \u2500\u2500 LIST PAGES (.fp-) \u2500\u2500 */'
idx_start = content.find(old_marker)
if idx_start == -1:
    # fallback
    idx_start = content.find('.fish-page {')
    idx_start = content.rfind('\n', 0, idx_start) + 1

idx_end = content.find('</style>', idx_start)
if idx_start == -1 or idx_end == -1:
    print("Could not find fish CSS block!")
    sys.exit(1)

print(f"Replacing fish CSS at chars {idx_start} to {idx_end}")
new_content = content[:idx_start] + new_css + '\n' + content[idx_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Fish CSS updated in index.html!")

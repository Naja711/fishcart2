with open('patch_index.py', 'r', encoding='utf-8') as f:
    patch = f.read()

target = "window.addEventListener('resize', fitApp);"
replacement = "window.addEventListener('resize', fitApp);\n    window.addEventListener('orientationchange', fitApp);"

if "orientationchange" not in patch:
    patch = patch.replace(target, replacement)
    with open('patch_index.py', 'w', encoding='utf-8') as f:
        f.write(patch)
    print("Updated patch_index.py with orientationchange listener.")

with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

if "orientationchange" not in idx:
    idx = idx.replace(target, replacement)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(idx)
    print("Updated index.html with orientationchange listener.")

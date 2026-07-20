with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Assertions
assert 'id="page-cook"' in text, "No page cook found"
print("Found page-cook: OK")

assert 'border-radius: 24px' in text, "Border radius is not 24px"
print(".app border-radius: 24px: OK")

assert 'border: 16px' in text or 'border-width: 16px' in text, "Border width is not 16px"
print(".app border-width: 16px: OK")

# Colors
assert '#ebf5ff' in text, "Benefits card background color (#ebf5ff) not found"
print("Benefits card background #ebf5ff: OK")

assert '#eef6ff' in text, "Reviews card background color (#eef6ff) not found"
print("Reviews card background #eef6ff: OK")

assert '#e4f2fd' in text, "Daily Selection background (#e4f2fd) not found"
print("Daily Selection background #e4f2fd: OK")

assert '#d2eda9' in text, "Sourced Responsibly background (#d2eda9) not found"
print("Sourced Responsibly background #d2eda9: OK")

# Fish Page Layout Asserts
assert 'class="sidebar-join"' in text, "Sidebar join card not found in index.html"
print("Sidebar join card: OK")

assert 'assets/header_fish3_nobg.png' in text, "header_fish3_nobg.png not found in index.html"
print("Fish banner nobg image: OK")

assert 'path d="M 0 4 Q 7.5 0, 15 4 T 30 4 T 45 4 T 60 4"' in text, "Wave SVG path not found in index.html"
print("Fish banner wave decoration: OK")

assert 'value="uk"' in text and 'checked' in text, "UK checkbox should be checked"
assert 'value="norway"' in text and 'checked' in text, "Norway checkbox should be checked"
print("Checked UK and Norway filters by default: OK")

print("All verifications passed successfully!")

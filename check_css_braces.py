with open('patch_index.py', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('NEW_STYLES = """')
end = text.find('NEW_BODY = """')
styles = text[start:end]

lines = styles.split('\n')
stack = []
for line_num, line in enumerate(lines, 1):
    for char in line:
        if char == '{':
            stack.append((line_num, line.strip()))
        elif char == '}':
            if stack:
                stack.pop()
            else:
                print(f"Extra closing brace at line {line_num}: {line.strip()}")

print(f"Remaining unclosed braces: {len(stack)}")
for line_num, content in stack:
    print(f"Unclosed '{'{'}' opened at line {line_num}: {content}")

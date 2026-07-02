import re

with open('/Users/ikhaisoshuare/Cascade/presentation.html', 'r') as f:
    text = f.read()

# Update CSS variables
text = text.replace(
    '--bg-gradient: radial-gradient(circle at 50% -10%, #36302c 0%, #171514 100%);',
    '--bg-gradient: radial-gradient(circle at 50% -10%, #0f172a 0%, #020617 100%);'
)
text = text.replace(
    '--bg-solid: #171514;',
    '--bg-solid: #020617;'
)
text = text.replace(
    '--text: #F8F5F0;',
    '--text: #f8fafc;'
)
text = text.replace(
    '--text-muted: #9E948A;',
    '--text-muted: #94a3b8;'
)
text = text.replace(
    '--accent: #E27953;',
    '--accent: #38bdf8;'
)

# Update the inline RGBA colors (226, 121, 83 -> 56, 189, 248)
text = re.sub(r'rgba\(226,\s*121,\s*83,', 'rgba(56, 189, 248,', text)

with open('/Users/ikhaisoshuare/Cascade/presentation.html', 'w') as f:
    f.write(text)

print("Colors updated successfully in presentation.html")

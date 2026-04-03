import re

html_path = r'c:\Users\jm881\OneDrive\CRASTO.COM\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Determine the exact block of CSS modifying the ambient
match = re.search(r'(#crastoAmbient\{.*?\})', html)
if match:
    # Replace the ambient with a sophisticated, monogenic dark gradient (Editorial/Anti-AI)
    new_ambient = "#crastoAmbient{position:fixed;inset:0;background:radial-gradient(120% 100% at 50% 0%, rgb(201 168 76 / .04) 0%, rgb(13 13 13 / 1) 100%);pointer-events:none;z-index:0}"
    html = html.replace(match.group(1), new_ambient)

# Hide cursor glow and particles
html = html.replace('#crastoCursorGlow{', '#crastoCursorGlow{display:none!important;')
html = html.replace('#crastoParticles{', '#crastoParticles{display:none!important;')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Anti-AI Professional UX adjustments applied!")

import re

html_path = r'c:\Users\jm881\OneDrive\CRASTO.COM\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Find the CSS block
match = re.search(r'(<style>:root\{--gold:.*?</style>)', html, flags=re.DOTALL)
if not match:
    print("CSS block not found!")
    exit(1)

css = match.group(1)

# 1. Typography letter-spacing (uppercase is more premium with tighter spacing)
css = css.replace('letter-spacing:.2em!important', 'letter-spacing:.08em!important')
css = css.replace('letter-spacing:.15em', 'letter-spacing:.06em')
css = css.replace('letter-spacing:.1em', 'letter-spacing:.05em')

# 2. Bento Grid / Glassmorphism on cards
# We prepend generic high-end styles for cards right after body styles
bento_styles = """.bento-card, .pain-card, .solution-card, .pessoal-card, .caso-card, .proof-stat {
    border-radius: 24px !important;
    background: rgb(20 20 20 / .45) !important;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgb(255 255 255 / .04) !important;
    box-shadow: inset 0 1px 0 rgb(255 255 255 / .06), 0 10px 40px rgba(0,0,0,0.2) !important;
}"""

css = css.replace('}#crastoAmbient', '}' + bento_styles + '#crastoAmbient')

# 3. Enhance hover scale across all interactive cards (Liquid UI micro-interaction)
# Find existing transform Y and add a scale
css = css.replace('transform:translateY(-4px)', 'transform:translateY(-4px) scale(1.01)')
css = css.replace('transform:translateY(-6px)', 'transform:translateY(-6px) scale(1.015)')
css = css.replace('transform:translateY(-3px)', 'transform:translateY(-3px) scale(1.01)')

# 4. Enhance noise visibility very slightly
css = css.replace("opacity='0.03'", "opacity='0.045'")

# Replace CSS back into html
new_html = html.replace(match.group(1), css)
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("UX Improvements applied!")

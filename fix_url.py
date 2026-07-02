with open('/Users/ikhaisoshuare/Cascade/presentation.html', 'r') as f:
    html = f.read()

replacement = """           <div style="border-top: 1px solid var(--border); padding-top: 3rem; display: flex; justify-content: center; align-items: center; gap: 4rem;">
              <div style="font-family: 'Inter', sans-serif; font-size: 1.6rem; color: var(--accent); font-weight: 600; letter-spacing: 0.1em;">
                 sylon.vercel.app
              </div>
           </div>"""

import re
pattern = re.compile(r'<div style="border-top: 1px solid var\(--border\); padding-top: 3rem; display: flex; justify-content: center; align-items: center; gap: 4rem;">.*?</div>\s*</div>\s*</div>', re.DOTALL)
html = pattern.sub(replacement + '\n           \n        </div>', html)

with open('/Users/ikhaisoshuare/Cascade/presentation.html', 'w') as f:
    f.write(html)

print("URL fixed.")

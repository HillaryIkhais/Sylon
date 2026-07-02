import re

with open('/Users/ikhaisoshuare/Cascade/presentation.html', 'r') as f:
    html = f.read()

# Replace fonts in the <head>
html = html.replace(
    '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">',
    '<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;1,400&family=Outfit:wght@300;400;500;600&display=swap" rel="stylesheet">'
)

# New CSS block
new_css = """    :root {
      /* CANVA STYLE: MIDNIGHT & WARM GOLD */
      --bg-gradient: radial-gradient(circle at 80% 20%, #0a1118 0%, #05080c 100%);
      --bg-solid: #05080c;
      
      --text: #FDFBF7;
      --text-muted: #8b9bb4;
      
      --accent: #D4AF37;       /* Warm Gold */
      --accent-alt: #E27D60;   /* Terracotta */
      
      --card-bg: #0F1722;
      --card-border: rgba(253, 251, 247, 0.08);
      --card-highlight: rgba(212, 175, 55, 0.3);
      
      --shadow-soft: 0 30px 60px rgba(0, 0, 0, 0.5);
      --ease: cubic-bezier(0.22, 1, 0.36, 1);
    }
    
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    
    body {
      width: 100vw;
      height: 100vh;
      overflow: hidden;
      background: var(--bg-solid);
      background-image: var(--bg-gradient);
      color: var(--text);
      font-family: 'Outfit', sans-serif;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    /* Subtle Canva-style abstract vector background (static, elegant) */
    body::before {
      content: "";
      position: fixed;
      top: -30vh;
      right: -10vw;
      width: 80vw;
      height: 80vw;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(212, 175, 55, 0.03) 0%, transparent 60%);
      pointer-events: none;
      z-index: 0;
    }
    
    body::after {
      content: "";
      position: fixed;
      bottom: -40vh;
      left: -20vw;
      width: 90vw;
      height: 90vw;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(226, 125, 96, 0.02) 0%, transparent 60%);
      pointer-events: none;
      z-index: 0;
    }

    /* Grain overlay for premium editorial feel */
    .grain-overlay {
      position: fixed;
      inset: 0;
      z-index: 9999;
      pointer-events: none;
      opacity: 0.04;
      background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
    }

    #presentation {
      position: relative;
      width: 100%;
      height: 100%;
    }

    /* BASE SLIDE MECHANICS */
    .slide {
      position: absolute;
      inset: 0;
      display: flex;
      flex-direction: column;
      padding: 4rem 6rem;
      visibility: hidden;
      z-index: 1;
    }
    .slide.active {
      visibility: visible;
      z-index: 10;
    }

    /* IN-PAGE ANIMATION CHOREOGRAPHY */
    .slide > div, .slide > header, .slide > main {
      opacity: 0;
      transform: translateY(40px) scale(0.98);
      filter: blur(8px);
      transition: opacity 1000ms var(--ease), transform 1200ms var(--ease), filter 1000ms var(--ease);
    }
    
    .slide.active > div:nth-child(1), .slide.active > header:nth-child(1), .slide.active > main:nth-child(1) { opacity: 1; transform: translateY(0) scale(1); filter: blur(0); transition-delay: 150ms; }
    .slide.active > div:nth-child(2), .slide.active > header:nth-child(2), .slide.active > main:nth-child(2) { opacity: 1; transform: translateY(0) scale(1); filter: blur(0); transition-delay: 350ms; }
    .slide.active > div:nth-child(3), .slide.active > header:nth-child(3), .slide.active > main:nth-child(3) { opacity: 1; transform: translateY(0) scale(1); filter: blur(0); transition-delay: 550ms; }

    .anim-seq > * {
      opacity: 0;
      transform: translateY(30px) scale(0.98);
      filter: blur(4px);
      transition: opacity 800ms var(--ease), transform 1000ms var(--ease), filter 800ms var(--ease);
    }
    .slide.active .anim-seq > *:nth-child(1) { opacity: 1; transform: translateY(0) scale(1); filter: blur(0); transition-delay: 450ms; }
    .slide.active .anim-seq > *:nth-child(2) { opacity: 1; transform: translateY(0) scale(1); filter: blur(0); transition-delay: 650ms; }
    .slide.active .anim-seq > *:nth-child(3) { opacity: 1; transform: translateY(0) scale(1); filter: blur(0); transition-delay: 850ms; }
    .slide.active .anim-seq > *:nth-child(4) { opacity: 1; transform: translateY(0) scale(1); filter: blur(0); transition-delay: 1050ms; }
    .slide.active .anim-seq > *:nth-child(5) { opacity: 1; transform: translateY(0) scale(1); filter: blur(0); transition-delay: 1250ms; }
    .slide.active .anim-seq > *:nth-child(6) { opacity: 1; transform: translateY(0) scale(1); filter: blur(0); transition-delay: 1450ms; }

    /* TYPOGRAPHY */
    .headline {
      font-family: 'Lora', serif;
      font-weight: 500;
      font-size: 4rem;
      line-height: 1.1;
      letter-spacing: -0.02em;
      color: var(--text);
    }
    .headline strong, .headline em {
      font-style: italic;
      color: var(--accent);
      font-weight: 500;
    }

    .subhead {
      font-family: 'Outfit', sans-serif;
      font-weight: 300;
      font-size: 1.5rem;
      color: var(--text-muted);
      margin-top: 2rem;
      max-width: 800px;
      line-height: 1.6;
    }

    .slide-kicker {
      font-family: 'Outfit', sans-serif;
      font-weight: 500;
      font-size: 0.85rem;
      text-transform: uppercase;
      letter-spacing: 0.25em;
      color: var(--accent);
      margin-bottom: 2.5rem;
      border-bottom: 1px solid var(--card-border);
      padding-bottom: 1rem;
      display: inline-block;
    }

    /* LAYOUTS */
    .layout-asymmetric {
      display: grid;
      grid-template-columns: 1.1fr 0.9fr;
      gap: 6rem;
      align-items: center;
      height: 100%;
    }
    
    .layout-center {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      height: 100%;
    }

    /* CARDS & CHAT BUBBLES */
    .chat-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      padding: 2.5rem;
      border-radius: 4px; /* Sharper corners for editorial look */
      margin-bottom: 2rem;
      box-shadow: var(--shadow-soft);
    }

    .chat-text {
      font-family: 'Lora', serif;
      font-size: 1.6rem;
      color: var(--text);
      line-height: 1.5;
    }
    
    .chat-response {
      color: var(--accent);
      font-style: italic;
    }

    /* BOARD GRID */
    .board-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 3rem;
      margin-top: 3rem;
      width: 100%;
    }
    
    .agent-card {
      padding: 3rem 2.5rem;
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 4px;
    }
    
    .agent-name {
      font-family: 'Outfit', sans-serif;
      font-size: 0.85rem;
      text-transform: uppercase;
      letter-spacing: 0.15em;
      font-weight: 600;
      margin-bottom: 1.5rem;
      color: var(--accent);
    }
    
    .agent-insight {
      font-family: 'Lora', serif;
      font-size: 1.5rem;
      line-height: 1.5;
      color: var(--text);
    }

    /* SYLON LOGO WATERMARK */
    .sylon-watermark {
      position: fixed;
      bottom: 3rem;
      right: 4rem;
      font-family: 'Outfit', sans-serif;
      font-weight: 700;
      font-size: 1.5rem;
      text-transform: uppercase;
      letter-spacing: 0.4em;
      color: var(--text);
      opacity: 0.1;
      z-index: 50;
      pointer-events: none;
    }
"""

start_css = html.find('    :root {')
end_css = html.find('  </style>')
if start_css != -1 and end_css != -1:
    html = html[:start_css] + new_css + html[end_css:]

# Replace font-family inline usages across the document
html = html.replace("font-family: 'Playfair Display'", "font-family: 'Lora'")
html = html.replace("font-family: 'Inter'", "font-family: 'Outfit'")

# Replace old CSS variable references and RGBA that might still be in inline styles
html = html.replace("var(--border)", "var(--card-border)")
html = html.replace("var(--card-glass)", "var(--card-bg)")
html = html.replace("rgba(168, 85, 247, 0.05)", "rgba(212, 175, 55, 0.04)") # gold faint
html = html.replace("rgba(168, 85, 247, 0.1)", "rgba(226, 125, 96, 0.06)") # terracotta faint
html = html.replace("rgba(168, 85, 247, 0.3)", "rgba(212, 175, 55, 0.3)") # gold border
html = html.replace("rgba(168, 85, 247, 0.08)", "rgba(212, 175, 55, 0.08)") # gold faint
html = html.replace("rgba(255,255,255,0.05)", "var(--card-bg)")

# Remove old watermark if any
html = html.replace('\n  <div class="sylon-watermark">SYLON</div>\n', '')

# Insert the grain overlay right after body starts
if '<div class="grain-overlay"></div>' not in html:
    html = html.replace('<body>', '<body>\n  <div class="grain-overlay"></div>')

# Insert the logo watermark back
html = html.replace('</body>', '  <div class="sylon-watermark">SYLON</div>\n</body>')

with open('/Users/ikhaisoshuare/Cascade/presentation.html', 'w') as f:
    f.write(html)

print("Canva Theme applied successfully.")

import re

new_slides = """<!-- SLIDE 7: The Opportunity -->
    <section class="slide">
      <header>
         <div class="slide-kicker">The Opportunity</div>
      </header>
      <main class="layout-center" style="padding-top: 2rem;">
        <h2 class="headline" style="font-size: 3.5rem; margin-bottom: 4rem; max-width: 1200px;">Nigeria has millions of businesses generating customer interactions every day. Almost none of it becomes structured knowledge.</h2>
        
        <div class="board-grid anim-seq" style="gap: 2rem; width: 100%;">
          <div class="agent-card" style="text-align: left; padding: 3rem 2.5rem; display: flex; flex-direction: column; justify-content: space-between; border-top: 4px solid var(--accent);">
            <div style="font-family: 'Playfair Display', serif; font-size: 4rem; color: var(--text); margin-bottom: 1rem;">14M+</div>
            <div style="font-family: 'Inter', sans-serif; font-size: 1.2rem; color: var(--text-muted); line-height: 1.5;">Nigerian SMEs use Meta platforms (WhatsApp, IG, FB) to operate and grow their businesses.</div>
          </div>
          
          <div class="agent-card" style="text-align: left; padding: 3rem 2.5rem; display: flex; flex-direction: column; justify-content: space-between; border-top: 4px solid var(--accent-alt);">
            <div style="font-family: 'Playfair Display', serif; font-size: 4rem; color: var(--text); margin-bottom: 1rem;">81%</div>
            <div style="font-family: 'Inter', sans-serif; font-size: 1.2rem; color: var(--text-muted); line-height: 1.5;">Report that Meta platforms helped them expand, yet all historical context is lost in endless chat logs.</div>
          </div>
          
          <div class="agent-card" style="text-align: left; padding: 3rem 2.5rem; display: flex; flex-direction: column; justify-content: space-between; border-top: 4px solid var(--border-highlight); background: rgba(168, 85, 247, 0.05);">
            <div style="font-family: 'Playfair Display', serif; font-size: 4rem; color: var(--accent); margin-bottom: 1rem;">0%</div>
            <div style="font-family: 'Inter', sans-serif; font-size: 1.2rem; color: var(--text); line-height: 1.5; font-weight: 500;">Of these interactions are currently being used to predict demand or map customer psychology.</div>
          </div>
        </div>
      </main>
    </section>

    <!-- SLIDE 8: Business Model -->
    <section class="slide">
      <header>
         <div class="slide-kicker">Building a Sustainable Business</div>
      </header>
      <main class="layout-center" style="padding-top: 2rem;">
        
        <div class="anim-seq" style="width: 100%; display: flex; flex-direction: column; gap: 1.5rem; max-width: 1200px; margin-top: 2rem;">
           
           <div style="display: flex; align-items: center; background: var(--card-glass); border: 1px solid var(--border); border-radius: 16px; padding: 2rem 3rem; backdrop-filter: blur(12px);">
              <div style="flex: 0 0 200px; font-family: 'Playfair Display', serif; font-size: 2.5rem; color: var(--text);">Free / Pilot</div>
              <div style="flex: 1; padding-left: 3rem; border-left: 1px solid var(--border); margin-left: 2rem;">
                 <div style="font-family: 'Inter', sans-serif; font-size: 1.2rem; font-weight: 600; color: var(--text); margin-bottom: 0.5rem;">Manual Review Ingestion</div>
                 <div style="font-family: 'Inter', sans-serif; font-size: 1rem; color: var(--text-muted);">Businesses paste text or upload CSVs to experience immediate persona excavation and simulation value.</div>
              </div>
           </div>

           <div style="display: flex; align-items: center; background: var(--card-glass); border: 1px solid var(--border); border-radius: 16px; padding: 2rem 3rem; backdrop-filter: blur(12px);">
              <div style="flex: 0 0 200px; font-family: 'Playfair Display', serif; font-size: 2.5rem; color: var(--accent-alt);">Subscription</div>
              <div style="flex: 1; padding-left: 3rem; border-left: 1px solid var(--border); margin-left: 2rem;">
                 <div style="font-family: 'Inter', sans-serif; font-size: 1.2rem; font-weight: 600; color: var(--text); margin-bottom: 0.5rem;">Automated Intelligence (SaaS)</div>
                 <div style="font-family: 'Inter', sans-serif; font-size: 1rem; color: var(--text-muted);">Continuous syncing with WhatsApp Business, Instagram, and Facebook for real-time customer health scores.</div>
              </div>
           </div>

           <div style="display: flex; align-items: center; background: rgba(168, 85, 247, 0.08); border: 1px solid var(--border-highlight); border-radius: 16px; padding: 2rem 3rem; backdrop-filter: blur(12px);">
              <div style="flex: 0 0 200px; font-family: 'Playfair Display', serif; font-size: 2.5rem; color: var(--accent);">Enterprise</div>
              <div style="flex: 1; padding-left: 3rem; border-left: 1px solid var(--border-highlight); margin-left: 2rem;">
                 <div style="font-family: 'Inter', sans-serif; font-size: 1.2rem; font-weight: 600; color: var(--text); margin-bottom: 0.5rem;">Custom Integrations & Platform API</div>
                 <div style="font-family: 'Inter', sans-serif; font-size: 1rem; color: var(--text-muted);">Direct integrations into legacy POS systems and inventory management tools for large-scale operations.</div>
              </div>
           </div>

        </div>
      </main>
    </section>

    <!-- SLIDE 9: Traction -->
    <section class="slide">
      <header>
         <div class="slide-kicker">Progress So Far</div>
      </header>
      <main class="layout-center" style="padding-top: 2rem;">
        <div class="anim-seq" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; width: 100%; max-width: 1200px;">
           
           <div style="background: var(--card-glass); border: 1px solid var(--border); padding: 3rem 2rem; border-radius: 16px; text-align: left;">
              <div style="color: var(--accent); font-size: 2rem; margin-bottom: 1rem;">⚡️</div>
              <div style="font-family: 'Inter', sans-serif; font-weight: 600; font-size: 1.3rem; color: var(--text); margin-bottom: 0.5rem;">Live Web Platform</div>
              <div style="font-family: 'Inter', sans-serif; font-size: 1rem; color: var(--text-muted);">Fully functional frontend deployed on Vercel with real-time API connectivity.</div>
           </div>
           
           <div style="background: var(--card-glass); border: 1px solid var(--border); padding: 3rem 2rem; border-radius: 16px; text-align: left;">
              <div style="color: var(--accent); font-size: 2rem; margin-bottom: 1rem;">🧠</div>
              <div style="font-family: 'Inter', sans-serif; font-weight: 600; font-size: 1.3rem; color: var(--text); margin-bottom: 0.5rem;">Multi-Agent Engine</div>
              <div style="font-family: 'Inter', sans-serif; font-size: 1rem; color: var(--text-muted);">Complex backend routing capable of handling CX, Ops, and Strategy debates.</div>
           </div>
           
           <div style="background: var(--card-glass); border: 1px solid var(--border); padding: 3rem 2rem; border-radius: 16px; text-align: left;">
              <div style="color: var(--accent); font-size: 2rem; margin-bottom: 1rem;">🚀</div>
              <div style="font-family: 'Inter', sans-serif; font-weight: 600; font-size: 1.3rem; color: var(--text); margin-bottom: 0.5rem;">Powered by Qwen</div>
              <div style="font-family: 'Inter', sans-serif; font-size: 1rem; color: var(--text-muted);">Leveraging Cerebras Qwen 235B for lightning-fast inference and deep reasoning.</div>
           </div>
           
           <div style="background: var(--card-glass); border: 1px solid var(--border); padding: 3rem 2rem; border-radius: 16px; text-align: left; grid-column: span 2;">
              <div style="color: var(--accent); font-size: 2rem; margin-bottom: 1rem;">🎯</div>
              <div style="font-family: 'Inter', sans-serif; font-weight: 600; font-size: 1.3rem; color: var(--text); margin-bottom: 0.5rem;">Pitch Ready</div>
              <div style="font-family: 'Inter', sans-serif; font-size: 1rem; color: var(--text-muted);">Successfully mapped Sylon's core value proposition to actual business owner pain points. Ready to demo live.</div>
           </div>
           
           <div style="background: rgba(168, 85, 247, 0.1); border: 1px solid var(--border-highlight); padding: 3rem 2rem; border-radius: 16px; text-align: left;">
              <div style="color: var(--accent); font-size: 2rem; margin-bottom: 1rem;">🗺</div>
              <div style="font-family: 'Inter', sans-serif; font-weight: 600; font-size: 1.3rem; color: var(--text); margin-bottom: 0.5rem;">Roadmap Locked</div>
              <div style="font-family: 'Inter', sans-serif; font-size: 1rem; color: var(--text-muted);">Clear 3-phase path to autonomous CRM and enterprise integration.</div>
           </div>

        </div>
      </main>
    </section>

    <!-- SLIDE 10: Roadmap -->
    <section class="slide">
      <header>
         <div class="slide-kicker">Technical & Business Roadmap</div>
      </header>
      <main class="layout-center" style="padding-top: 2rem;">
        
        <div class="anim-seq" style="width: 100%; display: flex; flex-direction: column; gap: 2rem; max-width: 1300px; margin-top: 1rem;">
           
           <div style="display: flex; gap: 3rem; background: var(--card-glass); border: 1px solid var(--border); border-radius: 16px; padding: 2.5rem; backdrop-filter: blur(12px);">
              <div style="flex: 0 0 250px; border-right: 1px solid var(--border); padding-right: 2rem; text-align: left;">
                 <div style="font-family: 'Playfair Display', serif; font-size: 2.5rem; color: var(--text);">Phase 1</div>
                 <div style="font-family: 'Inter', sans-serif; font-size: 1rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--accent); margin-top: 0.5rem;">Foundation</div>
              </div>
              <div style="flex: 1; text-align: left; display: flex; flex-direction: column; justify-content: center;">
                 <ul style="font-family: 'Inter', sans-serif; font-size: 1.2rem; color: var(--text-muted); line-height: 1.8; list-style-type: none;">
                    <li><span style="color: var(--accent);">✦</span> Deploy multi-agent reasoning engine</li>
                    <li><span style="color: var(--accent);">✦</span> Manual review & feedback ingestion pipeline</li>
                    <li><span style="color: var(--accent);">✦</span> Dashboard analytics & automatic persona excavation</li>
                 </ul>
              </div>
           </div>

           <div style="display: flex; gap: 3rem; background: var(--card-glass); border: 1px solid var(--border); border-radius: 16px; padding: 2.5rem; backdrop-filter: blur(12px);">
              <div style="flex: 0 0 250px; border-right: 1px solid var(--border); padding-right: 2rem; text-align: left;">
                 <div style="font-family: 'Playfair Display', serif; font-size: 2.5rem; color: var(--text);">Phase 2</div>
                 <div style="font-family: 'Inter', sans-serif; font-size: 1rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--text-muted); margin-top: 0.5rem;">Omni-Channel</div>
              </div>
              <div style="flex: 1; text-align: left; display: flex; flex-direction: column; justify-content: center;">
                 <ul style="font-family: 'Inter', sans-serif; font-size: 1.2rem; color: var(--text-muted); line-height: 1.8; list-style-type: none;">
                    <li><span style="color: var(--text-muted);">✦</span> Direct WhatsApp Business API integration</li>
                    <li><span style="color: var(--text-muted);">✦</span> Instagram & Facebook comment scraping & analysis</li>
                    <li><span style="color: var(--text-muted);">✦</span> Automated sentiment triggers & real-time risk alerts</li>
                 </ul>
              </div>
           </div>

           <div style="display: flex; gap: 3rem; background: var(--card-glass); border: 1px solid var(--border); border-radius: 16px; padding: 2.5rem; backdrop-filter: blur(12px);">
              <div style="flex: 0 0 250px; border-right: 1px solid var(--border); padding-right: 2rem; text-align: left;">
                 <div style="font-family: 'Playfair Display', serif; font-size: 2.5rem; color: var(--text);">Phase 3</div>
                 <div style="font-family: 'Inter', sans-serif; font-size: 1rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--text-muted); margin-top: 0.5rem;">Autonomous CRM</div>
              </div>
              <div style="flex: 1; text-align: left; display: flex; flex-direction: column; justify-content: center;">
                 <ul style="font-family: 'Inter', sans-serif; font-size: 1.2rem; color: var(--text-muted); line-height: 1.8; list-style-type: none;">
                    <li><span style="color: var(--text-muted);">✦</span> Sylon autonomously drafting review responses</li>
                    <li><span style="color: var(--text-muted);">✦</span> Direct inventory management integrations (Shopify, Square)</li>
                    <li><span style="color: var(--text-muted);">✦</span> Predictive trend forecasting and automated strategic advice</li>
                 </ul>
              </div>
           </div>

        </div>
      </main>
    </section>

    <!-- SLIDE 11: Join Us -->
    <section class="slide">
      <main class="layout-center" style="padding-top: 0rem;">
        
        <div class="anim-seq" style="width: 100%; max-width: 1300px;">
           <h1 class="headline" style="font-size: 5rem; margin-bottom: 1rem; color: var(--text);">Sylon.</h1>
           <h2 style="font-family: 'Inter', sans-serif; font-size: 1.8rem; font-weight: 300; color: var(--accent); margin-bottom: 4rem;">The Operating System for Business Intelligence.</h2>
           
           <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; margin-bottom: 4rem;">
              
              <div style="background: rgba(168, 85, 247, 0.05); border: 1px solid var(--border-highlight); padding: 3rem 2rem; border-radius: 16px;">
                 <div style="font-family: 'Playfair Display', serif; font-size: 2.5rem; color: var(--text); margin-bottom: 1rem;">Beta Partners</div>
                 <div style="font-family: 'Inter', sans-serif; font-size: 1.1rem; color: var(--text-muted); line-height: 1.5;">Seeking 10 businesses to pilot Sylon and shape the core reasoning engine.</div>
              </div>
              
              <div style="background: rgba(168, 85, 247, 0.05); border: 1px solid var(--border-highlight); padding: 3rem 2rem; border-radius: 16px;">
                 <div style="font-family: 'Playfair Display', serif; font-size: 2.5rem; color: var(--text); margin-bottom: 1rem;">Integrators</div>
                 <div style="font-family: 'Inter', sans-serif; font-size: 1.1rem; color: var(--text-muted); line-height: 1.5;">Looking for technical partners to help expand our Meta ecosystem pipelines.</div>
              </div>
              
              <div style="background: rgba(168, 85, 247, 0.05); border: 1px solid var(--border-highlight); padding: 3rem 2rem; border-radius: 16px;">
                 <div style="font-family: 'Playfair Display', serif; font-size: 2.5rem; color: var(--text); margin-bottom: 1rem;">Seed Resources</div>
                 <div style="font-family: 'Inter', sans-serif; font-size: 1.1rem; color: var(--text-muted); line-height: 1.5;">Seeking early-stage capital and compute resources to scale our Qwen infrastructure.</div>
              </div>

           </div>
           
           <div style="border-top: 1px solid var(--border); padding-top: 3rem; display: flex; justify-content: center; align-items: center; gap: 4rem;">
              <div style="font-family: 'Inter', sans-serif; font-size: 1.4rem; color: var(--text); font-weight: 600;">
                 trysylon.com
              </div>
              <div style="width: 1px; height: 30px; background: var(--border);"></div>
              <div style="font-family: 'Inter', sans-serif; font-size: 1.4rem; color: var(--text); font-weight: 600;">
                 founder@trysylon.com
              </div>
           </div>
           
        </div>

      </main>
    </section>
  </div>"""

with open('/Users/ikhaisoshuare/Cascade/presentation.html', 'r') as f:
    html = f.read()

# Replace Slides 7 to 11
import re
slides_pattern = re.compile(r'<!-- SLIDE 7: The Opportunity -->.*?</section>\n  </div>', re.DOTALL)
html = slides_pattern.sub(new_slides, html)

with open('/Users/ikhaisoshuare/Cascade/presentation.html', 'w') as f:
    f.write(html)

print("Slides 7-11 completely overhauled to Canva-style layouts.")

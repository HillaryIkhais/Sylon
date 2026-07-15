import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Morlen - Pitch Deck</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Geist', 'sans-serif'],
                    },
                    colors: {
                        obsidian: '#0B0C10',
                        slate: '#15181E',
                        steel: '#64748B',
                        platinum: '#E2E8F0'
                    }
                }
            }
        }
    </script>

    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            background-color: #0B0C10;
            color: #E2E8F0;
            font-family: 'Geist', sans-serif;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            width: 100vw;
            height: 100vh;
        }

        #presentation-container {
            width: 1920px;
            height: 1080px;
            position: relative;
            background-image: radial-gradient(circle at 50% 0%, #15181E 0%, #0B0C10 70%);
            overflow: hidden;
        }

        /* Ambient light */
        .ambient-light {
            position: absolute;
            width: 1200px; height: 800px;
            background: radial-gradient(ellipse, rgba(255,255,255,0.04) 0%, transparent 60%);
            top: -200px; left: 50%;
            transform: translateX(-50%);
            border-radius: 50%;
            pointer-events: none;
            z-index: 0;
        }

        /* Architectural structural framing */
        .frame-line-v {
            position: absolute; top: 0; bottom: 0; width: 1px;
            background: linear-gradient(180deg, transparent, rgba(255,255,255,0.06), transparent);
            z-index: 0;
        }
        .frame-line-h {
            position: absolute; left: 0; right: 0; height: 1px;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.06), transparent);
            z-index: 0;
        }

        /* Glass Cards (Used SPARINGLY for distinct UI blocks, not body text) */
        .glass-card {
            background: rgba(21, 24, 30, 0.4);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-top: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 16px;
            box-shadow: 0 30px 60px rgba(0,0,0,0.4);
            backdrop-filter: blur(40px);
            -webkit-backdrop-filter: blur(40px);
            position: relative;
            overflow: hidden;
        }
        
        .slide {
            position: absolute; top: 0; left: 0;
            width: 100%; height: 100%;
            padding: 120px 160px;
            opacity: 0;
            visibility: hidden;
            z-index: 10;
        }

        .slide.active {
            opacity: 1; visibility: visible;
        }
        
        .overline-text {
            font-size: 13px; letter-spacing: 0.25em; text-transform: uppercase;
            color: #64748B; font-weight: 600;
        }
    </style>
</head>
<body>

    <div id="presentation-container">
        <!-- Structural Background Elements -->
        <div class="ambient-light"></div>
        <div class="frame-line-v" style="left: 160px;"></div>
        <div class="frame-line-v" style="right: 160px;"></div>
        <div class="frame-line-h" style="top: 120px;"></div>
        <div class="frame-line-h" style="bottom: 120px;"></div>

        <!-- SLIDE 1 -->
        <div class="slide" id="slide1">
            <div class="w-full h-full flex flex-col justify-between">
                <div></div>
                <div class="max-w-4xl stagger-element opacity-0 transform translate-y-8">
                    <p class="overline-text mb-8">SLIDE 1 — MORLEN</p>
                    <h1 class="text-[100px] font-bold tracking-tight text-white leading-none mb-6">Morlen</h1>
                    <p class="text-4xl text-platinum font-medium mb-6">The Operating System for Business Decisions.</p>
                    <p class="text-2xl text-steel">Turning customer conversations into executive decisions.</p>
                </div>
                <div class="stagger-element opacity-0 flex justify-between items-end border-t border-white/10 pt-8">
                    <div>
                        <p class="overline-text mb-2 text-steel/60">Bottom:</p>
                        <p class="text-steel uppercase tracking-widest text-sm mb-1">Founder Name</p>
                        <p class="text-xl text-platinum">Hillary Ikhais</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 2 -->
        <div class="slide" id="slide2">
            <div class="w-full h-full flex flex-col justify-center">
                <p class="overline-text mb-12 stagger-element opacity-0">The Problem</p>
                <div class="flex gap-24">
                    <div class="flex-1">
                        <h2 class="text-5xl font-medium text-white mb-6 leading-tight stagger-element opacity-0">Businesses have automated transactions.</h2>
                        <p class="text-xl text-steel leading-relaxed mb-10 stagger-element opacity-0">Over the last two decades, businesses have adopted software for almost every operational function</p>
                        
                        <div class="stagger-element opacity-0 pl-6 border-l-2 border-white/20">
                            <ul class="text-3xl text-platinum space-y-4 font-medium">
                                <li class="text-steel">Payments.</li>
                                <li class="text-steel">Inventory.</li>
                                <li class="text-steel">Accounting.</li>
                                <li class="text-steel">CRM.</li>
                                <li class="text-steel">Marketing.</li>
                                <li class="text-white mt-4">Conversations</li>
                            </ul>
                        </div>
                    </div>
                    <div class="flex-1 pt-4">
                        <p class="text-2xl text-white mb-8 stagger-element opacity-0">Yet business owners still ask the same questions:</p>
                        <ul class="text-2xl text-steel space-y-6 mb-16 stagger-element opacity-0">
                            <li>What deserves attention today?</li>
                            <li>Which products should I restock?</li>
                            <li>Which customers need follow-up?</li>
                            <li>Where am I losing revenue?</li>
                            <li>Why have sales reduced?</li>
                        </ul>
                        <div class="stagger-element opacity-0 border-t border-white/10 pt-8">
                            <p class="text-2xl text-white mb-2">Business software automates operations.</p>
                            <p class="text-2xl text-steel">It records what happened</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 3 -->
        <div class="slide" id="slide3">
            <div class="w-full h-full flex flex-col justify-center max-w-5xl">
                <p class="overline-text mb-8 stagger-element opacity-0">SLIDE 2 — THE SHIFT</p>
                <h2 class="text-[72px] leading-tight font-medium text-white mb-12 stagger-element opacity-0 max-w-4xl">Commerce has moved into conversations</h2>
                
                <div class="space-y-8 text-2xl text-steel leading-relaxed stagger-element opacity-0">
                    <p>Across Nigeria, businesses now operate inside messaging platforms.<br>
                    Customers now discover products, negotiate prices, confirm payments and arrange deliveries inside WhatsApp, Instagram and Facebook.</p>
                    
                    <p class="text-white font-medium pl-6 border-l-2 border-white/30">For Nigerian MSMEs, the entire sales funnel now exists inside conversations.</p>
                    
                    <p>Yet traditional software was designed for structured forms, not unstructured conversations.</p>
                    
                    <p>As conversational commerce grows, businesses generate thousands of customer signals every day</p>
                    
                    <p class="text-white pt-6 border-t border-white/10">Most disappear without ever becoming business intelligence.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 4 -->
        <div class="slide" id="slide4">
            <div class="w-full h-full flex flex-col justify-center max-w-6xl">
                <p class="overline-text mb-8 stagger-element opacity-0">SLIDE 3 — THE PROBLEM</p>
                <h2 class="text-6xl font-medium text-white mb-8 stagger-element opacity-0">Every conversation creates decisions.</h2>
                <p class="text-2xl text-steel mb-12 stagger-element opacity-0">A business owner doesn't just receive messages.<br>They constantly decide:</p>
                
                <ul class="text-3xl text-platinum space-y-6 mb-16 stagger-element opacity-0 pl-6 border-l border-white/20">
                    <li>• Should this customer receive follow-up?</li>
                    <li>• Is demand increasing for this product?</li>
                    <li>• Should inventory be reordered?</li>
                    <li>• Are customers becoming more price-sensitive?</li>
                    <li>• Which complaints appear repeatedly?</li>
                    <li>• Which customers are likely to return?</li>
                </ul>
                
                <div class="stagger-element opacity-0">
                    <p class="text-2xl text-steel mb-2">These decisions are still made manually.</p>
                    <p class="text-2xl text-white">As conversations increase,<br>Decision complexity grows even faster.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 5 -->
        <div class="slide" id="slide5">
            <div class="w-full h-full flex flex-col justify-center">
                <p class="overline-text mb-6 stagger-element opacity-0">SLIDE 4 — MORLEN</p>
                <h2 class="text-5xl font-medium text-white mb-6 stagger-element opacity-0">Morlen is an Executive Decision Intelligence Platform.</h2>
                <p class="text-xl text-steel mb-8 max-w-4xl stagger-element opacity-0">Morlen continuously analyzes customer conversations, identifies business patterns and delivers prioritized business decisions.</p>
                <p class="text-xl text-steel mb-12 max-w-4xl stagger-element opacity-0">Instead of presenting plain dashboards,<br>Morlen produces a daily executive briefing.</p>
                
                <div class="grid grid-cols-2 gap-12 mb-12">
                    <div class="stagger-element opacity-0 flex flex-col pl-6 border-l-2 border-white/10">
                        <h3 class="text-2xl font-medium text-white mb-3">Executive Brief</h3>
                        <p class="text-lg text-steel mb-2">A daily summary of the highest priority decisions.</p>
                        <p class="text-lg text-steel">inventory risks, customer churn, demand spikes, operational issues.</p>
                    </div>
                    <div class="stagger-element opacity-0 flex flex-col pl-6 border-l-2 border-white/10">
                        <h3 class="text-2xl font-medium text-white mb-3">Opportunity Feed</h3>
                        <p class="text-lg text-steel">Revenue opportunities detected from conversations including estimated impact, confidence score, supporting evidence.</p>
                    </div>
                    <div class="stagger-element opacity-0 flex flex-col pl-6 border-l-2 border-white/10">
                        <h3 class="text-2xl font-medium text-white mb-3">Business Memory</h3>
                        <p class="text-lg text-steel">Long-term behavioural intelligence about customers.</p>
                        <p class="text-base text-steel mt-2 opacity-80">for example customers increasingly ask for same day delivery, demand for product A rises every month end, customers compare prices before purchasing, repeat customers typically reorder after 21 days.</p>
                    </div>
                    <div class="stagger-element opacity-0 flex flex-col pl-6 border-l-2 border-white/10">
                        <h3 class="text-2xl font-medium text-white mb-3">Evidence-Based Recommendations</h3>
                        <p class="text-lg text-steel mb-3">Every recommendation explains</p>
                        <ul class="text-lg text-steel space-y-1 ml-4">
                            <li>• Why it exists</li>
                            <li>• Expected impact</li>
                            <li>• Supporting evidence</li>
                        </ul>
                    </div>
                </div>
                
                <div class="stagger-element opacity-0 pt-6 border-t border-white/10">
                    <p class="text-xl text-steel mb-1">Business owners stop searching for answers.</p>
                    <p class="text-xl text-white">Morlen brings the answers to them.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 6 -->
        <div class="slide" id="slide6">
            <div class="w-full h-full flex flex-col justify-center items-center text-center">
                <p class="overline-text mb-8 stagger-element opacity-0">SLIDE 5 — MARKET + BUSINESS MODEL</p>
                <h2 class="text-5xl font-medium text-white mb-12 stagger-element opacity-0">A Massive Market</h2>
                <p class="text-2xl text-steel mb-6 stagger-element opacity-0">Nigeria has approximately:</p>
                
                <div class="mb-12 stagger-element opacity-0">
                    <p class="text-[120px] font-bold text-white leading-none">39.6 Million MSMEs</p>
                </div>
                
                <p class="text-2xl text-steel mb-6 stagger-element opacity-0">Representing:</p>
                <div class="flex gap-16 justify-center mb-16 stagger-element opacity-0 text-3xl text-white">
                    <p>• 96% of businesses</p>
                    <p>• 87.9% of employment</p>
                    <p>• 46.3% of GDP</p>
                </div>
                
                <div class="stagger-element opacity-0 pt-8 border-t border-white/10">
                    <p class="text-2xl text-steel mb-2">Millions already conduct business primarily through messaging platforms.</p>
                    <p class="text-2xl text-white">Morlen is built for this new operating environment.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 7: BUSINESS MODEL (Kept cards here because it's pricing) -->
        <div class="slide" id="slide7">
            <div class="w-full h-full flex flex-col justify-center">
                <p class="overline-text mb-6 stagger-element opacity-0">Business Model</p>
                <h2 class="text-5xl font-medium text-white mb-6 stagger-element opacity-0">Subscription SaaS</h2>
                <p class="text-xl text-steel mb-12 max-w-4xl stagger-element opacity-0">Starting with a 30 day free trial giving Morlen enough time to learn from customer conversations, build business memory, generate meaningful insights</p>
                
                <div class="grid grid-cols-3 gap-8 mb-12">
                    <div class="glass-card p-10 stagger-element opacity-0 flex flex-col">
                        <h3 class="text-3xl font-medium text-white mb-2">Starter <span class="text-xl text-steel font-normal">[N8,000/month]</span></h3>
                        <p class="text-sm text-steel mb-6 min-h-[40px]">For early stage businesses</p>
                        <ul class="text-platinum space-y-4 flex-1 border-t border-white/10 pt-6">
                            <li>- Executive brief</li>
                            <li>- Business memory</li>
                            <li>- Basic decision intelligence</li>
                            <li>- Single workspace</li>
                        </ul>
                    </div>
                    
                    <div class="glass-card p-10 stagger-element opacity-0 flex flex-col relative">
                        <div class="absolute inset-0 border-2 border-white/20 rounded-2xl pointer-events-none"></div>
                        <h3 class="text-3xl font-medium text-white mb-2">Growth</h3>
                        <p class="text-sm text-steel mb-6 min-h-[40px]">Businesses managing increasing customer conversations.</p>
                        <ul class="text-platinum space-y-4 flex-1 border-t border-white/10 pt-6">
                            <li>- Everything in starter</li>
                            <li>- Opportunity feed</li>
                            <li>- Advanced AI recommendations</li>
                            <li>- Multi channel integrations</li>
                            <li>- Team Collaboration</li>
                        </ul>
                    </div>
                    
                    <div class="glass-card p-10 stagger-element opacity-0 flex flex-col">
                        <h3 class="text-3xl font-medium text-white mb-2">Enterprise</h3>
                        <p class="text-sm text-steel mb-6 min-h-[40px]">Organizations requiring company-wide decision intelligence and integrations.</p>
                        <ul class="text-platinum space-y-4 flex-1 border-t border-white/10 pt-6">
                            <li>- Everything in growth</li>
                            <li>- Custom AI deployment</li>
                            <li>- Dedicate Support</li>
                            <li>- Enterprise security and governance</li>
                        </ul>
                    </div>
                </div>
                
                <p class="text-lg text-steel stagger-element opacity-0">Additional revenue:<br><span class="text-white mt-1 block">• Enterprise Implementation & Onboarding</span></p>
            </div>
        </div>

        <!-- SLIDE 8 -->
        <div class="slide" id="slide8">
            <div class="w-full h-full flex flex-col justify-center max-w-5xl">
                <p class="overline-text mb-6 stagger-element opacity-0">SLIDE 6 — FUNDING</p>
                <h2 class="text-6xl font-medium text-white mb-6 stagger-element opacity-0">Raising Pre-Seed Capital</h2>
                <p class="text-2xl text-steel mb-16 stagger-element opacity-0">Investment will accelerate:</p>
                
                <div class="space-y-10 pl-8 border-l-2 border-white/10">
                    <div class="stagger-element opacity-0">
                        <h3 class="text-3xl font-medium text-white mb-2">40% — Product Development</h3>
                        <p class="text-xl text-steel">Complete commercial MVP and core intelligence engine.</p>
                    </div>
                    
                    <div class="stagger-element opacity-0">
                        <h3 class="text-3xl font-medium text-white mb-2">25% — AI Infrastructure</h3>
                        <p class="text-xl text-steel">Inference, data pipelines and production infrastructure.</p>
                    </div>
                    
                    <div class="stagger-element opacity-0">
                        <h3 class="text-3xl font-medium text-white mb-2">20% — Customer Acquisition</h3>
                        <p class="text-xl text-steel">Pilot programs and early customer onboarding.</p>
                    </div>
                    
                    <div class="stagger-element opacity-0">
                        <h3 class="text-3xl font-medium text-white mb-2">15% — Strategic Partnerships & Operations</h3>
                        <p class="text-xl text-steel">Messaging integrations and business development.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 9 -->
        <div class="slide" id="slide9">
            <div class="w-full h-full flex flex-col justify-center max-w-4xl">
                <p class="overline-text mb-12 stagger-element opacity-0">Expected Outcomes</p>
                
                <div class="space-y-12 text-5xl font-medium text-white stagger-element opacity-0 pl-8 border-l-[3px] border-white/20">
                    <p>Commercial MVP</p>
                    <p>First paying customers</p>
                    <p>Validated product-market fit</p>
                    <p>Foundation for national expansion</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 10 -->
        <div class="slide" id="slide10">
            <div class="w-full h-full flex flex-col justify-center">
                <p class="overline-text mb-12 stagger-element opacity-0">SLIDE 7 — WHY MORLEN?</p>
                
                <div class="flex gap-24">
                    <div class="flex-1 stagger-element opacity-0">
                        <p class="text-2xl text-steel mb-6">Business software has always answered one question:</p>
                        <h2 class="text-[64px] font-medium text-white leading-tight mb-12">"What happened?"</h2>
                        
                        <ul class="text-2xl text-steel space-y-6">
                            <li>CRM stores customer records</li>
                            <li>ERP manages operations</li>
                            <li>BI dashboards visualize historical metrics</li>
                            <li>Chatbots automate converstaions</li>
                        </ul>
                    </div>
                    
                    <div class="flex-1 stagger-element opacity-0 pt-4">
                        <p class="text-2xl text-steel mb-6">Morlen answers a different question:</p>
                        <h2 class="text-[64px] font-medium text-white leading-tight mb-12">"What should I do next?"</h2>
                        
                        <ul class="text-2xl text-white space-y-6 font-medium">
                            <li>Every conversation contains intelligence.</li>
                            <li>Every business generates opportunities.</li>
                            <li>Every owner has limited attention.</li>
                        </ul>
                        
                        <div class="mt-12 pt-8 border-t border-white/10">
                            <p class="text-3xl text-white leading-relaxed">Morlen exists to protect that attention—<br>by turning conversations into decisions.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 11 -->
        <div class="slide" id="slide11">
            <div class="w-full h-full flex flex-col justify-center items-center text-center">
                <p class="overline-text mb-16 stagger-element opacity-0">FINAL SLIDE</p>
                
                <h1 class="text-[160px] font-bold tracking-tighter text-white leading-none mb-16 stagger-element opacity-0">MORLEN</h1>
                
                <p class="text-5xl text-steel mb-6 stagger-element opacity-0">The future of business isn't more software.</p>
                <p class="text-6xl font-medium text-white mb-24 stagger-element opacity-0">It's better decisions.</p>
                
                <div class="stagger-element opacity-0 pt-12 border-t border-white/10 w-full max-w-2xl">
                    <p class="text-3xl text-steel mb-3">Businesses already have the conversations.</p>
                    <p class="text-4xl text-white font-medium">Morlen turns them into decisions.</p>
                </div>
            </div>
        </div>

    </div>

    <script>
        const slides = document.querySelectorAll('.slide');
        let currentSlide = 0;
        let isAnimating = false;

        function goToSlide(index) {
            if (isAnimating || index < 0 || index >= slides.length) return;
            isAnimating = true;

            const current = slides[currentSlide];
            const next = slides[index];
            
            if (current) {
                gsap.to(current, {
                    opacity: 0,
                    duration: 0.6,
                    ease: "power2.inOut",
                    onComplete: () => {
                        current.classList.remove('active');
                        current.style.visibility = 'hidden';
                    }
                });
            }

            next.classList.add('active');
            next.style.visibility = 'visible';
            
            // Setup next elements
            const elements = next.querySelectorAll('.stagger-element');
            gsap.set(elements, { opacity: 0, y: 40 });

            // Animate next elements
            gsap.to(elements, {
                opacity: 1,
                y: 0,
                duration: 1,
                stagger: 0.15,
                ease: "power3.out",
                delay: 0.2,
                onComplete: () => {
                    currentSlide = index;
                    isAnimating = false;
                }
            });
        }

        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight' || e.key === 'Space') goToSlide(currentSlide + 1);
            if (e.key === 'ArrowLeft') goToSlide(currentSlide - 1);
        });

        // Start first slide
        slides[0].classList.add('active');
        slides[0].style.visibility = 'visible';
        slides[0].style.opacity = 1;
        gsap.set(slides[0].querySelectorAll('.stagger-element'), { opacity: 0, y: 40 });
        gsap.to(slides[0].querySelectorAll('.stagger-element'), {
            opacity: 1, y: 0, duration: 1, stagger: 0.15, ease: "power3.out", delay: 0.2
        });
        
        // AUTO ADVANCE for the video recorder (Every 7.5 seconds)
        setInterval(() => {
            if (currentSlide < slides.length - 1) {
                goToSlide(currentSlide + 1);
            }
        }, 7500);
        
        window.goToSlide = goToSlide;
    </script>
</body>
</html>"""

with open('presentation.html', 'w') as f:
    f.write(html_content)

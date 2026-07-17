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
                        obsidian: '#050505',
                        slate: '#111111',
                        steel: '#888888',
                        platinum: '#FFFFFF'
                    }
                }
            }
        }
    </script>

    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            background-color: #050505;
            color: #FFFFFF;
            font-family: 'Geist', sans-serif;
            overflow: hidden;
            width: 100vw;
            height: 100vh;
        }

        #presentation-container {
            width: 1920px;
            height: 1080px;
            position: relative;
            background: #050505;
            overflow: hidden;
        }

        /* 1. CINEMATIC FILM GRAIN */
        .film-grain {
            position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
            opacity: 0.04;
            pointer-events: none;
            z-index: 100;
        }

        /* 2. DYNAMIC SLOW MOVING LIGHT BEAMS */
        .light-beam {
            position: absolute;
            width: 150vw; height: 300px;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.02), transparent);
            transform-origin: center;
            pointer-events: none;
            z-index: 1;
        }
        
        .beam-1 { top: 20%; left: -25%; transform: rotate(-15deg); animation: pulseBeam 12s infinite alternate ease-in-out; }
        .beam-2 { bottom: 20%; right: -25%; transform: rotate(-15deg); animation: pulseBeam 15s infinite alternate-reverse ease-in-out; }
        
        @keyframes pulseBeam {
            0% { opacity: 0.3; transform: rotate(-15deg) translateY(0); }
            100% { opacity: 0.8; transform: rotate(-15deg) translateY(100px); }
        }

        /* 3. KINETIC BACKGROUND TYPOGRAPHY */
        .kinetic-bg {
            position: absolute;
            top: 50%; left: 50%;
            transform: translate(-50%, -50%);
            font-size: 400px;
            font-weight: 700;
            color: rgba(255,255,255,0.015);
            white-space: nowrap;
            z-index: 0;
            pointer-events: none;
            user-select: none;
            letter-spacing: -10px;
        }

        /* 4. ARCHITECTURAL FRAMING */
        .frame-corner {
            position: absolute;
            width: 40px; height: 40px;
            border: 1px solid rgba(255,255,255,0.2);
            z-index: 50;
        }
        .fc-tl { top: 60px; left: 80px; border-right: none; border-bottom: none; }
        .fc-tr { top: 60px; right: 80px; border-left: none; border-bottom: none; }
        .fc-bl { bottom: 60px; left: 80px; border-right: none; border-top: none; }
        .fc-br { bottom: 60px; right: 80px; border-left: none; border-top: none; }

        .slide {
            position: absolute; top: 0; left: 0;
            width: 100%; height: 100%;
            padding: 120px 160px;
            opacity: 0;
            visibility: hidden;
            z-index: 10;
        }

        .slide.active { opacity: 1; visibility: visible; }
        
        .overline-text {
            font-size: 13px; letter-spacing: 0.3em; text-transform: uppercase;
            color: #888888; font-weight: 600;
        }

        /* Custom text mask for word-by-word reveal */
        .word-mask { display: inline-block; overflow: hidden; vertical-align: top; padding-bottom: 5px; }
        .word-inner { display: inline-block; transform: translateY(100%); }

        /* Pricing Card Design */
        .pricing-card {
            background: linear-gradient(180deg, rgba(20,20,20,0.8) 0%, rgba(10,10,10,0.9) 100%);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-top: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 4px;
            position: relative;
        }
        
        /* High-end gradient text */
        .text-gradient {
            background: linear-gradient(180deg, #FFFFFF 0%, #888888 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

    </style>
</head>
<body>

    <div id="presentation-container">
        <div class="film-grain"></div>
        <div class="light-beam beam-1"></div>
        <div class="light-beam beam-2"></div>
        
        <!-- Corners -->
        <div class="frame-corner fc-tl"></div>
        <div class="frame-corner fc-tr"></div>
        <div class="frame-corner fc-bl"></div>
        <div class="frame-corner fc-br"></div>
        
        <!-- Kinetic BG changes per slide via JS -->
        <div class="kinetic-bg" id="bg-text">MORLEN</div>

        <!-- SLIDE 1 -->
        <div class="slide" id="slide1" data-bg="MORLEN">
            <div class="w-full h-full flex flex-col justify-between">
                <div></div>
                <div class="max-w-4xl">
                    <p class="overline-text mb-8 stagger-fade">SLIDE 1 — MORLEN</p>
                    <h1 class="text-[120px] font-bold tracking-tighter text-gradient leading-none mb-6 split-text">Morlen</h1>
                    <p class="text-4xl text-platinum font-medium mb-6 split-text">The Operating System for Business Decisions.</p>
                    <p class="text-2xl text-steel stagger-fade">Turning customer conversations into executive decisions.</p>
                </div>
                <div class="stagger-fade flex justify-between items-end border-t border-white/10 pt-8 w-1/3">
                    <div>
                        <p class="overline-text mb-2 text-steel/40">Founder Name</p>
                        <p class="text-2xl text-platinum tracking-wide">Hillary Ikhais</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 2 -->
        <div class="slide" id="slide2" data-bg="PROBLEM">
            <div class="w-full h-full flex flex-col justify-center">
                <p class="overline-text mb-12 stagger-fade">The Problem</p>
                <div class="flex gap-24">
                    <div class="flex-1">
                        <h2 class="text-6xl font-medium text-white mb-8 leading-tight split-text">Businesses have automated transactions.</h2>
                        <p class="text-2xl text-steel leading-relaxed mb-12 stagger-fade">Over the last two decades, businesses have adopted software for almost every operational function</p>
                        
                        <div class="stagger-fade">
                            <ul class="text-3xl text-steel space-y-4 font-medium grid grid-cols-2">
                                <li>Payments.</li>
                                <li>CRM.</li>
                                <li>Inventory.</li>
                                <li>Marketing.</li>
                                <li>Accounting.</li>
                                <li class="text-white col-span-2 mt-4 pt-4 border-t border-white/10">Conversations</li>
                            </ul>
                        </div>
                    </div>
                    <div class="flex-1 pt-4 border-l border-white/10 pl-16">
                        <p class="text-3xl text-white mb-10 split-text">Yet business owners still ask the same questions:</p>
                        <ul class="text-2xl text-steel space-y-8 mb-16 stagger-fade list-disc pl-6">
                            <li>What deserves attention today?</li>
                            <li>Which products should I restock?</li>
                            <li>Which customers need follow-up?</li>
                            <li>Where am I losing revenue?</li>
                            <li>Why have sales reduced?</li>
                        </ul>
                        <div class="stagger-fade">
                            <p class="text-2xl text-white mb-2">Business software automates operations.</p>
                            <p class="text-2xl text-steel">It records what happened</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 3 -->
        <div class="slide" id="slide3" data-bg="SHIFT">
            <div class="w-full h-full flex flex-col justify-center max-w-5xl">
                <p class="overline-text mb-8 stagger-fade">SLIDE 2 — THE SHIFT</p>
                <h2 class="text-[80px] tracking-tight leading-none font-medium text-gradient mb-12 split-text">Commerce has moved into conversations</h2>
                
                <div class="space-y-10 text-3xl text-steel leading-relaxed stagger-fade">
                    <p>Across Nigeria, businesses now operate inside messaging platforms.<br>
                    <span class="text-2xl">Customers now discover products, negotiate prices, confirm payments and arrange deliveries inside WhatsApp, Instagram and Facebook.</span></p>
                    
                    <p class="text-white font-medium pl-8 border-l-4 border-white/30">For Nigerian MSMEs, the entire sales funnel now exists inside conversations.</p>
                    
                    <p class="text-2xl">Yet traditional software was designed for structured forms, not unstructured conversations.</p>
                    
                    <p class="text-2xl">As conversational commerce grows, businesses generate thousands of customer signals every day.</p>
                    
                    <p class="text-white text-3xl pt-8 border-t border-white/10">Most disappear without ever becoming business intelligence.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 4 -->
        <div class="slide" id="slide4" data-bg="DECISIONS">
            <div class="w-full h-full flex flex-col justify-center max-w-6xl">
                <p class="overline-text mb-8 stagger-fade">SLIDE 3 — THE PROBLEM</p>
                <h2 class="text-7xl font-medium text-white mb-10 split-text">Every conversation creates decisions.</h2>
                <p class="text-3xl text-steel mb-12 split-text">A business owner doesn't just receive messages.<br>They constantly decide:</p>
                
                <ul class="text-3xl text-platinum space-y-6 mb-16 stagger-fade grid grid-cols-2 gap-x-12">
                    <li class="border-b border-white/5 pb-4">• Should this customer receive follow-up?</li>
                    <li class="border-b border-white/5 pb-4">• Is demand increasing for this product?</li>
                    <li class="border-b border-white/5 pb-4">• Should inventory be reordered?</li>
                    <li class="border-b border-white/5 pb-4">• Are customers becoming more price-sensitive?</li>
                    <li class="border-b border-white/5 pb-4">• Which complaints appear repeatedly?</li>
                    <li class="border-b border-white/5 pb-4">• Which customers are likely to return?</li>
                </ul>
                
                <div class="stagger-fade pt-8">
                    <p class="text-3xl text-steel mb-3">These decisions are still made manually.</p>
                    <p class="text-4xl text-gradient">As conversations increase,<br>Decision complexity grows even faster.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 5 -->
        <div class="slide" id="slide5" data-bg="INTELLIGENCE">
            <div class="w-full h-full flex flex-col justify-center">
                <p class="overline-text mb-6 stagger-fade">SLIDE 4 — MORLEN</p>
                <h2 class="text-6xl font-medium text-white mb-6 split-text">Morlen is an Executive Decision Intelligence Platform.</h2>
                <p class="text-2xl text-steel mb-8 max-w-4xl stagger-fade">Morlen continuously analyzes customer conversations, identifies business patterns and delivers prioritized business decisions.</p>
                <p class="text-2xl text-steel mb-16 max-w-4xl stagger-fade">Instead of presenting plain dashboards,<br><span class="text-white">Morlen produces a daily executive briefing.</span></p>
                
                <div class="grid grid-cols-4 gap-12 mb-16">
                    <div class="stagger-fade flex flex-col">
                        <div class="w-8 h-1 bg-white mb-6"></div>
                        <h3 class="text-2xl font-medium text-white mb-4">Executive Brief</h3>
                        <p class="text-lg text-steel">A daily summary of the highest priority decisions. inventory risks, customer churn, demand spikes, operational issues.</p>
                    </div>
                    <div class="stagger-fade flex flex-col">
                        <div class="w-8 h-1 bg-white/40 mb-6"></div>
                        <h3 class="text-2xl font-medium text-white mb-4">Opportunity Feed</h3>
                        <p class="text-lg text-steel">Revenue opportunities detected from conversations including estimated impact, confidence score, supporting evidence.</p>
                    </div>
                    <div class="stagger-fade flex flex-col">
                        <div class="w-8 h-1 bg-white/40 mb-6"></div>
                        <h3 class="text-2xl font-medium text-white mb-4">Business Memory</h3>
                        <p class="text-lg text-steel mb-3">Long-term behavioural intelligence about customers.</p>
                        <p class="text-sm text-steel/60">for example customers increasingly ask for same day delivery, demand for product A rises every month end, customers compare prices before purchasing...</p>
                    </div>
                    <div class="stagger-fade flex flex-col">
                        <div class="w-8 h-1 bg-white/40 mb-6"></div>
                        <h3 class="text-2xl font-medium text-white mb-4">Evidence-Based Recommendations</h3>
                        <p class="text-lg text-steel mb-3">Every recommendation explains:</p>
                        <ul class="text-base text-steel/80 space-y-1">
                            <li>• Why it exists</li>
                            <li>• Expected impact</li>
                            <li>• Supporting evidence</li>
                        </ul>
                    </div>
                </div>
                
                <div class="stagger-fade">
                    <p class="text-2xl text-steel mb-1">Business owners stop searching for answers.</p>
                    <p class="text-3xl text-gradient">Morlen brings the answers to them.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 6 -->
        <div class="slide" id="slide6" data-bg="SCALE">
            <div class="w-full h-full flex flex-col justify-center items-center text-center">
                <p class="overline-text mb-8 stagger-fade">SLIDE 5 — MARKET + BUSINESS MODEL</p>
                <h2 class="text-5xl font-medium text-steel mb-12 split-text">A Massive Market</h2>
                
                <p class="text-3xl text-steel mb-8 stagger-fade">Nigeria has approximately:</p>
                
                <div class="mb-16 stagger-fade relative">
                    <p class="text-[140px] font-bold text-gradient leading-none tracking-tighter">39.6 Million MSMEs</p>
                </div>
                
                <p class="text-2xl text-steel mb-8 stagger-fade">Representing:</p>
                <div class="flex gap-20 justify-center mb-20 stagger-fade text-4xl text-white font-medium">
                    <p>96% <span class="block text-xl text-steel mt-2 font-normal">of businesses</span></p>
                    <div class="w-px h-16 bg-white/10"></div>
                    <p>87.9% <span class="block text-xl text-steel mt-2 font-normal">of employment</span></p>
                    <div class="w-px h-16 bg-white/10"></div>
                    <p>46.3% <span class="block text-xl text-steel mt-2 font-normal">of GDP</span></p>
                </div>
                
                <div class="stagger-fade">
                    <p class="text-2xl text-steel mb-2">Millions already conduct business primarily through messaging platforms.</p>
                    <p class="text-3xl text-white">Morlen is built for this new operating environment.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 7 -->
        <div class="slide" id="slide7" data-bg="SAAS">
            <div class="w-full h-full flex flex-col justify-center">
                <p class="overline-text mb-6 stagger-fade">Business Model</p>
                <h2 class="text-6xl font-medium text-gradient mb-8 split-text">Subscription SaaS</h2>
                <p class="text-2xl text-steel mb-12 max-w-4xl stagger-fade">Starting with a 30 day free trial giving Morlen enough time to learn from customer conversations, build business memory, generate meaningful insights</p>
                
                <div class="grid grid-cols-3 gap-8 mb-12 stagger-fade">
                    <div class="pricing-card p-10 flex flex-col">
                        <h3 class="text-4xl font-medium text-white mb-2">Starter</h3>
                        <p class="text-xl text-steel font-medium mb-4">[N8,000/month]</p>
                        <p class="text-base text-steel mb-8">For early stage businesses</p>
                        <ul class="text-platinum space-y-4 flex-1 border-t border-white/10 pt-8">
                            <li>- Executive brief</li>
                            <li>- Business memory</li>
                            <li>- Basic decision intelligence</li>
                            <li>- Single workspace</li>
                        </ul>
                    </div>
                    
                    <div class="pricing-card p-10 flex flex-col border-white/30 shadow-[0_0_30px_rgba(255,255,255,0.05)] transform scale-105 z-10">
                        <div class="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-transparent via-white to-transparent"></div>
                        <h3 class="text-4xl font-medium text-white mb-2">Growth</h3>
                        <p class="text-xl text-white font-medium mb-4">[N15,000/month]</p>
                        <p class="text-base text-steel mb-8">Businesses managing increasing customer conversations.</p>
                        <ul class="text-platinum space-y-4 flex-1 border-t border-white/10 pt-8">
                            <li>- Everything in starter</li>
                            <li>- Opportunity feed</li>
                            <li>- Advanced AI recommendations</li>
                            <li>- Multi channel integrations</li>
                            <li>- Team Collaboration</li>
                        </ul>
                    </div>
                    
                    <div class="pricing-card p-10 flex flex-col">
                        <h3 class="text-4xl font-medium text-white mb-2">Enterprise</h3>
                        <p class="text-xl text-steel font-medium mb-4">[CUSTOM PRICING]</p>
                        <p class="text-base text-steel mb-8">Organizations requiring company-wide decision intelligence and integrations.</p>
                        <ul class="text-platinum space-y-4 flex-1 border-t border-white/10 pt-8">
                            <li>- Everything in growth</li>
                            <li>- Custom AI deployment</li>
                            <li>- Dedicate Support</li>
                            <li>- Enterprise security and governance</li>
                        </ul>
                    </div>
                </div>
                
                <p class="text-xl text-steel stagger-fade">Additional revenue: <span class="text-white">• Enterprise Implementation & Onboarding</span></p>
            </div>
        </div>

        <!-- SLIDE 8: MERGED FUNDING & OUTCOMES -->
        <div class="slide" id="slide8" data-bg="CAPITAL">
            <div class="w-full h-full flex flex-col justify-center">
                <p class="overline-text mb-8 stagger-fade">SLIDE 6 — FUNDING & OUTCOMES</p>
                
                <div class="flex gap-20">
                    <div class="flex-1">
                        <h2 class="text-5xl font-medium text-white mb-6 split-text">Raising Pre-Seed Capital</h2>
                        <p class="text-2xl text-steel mb-12 stagger-fade">Investment will accelerate:</p>
                        
                        <div class="space-y-8 pl-8 border-l border-white/20 stagger-fade">
                            <div>
                                <h3 class="text-3xl font-medium text-white mb-1">40% — Product Development</h3>
                                <p class="text-xl text-steel">Complete commercial MVP and core intelligence engine.</p>
                            </div>
                            <div>
                                <h3 class="text-3xl font-medium text-white mb-1">25% — AI Infrastructure</h3>
                                <p class="text-xl text-steel">Inference, data pipelines and production infrastructure.</p>
                            </div>
                            <div>
                                <h3 class="text-3xl font-medium text-white mb-1">20% — Customer Acquisition</h3>
                                <p class="text-xl text-steel">Pilot programs and early customer onboarding.</p>
                            </div>
                            <div>
                                <h3 class="text-3xl font-medium text-white mb-1">15% — Strategic Partnerships & Operations</h3>
                                <p class="text-xl text-steel">Messaging integrations and business development.</p>
                            </div>
                        </div>
                    </div>
                    
                    <div class="flex-1 pt-4 border-l border-white/10 pl-20">
                        <h2 class="text-5xl font-medium text-steel mb-12 split-text">Expected Outcomes</h2>
                        
                        <div class="space-y-10 stagger-fade">
                            <div class="flex items-center gap-6">
                                <div class="w-4 h-4 rounded-full border-2 border-white"></div>
                                <p class="text-3xl text-white">Commercial MVP</p>
                            </div>
                            <div class="flex items-center gap-6">
                                <div class="w-4 h-4 rounded-full border-2 border-white"></div>
                                <p class="text-3xl text-white">First paying customers</p>
                            </div>
                            <div class="flex items-center gap-6">
                                <div class="w-4 h-4 rounded-full border-2 border-white"></div>
                                <p class="text-3xl text-white">Validated product-market fit</p>
                            </div>
                            <div class="flex items-center gap-6">
                                <div class="w-4 h-4 rounded-full border-2 border-white"></div>
                                <p class="text-3xl text-white">Foundation for national expansion</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 9: WHY MORLEN -->
        <div class="slide" id="slide9" data-bg="VISION">
            <div class="w-full h-full flex flex-col justify-center">
                <p class="overline-text mb-12 stagger-fade">SLIDE 7 — WHY MORLEN?</p>
                
                <div class="flex gap-24">
                    <div class="flex-1 border-t border-white/10 pt-12">
                        <p class="text-3xl text-steel mb-8 split-text">Business software has always answered one question:</p>
                        <h2 class="text-[72px] font-medium text-white leading-none mb-12 stagger-fade">"What happened?"</h2>
                        
                        <ul class="text-2xl text-steel space-y-6 stagger-fade">
                            <li>CRM stores customer records</li>
                            <li>ERP manages operations</li>
                            <li>BI dashboards visualize historical metrics</li>
                            <li>Chatbots automate converstaions</li>
                        </ul>
                    </div>
                    
                    <div class="flex-1 border-t-4 border-white pt-12">
                        <p class="text-3xl text-steel mb-8 split-text">Morlen answers a different question:</p>
                        <h2 class="text-[72px] font-medium text-gradient leading-none mb-12 stagger-fade">"What should I do next?"</h2>
                        
                        <ul class="text-2xl text-white space-y-6 font-medium stagger-fade">
                            <li>Every conversation contains intelligence.</li>
                            <li>Every business generates opportunities.</li>
                            <li>Every owner has limited attention.</li>
                        </ul>
                        
                        <div class="mt-16 pt-8 stagger-fade">
                            <p class="text-3xl text-white leading-relaxed">Morlen exists to protect that attention—<br>by turning conversations into decisions.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 10: FINAL -->
        <div class="slide" id="slide10" data-bg="FUTURE">
            <div class="w-full h-full flex flex-col justify-center items-center text-center">
                <p class="overline-text mb-16 stagger-fade">FINAL SLIDE</p>
                
                <h1 class="text-[200px] font-bold tracking-tighter text-gradient leading-none mb-16 split-text">MORLEN</h1>
                
                <div class="stagger-fade">
                    <p class="text-5xl text-steel mb-6">The future of business isn't more software.</p>
                    <p class="text-6xl font-medium text-white mb-24">It's better decisions.</p>
                </div>
                
                <div class="stagger-fade pt-12 border-t border-white/20 w-full max-w-4xl">
                    <p class="text-3xl text-steel mb-4">Businesses already have the conversations.</p>
                    <p class="text-5xl text-white font-medium tracking-tight">Morlen turns them into decisions.</p>
                </div>
            </div>
        </div>

    </div>

    <script>
        // Custom text splitter to create spans for words
        document.querySelectorAll('.split-text').forEach(el => {
            const text = el.innerText;
            const words = text.split(' ');
            el.innerHTML = '';
            words.forEach(word => {
                const mask = document.createElement('span');
                mask.className = 'word-mask';
                const inner = document.createElement('span');
                inner.className = 'word-inner';
                inner.innerHTML = word + '&nbsp;';
                mask.appendChild(inner);
                el.appendChild(mask);
            });
        });

        const slides = document.querySelectorAll('.slide');
        let currentSlide = 0;
        let isAnimating = false;
        const bgText = document.getElementById('bg-text');

        function goToSlide(index) {
            if (isAnimating || index < 0 || index >= slides.length) return;
            isAnimating = true;

            const current = slides[currentSlide];
            const next = slides[index];
            
            // Update Kinetic BG
            const newBg = next.getAttribute('data-bg');
            if(newBg) {
                gsap.to(bgText, {
                    opacity: 0, duration: 0.5, onComplete: () => {
                        bgText.innerText = newBg;
                        gsap.to(bgText, { opacity: 1, duration: 1.5 });
                    }
                });
            }
            
            if (current) {
                gsap.to(current, {
                    opacity: 0, y: -50,
                    duration: 0.8,
                    ease: "power3.inOut",
                    onComplete: () => {
                        current.classList.remove('active');
                        current.style.visibility = 'hidden';
                        gsap.set(current, { y: 0 }); // reset
                    }
                });
            }

            next.classList.add('active');
            next.style.visibility = 'visible';
            
            // Reset next elements
            const fadeElements = next.querySelectorAll('.stagger-fade');
            const wordInners = next.querySelectorAll('.word-inner');
            
            gsap.set(fadeElements, { opacity: 0, y: 30 });
            gsap.set(wordInners, { y: '100%', rotationX: 20 });

            // Animate next elements
            const tl = gsap.timeline({
                onComplete: () => {
                    currentSlide = index;
                    isAnimating = false;
                }
            });
            
            tl.to(next, { opacity: 1, duration: 0.2 })
              .to(wordInners, {
                  y: '0%', rotationX: 0, duration: 1.2, 
                  stagger: 0.05, ease: "expo.out"
              }, "-=0.2")
              .to(fadeElements, {
                  opacity: 1, y: 0, duration: 1,
                  stagger: 0.1, ease: "power3.out"
              }, "-=0.8");
        }

        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight' || e.key === 'Space') goToSlide(currentSlide + 1);
            if (e.key === 'ArrowLeft') goToSlide(currentSlide - 1);
        });

        // Initialize First Slide
        slides[0].classList.add('active');
        slides[0].style.visibility = 'visible';
        slides[0].style.opacity = 1;
        
        gsap.set(slides[0].querySelectorAll('.stagger-fade'), { opacity: 0, y: 30 });
        gsap.set(slides[0].querySelectorAll('.word-inner'), { y: '100%', rotationX: 20 });
        
        setTimeout(() => {
            gsap.to(slides[0].querySelectorAll('.word-inner'), {
                y: '0%', rotationX: 0, duration: 1.2, 
                stagger: 0.05, ease: "expo.out"
            });
            gsap.to(slides[0].querySelectorAll('.stagger-fade'), {
                opacity: 1, y: 0, duration: 1,
                stagger: 0.1, ease: "power3.out", delay: 0.4
            });
        }, 100);
        
        // AUTO ADVANCE for the video recorder (Every 8.5 seconds to account for 10 slides in 85 seconds)
        setInterval(() => {
            if (currentSlide < slides.length - 1) {
                goToSlide(currentSlide + 1);
            }
        }, 8500);
        
        window.goToSlide = goToSlide;
    </script>
</body>
</html>"""

with open('presentation.html', 'w') as f:
    f.write(html_content)

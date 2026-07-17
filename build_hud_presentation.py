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
    <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@100;300;400;700&display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        display: ['Instrument Serif', 'serif'],
                        body: ['Inter', 'sans-serif'],
                        mono: ['JetBrains Mono', 'monospace'],
                    },
                    colors: {
                        void: '#010101',
                        bone: '#FFFFFF',
                        ash: '#7A7A7A'
                    }
                }
            }
        }
    </script>

    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            background-color: #010101;
            color: #FFFFFF;
            font-family: 'Inter', sans-serif;
            overflow: hidden;
            width: 100vw;
            height: 100vh;
        }

        #presentation-container {
            width: 1920px;
            height: 1080px;
            position: relative;
            background: #010101;
            overflow: hidden;
        }

        /* 
         * INSANELY COMPLEX 2D ELEMENTS (HUD / DATA VISUALIZATION)
         */
         
        /* Dense Technical Grid */
        .tech-grid {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background-image: 
                linear-gradient(rgba(255,255,255,0.04) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255,255,255,0.04) 1px, transparent 1px),
                linear-gradient(rgba(255,255,255,0.01) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255,255,255,0.01) 1px, transparent 1px);
            background-size: 100px 100px, 100px 100px, 20px 20px, 20px 20px;
            z-index: 0;
            mask-image: radial-gradient(circle at 50% 50%, black 20%, transparent 80%);
            -webkit-mask-image: radial-gradient(circle at 50% 50%, black 20%, transparent 80%);
            animation: grid-scan 20s linear infinite;
        }

        @keyframes grid-scan {
            0% { transform: translateY(0); }
            100% { transform: translateY(100px); }
        }
        
        /* Massive Rotating Data Dials */
        .data-dial {
            position: absolute;
            border-radius: 50%;
            border: 1px dashed rgba(255,255,255,0.1);
            z-index: 1;
            pointer-events: none;
        }
        .data-dial::before, .data-dial::after {
            content: ''; position: absolute; border-radius: 50%; border: 1px solid rgba(255,255,255,0.05);
        }
        .data-dial::before { inset: 20px; border-style: dotted; }
        .data-dial::after { inset: 40px; border-left-color: rgba(255,255,255,0.2); }
        
        .dial-1 { width: 1800px; height: 1800px; top: -900px; left: -900px; animation: spin-slow 120s linear infinite; }
        .dial-2 { width: 1200px; height: 1200px; bottom: -600px; right: -400px; animation: spin-slow 90s linear infinite reverse; }

        @keyframes spin-slow { 100% { transform: rotate(360deg); } }
        
        /* Flowing SVG Data Waves (Sine Waves) */
        .data-wave {
            position: absolute;
            top: 40%; left: -10%; width: 120%; height: 200px;
            background-image: url("data:image/svg+xml,%3Csvg width='1200' height='200' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 100 Q 150 0, 300 100 T 600 100 T 900 100 T 1200 100' fill='none' stroke='rgba(255,255,255,0.08)' stroke-width='1'/%3E%3Cpath d='M0 100 Q 150 200, 300 100 T 600 100 T 900 100 T 1200 100' fill='none' stroke='rgba(255,255,255,0.04)' stroke-width='1'/%3E%3C/svg%3E");
            background-size: 600px 100%;
            animation: wave-flow 10s linear infinite;
            z-index: 1;
            opacity: 0.6;
        }
        
        @keyframes wave-flow { 100% { background-position: 600px 0; } }

        /* 
         * COMPLEX ASYMMETRICAL GLASSMORPHISM PANELS 
         * Not just cards. Tactical, high-end panels with UI accents.
         */
        .glass-panel {
            background: linear-gradient(135deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.01) 100%);
            backdrop-filter: blur(30px);
            -webkit-backdrop-filter: blur(30px);
            border: 1px solid rgba(255,255,255,0.08);
            border-top: 1px solid rgba(255,255,255,0.2);
            border-left: 1px solid rgba(255,255,255,0.15);
            box-shadow: 0 40px 80px rgba(0,0,0,0.8), inset 0 1px 1px rgba(255,255,255,0.05);
            position: relative;
            z-index: 5;
            /* Clipped corners for tactical aesthetic */
            clip-path: polygon(
                0 20px, 20px 0, 
                100% 0, 100% calc(100% - 20px), 
                calc(100% - 20px) 100%, 0 100%
            );
        }
        
        /* UI Accents on Glass Panels */
        .glass-panel::after {
            content: ''; position: absolute; bottom: 0; left: 0; width: 30%; height: 2px; background: rgba(255,255,255,0.3);
        }

        .slide {
            position: absolute; top: 0; left: 0;
            width: 100%; height: 100%;
            padding: 80px 120px;
            opacity: 0;
            visibility: hidden;
            z-index: 10;
        }

        .slide.active { opacity: 1; visibility: visible; }
        
        /* Typography */
        .huge-headline {
            font-family: 'Instrument Serif', serif;
            font-size: 130px;
            font-weight: 400;
            line-height: 1.0;
            color: #FFFFFF;
            margin-bottom: 24px;
            letter-spacing: -0.02em;
        }
        
        .huge-italic { font-style: italic; font-weight: 400; color: #FFFFFF; }
        
        .sub-headline {
            font-size: 36px;
            font-weight: 300;
            color: rgba(255,255,255,0.9);
            margin-bottom: 24px;
            line-height: 1.3;
        }
        
        /* High-tech Mono Accents */
        .mono-accent {
            font-family: 'JetBrains Mono', monospace;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 0.3em;
            color: rgba(255,255,255,0.5);
        }

    </style>
</head>
<body>

    <div id="presentation-container">
        <!-- Intense 2D Elements (HUD / Data Vis) -->
        <div class="tech-grid"></div>
        <div class="data-dial dial-1"></div>
        <div class="data-dial dial-2"></div>
        <div class="data-wave"></div>

        <!-- Global UI HUD Frame -->
        <div class="absolute top-[40px] left-[40px] mono-accent">SYS.ON // MORLEN_OS</div>
        <div class="absolute top-[40px] right-[40px] mono-accent flex gap-4"><span>DATA_STREAM</span><div class="w-2 h-2 bg-white rounded-full animate-pulse"></div></div>
        <div class="absolute bottom-[40px] left-[40px] mono-accent">LAT: 04.281 / LNG: 09.321</div>
        <div class="absolute bottom-[40px] right-[40px] mono-accent text-right">SECURE_CONNECTION<br>v1.0.4</div>

        <!-- SLIDE 1 -->
        <div class="slide" id="slide1">
            <div class="w-full h-full flex flex-col justify-center">
                <div class="max-w-5xl relative z-10 pl-[80px]">
                    <div class="glass-panel inline-flex items-center gap-6 px-8 py-3 mb-10 stagger-anim" style="clip-path: none; border-radius: 100px;">
                        <div class="w-3 h-3 bg-white shadow-[0_0_15px_white]"></div>
                        <p class="mono-accent text-white">EXECUTIVE PITCH</p>
                    </div>
                    
                    <h1 class="huge-headline stagger-anim">Morlen.</h1>
                    <p class="sub-headline stagger-anim font-medium text-white/90">The Operating System for Business Decisions.</p>
                    <p class="text-3xl text-ash font-light mb-16 stagger-anim">Turning customer conversations into executive decisions.</p>
                    
                    <div class="stagger-anim glass-panel p-6 px-10 inline-flex items-center gap-8 mt-4">
                        <div class="flex flex-col">
                            <p class="mono-accent mb-2">FOUNDER_ID</p>
                            <p class="text-3xl text-white font-display italic tracking-wide">Hillary Ikhais</p>
                        </div>
                        <div class="w-px h-12 bg-white/20"></div>
                        <div class="mono-accent text-[10px] text-white/30 text-right">
                            AUTH: VERIFIED<br>
                            ACCESS: L1<br>
                            NODE: 0x8F9A
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 2 -->
        <div class="slide" id="slide2">
            <div class="w-full h-full flex flex-col justify-center">
                <div class="flex gap-20">
                    <div class="flex-1">
                        <h1 class="huge-headline stagger-anim" style="font-size: 110px;">The Problem.</h1>
                        <h2 class="sub-headline stagger-anim text-white">Businesses have <span class="huge-italic">automated</span> transactions.</h2>
                        
                        <div class="glass-panel p-12 stagger-anim mt-12">
                            <p class="text-2xl text-ash leading-relaxed mb-10 font-light">Over the last two decades, businesses have adopted software for almost every operational function:</p>
                            
                            <ul class="text-2xl text-white space-y-6 font-medium">
                                <li class="flex items-center justify-between"><div class="flex items-center gap-6"><span class="mono-accent text-white/40">01</span> Payments</div> <div class="w-20 h-px bg-white/10"></div></li>
                                <li class="flex items-center justify-between"><div class="flex items-center gap-6"><span class="mono-accent text-white/40">02</span> CRM</div> <div class="w-20 h-px bg-white/10"></div></li>
                                <li class="flex items-center justify-between"><div class="flex items-center gap-6"><span class="mono-accent text-white/40">03</span> Inventory</div> <div class="w-20 h-px bg-white/10"></div></li>
                                <li class="flex items-center justify-between"><div class="flex items-center gap-6"><span class="mono-accent text-white/40">04</span> Marketing</div> <div class="w-20 h-px bg-white/10"></div></li>
                                <li class="flex items-center justify-between"><div class="flex items-center gap-6"><span class="mono-accent text-white/40">05</span> Accounting</div> <div class="w-20 h-px bg-white/10"></div></li>
                                <li class="flex items-center gap-6 mt-8 pt-8 border-t border-white/20 text-4xl font-display italic text-white"><span class="mono-accent text-white not-italic text-sm">06</span> Conversations</li>
                            </ul>
                        </div>
                    </div>
                    
                    <div class="flex-1 flex flex-col justify-center pl-16">
                        <p class="text-3xl font-light text-white mb-12 stagger-anim leading-tight">Yet business owners still ask the same questions:</p>
                        
                        <div class="glass-panel p-12 mb-16 stagger-anim">
                            <ul class="text-2xl text-ash space-y-8 font-light">
                                <li class="flex gap-6 items-start"><div class="mt-2 w-2 h-2 bg-white/40 rounded-none"></div>What deserves attention today?</li>
                                <li class="flex gap-6 items-start"><div class="mt-2 w-2 h-2 bg-white/40 rounded-none"></div>Which products should I restock?</li>
                                <li class="flex gap-6 items-start"><div class="mt-2 w-2 h-2 bg-white/40 rounded-none"></div>Which customers need follow-up?</li>
                                <li class="flex gap-6 items-start"><div class="mt-2 w-2 h-2 bg-white/40 rounded-none"></div>Where am I losing revenue?</li>
                                <li class="flex gap-6 items-start"><div class="mt-2 w-2 h-2 bg-white/40 rounded-none"></div>Why have sales reduced?</li>
                            </ul>
                        </div>
                        
                        <div class="stagger-anim flex items-center gap-8">
                            <div class="w-16 h-16 border border-white/20 flex items-center justify-center p-2"><div class="w-full h-full border border-white/40"></div></div>
                            <div>
                                <p class="text-2xl text-white mb-2 font-medium">Business software automates operations.</p>
                                <p class="text-2xl text-ash font-light font-display italic">It records what happened.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 3 -->
        <div class="slide" id="slide3">
            <div class="w-full h-full flex flex-col justify-center pl-[80px]">
                <div class="max-w-5xl">
                    <div class="glass-panel inline-flex items-center gap-6 px-6 py-2 mb-10 stagger-anim" style="clip-path: none; border-radius: 100px;">
                        <p class="mono-accent text-white">SYS_UPDATE // THE_SHIFT</p>
                    </div>
                    
                    <h1 class="huge-headline stagger-anim" style="font-size: 110px;">Commerce has moved<br>into <span class="huge-italic">conversations.</span></h1>
                    
                    <div class="space-y-12 text-2xl text-ash leading-relaxed stagger-anim mt-16 font-light max-w-4xl">
                        <p>Across Nigeria, businesses now operate inside messaging platforms.<br>
                        <span class="text-xl mt-4 block text-ash/80">Customers now discover products, negotiate prices, confirm payments and arrange deliveries inside WhatsApp, Instagram and Facebook.</span></p>
                        
                        <div class="glass-panel p-10 border-l-4 border-l-white">
                            <p class="text-white font-medium text-4xl font-display italic leading-snug">For Nigerian MSMEs, the entire sales funnel now exists inside conversations.</p>
                        </div>
                        
                        <p>Yet traditional software was designed for structured forms, not unstructured conversations.</p>
                        
                        <div class="flex items-end gap-12 mt-12 pt-12 border-t border-white/10">
                            <p class="flex-1">As conversational commerce grows, businesses generate thousands of customer signals every day.</p>
                            <p class="flex-1 text-white font-medium text-2xl leading-tight">Most disappear without ever becoming business intelligence.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 4 -->
        <div class="slide" id="slide4">
            <div class="w-full h-full flex flex-col justify-center max-w-6xl pl-[80px]">
                <h1 class="huge-headline stagger-anim" style="font-size: 110px;">The Problem.</h1>
                <h2 class="sub-headline stagger-anim text-white">Every conversation creates decisions.</h2>
                <p class="text-2xl text-ash mb-12 stagger-anim font-light border-l border-white/20 pl-8">A business owner doesn't just receive messages.<br>They constantly decide:</p>
                
                <div class="glass-panel p-12 mb-16 stagger-anim">
                    <ul class="text-3xl text-white space-y-10 font-display italic grid grid-cols-2 gap-x-16">
                        <li class="flex items-center gap-6"><div class="w-1.5 h-1.5 bg-white/40"></div>Should this customer receive follow-up?</li>
                        <li class="flex items-center gap-6"><div class="w-1.5 h-1.5 bg-white/40"></div>Is demand increasing for this product?</li>
                        <li class="flex items-center gap-6"><div class="w-1.5 h-1.5 bg-white/40"></div>Should inventory be reordered?</li>
                        <li class="flex items-center gap-6"><div class="w-1.5 h-1.5 bg-white/40"></div>Are customers becoming more price-sensitive?</li>
                        <li class="flex items-center gap-6"><div class="w-1.5 h-1.5 bg-white/40"></div>Which complaints appear repeatedly?</li>
                        <li class="flex items-center gap-6"><div class="w-1.5 h-1.5 bg-white/40"></div>Which customers are likely to return?</li>
                    </ul>
                </div>
                
                <div class="stagger-anim mt-10 flex gap-20 items-end">
                    <p class="text-2xl text-ash font-light flex-1">These decisions are still made manually.</p>
                    <p class="text-4xl text-white font-medium flex-2 leading-tight">As conversations increase, decision complexity grows even faster.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 5 -->
        <div class="slide" id="slide5">
            <div class="w-full h-full flex flex-col justify-center pl-[80px]">
                <h1 class="huge-headline stagger-anim">Morlen.</h1>
                <h2 class="sub-headline stagger-anim text-white">An Executive <span class="huge-italic">Decision Intelligence</span> Platform.</h2>
                
                <div class="stagger-anim max-w-5xl mb-12 mt-8 glass-panel p-8">
                    <p class="text-2xl text-ash mb-6 font-light">Morlen continuously analyzes customer conversations, identifies business patterns and delivers prioritized business decisions.</p>
                    <p class="text-3xl text-white font-display italic">Instead of presenting plain dashboards, Morlen produces a daily executive briefing.</p>
                </div>
                
                <div class="grid grid-cols-4 gap-8 mb-16 relative z-10">
                    <div class="stagger-anim flex flex-col glass-panel p-8">
                        <p class="mono-accent mb-4">MODULE_01</p>
                        <h3 class="text-3xl font-display italic text-white mb-6">Executive Brief</h3>
                        <p class="text-lg text-ash font-light leading-relaxed">A daily summary of the highest priority decisions. inventory risks, customer churn, demand spikes.</p>
                    </div>
                    <div class="stagger-anim flex flex-col glass-panel p-8">
                        <p class="mono-accent mb-4">MODULE_02</p>
                        <h3 class="text-3xl font-display italic text-white mb-6">Opportunity Feed</h3>
                        <p class="text-lg text-ash font-light leading-relaxed">Revenue opportunities detected from conversations including estimated impact, confidence score.</p>
                    </div>
                    <div class="stagger-anim flex flex-col glass-panel p-8">
                        <p class="mono-accent mb-4">MODULE_03</p>
                        <h3 class="text-3xl font-display italic text-white mb-6">Business Memory</h3>
                        <p class="text-lg text-ash font-light leading-relaxed mb-6">Long-term behavioural intelligence about customers.</p>
                        <p class="text-xs text-white uppercase tracking-widest font-mono mt-auto pt-4 border-t border-white/10">Ex: Demand rises</p>
                    </div>
                    <div class="stagger-anim flex flex-col glass-panel p-8">
                        <p class="mono-accent mb-4">MODULE_04</p>
                        <h3 class="text-3xl font-display italic text-white mb-6">Evidence-Based</h3>
                        <p class="text-lg text-ash font-light leading-relaxed mb-4">Every recommendation explains:</p>
                        <ul class="text-sm text-white space-y-2 font-mono">
                            <li>01. Why it exists</li>
                            <li>02. Expected impact</li>
                            <li>03. Supporting evidence</li>
                        </ul>
                    </div>
                </div>
                
                <div class="stagger-anim flex items-center gap-12 w-max">
                    <p class="text-2xl text-ash font-light">Business owners stop searching for answers.</p>
                    <p class="text-4xl font-display italic text-white">Morlen brings the answers to them.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 6 -->
        <div class="slide" id="slide6">
            <div class="w-full h-full flex flex-col justify-center items-center text-center relative">
                <div class="stagger-anim mb-12 glass-panel px-8 py-3" style="clip-path:none; border-radius:100px;">
                    <p class="mono-accent text-white">MARKET_ANALYSIS</p>
                </div>
                
                <h1 class="huge-headline stagger-anim" style="font-size: 110px;">A Massive <span class="huge-italic">Market.</span></h1>
                <p class="text-3xl text-ash mb-12 stagger-anim font-light">Nigeria has approximately:</p>
                
                <div class="stagger-anim glass-panel p-16 px-32 mb-16">
                    <p class="text-[160px] font-display italic text-white leading-none tracking-tight">39.6M <span class="text-6xl font-sans not-italic text-ash font-light">MSMEs</span></p>
                </div>
                    
                <p class="text-sm text-ash mb-10 stagger-anim uppercase tracking-[0.3em] font-medium">Representing</p>
                <div class="flex gap-20 items-center mb-16 stagger-anim">
                    <div class="flex flex-col items-center">
                        <p class="text-7xl font-display italic text-white mb-4">96%</p>
                        <p class="text-xl text-ash font-light">of businesses</p>
                    </div>
                    <div class="w-px h-20 bg-white/20"></div>
                    <div class="flex flex-col items-center">
                        <p class="text-7xl font-display italic text-white mb-4">87.9%</p>
                        <p class="text-xl text-ash font-light">of employment</p>
                    </div>
                    <div class="w-px h-20 bg-white/20"></div>
                    <div class="flex flex-col items-center">
                        <p class="text-7xl font-display italic text-white mb-4">46.3%</p>
                        <p class="text-xl text-ash font-light">of GDP</p>
                    </div>
                </div>
                
                <div class="stagger-anim mt-4">
                    <p class="text-2xl font-light text-ash leading-relaxed">Millions already conduct business primarily through messaging platforms. <span class="text-white font-medium">Morlen is built for this new operating environment.</span></p>
                </div>
            </div>
        </div>

        <!-- SLIDE 7 -->
        <div class="slide" id="slide7">
            <div class="w-full h-full flex flex-col justify-center pl-[80px]">
                <h1 class="huge-headline stagger-anim" style="font-size: 110px;">Business <span class="huge-italic">Model.</span></h1>
                
                <div class="flex items-center gap-12 mb-16 stagger-anim">
                    <div class="glass-panel px-6 py-2" style="clip-path:none; border-radius:100px;">
                        <h2 class="mono-accent text-white">SUBSCRIPTION_SAAS</h2>
                    </div>
                    <p class="text-xl text-ash max-w-3xl font-light leading-relaxed">Starting with a 30-day free trial giving Morlen enough time to learn from customer conversations, build business memory, and generate meaningful insights.</p>
                </div>
                
                <div class="flex gap-12 mb-16 stagger-anim relative z-10">
                    <div class="flex-1 glass-panel p-10 flex flex-col">
                        <h3 class="text-5xl font-display italic text-white mb-4">Starter</h3>
                        <p class="text-2xl text-ash font-mono mb-8">N8,000/mo</p>
                        <p class="text-base text-ash mb-10 font-light h-12">For early stage businesses</p>
                        <ul class="text-white space-y-4 text-base font-light border-t border-white/10 pt-8">
                            <li class="flex items-center gap-4"><div class="w-1.5 h-1.5 bg-white/30 rounded-none"></div>Executive brief</li>
                            <li class="flex items-center gap-4"><div class="w-1.5 h-1.5 bg-white/30 rounded-none"></div>Business memory</li>
                            <li class="flex items-center gap-4"><div class="w-1.5 h-1.5 bg-white/30 rounded-none"></div>Basic decision intelligence</li>
                            <li class="flex items-center gap-4"><div class="w-1.5 h-1.5 bg-white/30 rounded-none"></div>Single workspace</li>
                        </ul>
                    </div>
                    
                    <div class="flex-1 glass-panel p-10 flex flex-col border-white/30 transform scale-[1.05]" style="box-shadow: 0 50px 100px rgba(0,0,0,0.9);">
                        <div class="absolute -top-4 right-10 bg-white text-black px-4 py-1 mono-accent font-bold">POPULAR_TIER</div>
                        <h3 class="text-5xl font-display italic text-white mb-4">Growth</h3>
                        <p class="text-2xl text-white font-mono mb-8 font-bold">N15,000/mo</p>
                        <p class="text-base text-ash mb-10 font-light h-12">Businesses managing increasing customer conversations.</p>
                        <ul class="text-white space-y-4 text-base font-medium border-t border-white/30 pt-8">
                            <li class="flex items-center gap-4"><div class="w-1.5 h-1.5 bg-white shadow-[0_0_10px_white]"></div>Everything in starter</li>
                            <li class="flex items-center gap-4"><div class="w-1.5 h-1.5 bg-white shadow-[0_0_10px_white]"></div>Opportunity feed</li>
                            <li class="flex items-center gap-4"><div class="w-1.5 h-1.5 bg-white shadow-[0_0_10px_white]"></div>Advanced AI recommendations</li>
                            <li class="flex items-center gap-4"><div class="w-1.5 h-1.5 bg-white shadow-[0_0_10px_white]"></div>Multi channel integrations</li>
                            <li class="flex items-center gap-4"><div class="w-1.5 h-1.5 bg-white shadow-[0_0_10px_white]"></div>Team Collaboration</li>
                        </ul>
                    </div>
                    
                    <div class="flex-1 glass-panel p-10 flex flex-col">
                        <h3 class="text-5xl font-display italic text-white mb-4">Enterprise</h3>
                        <p class="text-2xl text-ash font-mono mb-8">CUSTOM</p>
                        <p class="text-base text-ash mb-10 font-light h-12">Organizations requiring company-wide decision intelligence.</p>
                        <ul class="text-white space-y-4 text-base font-light border-t border-white/10 pt-8">
                            <li class="flex items-center gap-4"><div class="w-1.5 h-1.5 bg-white/30 rounded-none"></div>Everything in growth</li>
                            <li class="flex items-center gap-4"><div class="w-1.5 h-1.5 bg-white/30 rounded-none"></div>Custom AI deployment</li>
                            <li class="flex items-center gap-4"><div class="w-1.5 h-1.5 bg-white/30 rounded-none"></div>Dedicated Support</li>
                            <li class="flex items-center gap-4"><div class="w-1.5 h-1.5 bg-white/30 rounded-none"></div>Enterprise security</li>
                        </ul>
                    </div>
                </div>
                
                <p class="text-lg text-ash stagger-anim font-light flex items-center gap-6">
                    Additional revenue: <span class="text-white font-medium font-mono uppercase tracking-widest text-sm bg-white/10 px-4 py-2">Enterprise Implementation & Onboarding</span>
                </p>
            </div>
        </div>

        <!-- SLIDE 8 -->
        <div class="slide" id="slide8">
            <div class="w-full h-full flex flex-col justify-center pl-[80px]">
                <div class="flex gap-24 relative z-10">
                    <div class="flex-1">
                        <h1 class="huge-headline stagger-anim" style="font-size: 110px;">Funding.</h1>
                        <h2 class="text-4xl font-display italic text-white mb-12 stagger-anim">Raising Pre-Seed Capital</h2>
                        <p class="text-sm text-ash mb-12 stagger-anim font-mono uppercase tracking-widest">Investment will accelerate:</p>
                        
                        <div class="glass-panel p-12 space-y-10 stagger-anim">
                            <div class="flex items-center gap-10">
                                <h3 class="text-6xl font-display italic text-white w-32">40%</h3>
                                <div class="w-px h-16 bg-white/20"></div>
                                <div>
                                    <p class="text-xl font-medium text-white mb-2">Product Development</p>
                                    <p class="text-base text-ash font-light">Complete commercial MVP and core intelligence engine.</p>
                                </div>
                            </div>
                            <div class="flex items-center gap-10">
                                <h3 class="text-6xl font-display italic text-white/80 w-32">25%</h3>
                                <div class="w-px h-16 bg-white/20"></div>
                                <div>
                                    <p class="text-xl font-medium text-white mb-2">AI Infrastructure</p>
                                    <p class="text-base text-ash font-light">Inference, data pipelines and production infrastructure.</p>
                                </div>
                            </div>
                            <div class="flex items-center gap-10">
                                <h3 class="text-6xl font-display italic text-white/60 w-32">20%</h3>
                                <div class="w-px h-16 bg-white/20"></div>
                                <div>
                                    <p class="text-xl font-medium text-white mb-2">Customer Acq.</p>
                                    <p class="text-base text-ash font-light">Pilot programs and early customer onboarding.</p>
                                </div>
                            </div>
                            <div class="flex items-center gap-10">
                                <h3 class="text-6xl font-display italic text-white/40 w-32">15%</h3>
                                <div class="w-px h-16 bg-white/20"></div>
                                <div>
                                    <p class="text-xl font-medium text-white mb-2">Operations</p>
                                    <p class="text-base text-ash font-light">Messaging integrations and business development.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="flex-1 flex flex-col justify-center pl-16">
                        <h1 class="huge-headline stagger-anim" style="font-size: 110px;">Outcomes.</h1>
                        <h2 class="text-4xl font-display italic text-white mb-16 stagger-anim">Expected Milestones</h2>
                        
                        <div class="space-y-8 stagger-anim">
                            <div class="glass-panel p-8 flex items-center gap-8">
                                <div class="mono-accent text-white/40">M.01</div>
                                <div class="w-px h-8 bg-white/20"></div>
                                <p class="text-3xl text-white font-light">Commercial MVP</p>
                            </div>
                            <div class="glass-panel p-8 flex items-center gap-8">
                                <div class="mono-accent text-white/40">M.02</div>
                                <div class="w-px h-8 bg-white/20"></div>
                                <p class="text-3xl text-white font-light">First paying customers</p>
                            </div>
                            <div class="glass-panel p-8 flex items-center gap-8">
                                <div class="mono-accent text-white/40">M.03</div>
                                <div class="w-px h-8 bg-white/20"></div>
                                <p class="text-3xl text-white font-light">Validated product-market fit</p>
                            </div>
                            <div class="glass-panel p-8 flex items-center gap-8">
                                <div class="mono-accent text-white/40">M.04</div>
                                <div class="w-px h-8 bg-white/20"></div>
                                <p class="text-3xl text-white font-light">Foundation for national expansion</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 9 -->
        <div class="slide" id="slide9">
            <div class="w-full h-full flex flex-col justify-center pl-[80px]">
                <h1 class="huge-headline stagger-anim" style="font-size: 110px;">Why Morlen?</h1>
                
                <div class="flex gap-24 mt-16 relative z-10">
                    <div class="flex-1 stagger-anim flex flex-col justify-center border-l border-white/20 pl-16">
                        <p class="text-xl text-ash mb-8 font-light uppercase tracking-widest">Software answers:</p>
                        <h2 class="text-[90px] font-display italic text-white leading-none mb-16">"What happened?"</h2>
                        
                        <ul class="text-3xl text-ash space-y-8 font-light">
                            <li class="flex items-center gap-6"><div class="w-2 h-2 bg-white/30 rounded-none"></div>CRM stores customer records</li>
                            <li class="flex items-center gap-6"><div class="w-2 h-2 bg-white/30 rounded-none"></div>ERP manages operations</li>
                            <li class="flex items-center gap-6"><div class="w-2 h-2 bg-white/30 rounded-none"></div>BI visualizes historical metrics</li>
                            <li class="flex items-center gap-6"><div class="w-2 h-2 bg-white/30 rounded-none"></div>Chatbots automate conversations</li>
                        </ul>
                    </div>
                    
                    <div class="flex-1 glass-panel p-16 stagger-anim flex flex-col justify-center">
                        <p class="text-xl text-white mb-8 font-medium uppercase tracking-widest">Morlen answers:</p>
                        <h2 class="text-[90px] font-display italic text-white leading-none mb-16 drop-shadow-[0_0_30px_rgba(255,255,255,0.2)]">"What should I do next?"</h2>
                        
                        <ul class="text-3xl text-white space-y-8 font-medium">
                            <li class="flex items-center gap-6"><div class="w-2 h-2 bg-white shadow-[0_0_10px_white] rounded-none"></div>Every conversation contains intelligence.</li>
                            <li class="flex items-center gap-6"><div class="w-2 h-2 bg-white shadow-[0_0_10px_white] rounded-none"></div>Every business generates opportunities.</li>
                            <li class="flex items-center gap-6"><div class="w-2 h-2 bg-white shadow-[0_0_10px_white] rounded-none"></div>Every owner has limited attention.</li>
                        </ul>
                        
                        <div class="mt-16 pt-12 border-t border-white/20">
                            <p class="text-4xl text-white leading-relaxed font-light">Morlen exists to protect that attention—<br><span class="font-display italic text-ash">by turning conversations into decisions.</span></p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 10 -->
        <div class="slide" id="slide10">
            <div class="w-full h-full flex flex-col justify-center items-center text-center relative z-10">
                <div class="stagger-anim mb-20 flex items-center gap-8 glass-panel px-10 py-4" style="clip-path:none; border-radius:100px;">
                    <p class="text-xl font-medium text-white uppercase tracking-[0.4em]">The future of business isn't more software.</p>
                </div>

                <h1 class="text-[350px] font-display italic text-white leading-none tracking-tighter mb-20 stagger-anim drop-shadow-[0_0_60px_rgba(255,255,255,0.15)]">Morlen.</h1>
                
                <div class="stagger-anim">
                    <p class="text-3xl text-ash mb-6 font-light">Businesses already have the conversations.</p>
                    <p class="text-5xl text-white font-medium tracking-wide">Morlen turns them into decisions.</p>
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
                    opacity: 0, scale: 0.98, filter: 'blur(10px)',
                    duration: 0.6,
                    ease: "power2.inOut",
                    onComplete: () => {
                        current.classList.remove('active');
                        current.style.visibility = 'hidden';
                        gsap.set(current, { scale: 1, filter: 'blur(0px)' }); 
                    }
                });
            }

            next.classList.add('active');
            next.style.visibility = 'visible';
            
            const fadeElements = next.querySelectorAll('.stagger-anim');
            gsap.set(fadeElements, { opacity: 0, x: -30, filter: 'blur(10px)' });

            const tl = gsap.timeline({
                onComplete: () => {
                    currentSlide = index;
                    isAnimating = false;
                }
            });
            
            tl.to(next, { opacity: 1, duration: 0.2 })
              .to(fadeElements, {
                  opacity: 1, x: 0, filter: 'blur(0px)', duration: 1.2,
                  stagger: 0.1, ease: "power3.out"
              }, "-=0.1");
        }

        slides[0].classList.add('active');
        slides[0].style.visibility = 'visible';
        slides[0].style.opacity = 1;
        
        gsap.set(slides[0].querySelectorAll('.stagger-anim'), { opacity: 0, x: -30, filter: 'blur(10px)' });
        
        setTimeout(() => {
            gsap.to(slides[0].querySelectorAll('.stagger-anim'), {
                opacity: 1, x: 0, filter: 'blur(0px)', duration: 1.2,
                stagger: 0.1, ease: "power3.out"
            });
        }, 300);
        
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

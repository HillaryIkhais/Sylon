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
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        display: ['Outfit', 'sans-serif'],
                        body: ['Plus Jakarta Sans', 'sans-serif'],
                    },
                    colors: {
                        titanium: '#1C1C1E',
                        obsidian: '#09090B',
                        platinum: '#E5E5EA',
                        muted: '#8E8E93'
                    }
                }
            }
        }
    </script>

    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            background-color: #09090B;
            color: #E5E5EA;
            font-family: 'Plus Jakarta Sans', sans-serif;
            overflow: hidden;
            width: 100vw;
            height: 100vh;
        }

        #presentation-container {
            width: 1920px;
            height: 1080px;
            position: relative;
            background: #09090B;
            overflow: hidden;
        }

        /* Animated Liquid Metallic Mesh Background */
        .liquid-mesh {
            position: absolute;
            top: -50%; left: -50%; width: 200%; height: 200%;
            background: 
                radial-gradient(circle at 50% 50%, rgba(28, 28, 30, 0.8) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, rgba(40, 40, 45, 0.6) 0%, transparent 40%),
                radial-gradient(circle at 20% 80%, rgba(15, 15, 18, 0.9) 0%, transparent 50%);
            z-index: 0;
            animation: fluid-mesh 25s ease-in-out infinite alternate;
            filter: blur(60px);
        }

        @keyframes fluid-mesh {
            0% { transform: rotate(0deg) scale(1); }
            50% { transform: rotate(180deg) scale(1.2); }
            100% { transform: rotate(360deg) scale(1); }
        }

        /* Creative 2D Topographic SVG Background */
        .topo-bg {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background-image: url("data:image/svg+xml,%3Csvg width='800' height='800' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M100 100 Q 200 50, 300 150 T 500 200 T 700 100' fill='none' stroke='rgba(255,255,255,0.03)' stroke-width='2'/%3E%3Cpath d='M100 200 Q 250 100, 350 250 T 550 300 T 700 200' fill='none' stroke='rgba(255,255,255,0.03)' stroke-width='2'/%3E%3Cpath d='M100 300 Q 300 150, 400 350 T 600 400 T 700 300' fill='none' stroke='rgba(255,255,255,0.03)' stroke-width='2'/%3E%3Cpath d='M100 400 Q 350 200, 450 450 T 650 500 T 700 400' fill='none' stroke='rgba(255,255,255,0.03)' stroke-width='2'/%3E%3Cpath d='M100 500 Q 400 250, 500 550 T 700 600 T 700 500' fill='none' stroke='rgba(255,255,255,0.03)' stroke-width='2'/%3E%3Cpath d='M100 600 Q 450 300, 550 650 T 750 700 T 700 600' fill='none' stroke='rgba(255,255,255,0.03)' stroke-width='2'/%3E%3Cpath d='M100 700 Q 500 350, 600 750 T 800 800 T 700 700' fill='none' stroke='rgba(255,255,255,0.03)' stroke-width='2'/%3E%3C/svg%3E");
            background-size: 150%;
            z-index: 1;
            animation: topo-pan 40s linear infinite alternate;
        }

        @keyframes topo-pan {
            0% { background-position: 0% 0%; background-size: 100%; }
            100% { background-position: 100% 100%; background-size: 150%; }
        }
        
        /* Interactive 2D Elements */
        .vector-element {
            position: absolute;
            border: 1px solid rgba(255,255,255,0.05);
            z-index: 1;
            pointer-events: none;
        }
        .v-box { width: 500px; height: 500px; border-radius: 40px; transform: rotate(45deg); top: -200px; right: -100px; animation: slow-spin 30s linear infinite; }
        .v-circle { width: 700px; height: 700px; border-radius: 50%; bottom: -300px; left: -100px; animation: pulse-ring 15s ease-in-out infinite alternate; border: 2px dashed rgba(255,255,255,0.03); }

        @keyframes slow-spin { 100% { transform: rotate(405deg); } }
        @keyframes pulse-ring { 100% { transform: scale(1.1); } }

        /* High-End Frosted Glassmorphism */
        .glass-card {
            background: rgba(255, 255, 255, 0.03);
            background-blend-mode: luminosity;
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-top: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 30px 60px rgba(0,0,0,0.4), inset 0 1px 1px rgba(255,255,255,0.1);
            position: relative;
            z-index: 5;
            border-radius: 24px;
        }

        .slide {
            position: absolute; top: 0; left: 0;
            width: 100%; height: 100%;
            padding: 100px 140px;
            opacity: 0;
            visibility: hidden;
            z-index: 10;
        }

        .slide.active { opacity: 1; visibility: visible; }
        
        /* Typography */
        h1, h2 { font-family: 'Outfit', sans-serif; }
        
        .huge-headline {
            font-size: 110px;
            font-weight: 700;
            line-height: 1.05;
            color: #FFFFFF;
            margin-bottom: 30px;
            letter-spacing: -0.03em;
            text-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }
        
        .sub-headline {
            font-size: 52px;
            font-weight: 500;
            color: rgba(255,255,255,0.9);
            margin-bottom: 24px;
            line-height: 1.2;
            letter-spacing: -0.01em;
        }

    </style>
</head>
<body>

    <div id="presentation-container">
        <!-- Liquid Metallic Background & 2D Topography -->
        <div class="liquid-mesh"></div>
        <div class="topo-bg"></div>
        <div class="vector-element v-box"></div>
        <div class="vector-element v-circle"></div>

        <!-- SLIDE 1 -->
        <div class="slide" id="slide1">
            <div class="w-full h-full flex flex-col justify-center">
                <div class="max-w-4xl relative z-10">
                    <div class="glass-card inline-block px-6 py-2 mb-8 stagger-anim rounded-full">
                        <p class="text-xs uppercase tracking-[0.4em] text-white/80 font-bold">Executive Pitch</p>
                    </div>
                    <h1 class="huge-headline stagger-anim">Morlen.</h1>
                    <p class="sub-headline stagger-anim">The Operating System for Business Decisions.</p>
                    <p class="text-3xl text-muted font-light mb-16 stagger-anim">Turning customer conversations into executive decisions.</p>
                    
                    <div class="stagger-anim glass-card p-6 inline-flex items-center gap-6 mt-6">
                        <div class="w-12 h-12 rounded-full border border-white/20 flex items-center justify-center">
                            <div class="w-2 h-2 bg-white rounded-full"></div>
                        </div>
                        <div>
                            <p class="text-xs text-muted uppercase tracking-[0.2em] mb-1 font-bold">Founder</p>
                            <p class="text-2xl text-white font-medium">Hillary Ikhais</p>
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
                        <h1 class="huge-headline stagger-anim">The Problem</h1>
                        <h2 class="sub-headline stagger-anim text-white/90">Businesses have automated transactions.</h2>
                        <div class="glass-card p-10 stagger-anim mt-10">
                            <p class="text-2xl text-muted leading-relaxed mb-8 font-light">Over the last two decades, businesses have adopted software for almost every operational function:</p>
                            
                            <ul class="text-2xl text-white space-y-4 font-medium grid grid-cols-2">
                                <li class="flex items-center gap-4"><div class="w-2 h-2 rounded-full bg-white/40"></div>Payments.</li>
                                <li class="flex items-center gap-4"><div class="w-2 h-2 rounded-full bg-white/40"></div>CRM.</li>
                                <li class="flex items-center gap-4"><div class="w-2 h-2 rounded-full bg-white/40"></div>Inventory.</li>
                                <li class="flex items-center gap-4"><div class="w-2 h-2 rounded-full bg-white/40"></div>Marketing.</li>
                                <li class="flex items-center gap-4"><div class="w-2 h-2 rounded-full bg-white/40"></div>Accounting.</li>
                                <li class="flex items-center gap-4 text-white col-span-2 mt-4 pt-4 border-t border-white/10 text-3xl font-bold"><div class="w-3 h-3 rounded-full bg-white shadow-[0_0_15px_rgba(255,255,255,0.8)]"></div>Conversations</li>
                            </ul>
                        </div>
                    </div>
                    <div class="flex-1 flex flex-col justify-center pl-10 pt-8 border-l border-white/10">
                        <p class="text-4xl font-semibold text-white mb-10 stagger-anim leading-tight">Yet business owners still ask the same questions:</p>
                        
                        <ul class="text-2xl text-muted space-y-6 mb-16 stagger-anim font-light">
                            <li class="flex items-center gap-4"><div class="w-1.5 h-1.5 bg-white/20 rounded-full"></div>What deserves attention today?</li>
                            <li class="flex items-center gap-4"><div class="w-1.5 h-1.5 bg-white/20 rounded-full"></div>Which products should I restock?</li>
                            <li class="flex items-center gap-4"><div class="w-1.5 h-1.5 bg-white/20 rounded-full"></div>Which customers need follow-up?</li>
                            <li class="flex items-center gap-4"><div class="w-1.5 h-1.5 bg-white/20 rounded-full"></div>Where am I losing revenue?</li>
                            <li class="flex items-center gap-4"><div class="w-1.5 h-1.5 bg-white/20 rounded-full"></div>Why have sales reduced?</li>
                        </ul>
                        
                        <div class="stagger-anim glass-card p-8">
                            <p class="text-2xl text-white mb-2 font-semibold">Business software automates operations.</p>
                            <p class="text-2xl text-muted font-light">It records what happened.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 3 -->
        <div class="slide" id="slide3">
            <div class="w-full h-full flex flex-col justify-center max-w-5xl">
                <div class="glass-card inline-block px-6 py-2 mb-8 stagger-anim rounded-full w-max">
                    <p class="text-xs uppercase tracking-[0.4em] text-white/70 font-bold">02 / The Shift</p>
                </div>
                <h1 class="huge-headline stagger-anim">Commerce has moved into conversations.</h1>
                
                <div class="space-y-8 text-3xl text-muted leading-relaxed stagger-anim mt-8 font-light">
                    <p>Across Nigeria, businesses now operate inside messaging platforms.<br>
                    <span class="text-2xl mt-4 block text-muted/80">Customers now discover products, negotiate prices, confirm payments and arrange deliveries inside WhatsApp, Instagram and Facebook.</span></p>
                    
                    <div class="glass-card p-8 border-l-4 border-l-white">
                        <p class="text-white font-semibold text-3xl">For Nigerian MSMEs, the entire sales funnel now exists inside conversations.</p>
                    </div>
                    
                    <p>Yet traditional software was designed for structured forms, not unstructured conversations.</p>
                    <p>As conversational commerce grows, businesses generate thousands of customer signals every day.</p>
                    
                    <p class="text-white font-bold text-3xl pt-8 border-t border-white/10 uppercase tracking-wide">Most disappear without ever becoming business intelligence.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 4 -->
        <div class="slide" id="slide4">
            <div class="w-full h-full flex flex-col justify-center max-w-6xl">
                <h1 class="huge-headline stagger-anim">The Problem</h1>
                <h2 class="sub-headline stagger-anim">Every conversation creates decisions.</h2>
                <p class="text-3xl text-muted mb-12 stagger-anim font-light">A business owner doesn't just receive messages.<br>They constantly decide:</p>
                
                <div class="glass-card p-10 rounded-[3rem] stagger-anim mb-16">
                    <ul class="text-2xl text-white space-y-6 grid grid-cols-2 gap-x-12 font-medium">
                        <li class="flex items-center gap-4"><div class="w-2 h-2 bg-white/40 rounded-full"></div>Should this customer receive follow-up?</li>
                        <li class="flex items-center gap-4"><div class="w-2 h-2 bg-white/40 rounded-full"></div>Is demand increasing for this product?</li>
                        <li class="flex items-center gap-4"><div class="w-2 h-2 bg-white/40 rounded-full"></div>Should inventory be reordered?</li>
                        <li class="flex items-center gap-4"><div class="w-2 h-2 bg-white/40 rounded-full"></div>Are customers becoming more price-sensitive?</li>
                        <li class="flex items-center gap-4"><div class="w-2 h-2 bg-white/40 rounded-full"></div>Which complaints appear repeatedly?</li>
                        <li class="flex items-center gap-4"><div class="w-2 h-2 bg-white/40 rounded-full"></div>Which customers are likely to return?</li>
                    </ul>
                </div>
                
                <div class="stagger-anim border-l-2 border-white pl-8">
                    <p class="text-2xl text-muted mb-2 font-medium">These decisions are still made manually.</p>
                    <p class="text-4xl text-white font-bold">As conversations increase, decision complexity grows even faster.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 5 -->
        <div class="slide" id="slide5">
            <div class="w-full h-full flex flex-col justify-center">
                <h1 class="huge-headline stagger-anim">Morlen</h1>
                <h2 class="sub-headline stagger-anim">An Executive Decision Intelligence Platform.</h2>
                <div class="stagger-anim max-w-5xl mb-12 mt-4 glass-card p-8 rounded-[2rem]">
                    <p class="text-2xl text-muted mb-4 font-light">Morlen continuously analyzes customer conversations, identifies business patterns and delivers prioritized business decisions.</p>
                    <p class="text-3xl text-white font-bold">Instead of presenting plain dashboards, Morlen produces a daily executive briefing.</p>
                </div>
                
                <div class="grid grid-cols-4 gap-8 mb-12">
                    <div class="stagger-anim flex flex-col glass-card p-8 rounded-3xl">
                        <h3 class="text-2xl font-bold text-white mb-4">Executive Brief</h3>
                        <p class="text-base text-muted font-light">A daily summary of the highest priority decisions. inventory risks, customer churn, demand spikes, operational issues.</p>
                    </div>
                    <div class="stagger-anim flex flex-col glass-card p-8 rounded-3xl">
                        <h3 class="text-2xl font-bold text-white mb-4">Opportunity Feed</h3>
                        <p class="text-base text-muted font-light">Revenue opportunities detected from conversations including estimated impact, confidence score, supporting evidence.</p>
                    </div>
                    <div class="stagger-anim flex flex-col glass-card p-8 rounded-3xl">
                        <h3 class="text-2xl font-bold text-white mb-4">Business Memory</h3>
                        <p class="text-base text-muted mb-4 font-light">Long-term behavioural intelligence about customers.</p>
                        <div class="border border-white/20 rounded-full px-4 py-2 mt-auto w-max"><p class="text-xs text-white/70 uppercase tracking-widest font-bold">Ex: Demand rises</p></div>
                    </div>
                    <div class="stagger-anim flex flex-col glass-card p-8 rounded-3xl">
                        <h3 class="text-2xl font-bold text-white mb-4">Evidence-Based</h3>
                        <p class="text-base text-muted mb-4 font-light">Every recommendation explains:</p>
                        <ul class="text-sm text-platinum space-y-2 font-medium">
                            <li>• Why it exists</li>
                            <li>• Expected impact</li>
                            <li>• Supporting evidence</li>
                        </ul>
                    </div>
                </div>
                
                <div class="stagger-anim flex items-center gap-6 mt-2">
                    <p class="text-3xl text-muted font-light">Business owners stop searching for answers.</p>
                    <div class="w-12 h-px bg-white/20"></div>
                    <p class="text-3xl font-bold text-white">Morlen brings the answers to them.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 6 -->
        <div class="slide" id="slide6">
            <div class="w-full h-full flex flex-col justify-center items-center text-center">
                <div class="stagger-anim mb-12 glass-card px-8 py-3 rounded-full">
                    <p class="text-sm uppercase tracking-[0.3em] font-bold text-white/80">Market & Business Model</p>
                </div>
                <h1 class="huge-headline stagger-anim">A Massive Market</h1>
                
                <p class="text-3xl text-muted mb-10 stagger-anim font-light">Nigeria has approximately:</p>
                
                <div class="mb-16 stagger-anim relative glass-card p-16 rounded-[4rem]">
                    <p class="text-[140px] font-bold text-white leading-none tracking-tight drop-shadow-[0_0_20px_rgba(255,255,255,0.2)]">39.6 Million MSMEs</p>
                </div>
                
                <p class="text-xl text-muted mb-8 stagger-anim uppercase tracking-[0.3em] font-bold">Representing</p>
                <div class="flex gap-20 justify-center mb-16 stagger-anim text-5xl font-bold text-white">
                    <div class="flex flex-col items-center"><p>96%</p><p class="text-xl text-muted mt-4 font-medium uppercase tracking-widest">of businesses</p></div>
                    <div class="w-px h-20 bg-white/10"></div>
                    <div class="flex flex-col items-center"><p>87.9%</p><p class="text-xl text-muted mt-4 font-medium uppercase tracking-widest">of employment</p></div>
                    <div class="w-px h-20 bg-white/10"></div>
                    <div class="flex flex-col items-center"><p>46.3%</p><p class="text-xl text-muted mt-4 font-medium uppercase tracking-widest">of GDP</p></div>
                </div>
                
                <div class="stagger-anim glass-card p-8 rounded-full">
                    <p class="text-2xl font-light text-white">Millions already conduct business primarily through messaging platforms. <span class="font-bold ml-2">Morlen is built for this new operating environment.</span></p>
                </div>
            </div>
        </div>

        <!-- SLIDE 7 -->
        <div class="slide" id="slide7">
            <div class="w-full h-full flex flex-col justify-center">
                <h1 class="huge-headline stagger-anim">Business Model</h1>
                <div class="stagger-anim mb-10 glass-card inline-block px-6 py-2 rounded-full">
                    <h2 class="text-lg font-bold text-white uppercase tracking-[0.2em]">Subscription SaaS</h2>
                </div>
                <p class="text-2xl text-muted mb-12 max-w-5xl stagger-anim font-light">Starting with a 30 day free trial giving Morlen enough time to learn from customer conversations, build business memory, generate meaningful insights.</p>
                
                <div class="grid grid-cols-3 gap-8 mb-16 stagger-anim">
                    <div class="glass-card p-10 rounded-[2.5rem] flex flex-col">
                        <h3 class="text-4xl font-bold text-white mb-2">Starter</h3>
                        <p class="text-2xl text-white/60 font-mono mb-4">N8,000/mo</p>
                        <p class="text-base text-muted mb-8 font-light">For early stage businesses</p>
                        <ul class="text-white space-y-4 text-lg flex-1 border-t border-white/10 pt-8 font-light">
                            <li>• Executive brief</li>
                            <li>• Business memory</li>
                            <li>• Basic decision intelligence</li>
                            <li>• Single workspace</li>
                        </ul>
                    </div>
                    
                    <div class="glass-card p-10 rounded-[2.5rem] flex flex-col transform scale-[1.05] z-10 border-white/30" style="background: rgba(255,255,255,0.06); box-shadow: 0 40px 80px rgba(0,0,0,0.6);">
                        <div class="absolute -top-4 left-1/2 transform -translate-x-1/2 bg-white text-black px-6 py-1.5 rounded-full text-xs font-bold tracking-[0.2em] uppercase">Popular</div>
                        <h3 class="text-4xl font-bold text-white mb-2">Growth</h3>
                        <p class="text-2xl text-white font-bold mb-4 font-mono">N15,000/mo</p>
                        <p class="text-base text-white/90 mb-8 font-light">Businesses managing increasing customer conversations.</p>
                        <ul class="text-white space-y-4 text-lg flex-1 border-t border-white/20 pt-8 font-medium">
                            <li>• Everything in starter</li>
                            <li>• Opportunity feed</li>
                            <li>• Advanced AI recommendations</li>
                            <li>• Multi channel integrations</li>
                            <li>• Team Collaboration</li>
                        </ul>
                    </div>
                    
                    <div class="glass-card p-10 rounded-[2.5rem] flex flex-col">
                        <h3 class="text-4xl font-bold text-white mb-2">Enterprise</h3>
                        <p class="text-2xl text-white/60 font-mono mb-4">CUSTOM</p>
                        <p class="text-base text-muted mb-8 font-light">Organizations requiring company-wide decision intelligence.</p>
                        <ul class="text-white space-y-4 text-lg flex-1 border-t border-white/10 pt-8 font-light">
                            <li>• Everything in growth</li>
                            <li>• Custom AI deployment</li>
                            <li>• Dedicated Support</li>
                            <li>• Enterprise security and governance</li>
                        </ul>
                    </div>
                </div>
                
                <p class="text-xl text-muted stagger-anim glass-card inline-block px-8 py-4 rounded-full font-light">
                    Additional revenue: <span class="text-white font-bold ml-2">Enterprise Implementation & Onboarding</span>
                </p>
            </div>
        </div>

        <!-- SLIDE 8 -->
        <div class="slide" id="slide8">
            <div class="w-full h-full flex flex-col justify-center">
                <div class="flex gap-20">
                    <div class="flex-1">
                        <h1 class="huge-headline stagger-anim">Funding</h1>
                        <h2 class="text-4xl font-semibold text-white mb-10 stagger-anim">Raising Pre-Seed Capital</h2>
                        <p class="text-xl text-muted mb-10 stagger-anim font-light uppercase tracking-widest">Investment will accelerate:</p>
                        
                        <div class="space-y-6 stagger-anim glass-card p-10 rounded-[3rem]">
                            <div class="flex items-center gap-6">
                                <h3 class="text-4xl font-bold text-white w-24">40%</h3>
                                <div>
                                    <p class="text-lg font-bold text-white mb-1">Product Development</p>
                                    <p class="text-sm text-muted font-light">Complete commercial MVP and core intelligence engine.</p>
                                </div>
                            </div>
                            <div class="w-full h-px bg-white/10"></div>
                            <div class="flex items-center gap-6">
                                <h3 class="text-4xl font-bold text-white/80 w-24">25%</h3>
                                <div>
                                    <p class="text-lg font-bold text-white mb-1">AI Infrastructure</p>
                                    <p class="text-sm text-muted font-light">Inference, data pipelines and production infrastructure.</p>
                                </div>
                            </div>
                            <div class="w-full h-px bg-white/10"></div>
                            <div class="flex items-center gap-6">
                                <h3 class="text-4xl font-bold text-white/60 w-24">20%</h3>
                                <div>
                                    <p class="text-lg font-bold text-white mb-1">Customer Acq.</p>
                                    <p class="text-sm text-muted font-light">Pilot programs and early customer onboarding.</p>
                                </div>
                            </div>
                            <div class="w-full h-px bg-white/10"></div>
                            <div class="flex items-center gap-6">
                                <h3 class="text-4xl font-bold text-white/40 w-24">15%</h3>
                                <div>
                                    <p class="text-lg font-bold text-white mb-1">Operations</p>
                                    <p class="text-sm text-muted font-light">Messaging integrations and business development.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="flex-1 flex flex-col justify-center pt-8 border-l border-white/10 pl-20 relative">
                        <h1 class="huge-headline stagger-anim">Outcomes</h1>
                        <h2 class="text-4xl font-semibold text-white mb-12 stagger-anim">Expected Milestones</h2>
                        
                        <div class="space-y-6 stagger-anim mt-10">
                            <div class="flex items-center gap-8 glass-card p-6 px-8 rounded-full">
                                <div class="w-3 h-3 rounded-full bg-white shadow-[0_0_10px_white]"></div>
                                <p class="text-2xl text-white font-medium">Commercial MVP</p>
                            </div>
                            <div class="flex items-center gap-8 glass-card p-6 px-8 rounded-full">
                                <div class="w-3 h-3 rounded-full bg-white shadow-[0_0_10px_white]"></div>
                                <p class="text-2xl text-white font-medium">First paying customers</p>
                            </div>
                            <div class="flex items-center gap-8 glass-card p-6 px-8 rounded-full">
                                <div class="w-3 h-3 rounded-full bg-white shadow-[0_0_10px_white]"></div>
                                <p class="text-2xl text-white font-medium">Validated product-market fit</p>
                            </div>
                            <div class="flex items-center gap-8 glass-card p-6 px-8 rounded-full">
                                <div class="w-3 h-3 rounded-full bg-white shadow-[0_0_10px_white]"></div>
                                <p class="text-2xl text-white font-medium">Foundation for national expansion</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 9 -->
        <div class="slide" id="slide9">
            <div class="w-full h-full flex flex-col justify-center">
                <h1 class="huge-headline stagger-anim">Why Morlen?</h1>
                
                <div class="flex gap-16 mt-10">
                    <div class="flex-1 stagger-anim flex flex-col justify-center border-l-2 border-l-white/20 pl-12 relative">
                        <p class="text-2xl text-muted mb-6 font-light uppercase tracking-widest">Software answers:</p>
                        <h2 class="text-[72px] font-bold text-white leading-none mb-12">"What happened?"</h2>
                        
                        <ul class="text-2xl text-muted space-y-6 font-light">
                            <li class="flex items-center gap-4"><div class="w-2 h-2 bg-white/30 rounded-full"></div>CRM stores customer records</li>
                            <li class="flex items-center gap-4"><div class="w-2 h-2 bg-white/30 rounded-full"></div>ERP manages operations</li>
                            <li class="flex items-center gap-4"><div class="w-2 h-2 bg-white/30 rounded-full"></div>BI dashboards visualize historical metrics</li>
                            <li class="flex items-center gap-4"><div class="w-2 h-2 bg-white/30 rounded-full"></div>Chatbots automate conversations</li>
                        </ul>
                    </div>
                    
                    <div class="flex-1 glass-card p-16 rounded-[3rem] stagger-anim flex flex-col justify-center relative">
                        <p class="text-2xl text-white mb-6 font-bold uppercase tracking-widest">Morlen answers:</p>
                        <h2 class="text-[72px] font-bold text-white leading-none mb-12 drop-shadow-2xl">"What should I do next?"</h2>
                        
                        <ul class="text-2xl text-white space-y-6 font-medium">
                            <li class="flex items-center gap-4"><div class="w-2 h-2 bg-white rounded-full shadow-[0_0_10px_white]"></div>Every conversation contains intelligence.</li>
                            <li class="flex items-center gap-4"><div class="w-2 h-2 bg-white rounded-full shadow-[0_0_10px_white]"></div>Every business generates opportunities.</li>
                            <li class="flex items-center gap-4"><div class="w-2 h-2 bg-white rounded-full shadow-[0_0_10px_white]"></div>Every owner has limited attention.</li>
                        </ul>
                        
                        <div class="mt-12 pt-10 border-t border-white/20">
                            <p class="text-3xl text-white leading-relaxed font-semibold">Morlen exists to protect that attention—<br><span class="text-white/70 font-light">by turning conversations into decisions.</span></p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 10 -->
        <div class="slide" id="slide10">
            <div class="w-full h-full flex flex-col justify-center items-center text-center">
                <div class="stagger-anim mb-16 glass-card px-8 py-4 rounded-full">
                    <p class="text-2xl font-light text-white uppercase tracking-[0.2em]">The future of business isn't more software.</p>
                </div>

                <h1 class="text-[250px] font-bold text-white leading-none tracking-tighter mb-16 stagger-anim drop-shadow-[0_0_50px_rgba(255,255,255,0.1)]">MORLEN</h1>
                
                <div class="stagger-anim mt-10 glass-card p-12 rounded-[3rem]">
                    <p class="text-3xl text-white mb-6 font-light">Businesses already have the conversations.</p>
                    <p class="text-4xl text-white font-bold tracking-widest uppercase">Morlen turns them into decisions.</p>
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
                    opacity: 0, scale: 0.95,
                    duration: 0.6,
                    ease: "power2.inOut",
                    onComplete: () => {
                        current.classList.remove('active');
                        current.style.visibility = 'hidden';
                        gsap.set(current, { scale: 1 }); 
                    }
                });
            }

            next.classList.add('active');
            next.style.visibility = 'visible';
            
            const fadeElements = next.querySelectorAll('.stagger-anim');
            gsap.set(fadeElements, { opacity: 0, y: 40 });

            const tl = gsap.timeline({
                onComplete: () => {
                    currentSlide = index;
                    isAnimating = false;
                }
            });
            
            tl.to(next, { opacity: 1, duration: 0.2 })
              .to(fadeElements, {
                  opacity: 1, y: 0, duration: 1.2,
                  stagger: 0.1, ease: "power3.out"
              }, "-=0.1");
        }

        slides[0].classList.add('active');
        slides[0].style.visibility = 'visible';
        slides[0].style.opacity = 1;
        
        gsap.set(slides[0].querySelectorAll('.stagger-anim'), { opacity: 0, y: 40 });
        
        setTimeout(() => {
            gsap.to(slides[0].querySelectorAll('.stagger-anim'), {
                opacity: 1, y: 0, duration: 1.2,
                stagger: 0.1, ease: "power3.out"
            });
        }, 100);
        
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

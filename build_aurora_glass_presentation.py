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
    <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        display: ['Instrument Serif', 'serif'],
                        body: ['Inter', 'sans-serif'],
                    }
                }
            }
        }
    </script>

    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            background-color: #0A0A0C;
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
            background: #0A0A0C;
            overflow: hidden;
        }

        /* 
         * VIBRANT FLUID AURORA BACKGROUND 
         * This solves the "bleak and sad" issue entirely, without relying on AI slop.
         */
        .aurora-bg {
            position: absolute;
            top: -50%; left: -50%; width: 200%; height: 200%;
            background: 
                radial-gradient(circle at 30% 30%, rgba(0, 240, 255, 0.4) 0%, transparent 60%),
                radial-gradient(circle at 70% 70%, rgba(255, 0, 127, 0.3) 0%, transparent 50%),
                radial-gradient(circle at 50% 80%, rgba(0, 180, 255, 0.25) 0%, transparent 60%);
            z-index: 0;
            filter: blur(100px);
            animation: flow-aurora 25s ease-in-out infinite alternate;
            opacity: 0.8;
        }

        @keyframes flow-aurora {
            0% { transform: rotate(0deg) scale(1) translate(0, 0); }
            33% { transform: rotate(5deg) scale(1.1) translate(-50px, 100px); }
            66% { transform: rotate(-5deg) scale(0.9) translate(100px, -50px); }
            100% { transform: rotate(10deg) scale(1.2) translate(50px, 50px); }
        }

        /* 
         * CARDLESS GLASSMORPHISM (ARCHITECTURAL GLASS BANDS)
         * Solves the legibility issue without boxing content into "cards".
         */
        
        /* Edge-to-Edge Glass Band */
        .glass-band-full {
            position: absolute;
            bottom: 0; left: 0; width: 100%; height: 60%;
            background: linear-gradient(180deg, rgba(10,10,12,0.1) 0%, rgba(10,10,12,0.7) 100%);
            backdrop-filter: blur(50px);
            -webkit-backdrop-filter: blur(50px);
            border-top: 1px solid rgba(255,255,255,0.15);
            z-index: 5;
        }

        /* Diagonal Glass Split */
        .glass-band-diagonal {
            position: absolute;
            top: -20%; right: -10%; width: 60%; height: 140%;
            background: rgba(10,10,12,0.4);
            backdrop-filter: blur(60px);
            -webkit-backdrop-filter: blur(60px);
            border-left: 1px solid rgba(255,255,255,0.15);
            transform: rotate(-15deg);
            z-index: 5;
        }

        /* Horizontal Center Glass Band */
        .glass-band-center {
            position: absolute;
            top: 30%; left: 0; width: 100%; height: 40%;
            background: rgba(10,10,12,0.5);
            backdrop-filter: blur(40px);
            -webkit-backdrop-filter: blur(40px);
            border-top: 1px solid rgba(255,255,255,0.1);
            border-bottom: 1px solid rgba(255,255,255,0.1);
            z-index: 5;
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
        
        /* Editorial Typography */
        .huge-headline {
            font-family: 'Instrument Serif', serif;
            font-size: 140px;
            font-weight: 400;
            line-height: 1.0;
            color: #FFFFFF;
            margin-bottom: 30px;
            letter-spacing: -0.02em;
        }
        
        .huge-italic { font-style: italic; color: #FFFFFF; }
        
        .sub-headline {
            font-size: 40px;
            font-weight: 300;
            color: rgba(255,255,255,0.9);
            margin-bottom: 24px;
            line-height: 1.3;
        }

        .content-layer { position: relative; z-index: 15; width: 100%; height: 100%; }

    </style>
</head>
<body>

    <div id="presentation-container">
        <!-- Vibrant Ethereal Aurora -->
        <div class="aurora-bg"></div>

        <!-- SLIDE 1: Full Bottom Glass Band -->
        <div class="slide" id="slide1">
            <div class="glass-band-full" style="height: 55%;"></div>
            
            <div class="content-layer flex flex-col justify-between">
                <div class="stagger-anim mt-10">
                    <h1 class="huge-headline" style="font-size: 160px;">Morlen.</h1>
                </div>
                
                <div class="max-w-4xl mb-10">
                    <p class="text-sm uppercase tracking-[0.4em] text-white/50 font-bold mb-8 stagger-anim">Executive Pitch</p>
                    <p class="sub-headline stagger-anim font-medium text-white">The Operating System for Business Decisions.</p>
                    <p class="text-3xl text-white/70 font-light mb-16 stagger-anim">Turning customer conversations into executive decisions.</p>
                    
                    <div class="stagger-anim flex items-center gap-8 pt-10 border-t border-white/20">
                        <div class="w-2 h-2 bg-cyan-400 rounded-full shadow-[0_0_15px_rgba(0,240,255,0.8)]"></div>
                        <div>
                            <p class="text-xs text-white/60 uppercase tracking-[0.3em] mb-1 font-bold">Founder</p>
                            <p class="text-3xl text-white font-display italic tracking-wide">Hillary Ikhais</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 2: Diagonal Right Glass Panel -->
        <div class="slide" id="slide2">
            <div class="glass-band-diagonal"></div>
            
            <div class="content-layer flex gap-20">
                <div class="flex-1 pr-10">
                    <h1 class="huge-headline stagger-anim" style="font-size: 110px;">The Problem.</h1>
                    <h2 class="sub-headline stagger-anim text-white">Businesses have <span class="huge-italic">automated</span> transactions.</h2>
                    
                    <div class="stagger-anim mt-16">
                        <p class="text-2xl text-white/70 leading-relaxed mb-10 font-light">Over the last two decades, businesses have adopted software for almost every operational function:</p>
                        
                        <ul class="text-3xl text-white space-y-6 font-medium">
                            <li class="flex items-center gap-6"><div class="w-1.5 h-1.5 bg-white/40"></div> Payments</li>
                            <li class="flex items-center gap-6"><div class="w-1.5 h-1.5 bg-white/40"></div> CRM</li>
                            <li class="flex items-center gap-6"><div class="w-1.5 h-1.5 bg-white/40"></div> Inventory</li>
                            <li class="flex items-center gap-6"><div class="w-1.5 h-1.5 bg-white/40"></div> Marketing</li>
                            <li class="flex items-center gap-6"><div class="w-1.5 h-1.5 bg-white/40"></div> Accounting</li>
                            <li class="flex items-center gap-6 mt-8 pt-8 border-t border-white/20 text-5xl font-display italic text-white"><div class="w-2 h-2 bg-pink-500 shadow-[0_0_15px_rgba(255,0,127,0.8)]"></div> Conversations</li>
                        </ul>
                    </div>
                </div>
                
                <div class="flex-1 flex flex-col justify-center pl-24">
                    <p class="text-4xl font-light text-white mb-16 stagger-anim leading-tight">Yet business owners still ask the same questions:</p>
                    
                    <ul class="text-3xl text-white/80 space-y-10 mb-20 stagger-anim font-light">
                        <li>What deserves attention today?</li>
                        <li>Which products should I restock?</li>
                        <li>Which customers need follow-up?</li>
                        <li>Where am I losing revenue?</li>
                        <li>Why have sales reduced?</li>
                    </ul>
                    
                    <div class="stagger-anim border-l border-white/30 pl-8">
                        <p class="text-2xl text-white mb-2 font-medium">Business software automates operations.</p>
                        <p class="text-2xl text-white/60 font-light font-display italic">It records what happened.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 3: Center Horizontal Glass Band -->
        <div class="slide" id="slide3">
            <div class="glass-band-center" style="top: 25%; height: 50%;"></div>
            
            <div class="content-layer flex flex-col justify-center items-center text-center">
                <p class="text-sm uppercase tracking-[0.4em] text-white/50 font-bold mb-12 stagger-anim">The Shift</p>
                <h1 class="huge-headline stagger-anim" style="font-size: 130px;">Commerce has moved<br>into <span class="huge-italic">conversations.</span></h1>
                
                <div class="max-w-5xl mt-12 stagger-anim text-2xl text-white/80 font-light leading-relaxed">
                    <p class="mb-10">Across Nigeria, businesses now operate inside messaging platforms. Customers now discover products, negotiate prices, confirm payments and arrange deliveries inside WhatsApp, Instagram and Facebook.</p>
                    
                    <p class="text-4xl font-display italic text-white leading-snug mb-10">For Nigerian MSMEs, the entire sales funnel now exists inside conversations.</p>
                    
                    <p class="mb-10">Yet traditional software was designed for structured forms, not unstructured conversations. As conversational commerce grows, businesses generate thousands of customer signals every day.</p>
                    
                    <p class="text-3xl font-medium text-white">Most disappear without ever becoming business intelligence.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 4: Full Bottom Glass Band -->
        <div class="slide" id="slide4">
            <div class="glass-band-full" style="height: 65%;"></div>
            
            <div class="content-layer">
                <div class="stagger-anim mb-16 mt-8">
                    <h1 class="huge-headline mb-4">The Problem.</h1>
                    <h2 class="sub-headline text-white/80">Every conversation creates decisions.</h2>
                </div>
                
                <p class="text-3xl text-white/70 mb-16 stagger-anim font-light">A business owner doesn't just receive messages. They constantly decide:</p>
                
                <ul class="text-3xl text-white space-y-10 stagger-anim font-display italic grid grid-cols-2 gap-x-20">
                    <li class="flex items-center gap-6"><div class="w-1.5 h-1.5 bg-white/40"></div>Should this customer receive follow-up?</li>
                    <li class="flex items-center gap-6"><div class="w-1.5 h-1.5 bg-white/40"></div>Is demand increasing for this product?</li>
                    <li class="flex items-center gap-6"><div class="w-1.5 h-1.5 bg-white/40"></div>Should inventory be reordered?</li>
                    <li class="flex items-center gap-6"><div class="w-1.5 h-1.5 bg-white/40"></div>Are customers becoming more price-sensitive?</li>
                    <li class="flex items-center gap-6"><div class="w-1.5 h-1.5 bg-white/40"></div>Which complaints appear repeatedly?</li>
                    <li class="flex items-center gap-6"><div class="w-1.5 h-1.5 bg-white/40"></div>Which customers are likely to return?</li>
                </ul>
                
                <div class="stagger-anim mt-20 pt-10 border-t border-white/20 flex gap-20 items-end">
                    <p class="text-2xl text-white/70 font-light flex-1">These decisions are still made manually.</p>
                    <p class="text-4xl text-white font-medium flex-2 leading-tight">As conversations increase, decision complexity grows even faster.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 5: Full Right Split Glass Band -->
        <div class="slide" id="slide5">
            <div class="absolute top-0 right-0 w-[55%] height-[100%] h-full bg-black/40 backdrop-blur-[50px] border-l border-white/10 z-0"></div>
            
            <div class="content-layer flex">
                <div class="w-[45%] pr-16 flex flex-col justify-center">
                    <h1 class="huge-headline stagger-anim">Morlen.</h1>
                    <h2 class="text-4xl font-light text-white/80 stagger-anim leading-snug">An Executive <span class="huge-italic text-white">Decision Intelligence</span> Platform.</h2>
                    
                    <div class="stagger-anim mt-16 pt-12 border-t border-white/20">
                        <p class="text-2xl text-white/70 mb-8 font-light">Morlen continuously analyzes customer conversations, identifies business patterns and delivers prioritized business decisions.</p>
                        <p class="text-4xl text-white font-display italic">Instead of presenting plain dashboards, Morlen produces a daily executive briefing.</p>
                    </div>
                </div>
                
                <div class="w-[55%] pl-20 py-10 flex flex-col justify-center">
                    <div class="grid grid-cols-2 gap-x-12 gap-y-20">
                        <div class="stagger-anim">
                            <h3 class="text-3xl font-display italic text-white mb-4">Executive Brief</h3>
                            <p class="text-xl text-white/70 font-light leading-relaxed">A daily summary of the highest priority decisions. inventory risks, customer churn, demand spikes.</p>
                        </div>
                        <div class="stagger-anim">
                            <h3 class="text-3xl font-display italic text-white mb-4">Opportunity Feed</h3>
                            <p class="text-xl text-white/70 font-light leading-relaxed">Revenue opportunities detected from conversations including estimated impact, confidence score.</p>
                        </div>
                        <div class="stagger-anim">
                            <h3 class="text-3xl font-display italic text-white mb-4">Business Memory</h3>
                            <p class="text-xl text-white/70 font-light leading-relaxed mb-4">Long-term behavioural intelligence about customers.</p>
                            <p class="text-xs text-white/50 uppercase tracking-widest font-bold">Ex: Demand rises</p>
                        </div>
                        <div class="stagger-anim">
                            <h3 class="text-3xl font-display italic text-white mb-4">Evidence-Based</h3>
                            <p class="text-xl text-white/70 font-light leading-relaxed mb-4">Every recommendation explains:</p>
                            <ul class="text-base text-white space-y-2 font-light">
                                <li>• Why it exists</li>
                                <li>• Expected impact</li>
                                <li>• Supporting evidence</li>
                            </ul>
                        </div>
                    </div>
                    
                    <div class="stagger-anim flex items-center gap-8 mt-20 pt-10 border-t border-white/20">
                        <p class="text-2xl text-white/60 font-light">Business owners stop searching for answers.</p>
                        <p class="text-3xl font-display italic text-white">Morlen brings the answers to them.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 6: Center Horizontal Glass Band -->
        <div class="slide" id="slide6">
            <div class="glass-band-center" style="top: 30%; height: 40%;"></div>
            
            <div class="content-layer flex flex-col justify-center items-center text-center">
                <p class="text-sm uppercase tracking-[0.4em] font-bold text-white/50 mb-10 stagger-anim">Market & Business Model</p>
                <h1 class="huge-headline stagger-anim mb-16">A Massive <span class="huge-italic">Market.</span></h1>
                
                <div class="flex gap-16 items-center stagger-anim mt-4">
                    <p class="text-3xl text-white/80 font-light">Nigeria has approximately</p>
                    <div class="w-px h-16 bg-white/20"></div>
                    <p class="text-[100px] font-display italic text-white leading-none tracking-tight">39.6M <span class="text-4xl font-sans not-italic text-white/60 font-light tracking-normal">MSMEs</span></p>
                </div>
                    
                <div class="flex gap-20 items-center mt-20 stagger-anim pt-12 border-t border-white/10">
                    <p class="text-xl text-white/50 uppercase tracking-[0.3em] font-bold">Representing</p>
                    <div class="flex items-center gap-6">
                        <p class="text-6xl font-display italic text-white">96%</p>
                        <p class="text-xl text-white/70 font-light">of businesses</p>
                    </div>
                    <div class="flex items-center gap-6">
                        <p class="text-6xl font-display italic text-white">87.9%</p>
                        <p class="text-xl text-white/70 font-light">of employment</p>
                    </div>
                    <div class="flex items-center gap-6">
                        <p class="text-6xl font-display italic text-white">46.3%</p>
                        <p class="text-xl text-white/70 font-light">of GDP</p>
                    </div>
                </div>
                
                <div class="stagger-anim mt-20">
                    <p class="text-3xl font-light text-white/80">Millions already conduct business primarily through messaging platforms.<br><span class="text-white font-medium">Morlen is built for this new operating environment.</span></p>
                </div>
            </div>
        </div>

        <!-- SLIDE 7: Full Bottom Glass Band -->
        <div class="slide" id="slide7">
            <div class="glass-band-full" style="height: 60%;"></div>
            
            <div class="content-layer">
                <div class="flex items-end justify-between mb-20 stagger-anim mt-10">
                    <h1 class="huge-headline mb-0" style="font-size: 110px;">Business <span class="huge-italic">Model.</span></h1>
                    <p class="text-xl text-white/70 max-w-2xl font-light leading-relaxed text-right pb-4">Starting with a 30-day free trial giving Morlen enough time to learn from customer conversations, build business memory, and generate meaningful insights.</p>
                </div>
                
                <div class="flex gap-20 stagger-anim relative z-10 pt-10">
                    <div class="flex-1">
                        <h3 class="text-5xl font-display italic text-white mb-4">Starter</h3>
                        <p class="text-2xl text-white/60 font-light mb-8">N8,000/mo</p>
                        <p class="text-base text-white/80 mb-10 font-light h-12">For early stage businesses</p>
                        <ul class="text-white space-y-4 text-xl font-light border-t border-white/20 pt-8">
                            <li>Executive brief</li>
                            <li>Business memory</li>
                            <li>Basic decision intelligence</li>
                            <li>Single workspace</li>
                        </ul>
                    </div>
                    
                    <div class="flex-1">
                        <div class="flex items-center gap-4 mb-4">
                            <h3 class="text-5xl font-display italic text-white">Growth</h3>
                            <span class="bg-cyan-400 text-black px-3 py-1 text-xs font-bold uppercase tracking-widest rounded-sm">Popular</span>
                        </div>
                        <p class="text-2xl text-white font-medium mb-8">N15,000/mo</p>
                        <p class="text-base text-white/90 mb-10 font-light h-12">Businesses managing increasing customer conversations.</p>
                        <ul class="text-white space-y-4 text-xl font-medium border-t border-white/40 pt-8">
                            <li>Everything in starter</li>
                            <li>Opportunity feed</li>
                            <li>Advanced AI recommendations</li>
                            <li>Multi channel integrations</li>
                            <li>Team Collaboration</li>
                        </ul>
                    </div>
                    
                    <div class="flex-1">
                        <h3 class="text-5xl font-display italic text-white mb-4">Enterprise</h3>
                        <p class="text-2xl text-white/60 font-light mb-8">CUSTOM</p>
                        <p class="text-base text-white/80 mb-10 font-light h-12">Organizations requiring company-wide decision intelligence.</p>
                        <ul class="text-white space-y-4 text-xl font-light border-t border-white/20 pt-8">
                            <li>Everything in growth</li>
                            <li>Custom AI deployment</li>
                            <li>Dedicated Support</li>
                            <li>Enterprise security</li>
                        </ul>
                    </div>
                </div>
                
                <p class="text-xl text-white/60 stagger-anim font-light mt-16 pt-8 border-t border-white/10">
                    Additional revenue: <span class="text-white font-medium ml-4">Enterprise Implementation & Onboarding</span>
                </p>
            </div>
        </div>

        <!-- SLIDE 8: Diagonal Left Glass Panel -->
        <div class="slide" id="slide8">
            <div class="glass-band-diagonal" style="left: -10%; right: auto; border-left: none; border-right: 1px solid rgba(255,255,255,0.15);"></div>
            
            <div class="content-layer flex gap-20">
                <div class="flex-1 pr-16 pt-10">
                    <h1 class="huge-headline stagger-anim" style="font-size: 110px;">Funding.</h1>
                    <h2 class="text-4xl font-light text-white mb-12 stagger-anim">Raising Pre-Seed Capital</h2>
                    <p class="text-sm text-white/60 mb-12 stagger-anim uppercase tracking-widest font-bold">Investment will accelerate:</p>
                    
                    <div class="space-y-12 stagger-anim pt-8 border-t border-white/20">
                        <div class="flex items-center gap-10">
                            <h3 class="text-5xl font-display italic text-white w-24">40%</h3>
                            <div>
                                <p class="text-2xl font-medium text-white mb-2">Product Development</p>
                                <p class="text-lg text-white/70 font-light">Complete commercial MVP and core intelligence engine.</p>
                            </div>
                        </div>
                        <div class="flex items-center gap-10">
                            <h3 class="text-5xl font-display italic text-white/80 w-24">25%</h3>
                            <div>
                                <p class="text-2xl font-medium text-white mb-2">AI Infrastructure</p>
                                <p class="text-lg text-white/70 font-light">Inference, data pipelines and production infrastructure.</p>
                            </div>
                        </div>
                        <div class="flex items-center gap-10">
                            <h3 class="text-5xl font-display italic text-white/60 w-24">20%</h3>
                            <div>
                                <p class="text-2xl font-medium text-white mb-2">Customer Acq.</p>
                                <p class="text-lg text-white/70 font-light">Pilot programs and early customer onboarding.</p>
                            </div>
                        </div>
                        <div class="flex items-center gap-10">
                            <h3 class="text-5xl font-display italic text-white/40 w-24">15%</h3>
                            <div>
                                <p class="text-2xl font-medium text-white mb-2">Operations</p>
                                <p class="text-lg text-white/70 font-light">Messaging integrations and business development.</p>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="flex-1 flex flex-col justify-center pl-20">
                    <h1 class="huge-headline stagger-anim" style="font-size: 110px;">Outcomes.</h1>
                    <h2 class="text-4xl font-display italic text-white mb-16 stagger-anim">Expected Milestones</h2>
                    
                    <div class="space-y-12 stagger-anim">
                        <div class="flex items-center gap-8">
                            <div class="w-3 h-3 bg-white shadow-[0_0_10px_white]"></div>
                            <p class="text-3xl text-white font-light">Commercial MVP</p>
                        </div>
                        <div class="flex items-center gap-8">
                            <div class="w-3 h-3 bg-white shadow-[0_0_10px_white]"></div>
                            <p class="text-3xl text-white font-light">First paying customers</p>
                        </div>
                        <div class="flex items-center gap-8">
                            <div class="w-3 h-3 bg-white shadow-[0_0_10px_white]"></div>
                            <p class="text-3xl text-white font-light">Validated product-market fit</p>
                        </div>
                        <div class="flex items-center gap-8">
                            <div class="w-3 h-3 bg-white shadow-[0_0_10px_white]"></div>
                            <p class="text-3xl text-white font-light">Foundation for national expansion</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 9: Split Screen Glass -->
        <div class="slide" id="slide9">
            <div class="absolute top-0 right-0 w-[50%] h-[100%] bg-black/40 backdrop-blur-[50px] border-l border-white/10 z-0"></div>
            
            <div class="content-layer flex h-full">
                <div class="w-[50%] pr-20 flex flex-col justify-center">
                    <h1 class="huge-headline stagger-anim mb-16" style="font-size: 110px;">Why Morlen?</h1>
                    <p class="text-xl text-white/60 mb-8 font-bold uppercase tracking-widest stagger-anim">Software answers:</p>
                    <h2 class="text-[90px] font-display italic text-white leading-none mb-16 stagger-anim">"What happened?"</h2>
                    
                    <ul class="text-3xl text-white/80 space-y-8 font-light stagger-anim border-t border-white/20 pt-10">
                        <li>CRM stores customer records</li>
                        <li>ERP manages operations</li>
                        <li>BI visualizes historical metrics</li>
                        <li>Chatbots automate conversations</li>
                    </ul>
                </div>
                
                <div class="w-[50%] pl-20 flex flex-col justify-center">
                    <p class="text-xl text-white mb-8 font-bold uppercase tracking-widest stagger-anim">Morlen answers:</p>
                    <h2 class="text-[90px] font-display italic text-white leading-none mb-16 stagger-anim">"What should I do next?"</h2>
                    
                    <ul class="text-3xl text-white space-y-8 font-medium stagger-anim">
                        <li class="flex items-center gap-6"><div class="w-2 h-2 bg-white shadow-[0_0_10px_white]"></div>Every conversation contains intelligence.</li>
                        <li class="flex items-center gap-6"><div class="w-2 h-2 bg-white shadow-[0_0_10px_white]"></div>Every business generates opportunities.</li>
                        <li class="flex items-center gap-6"><div class="w-2 h-2 bg-white shadow-[0_0_10px_white]"></div>Every owner has limited attention.</li>
                    </ul>
                    
                    <div class="stagger-anim mt-16 pt-12 border-t border-white/20">
                        <p class="text-4xl text-white leading-relaxed font-light">Morlen exists to protect that attention—<br><span class="font-display italic text-white/80">by turning conversations into decisions.</span></p>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 10: Full Screen Ambient Aurora -->
        <div class="slide" id="slide10">
            <!-- No glass panels here, letting the pure Aurora shine for the final punchline -->
            <div class="content-layer flex flex-col justify-center items-center text-center">
                <p class="text-xl font-bold text-white/80 uppercase tracking-[0.4em] mb-16 stagger-anim">The future of business isn't more software.</p>

                <h1 class="text-[350px] font-display italic text-white leading-none tracking-tighter mb-16 stagger-anim drop-shadow-[0_0_40px_rgba(255,255,255,0.2)]">Morlen.</h1>
                
                <div class="stagger-anim">
                    <p class="text-3xl text-white/80 mb-6 font-light">Businesses already have the conversations.</p>
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
                    opacity: 0, scale: 1.02,
                    duration: 0.8,
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
            gsap.set(fadeElements, { opacity: 0, y: 30 });

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
        
        gsap.set(slides[0].querySelectorAll('.stagger-anim'), { opacity: 0, y: 30 });
        
        setTimeout(() => {
            gsap.to(slides[0].querySelectorAll('.stagger-anim'), {
                opacity: 1, y: 0, duration: 1.2,
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

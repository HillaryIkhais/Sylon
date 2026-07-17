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
    <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        display: ['Instrument Serif', 'serif'],
                        body: ['Inter', 'sans-serif'],
                    },
                    colors: {
                        background: '#010409', // Deep navy/black
                        foreground: '#FFFFFF',
                        muted: {
                            DEFAULT: '#161B22',
                            foreground: '#8B949E'
                        }
                    }
                }
            }
        }
    </script>

    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            background-color: #010409;
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
            background: #010409;
            overflow: hidden;
        }

        /* 
         * EXACT USER-PROVIDED LIQUID GLASS EFFECT
         */
        .liquid-glass {
            background: rgba(255, 255, 255, 0.01);
            background-blend-mode: luminosity;
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            border: none;
            box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.1);
            position: relative;
            overflow: hidden;
        }
        
        .liquid-glass::before {
            content: '';
            position: absolute;
            inset: 0;
            border-radius: inherit;
            padding: 1.4px;
            background: linear-gradient(180deg,
                rgba(255,255,255,0.45) 0%, rgba(255,255,255,0.15) 20%,
                rgba(255,255,255,0) 40%, rgba(255,255,255,0) 60%,
                rgba(255,255,255,0.15) 80%, rgba(255,255,255,0.45) 100%);
            -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
            -webkit-mask-composite: xor;
            mask-composite: exclude;
            pointer-events: none;
        }
        
        /* Strong variant for high-blur panels */
        .liquid-glass-strong {
            background: rgba(255, 255, 255, 0.03);
            background-blend-mode: luminosity;
            backdrop-filter: blur(40px);
            -webkit-backdrop-filter: blur(40px);
            border: none;
            box-shadow: 0 20px 40px rgba(0,0,0,0.4), inset 0 1px 1px rgba(255, 255, 255, 0.15);
            position: relative;
            overflow: hidden;
        }
        
        .liquid-glass-strong::before {
            content: '';
            position: absolute;
            inset: 0;
            border-radius: inherit;
            padding: 1.4px;
            background: linear-gradient(180deg,
                rgba(255,255,255,0.6) 0%, rgba(255,255,255,0.2) 20%,
                rgba(255,255,255,0.05) 40%, rgba(255,255,255,0.05) 60%,
                rgba(255,255,255,0.2) 80%, rgba(255,255,255,0.6) 100%);
            -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
            -webkit-mask-composite: xor;
            mask-composite: exclude;
            pointer-events: none;
        }

        /* 
         * EXACT USER-PROVIDED ANIMATIONS
         */
        @keyframes fade-rise {
            from { opacity: 0; transform: translateY(24px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        /* Instead of raw CSS classes, we'll use GSAP for slide transitions, 
           but the visual feeling is identical to fade-rise */

        .slide {
            position: absolute; top: 0; left: 0;
            width: 100%; height: 100%;
            opacity: 0;
            visibility: hidden;
            z-index: 10;
            display: flex;
            flex-direction: column;
        }

        .slide.active { opacity: 1; visibility: visible; }
        
        /* Typography */
        h1, h2, h3, .font-heading {
            font-family: 'Instrument Serif', serif;
        }
        
        .huge-headline {
            font-size: 130px;
            font-weight: 400;
            line-height: 0.95;
            letter-spacing: -2.46px;
            color: #FFFFFF;
        }
        
        .sub-headline {
            font-size: 32px;
            line-height: 1.4;
            color: #8B949E;
            font-family: 'Inter', sans-serif;
            font-weight: 300;
        }
        
        /* Dark overlay for video */
        .video-overlay {
            position: absolute;
            inset: 0;
            background: rgba(1, 4, 9, 0.4);
            z-index: 1;
        }
        
        .bottom-gradient {
            position: absolute;
            bottom: 0; left: 0; right: 0;
            height: 400px;
            background: linear-gradient(to top, rgba(1,4,9,1), rgba(1,4,9,0));
            z-index: 2;
        }

    </style>
</head>
<body>

    <div id="presentation-container">
        <!-- EXACT USER-PROVIDED VIDEO BACKGROUND -->
        <video 
            src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260324_151826_c7218672-6e92-402c-9e45-f1e0f454bdc4.mp4" 
            autoplay loop muted playsinline
            class="absolute inset-0 w-full h-full object-cover z-0"
        ></video>
        
        <div class="video-overlay"></div>
        <div class="bottom-gradient"></div>

        <!-- GLOBAL NAVBAR -->
        <nav class="relative z-50 flex flex-row justify-between px-16 py-10 w-full">
            <div class="font-heading text-4xl tracking-tight text-white italic">Morlen<sup class="text-sm not-italic text-white/50 ml-1">OS</sup></div>
            <div class="flex gap-12 text-sm text-white/60 items-center">
                <span class="text-white">Executive Pitch</span>
                <span>The Problem</span>
                <span>The Shift</span>
                <span>Platform</span>
                <span>Business Model</span>
            </div>
            <div class="liquid-glass rounded-full px-8 py-3 text-sm text-white font-medium tracking-wide">
                CONFIDENTIAL
            </div>
        </nav>

        <!-- SLIDE 1: Hero -->
        <div class="slide" id="slide1">
            <div class="flex-1 flex flex-col items-center justify-center text-center px-10 pb-40">
                <div class="liquid-glass rounded-full px-6 py-2 text-xs font-medium text-white/80 tracking-[0.2em] uppercase mb-10 stagger-anim">
                    Operating System for Business Decisions
                </div>
                
                <h1 class="huge-headline italic stagger-anim max-w-6xl mx-auto">
                    Focus in a <em class="not-italic text-white/40">distracted</em> world.
                </h1>
                
                <p class="sub-headline max-w-3xl mt-10 mx-auto stagger-anim">
                    Turning customer conversations into executive decisions.
                </p>
                
                <div class="liquid-glass rounded-full px-12 py-4 mt-16 stagger-anim inline-flex flex-col items-center">
                    <span class="text-xs text-white/50 uppercase tracking-widest font-semibold mb-1">Founder</span>
                    <span class="font-heading italic text-3xl text-white">Hillary Ikhais</span>
                </div>
            </div>
        </div>

        <!-- SLIDE 2: The Problem -->
        <div class="slide" id="slide2">
            <div class="flex-1 flex flex-col justify-center px-24">
                <div class="liquid-glass rounded-full px-5 py-1.5 text-xs font-medium text-white/80 tracking-widest uppercase mb-10 stagger-anim inline-block w-max">
                    01 // The Problem
                </div>
                
                <div class="flex gap-24 items-center">
                    <div class="flex-1">
                        <h1 class="huge-headline italic stagger-anim text-[110px]">
                            Businesses have <em class="not-italic text-white/40">automated</em> transactions.
                        </h1>
                        <p class="text-2xl text-white/60 font-light mt-10 stagger-anim leading-relaxed max-w-2xl">
                            Over the last two decades, businesses have adopted software for almost every operational function. <span class="text-white font-medium">Business software automates operations. It records what happened.</span>
                        </p>
                        
                        <div class="flex gap-4 mt-12 stagger-anim">
                            <span class="liquid-glass px-6 py-3 rounded-full text-sm text-white/70">Payments</span>
                            <span class="liquid-glass px-6 py-3 rounded-full text-sm text-white/70">CRM</span>
                            <span class="liquid-glass px-6 py-3 rounded-full text-sm text-white/70">Inventory</span>
                            <span class="liquid-glass px-6 py-3 rounded-full text-sm text-white/70">Marketing</span>
                        </div>
                    </div>
                    
                    <div class="flex-1">
                        <div class="liquid-glass-strong rounded-[2.5rem] p-16 stagger-anim">
                            <h3 class="font-heading italic text-5xl text-white mb-10">Yet owners still ask the same questions:</h3>
                            <ul class="space-y-8 text-xl text-white/80 font-light">
                                <li class="flex items-center gap-4"><div class="w-1.5 h-1.5 rounded-full bg-white/40"></div> What deserves attention today?</li>
                                <li class="flex items-center gap-4"><div class="w-1.5 h-1.5 rounded-full bg-white/40"></div> Which products should I restock?</li>
                                <li class="flex items-center gap-4"><div class="w-1.5 h-1.5 rounded-full bg-white/40"></div> Which customers need follow-up?</li>
                                <li class="flex items-center gap-4"><div class="w-1.5 h-1.5 rounded-full bg-white/40"></div> Where am I losing revenue?</li>
                                <li class="flex items-center gap-4"><div class="w-1.5 h-1.5 rounded-full bg-white/40"></div> Why have sales reduced?</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 3: The Shift -->
        <div class="slide" id="slide3">
            <div class="flex-1 flex flex-col justify-center px-24 pb-20">
                <div class="flex gap-20 items-end">
                    <div class="flex-1">
                        <div class="liquid-glass rounded-full px-5 py-1.5 text-xs font-medium text-white/80 tracking-widest uppercase mb-10 stagger-anim inline-block w-max">
                            02 // The Shift
                        </div>
                        <h1 class="huge-headline italic stagger-anim text-[120px]">
                            Commerce has moved into <em class="not-italic text-white/40">conversations.</em>
                        </h1>
                    </div>
                    
                    <div class="flex-1 liquid-glass-strong rounded-[2.5rem] p-12 stagger-anim border-l-[3px] border-l-white">
                        <p class="font-heading italic text-5xl text-white leading-tight">
                            For Nigerian MSMEs, the entire sales funnel now exists inside conversations.
                        </p>
                    </div>
                </div>
                
                <div class="grid grid-cols-3 gap-10 mt-20">
                    <div class="liquid-glass rounded-3xl p-10 stagger-anim">
                        <h4 class="text-white text-lg font-medium mb-4">Unstructured Operations</h4>
                        <p class="text-white/60 font-light leading-relaxed">Across Nigeria, businesses now operate inside messaging platforms. Customers discover, negotiate, and pay inside WhatsApp and Instagram.</p>
                    </div>
                    <div class="liquid-glass rounded-3xl p-10 stagger-anim">
                        <h4 class="text-white text-lg font-medium mb-4">Signal Loss</h4>
                        <p class="text-white/60 font-light leading-relaxed">As conversational commerce grows, businesses generate thousands of customer signals every day. Most disappear.</p>
                    </div>
                    <div class="liquid-glass rounded-3xl p-10 stagger-anim">
                        <h4 class="text-white text-lg font-medium mb-4">Decision Complexity</h4>
                        <p class="text-white/60 font-light leading-relaxed">These decisions are still made manually. As conversations increase, decision complexity grows even faster.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 4: Solution -->
        <div class="slide" id="slide4">
            <div class="flex-1 flex flex-col items-center justify-center text-center px-20">
                <div class="liquid-glass rounded-full px-5 py-1.5 text-xs font-medium text-white/80 tracking-widest uppercase mb-10 stagger-anim">
                    03 // The Platform
                </div>
                
                <h1 class="huge-headline italic stagger-anim text-[140px]">
                    Morlen.
                </h1>
                <p class="font-heading italic text-5xl text-white/60 stagger-anim mt-4">
                    An Executive Decision Intelligence Platform.
                </p>
                
                <div class="grid grid-cols-2 lg:grid-cols-4 gap-6 mt-20 w-full stagger-anim">
                    <div class="liquid-glass-strong rounded-3xl p-8 text-left">
                        <div class="w-10 h-10 liquid-glass rounded-full flex items-center justify-center mb-6">
                            <div class="w-2 h-2 bg-white rounded-full"></div>
                        </div>
                        <h3 class="font-heading italic text-3xl text-white mb-3">Executive Brief</h3>
                        <p class="text-white/60 font-light text-sm leading-relaxed">A daily summary of the highest priority decisions, inventory risks, and customer churn.</p>
                    </div>
                    <div class="liquid-glass-strong rounded-3xl p-8 text-left">
                        <div class="w-10 h-10 liquid-glass rounded-full flex items-center justify-center mb-6">
                            <div class="w-2 h-2 bg-white rounded-full"></div>
                        </div>
                        <h3 class="font-heading italic text-3xl text-white mb-3">Opportunity Feed</h3>
                        <p class="text-white/60 font-light text-sm leading-relaxed">Revenue opportunities detected from conversations with estimated impact and confidence.</p>
                    </div>
                    <div class="liquid-glass-strong rounded-3xl p-8 text-left">
                        <div class="w-10 h-10 liquid-glass rounded-full flex items-center justify-center mb-6">
                            <div class="w-2 h-2 bg-white rounded-full"></div>
                        </div>
                        <h3 class="font-heading italic text-3xl text-white mb-3">Business Memory</h3>
                        <p class="text-white/60 font-light text-sm leading-relaxed">Long-term behavioural intelligence about customers and operational trends.</p>
                    </div>
                    <div class="liquid-glass-strong rounded-3xl p-8 text-left">
                        <div class="w-10 h-10 liquid-glass rounded-full flex items-center justify-center mb-6">
                            <div class="w-2 h-2 bg-white rounded-full"></div>
                        </div>
                        <h3 class="font-heading italic text-3xl text-white mb-3">Evidence-Based</h3>
                        <p class="text-white/60 font-light text-sm leading-relaxed">Every recommendation explains why it exists, expected impact, and supporting evidence.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 5: Market & Stats -->
        <div class="slide" id="slide5">
            <div class="flex-1 flex flex-col justify-center px-24">
                <div class="liquid-glass rounded-full px-5 py-1.5 text-xs font-medium text-white/80 tracking-widest uppercase mb-10 stagger-anim inline-block w-max">
                    04 // Market
                </div>
                
                <h1 class="huge-headline italic stagger-anim text-[110px]">
                    A Massive <em class="not-italic text-white/40">Market.</em>
                </h1>
                
                <div class="liquid-glass-strong rounded-[3rem] p-16 mt-12 stagger-anim flex justify-between items-center">
                    <div>
                        <p class="text-white/60 font-light text-xl mb-4">Nigeria has approximately</p>
                        <h2 class="font-heading italic text-[130px] text-white leading-none">39.6M</h2>
                        <p class="text-white/80 font-medium text-2xl mt-2 tracking-wide">MSMEs</p>
                    </div>
                    
                    <div class="w-px h-40 bg-white/10 mx-10"></div>
                    
                    <div class="space-y-10">
                        <p class="text-xs font-medium text-white/50 tracking-widest uppercase">Representing</p>
                        <div class="grid grid-cols-3 gap-16 text-center">
                            <div>
                                <p class="font-heading italic text-6xl text-white mb-2">96%</p>
                                <p class="text-sm text-white/60">of businesses</p>
                            </div>
                            <div>
                                <p class="font-heading italic text-6xl text-white mb-2">87.9%</p>
                                <p class="text-sm text-white/60">of employment</p>
                            </div>
                            <div>
                                <p class="font-heading italic text-6xl text-white mb-2">46.3%</p>
                                <p class="text-sm text-white/60">of GDP</p>
                            </div>
                        </div>
                    </div>
                </div>
                
                <p class="text-xl text-white/70 font-light mt-12 text-center stagger-anim">
                    Millions already conduct business primarily through messaging platforms. <br>
                    <span class="text-white font-medium">Morlen is built for this new operating environment.</span>
                </p>
            </div>
        </div>

        <!-- SLIDE 6: Pricing -->
        <div class="slide" id="slide6">
            <div class="flex-1 flex flex-col justify-center px-24">
                <div class="liquid-glass rounded-full px-5 py-1.5 text-xs font-medium text-white/80 tracking-widest uppercase mb-10 stagger-anim inline-block w-max">
                    05 // Business Model
                </div>
                
                <div class="flex justify-between items-end mb-16 stagger-anim">
                    <h1 class="huge-headline italic text-[110px] mb-0">Subscription <em class="not-italic text-white/40">SaaS</em></h1>
                    <p class="text-lg text-white/60 max-w-xl text-right font-light leading-relaxed">
                        Starting with a 30-day free trial giving Morlen enough time to learn from customer conversations, build business memory, and generate meaningful insights.
                    </p>
                </div>
                
                <div class="grid grid-cols-3 gap-8 stagger-anim">
                    <div class="liquid-glass rounded-3xl p-10 flex flex-col">
                        <h3 class="font-heading italic text-5xl text-white mb-2">Starter</h3>
                        <p class="text-xl text-white/60 font-medium mb-6">N8,000 / mo</p>
                        <p class="text-sm text-white/50 font-light h-10 mb-6">For early stage businesses</p>
                        <ul class="space-y-4 text-sm text-white/80 font-light border-t border-white/10 pt-6">
                            <li>• Executive brief</li>
                            <li>• Business memory</li>
                            <li>• Basic decision intelligence</li>
                            <li>• Single workspace</li>
                        </ul>
                    </div>
                    
                    <div class="liquid-glass-strong rounded-3xl p-10 flex flex-col relative transform scale-105 z-10 border border-white/20">
                        <div class="absolute -top-4 right-8 liquid-glass px-4 py-1 rounded-full text-[10px] font-bold text-white uppercase tracking-widest">
                            Popular
                        </div>
                        <h3 class="font-heading italic text-5xl text-white mb-2">Growth</h3>
                        <p class="text-xl text-white font-medium mb-6">N15,000 / mo</p>
                        <p class="text-sm text-white/70 font-light h-10 mb-6">Businesses managing increasing customer conversations.</p>
                        <ul class="space-y-4 text-sm text-white font-medium border-t border-white/20 pt-6">
                            <li>• Everything in starter</li>
                            <li>• Opportunity feed</li>
                            <li>• Advanced AI recommendations</li>
                            <li>• Multi channel integrations</li>
                            <li>• Team Collaboration</li>
                        </ul>
                    </div>
                    
                    <div class="liquid-glass rounded-3xl p-10 flex flex-col">
                        <h3 class="font-heading italic text-5xl text-white mb-2">Enterprise</h3>
                        <p class="text-xl text-white/60 font-medium mb-6">Custom</p>
                        <p class="text-sm text-white/50 font-light h-10 mb-6">Organizations requiring company-wide decision intelligence.</p>
                        <ul class="space-y-4 text-sm text-white/80 font-light border-t border-white/10 pt-6">
                            <li>• Everything in growth</li>
                            <li>• Custom AI deployment</li>
                            <li>• Dedicated Support</li>
                            <li>• Enterprise security</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 7: Funding & Ask -->
        <div class="slide" id="slide7">
            <div class="flex-1 flex flex-col justify-center px-24">
                <div class="flex gap-20">
                    <div class="flex-1">
                        <div class="liquid-glass rounded-full px-5 py-1.5 text-xs font-medium text-white/80 tracking-widest uppercase mb-10 stagger-anim inline-block w-max">
                            06 // Pre-Seed Raise
                        </div>
                        <h1 class="huge-headline italic stagger-anim text-[110px] mb-6">
                            Seeking <em class="not-italic text-white/40">₦25M</em>
                        </h1>
                        <p class="text-2xl text-white/60 font-light mb-16 stagger-anim">Investment will accelerate three key milestones.</p>
                        
                        <div class="space-y-6 stagger-anim">
                            <div class="liquid-glass rounded-2xl p-6 flex gap-8 items-center">
                                <span class="font-heading italic text-5xl text-white w-20">40%</span>
                                <div>
                                    <h4 class="text-white font-medium mb-1">Product Development</h4>
                                    <p class="text-sm text-white/60 font-light">Complete commercial MVP and core intelligence engine.</p>
                                </div>
                            </div>
                            <div class="liquid-glass rounded-2xl p-6 flex gap-8 items-center">
                                <span class="font-heading italic text-5xl text-white/70 w-20">25%</span>
                                <div>
                                    <h4 class="text-white font-medium mb-1">AI Infrastructure</h4>
                                    <p class="text-sm text-white/60 font-light">Inference, data pipelines and production infrastructure.</p>
                                </div>
                            </div>
                            <div class="liquid-glass rounded-2xl p-6 flex gap-8 items-center">
                                <span class="font-heading italic text-5xl text-white/50 w-20">20%</span>
                                <div>
                                    <h4 class="text-white font-medium mb-1">Customer Acquisition</h4>
                                    <p class="text-sm text-white/60 font-light">Pilot programs and early customer onboarding.</p>
                                </div>
                            </div>
                            <div class="liquid-glass rounded-2xl p-6 flex gap-8 items-center">
                                <span class="font-heading italic text-5xl text-white/30 w-20">15%</span>
                                <div>
                                    <h4 class="text-white font-medium mb-1">Operations</h4>
                                    <p class="text-sm text-white/60 font-light">Messaging integrations and business development.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="flex-1 flex flex-col justify-center pl-16">
                        <h2 class="font-heading italic text-[80px] text-white mb-12 stagger-anim">Expected Outcomes</h2>
                        <div class="liquid-glass-strong rounded-[2.5rem] p-12 space-y-10 stagger-anim">
                            <div class="flex items-start gap-6">
                                <div class="w-2 h-2 mt-2 rounded-full bg-white"></div>
                                <div>
                                    <h4 class="text-white font-medium text-xl mb-2">Build</h4>
                                    <p class="text-white/60 font-light leading-relaxed">Complete the production-ready Morlen platform.</p>
                                </div>
                            </div>
                            <div class="flex items-start gap-6 border-t border-white/10 pt-10">
                                <div class="w-2 h-2 mt-2 rounded-full bg-white"></div>
                                <div>
                                    <h4 class="text-white font-medium text-xl mb-2">Validate</h4>
                                    <p class="text-white/60 font-light leading-relaxed">Onboard 20–30 pilot businesses and refine the product using real customer behaviour.</p>
                                </div>
                            </div>
                            <div class="flex items-start gap-6 border-t border-white/10 pt-10">
                                <div class="w-2 h-2 mt-2 rounded-full bg-white"></div>
                                <div>
                                    <h4 class="text-white font-medium text-xl mb-2">Launch</h4>
                                    <p class="text-white/60 font-light leading-relaxed">Validate pricing, acquire the first paying customers, and prepare for commercial rollout.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 8: Outro -->
        <div class="slide" id="slide8">
            <div class="flex-1 flex flex-col items-center justify-center text-center px-10">
                <div class="liquid-glass rounded-full px-6 py-2 text-xs font-medium text-white/80 tracking-[0.2em] uppercase mb-12 stagger-anim">
                    Why Morlen?
                </div>
                
                <h1 class="font-heading italic stagger-anim text-[90px] leading-tight max-w-5xl">
                    Business software answers "What happened?"
                </h1>
                <h1 class="font-heading italic stagger-anim text-[110px] leading-tight max-w-5xl text-white/40 mt-4 mb-20">
                    Morlen answers "What should I do next?"
                </h1>
                
                <div class="grid grid-cols-3 gap-8 w-full max-w-5xl stagger-anim">
                    <div class="liquid-glass rounded-2xl p-6 text-center text-sm text-white/70 font-light">Every conversation contains intelligence.</div>
                    <div class="liquid-glass rounded-2xl p-6 text-center text-sm text-white/70 font-light">Every business generates opportunities.</div>
                    <div class="liquid-glass rounded-2xl p-6 text-center text-sm text-white/70 font-light">Every owner has limited attention.</div>
                </div>
                
                <p class="text-2xl text-white mt-20 stagger-anim font-light">
                    Morlen exists to protect that attention— <br>
                    <span class="font-heading italic text-4xl mt-2 block">by turning conversations into decisions.</span>
                </p>
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
                    y: -40,
                    duration: 0.8,
                    ease: "power2.inOut",
                    onComplete: () => {
                        current.classList.remove('active');
                        current.style.visibility = 'hidden';
                        gsap.set(current, { y: 0 }); 
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
                  stagger: 0.15, ease: "power3.out"
              }, "-=0.1");
        }

        // Init
        slides[0].classList.add('active');
        slides[0].style.visibility = 'visible';
        slides[0].style.opacity = 1;
        
        gsap.set(slides[0].querySelectorAll('.stagger-anim'), { opacity: 0, y: 30 });
        
        setTimeout(() => {
            gsap.to(slides[0].querySelectorAll('.stagger-anim'), {
                opacity: 1, y: 0, duration: 1.2,
                stagger: 0.15, ease: "power3.out"
            });
        }, 300);
        
        // Auto-advance
        setInterval(() => {
            if (currentSlide < slides.length - 1) {
                goToSlide(currentSlide + 1);
            }
        }, 9000);
        
        window.goToSlide = goToSlide;
    </script>
</body>
</html>"""

with open('presentation.html', 'w') as f:
    f.write(html_content)

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
    <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Geist:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        display: ['Instrument Serif', 'serif'],
                        body: ['Geist', 'sans-serif'],
                    },
                    colors: {
                        void: '#030303',
                        bone: '#F8F8F5',
                        ash: '#8B8B8D'
                    }
                }
            }
        }
    </script>

    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            background-color: #030303;
            color: #F8F8F5;
            font-family: 'Geist', sans-serif;
            overflow: hidden;
            width: 100vw;
            height: 100vh;
        }

        #presentation-container {
            width: 1920px;
            height: 1080px;
            position: relative;
            background: #030303;
            overflow: hidden;
        }

        /* 
         * ATMOSPHERIC 2D GEOMETRY & GLASSMORPHISM 
         * No cards. Glass is used as floating structural art.
         */
        
        /* A massive, slow-moving blurred geometric shape in the background */
        .glass-orb {
            position: absolute;
            border-radius: 50%;
            background: linear-gradient(135deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.0) 100%);
            backdrop-filter: blur(40px);
            -webkit-backdrop-filter: blur(40px);
            border: 1px solid rgba(255,255,255,0.05);
            box-shadow: inset 0 0 100px rgba(255,255,255,0.02);
            pointer-events: none;
            z-index: 0;
            animation: float-orb 40s ease-in-out infinite alternate;
        }
        
        .orb-1 { width: 1200px; height: 1200px; top: -300px; right: -200px; }
        .orb-2 { width: 800px; height: 800px; bottom: -200px; left: -100px; animation-delay: -10s; }
        .orb-3 { width: 600px; height: 1400px; border-radius: 200px; top: -100px; left: 40%; transform: rotate(30deg); animation: float-pillar 50s ease-in-out infinite alternate; }

        @keyframes float-orb {
            0% { transform: translate(0, 0) scale(1) rotate(0deg); }
            50% { transform: translate(-100px, 100px) scale(1.1) rotate(15deg); }
            100% { transform: translate(-50px, 200px) scale(0.9) rotate(-15deg); }
        }

        @keyframes float-pillar {
            0% { transform: rotate(30deg) translate(0, 0); }
            100% { transform: rotate(45deg) translate(200px, -100px); }
        }
        
        /* Abstract structural lines (NOT boxes) */
        .struct-line {
            position: absolute;
            background: rgba(255,255,255,0.1);
            z-index: 1;
        }
        .line-v { width: 1px; height: 100vh; }
        .line-h { width: 100vw; height: 1px; }

        .slide {
            position: absolute; top: 0; left: 0;
            width: 100%; height: 100%;
            padding: 80px 120px;
            opacity: 0;
            visibility: hidden;
            z-index: 10;
        }

        .slide.active { opacity: 1; visibility: visible; }
        
        /* Editorial Typography */
        .huge-headline {
            font-family: 'Instrument Serif', serif;
            font-size: 130px;
            font-weight: 400;
            line-height: 0.9;
            color: #F8F8F5;
            margin-bottom: 40px;
            letter-spacing: -0.02em;
        }
        
        .huge-italic { font-style: italic; color: #FFFFFF; font-weight: 400; }
        
        .sub-headline {
            font-size: 32px;
            font-weight: 300;
            color: #8B8B8D;
            margin-bottom: 24px;
            line-height: 1.3;
            letter-spacing: 0.02em;
            max-width: 800px;
        }
        
        /* Structural Typography */
        .super-graphic {
            position: absolute;
            font-family: 'Instrument Serif', serif;
            font-size: 600px;
            font-weight: 400;
            color: rgba(255,255,255,0.02);
            line-height: 0.8;
            z-index: -1;
            pointer-events: none;
            white-space: nowrap;
            font-style: italic;
        }

        /* Connecting nodes instead of cards */
        .node-group {
            position: relative;
            padding-left: 40px;
            border-left: 1px solid rgba(255,255,255,0.15);
        }
        .node-group::before {
            content: ''; position: absolute; top: 12px; left: -4px; width: 7px; height: 7px;
            border-radius: 50%; background: #F8F8F5;
        }

    </style>
</head>
<body>

    <div id="presentation-container">
        <!-- Floating Glassmorphic Orbs & Structural Lines -->
        <div class="glass-orb orb-1"></div>
        <div class="glass-orb orb-2"></div>
        <div class="glass-orb orb-3"></div>
        
        <div class="struct-line line-v" style="left: 120px;"></div>
        <div class="struct-line line-v" style="left: 50%;"></div>
        <div class="struct-line line-v" style="right: 120px;"></div>
        <div class="struct-line line-h" style="top: 80px;"></div>
        <div class="struct-line line-h" style="bottom: 80px;"></div>

        <!-- SLIDE 1 -->
        <div class="slide" id="slide1">
            <div class="w-full h-full flex flex-col justify-center relative">
                <div class="super-graphic" style="top: 10%; right: -10%;">M.</div>
                
                <div class="max-w-4xl relative z-10 pl-[80px]">
                    <div class="flex items-center gap-6 mb-12 stagger-anim">
                        <div class="w-2 h-2 bg-bone rounded-full"></div>
                        <p class="text-sm uppercase tracking-[0.4em] text-ash font-medium">Executive Pitch</p>
                    </div>
                    
                    <h1 class="huge-headline stagger-anim">Morlen<span class="text-bone/30">.</span></h1>
                    <p class="sub-headline stagger-anim text-bone/90 font-medium">The Operating System for Business Decisions.</p>
                    <p class="text-3xl text-ash font-light mb-20 stagger-anim">Turning customer conversations into executive decisions.</p>
                    
                    <div class="stagger-anim flex items-center gap-8 pl-12 border-l border-bone/20">
                        <p class="text-xs text-ash uppercase tracking-[0.3em] font-medium rotate-180" style="writing-mode: vertical-rl;">Founder</p>
                        <p class="text-4xl text-bone font-display italic tracking-wide">Hillary Ikhais</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 2 -->
        <div class="slide" id="slide2">
            <div class="w-full h-full flex flex-col justify-center">
                <div class="flex gap-32 relative z-10 pl-[80px]">
                    <div class="flex-1">
                        <h1 class="huge-headline stagger-anim" style="font-size: 100px;">The Problem.</h1>
                        <h2 class="sub-headline stagger-anim text-bone">Businesses have <span class="huge-italic">automated</span> transactions.</h2>
                        
                        <div class="stagger-anim mt-16">
                            <p class="text-xl text-ash leading-relaxed mb-12 font-light">Over the last two decades, businesses have adopted software for almost every operational function:</p>
                            
                            <ul class="text-2xl text-bone space-y-6 font-light">
                                <li class="flex items-center gap-6"><span class="text-ash/40 font-mono text-sm">01</span> Payments</li>
                                <li class="flex items-center gap-6"><span class="text-ash/40 font-mono text-sm">02</span> CRM</li>
                                <li class="flex items-center gap-6"><span class="text-ash/40 font-mono text-sm">03</span> Inventory</li>
                                <li class="flex items-center gap-6"><span class="text-ash/40 font-mono text-sm">04</span> Marketing</li>
                                <li class="flex items-center gap-6"><span class="text-ash/40 font-mono text-sm">05</span> Accounting</li>
                                <li class="flex items-center gap-6 mt-8 pt-8 border-t border-bone/10 text-4xl font-display italic"><span class="text-bone font-mono text-sm not-italic mr-4">06</span> Conversations</li>
                            </ul>
                        </div>
                    </div>
                    
                    <div class="flex-1 flex flex-col justify-center pl-16 border-l border-bone/10">
                        <div class="super-graphic" style="top: 20%; right: 10%; font-size: 300px;">?</div>
                        
                        <p class="text-3xl font-light text-bone mb-12 stagger-anim leading-tight">Yet business owners still ask the same questions:</p>
                        
                        <ul class="text-2xl text-ash space-y-8 mb-20 stagger-anim font-light">
                            <li class="node-group">What deserves attention today?</li>
                            <li class="node-group">Which products should I restock?</li>
                            <li class="node-group">Which customers need follow-up?</li>
                            <li class="node-group">Where am I losing revenue?</li>
                            <li class="node-group">Why have sales reduced?</li>
                        </ul>
                        
                        <div class="stagger-anim pl-10 border-l-2 border-bone">
                            <p class="text-2xl text-bone mb-3 font-medium">Business software automates operations.</p>
                            <p class="text-2xl text-ash font-light font-display italic">It records what happened.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 3 -->
        <div class="slide" id="slide3">
            <div class="w-full h-full flex flex-col justify-center relative pl-[80px]">
                <div class="super-graphic" style="top: 30%; right: 5%; font-size: 400px;">Shift.</div>
                
                <div class="max-w-5xl">
                    <div class="flex items-center gap-6 mb-12 stagger-anim">
                        <span class="text-ash/40 font-mono text-sm">02</span>
                        <div class="w-12 h-px bg-bone/20"></div>
                        <p class="text-sm uppercase tracking-[0.4em] text-ash font-medium">The Shift</p>
                    </div>
                    
                    <h1 class="huge-headline stagger-anim" style="font-size: 110px;">Commerce has moved<br>into <span class="huge-italic">conversations.</span></h1>
                    
                    <div class="space-y-12 text-2xl text-ash leading-relaxed stagger-anim mt-16 font-light max-w-4xl">
                        <p>Across Nigeria, businesses now operate inside messaging platforms.<br>
                        <span class="text-xl mt-4 block text-ash/80">Customers now discover products, negotiate prices, confirm payments and arrange deliveries inside WhatsApp, Instagram and Facebook.</span></p>
                        
                        <div class="pl-12 border-l border-bone/30 py-4">
                            <p class="text-bone font-medium text-4xl font-display italic leading-snug">For Nigerian MSMEs, the entire sales funnel now exists inside conversations.</p>
                        </div>
                        
                        <p>Yet traditional software was designed for structured forms, not unstructured conversations.</p>
                        
                        <div class="flex items-end gap-12 mt-12 pt-12 border-t border-bone/10">
                            <p class="flex-1">As conversational commerce grows, businesses generate thousands of customer signals every day.</p>
                            <p class="flex-1 text-bone font-medium text-2xl leading-tight">Most disappear without ever becoming business intelligence.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 4 -->
        <div class="slide" id="slide4">
            <div class="w-full h-full flex flex-col justify-center relative pl-[80px]">
                <div class="super-graphic" style="top: 0; right: 10%; font-size: 400px; transform: rotate(-10deg);">Decide.</div>
                
                <div class="max-w-6xl z-10 relative">
                    <h1 class="huge-headline stagger-anim" style="font-size: 100px;">The Problem.</h1>
                    <h2 class="sub-headline stagger-anim text-bone">Every conversation creates decisions.</h2>
                    <p class="text-2xl text-ash mb-16 stagger-anim font-light border-l border-bone/20 pl-8">A business owner doesn't just receive messages.<br>They constantly decide:</p>
                    
                    <ul class="text-3xl text-bone space-y-10 stagger-anim font-display italic">
                        <li class="flex items-center gap-8"><span class="w-12 h-px bg-bone/30"></span>Should this customer receive follow-up?</li>
                        <li class="flex items-center gap-8"><span class="w-24 h-px bg-bone/30"></span>Is demand increasing for this product?</li>
                        <li class="flex items-center gap-8"><span class="w-12 h-px bg-bone/30"></span>Should inventory be reordered?</li>
                        <li class="flex items-center gap-8"><span class="w-32 h-px bg-bone/30"></span>Are customers becoming more price-sensitive?</li>
                        <li class="flex items-center gap-8"><span class="w-16 h-px bg-bone/30"></span>Which complaints appear repeatedly?</li>
                        <li class="flex items-center gap-8"><span class="w-8 h-px bg-bone/30"></span>Which customers are likely to return?</li>
                    </ul>
                    
                    <div class="stagger-anim mt-20 flex gap-20 items-end">
                        <p class="text-2xl text-ash font-light flex-1">These decisions are still made manually.</p>
                        <p class="text-4xl text-bone font-medium flex-2 leading-tight">As conversations increase, decision complexity grows even faster.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 5 -->
        <div class="slide" id="slide5">
            <div class="w-full h-full flex flex-col justify-center relative pl-[80px]">
                <h1 class="huge-headline stagger-anim">Morlen.</h1>
                <h2 class="sub-headline stagger-anim text-bone">An Executive <span class="huge-italic">Decision Intelligence</span> Platform.</h2>
                
                <div class="stagger-anim max-w-4xl mb-16 mt-8 flex gap-12 items-center">
                    <div class="w-20 h-px bg-bone/30"></div>
                    <div>
                        <p class="text-2xl text-ash mb-4 font-light">Morlen continuously analyzes customer conversations, identifies business patterns and delivers prioritized business decisions.</p>
                        <p class="text-3xl text-bone font-display italic">Instead of presenting plain dashboards, Morlen produces a daily executive briefing.</p>
                    </div>
                </div>
                
                <div class="flex gap-16 mb-20 relative z-10">
                    <div class="stagger-anim flex-1 node-group">
                        <h3 class="text-2xl font-medium text-bone mb-6">Executive Brief</h3>
                        <p class="text-lg text-ash font-light leading-relaxed">A daily summary of the highest priority decisions. inventory risks, customer churn, demand spikes, operational issues.</p>
                    </div>
                    <div class="stagger-anim flex-1 node-group">
                        <h3 class="text-2xl font-medium text-bone mb-6">Opportunity Feed</h3>
                        <p class="text-lg text-ash font-light leading-relaxed">Revenue opportunities detected from conversations including estimated impact, confidence score, supporting evidence.</p>
                    </div>
                    <div class="stagger-anim flex-1 node-group">
                        <h3 class="text-2xl font-medium text-bone mb-6">Business Memory</h3>
                        <p class="text-lg text-ash font-light leading-relaxed mb-6">Long-term behavioural intelligence about customers.</p>
                        <p class="text-xs text-bone uppercase tracking-widest font-mono">Ex: Demand rises at month end</p>
                    </div>
                    <div class="stagger-anim flex-1 node-group">
                        <h3 class="text-2xl font-medium text-bone mb-6">Evidence-Based</h3>
                        <p class="text-lg text-ash font-light leading-relaxed mb-4">Every recommendation explains:</p>
                        <ul class="text-sm text-bone space-y-2 font-mono">
                            <li>01. Why it exists</li>
                            <li>02. Expected impact</li>
                            <li>03. Supporting evidence</li>
                        </ul>
                    </div>
                </div>
                
                <div class="stagger-anim flex items-center gap-12 border-t border-bone/10 pt-10 w-max">
                    <p class="text-2xl text-ash font-light">Business owners stop searching for answers.</p>
                    <p class="text-4xl font-display italic text-bone">Morlen brings the answers to them.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 6 -->
        <div class="slide" id="slide6">
            <div class="w-full h-full flex flex-col justify-center relative pl-[80px]">
                <div class="super-graphic" style="top: 20%; right: -5%; font-size: 500px;">Scale.</div>
                
                <div class="stagger-anim mb-16 flex items-center gap-6">
                    <div class="w-8 h-px bg-bone/40"></div>
                    <p class="text-sm uppercase tracking-[0.4em] font-medium text-ash">Market & Business Model</p>
                </div>
                
                <h1 class="huge-headline stagger-anim" style="font-size: 100px;">A Massive <span class="huge-italic">Market.</span></h1>
                
                <div class="flex gap-32 items-center mt-10">
                    <div class="flex-1 stagger-anim">
                        <p class="text-2xl text-ash mb-8 font-light">Nigeria has approximately:</p>
                        <p class="text-[120px] font-display italic text-bone leading-none tracking-tight mb-8">39.6M <span class="text-5xl font-sans not-italic text-ash font-light">MSMEs</span></p>
                        <div class="pl-8 border-l border-bone/20 mt-12">
                            <p class="text-2xl font-light text-ash leading-relaxed">Millions already conduct business primarily through messaging platforms. <span class="text-bone font-medium">Morlen is built for this new operating environment.</span></p>
                        </div>
                    </div>
                    
                    <div class="flex-1 pl-20 border-l border-bone/10">
                        <p class="text-sm text-ash mb-12 stagger-anim uppercase tracking-[0.3em] font-medium">Representing</p>
                        <div class="space-y-16 stagger-anim">
                            <div class="flex items-end gap-8">
                                <p class="text-7xl font-display italic text-bone w-40">96%</p>
                                <p class="text-2xl text-ash font-light pb-2">of businesses</p>
                            </div>
                            <div class="flex items-end gap-8">
                                <p class="text-7xl font-display italic text-bone w-40">87.9%</p>
                                <p class="text-2xl text-ash font-light pb-2">of employment</p>
                            </div>
                            <div class="flex items-end gap-8">
                                <p class="text-7xl font-display italic text-bone w-40">46.3%</p>
                                <p class="text-2xl text-ash font-light pb-2">of GDP</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 7 -->
        <div class="slide" id="slide7">
            <div class="w-full h-full flex flex-col justify-center relative pl-[80px]">
                <h1 class="huge-headline stagger-anim" style="font-size: 100px;">Business <span class="huge-italic">Model.</span></h1>
                
                <div class="flex items-center gap-12 mb-16 stagger-anim">
                    <h2 class="text-lg font-mono text-bone uppercase tracking-[0.2em]">Subscription SaaS</h2>
                    <div class="w-px h-12 bg-bone/20"></div>
                    <p class="text-xl text-ash max-w-3xl font-light leading-relaxed">Starting with a 30-day free trial giving Morlen enough time to learn from customer conversations, build business memory, and generate meaningful insights.</p>
                </div>
                
                <div class="flex gap-20 mb-20 stagger-anim border-t border-b border-bone/10 py-16 relative z-10">
                    <div class="flex-1 node-group">
                        <h3 class="text-4xl font-display italic text-bone mb-4">Starter</h3>
                        <p class="text-xl text-ash font-mono mb-8">N8,000/mo</p>
                        <p class="text-base text-ash mb-10 font-light h-12">For early stage businesses</p>
                        <ul class="text-bone space-y-4 text-base font-light">
                            <li>Executive brief</li>
                            <li>Business memory</li>
                            <li>Basic decision intelligence</li>
                            <li>Single workspace</li>
                        </ul>
                    </div>
                    
                    <div class="flex-1 node-group relative">
                        <div class="absolute -top-12 left-0 text-xs font-mono text-bone tracking-[0.2em] uppercase flex items-center gap-4"><div class="w-2 h-2 bg-bone rounded-full"></div> Popular</div>
                        <h3 class="text-4xl font-display italic text-bone mb-4">Growth</h3>
                        <p class="text-xl text-bone font-mono mb-8">N15,000/mo</p>
                        <p class="text-base text-ash mb-10 font-light h-12">Businesses managing increasing customer conversations.</p>
                        <ul class="text-bone space-y-4 text-base font-medium">
                            <li>Everything in starter</li>
                            <li>Opportunity feed</li>
                            <li>Advanced AI recommendations</li>
                            <li>Multi channel integrations</li>
                            <li>Team Collaboration</li>
                        </ul>
                    </div>
                    
                    <div class="flex-1 node-group">
                        <h3 class="text-4xl font-display italic text-bone mb-4">Enterprise</h3>
                        <p class="text-xl text-ash font-mono mb-8">CUSTOM</p>
                        <p class="text-base text-ash mb-10 font-light h-12">Organizations requiring company-wide decision intelligence.</p>
                        <ul class="text-bone space-y-4 text-base font-light">
                            <li>Everything in growth</li>
                            <li>Custom AI deployment</li>
                            <li>Dedicated Support</li>
                            <li>Enterprise security and governance</li>
                        </ul>
                    </div>
                </div>
                
                <p class="text-lg text-ash stagger-anim font-light flex items-center gap-6">
                    Additional revenue: <span class="text-bone font-medium font-mono uppercase tracking-widest text-sm">Enterprise Implementation & Onboarding</span>
                </p>
            </div>
        </div>

        <!-- SLIDE 8 -->
        <div class="slide" id="slide8">
            <div class="w-full h-full flex flex-col justify-center relative pl-[80px]">
                <div class="super-graphic" style="top: -10%; left: 40%; font-size: 350px;">Grow.</div>
                
                <div class="flex gap-24 relative z-10">
                    <div class="flex-1">
                        <h1 class="huge-headline stagger-anim" style="font-size: 100px;">Funding.</h1>
                        <h2 class="text-4xl font-display italic text-bone mb-12 stagger-anim">Raising Pre-Seed Capital</h2>
                        <p class="text-sm text-ash mb-12 stagger-anim font-mono uppercase tracking-widest">Investment will accelerate:</p>
                        
                        <div class="space-y-12 stagger-anim">
                            <div class="flex items-center gap-10">
                                <h3 class="text-6xl font-display italic text-bone w-32">40%</h3>
                                <div class="w-px h-16 bg-bone/20"></div>
                                <div>
                                    <p class="text-xl font-medium text-bone mb-2">Product Development</p>
                                    <p class="text-base text-ash font-light">Complete commercial MVP and core intelligence engine.</p>
                                </div>
                            </div>
                            <div class="flex items-center gap-10">
                                <h3 class="text-6xl font-display italic text-bone w-32 opacity-80">25%</h3>
                                <div class="w-px h-16 bg-bone/20"></div>
                                <div>
                                    <p class="text-xl font-medium text-bone mb-2">AI Infrastructure</p>
                                    <p class="text-base text-ash font-light">Inference, data pipelines and production infrastructure.</p>
                                </div>
                            </div>
                            <div class="flex items-center gap-10">
                                <h3 class="text-6xl font-display italic text-bone w-32 opacity-60">20%</h3>
                                <div class="w-px h-16 bg-bone/20"></div>
                                <div>
                                    <p class="text-xl font-medium text-bone mb-2">Customer Acq.</p>
                                    <p class="text-base text-ash font-light">Pilot programs and early customer onboarding.</p>
                                </div>
                            </div>
                            <div class="flex items-center gap-10">
                                <h3 class="text-6xl font-display italic text-bone w-32 opacity-40">15%</h3>
                                <div class="w-px h-16 bg-bone/20"></div>
                                <div>
                                    <p class="text-xl font-medium text-bone mb-2">Operations</p>
                                    <p class="text-base text-ash font-light">Messaging integrations and business development.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="flex-1 flex flex-col justify-center border-l border-bone/10 pl-24">
                        <h1 class="huge-headline stagger-anim" style="font-size: 100px;">Outcomes.</h1>
                        <h2 class="text-4xl font-display italic text-bone mb-16 stagger-anim">Expected Milestones</h2>
                        
                        <div class="space-y-12 stagger-anim border-l border-bone/20 py-4">
                            <div class="flex items-center gap-8 -ml-3">
                                <div class="w-6 h-6 rounded-full bg-void border border-bone flex items-center justify-center"><div class="w-1.5 h-1.5 bg-bone rounded-full"></div></div>
                                <p class="text-3xl text-bone font-light">Commercial MVP</p>
                            </div>
                            <div class="flex items-center gap-8 -ml-3">
                                <div class="w-6 h-6 rounded-full bg-void border border-bone flex items-center justify-center"><div class="w-1.5 h-1.5 bg-bone rounded-full"></div></div>
                                <p class="text-3xl text-bone font-light">First paying customers</p>
                            </div>
                            <div class="flex items-center gap-8 -ml-3">
                                <div class="w-6 h-6 rounded-full bg-void border border-bone flex items-center justify-center"><div class="w-1.5 h-1.5 bg-bone rounded-full"></div></div>
                                <p class="text-3xl text-bone font-light">Validated product-market fit</p>
                            </div>
                            <div class="flex items-center gap-8 -ml-3">
                                <div class="w-6 h-6 rounded-full bg-void border border-bone flex items-center justify-center"><div class="w-1.5 h-1.5 bg-bone rounded-full"></div></div>
                                <p class="text-3xl text-bone font-light">Foundation for national expansion</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 9 -->
        <div class="slide" id="slide9">
            <div class="w-full h-full flex flex-col justify-center relative pl-[80px]">
                <h1 class="huge-headline stagger-anim" style="font-size: 100px;">Why Morlen?</h1>
                
                <div class="flex gap-24 mt-16 relative z-10">
                    <div class="flex-1 stagger-anim flex flex-col justify-center">
                        <p class="text-xl text-ash mb-8 font-light uppercase tracking-widest">Software answers:</p>
                        <h2 class="text-[80px] font-display italic text-bone leading-none mb-16">"What happened?"</h2>
                        
                        <ul class="text-2xl text-ash space-y-8 font-light border-l border-bone/20 pl-10">
                            <li>CRM stores customer records</li>
                            <li>ERP manages operations</li>
                            <li>BI dashboards visualize historical metrics</li>
                            <li>Chatbots automate conversations</li>
                        </ul>
                    </div>
                    
                    <div class="flex-1 stagger-anim flex flex-col justify-center pl-16 border-l border-bone/10 relative">
                        <p class="text-xl text-bone mb-8 font-medium uppercase tracking-widest">Morlen answers:</p>
                        <h2 class="text-[80px] font-display italic text-bone leading-none mb-16">"What should I do next?"</h2>
                        
                        <ul class="text-3xl text-bone space-y-8 font-medium border-l border-bone pl-10">
                            <li>Every conversation contains intelligence.</li>
                            <li>Every business generates opportunities.</li>
                            <li>Every owner has limited attention.</li>
                        </ul>
                        
                        <div class="mt-16 pt-12 border-t border-bone/10 w-4/5">
                            <p class="text-3xl text-bone leading-relaxed font-light">Morlen exists to protect that attention—<br><span class="text-ash font-display italic">by turning conversations into decisions.</span></p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 10 -->
        <div class="slide" id="slide10">
            <div class="super-graphic" style="top: 15%; left: -5%; font-size: 600px; opacity: 0.05;">OS.</div>
            
            <div class="w-full h-full flex flex-col justify-center items-center text-center relative z-10">
                <div class="stagger-anim mb-20 flex items-center gap-8">
                    <div class="w-16 h-px bg-bone/30"></div>
                    <p class="text-xl font-light text-ash uppercase tracking-[0.4em]">The future of business isn't more software.</p>
                    <div class="w-16 h-px bg-bone/30"></div>
                </div>

                <h1 class="text-[300px] font-display italic text-bone leading-none tracking-tighter mb-20 stagger-anim">Morlen.</h1>
                
                <div class="stagger-anim">
                    <p class="text-3xl text-ash mb-6 font-light">Businesses already have the conversations.</p>
                    <p class="text-5xl text-bone font-medium tracking-wide">Morlen turns them into decisions.</p>
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
                    opacity: 0, x: -50,
                    duration: 0.8,
                    ease: "power2.inOut",
                    onComplete: () => {
                        current.classList.remove('active');
                        current.style.visibility = 'hidden';
                        gsap.set(current, { x: 0 }); 
                    }
                });
            }

            next.classList.add('active');
            next.style.visibility = 'visible';
            
            const fadeElements = next.querySelectorAll('.stagger-anim');
            gsap.set(fadeElements, { opacity: 0, x: 50 });

            const tl = gsap.timeline({
                onComplete: () => {
                    currentSlide = index;
                    isAnimating = false;
                }
            });
            
            tl.to(next, { opacity: 1, duration: 0.2 })
              .to(fadeElements, {
                  opacity: 1, x: 0, duration: 1.2,
                  stagger: 0.15, ease: "power3.out"
              }, "-=0.1");
        }

        slides[0].classList.add('active');
        slides[0].style.visibility = 'visible';
        slides[0].style.opacity = 1;
        
        gsap.set(slides[0].querySelectorAll('.stagger-anim'), { opacity: 0, x: 50 });
        
        setTimeout(() => {
            gsap.to(slides[0].querySelectorAll('.stagger-anim'), {
                opacity: 1, x: 0, duration: 1.2,
                stagger: 0.15, ease: "power3.out"
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

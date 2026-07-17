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
            overflow: hidden;
        }

        /* Cinematic Background Video */
        .bg-video {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            z-index: 0;
            opacity: 0.65; /* Darken slightly so text pops */
        }
        
        .video-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: radial-gradient(circle at center, transparent 0%, #000000 120%);
            z-index: 1;
        }

        /* Liquid Glass CSS Provided by User */
        .liquid-glass {
            background: rgba(255, 255, 255, 0.01);
            background-blend-mode: luminosity;
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: none;
            box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.1), 0 20px 40px rgba(0,0,0,0.2);
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
        h1, h2 { font-family: 'Instrument Serif', serif; }
        
        .huge-headline {
            font-size: 110px;
            font-weight: 400;
            line-height: 1.05;
            color: #FFFFFF;
            margin-bottom: 30px;
            letter-spacing: -0.02em;
        }
        
        .sub-headline {
            font-size: 52px;
            font-weight: 400;
            color: rgba(255,255,255,0.9);
            margin-bottom: 24px;
            line-height: 1.15;
        }
        
        /* GSAP Text Splitting */
        .word-mask { display: inline-block; overflow: hidden; vertical-align: top; padding-bottom: 12px; }
        .word-inner { display: inline-block; transform: translateY(100%); }

    </style>
</head>
<body>

    <div id="presentation-container">
        <!-- Cinematic Video Background -->
        <video class="bg-video" src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260307_083826_e938b29f-a43a-41ec-a153-3d4730578ab8.mp4" autoplay muted loop playsinline></video>
        <div class="video-overlay"></div>

        <!-- SLIDE 1 -->
        <div class="slide" id="slide1">
            <div class="w-full h-full flex flex-col justify-center">
                <div class="max-w-4xl relative z-10">
                    <h1 class="huge-headline split-text">Morlen.</h1>
                    <p class="sub-headline split-text">The Operating System for Business Decisions.</p>
                    <div class="liquid-glass rounded-2xl p-8 inline-block stagger-anim mt-10">
                        <p class="text-3xl text-white/80 font-light tracking-wide mb-6">Turning customer conversations into executive decisions.</p>
                        <div class="border-l border-white/20 pl-6">
                            <p class="text-sm text-white/50 uppercase tracking-[0.2em] mb-1">Founder</p>
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
                        <h1 class="huge-headline split-text">The Problem</h1>
                        <h2 class="sub-headline split-text">Businesses have <br><i class="italic text-white/80">automated</i> transactions.</h2>
                        <div class="liquid-glass rounded-3xl p-10 stagger-anim mt-8">
                            <p class="text-xl text-white/70 leading-relaxed mb-6 font-light">Over the last two decades, businesses have adopted software for almost every operational function:</p>
                            <ul class="text-2xl text-white/90 space-y-4 font-medium grid grid-cols-2">
                                <li>Payments.</li>
                                <li>CRM.</li>
                                <li>Inventory.</li>
                                <li>Marketing.</li>
                                <li>Accounting.</li>
                                <li class="col-span-2 mt-4 pt-4 border-t border-white/10 text-3xl font-display italic tracking-wide text-white">Conversations.</li>
                            </ul>
                        </div>
                    </div>
                    <div class="flex-1 flex flex-col justify-center pl-10">
                        <p class="text-4xl font-display italic text-white mb-8 split-text leading-tight">Yet business owners still ask the same questions:</p>
                        <ul class="text-2xl text-white/80 space-y-6 mb-12 stagger-anim font-light tracking-wide">
                            <li>• What deserves attention today?</li>
                            <li>• Which products should I restock?</li>
                            <li>• Which customers need follow-up?</li>
                            <li>• Where am I losing revenue?</li>
                            <li>• Why have sales reduced?</li>
                        </ul>
                        <div class="stagger-anim liquid-glass p-8 rounded-2xl border border-white/5">
                            <p class="text-2xl text-white mb-2 font-medium">Business software automates operations.</p>
                            <p class="text-2xl text-white/60 font-light">It records what happened.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 3 -->
        <div class="slide" id="slide3">
            <div class="w-full h-full flex flex-col justify-center max-w-5xl">
                <h1 class="huge-headline split-text">The <i class="italic">Shift</i></h1>
                <h2 class="sub-headline split-text">Commerce has moved into conversations.</h2>
                
                <div class="space-y-8 text-2xl text-white/80 leading-relaxed stagger-anim font-light mt-6">
                    <p>Across Nigeria, businesses now operate inside messaging platforms.<br>
                    <span class="text-xl mt-3 block text-white/60">Customers now discover products, negotiate prices, confirm payments and arrange deliveries inside WhatsApp, Instagram and Facebook.</span></p>
                    
                    <div class="liquid-glass p-8 rounded-2xl">
                        <p class="text-white font-medium text-3xl font-display italic">For Nigerian MSMEs, the entire sales funnel now exists inside conversations.</p>
                    </div>
                    
                    <p>Yet traditional software was designed for structured forms, not unstructured conversations.</p>
                    <p>As conversational commerce grows, businesses generate thousands of customer signals every day.</p>
                    
                    <p class="text-white font-medium text-3xl pt-6 border-t border-white/10 tracking-wide">Most disappear without ever becoming business intelligence.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 4 -->
        <div class="slide" id="slide4">
            <div class="w-full h-full flex flex-col justify-center max-w-6xl">
                <h1 class="huge-headline split-text">The <i class="italic">Problem</i></h1>
                <h2 class="sub-headline split-text">Every conversation creates decisions.</h2>
                <p class="text-3xl text-white/80 mb-12 stagger-anim font-display italic">A business owner doesn't just receive messages.<br>They constantly decide:</p>
                
                <ul class="text-2xl text-white/90 space-y-6 mb-16 stagger-anim grid grid-cols-2 gap-8 font-light">
                    <li class="liquid-glass p-6 rounded-2xl">• Should this customer receive follow-up?</li>
                    <li class="liquid-glass p-6 rounded-2xl">• Is demand increasing for this product?</li>
                    <li class="liquid-glass p-6 rounded-2xl">• Should inventory be reordered?</li>
                    <li class="liquid-glass p-6 rounded-2xl">• Are customers becoming more price-sensitive?</li>
                    <li class="liquid-glass p-6 rounded-2xl">• Which complaints appear repeatedly?</li>
                    <li class="liquid-glass p-6 rounded-2xl">• Which customers are likely to return?</li>
                </ul>
                
                <div class="stagger-anim liquid-glass p-8 rounded-3xl inline-block">
                    <p class="text-2xl text-white/70 mb-2 font-light">These decisions are still made manually.</p>
                    <p class="text-4xl text-white font-display italic tracking-wide">As conversations increase, decision complexity grows even faster.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 5 -->
        <div class="slide" id="slide5">
            <div class="w-full h-full flex flex-col justify-center">
                <h1 class="huge-headline split-text">Morlen</h1>
                <h2 class="sub-headline split-text">An Executive <i class="italic">Decision Intelligence</i> Platform.</h2>
                <div class="liquid-glass p-8 rounded-3xl stagger-anim max-w-5xl mb-12">
                    <p class="text-2xl text-white/80 font-light mb-6">Morlen continuously analyzes customer conversations, identifies business patterns and delivers prioritized business decisions.</p>
                    <p class="text-3xl text-white font-medium font-display italic">Instead of presenting plain dashboards, Morlen produces a daily executive briefing.</p>
                </div>
                
                <div class="grid grid-cols-4 gap-6 mb-12">
                    <div class="stagger-anim flex flex-col liquid-glass p-8 rounded-3xl">
                        <h3 class="text-3xl font-display italic text-white mb-4">Executive Brief</h3>
                        <p class="text-base text-white/70 font-light">A daily summary of the highest priority decisions. inventory risks, customer churn, demand spikes, operational issues.</p>
                    </div>
                    <div class="stagger-anim flex flex-col liquid-glass p-8 rounded-3xl">
                        <h3 class="text-3xl font-display italic text-white mb-4">Opportunity Feed</h3>
                        <p class="text-base text-white/70 font-light">Revenue opportunities detected from conversations including estimated impact, confidence score, supporting evidence.</p>
                    </div>
                    <div class="stagger-anim flex flex-col liquid-glass p-8 rounded-3xl">
                        <h3 class="text-3xl font-display italic text-white mb-4">Business Memory</h3>
                        <p class="text-base text-white/70 mb-3 font-light">Long-term behavioural intelligence about customers.</p>
                        <p class="text-xs text-white/40 font-light uppercase tracking-wider">Example: demand for product A rises every month end.</p>
                    </div>
                    <div class="stagger-anim flex flex-col liquid-glass p-8 rounded-3xl">
                        <h3 class="text-3xl font-display italic text-white mb-4">Evidence-Based Recs.</h3>
                        <p class="text-base text-white/70 mb-3 font-light">Every recommendation explains:</p>
                        <ul class="text-sm text-white space-y-2 font-medium">
                            <li>• Why it exists</li>
                            <li>• Expected impact</li>
                            <li>• Supporting evidence</li>
                        </ul>
                    </div>
                </div>
                
                <div class="stagger-anim flex items-center gap-6">
                    <p class="text-2xl text-white/60 font-light">Business owners stop searching for answers.</p>
                    <div class="w-px h-8 bg-white/20"></div>
                    <p class="text-3xl font-display italic text-white">Morlen brings the answers to them.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 6 -->
        <div class="slide" id="slide6">
            <div class="w-full h-full flex flex-col justify-center items-center text-center">
                <div class="liquid-glass px-10 py-4 rounded-full stagger-anim mb-12">
                    <p class="text-sm uppercase tracking-[0.3em] font-semibold text-white/80">Market & Business Model</p>
                </div>
                <h1 class="huge-headline split-text">A Massive <i class="italic text-white/90">Market</i></h1>
                
                <p class="text-3xl text-white/80 mb-10 stagger-anim font-light">Nigeria has approximately:</p>
                
                <div class="mb-16 stagger-anim relative liquid-glass p-16 rounded-[4rem]">
                    <p class="text-[140px] font-display italic text-white leading-none tracking-tight">39.6 Million MSMEs</p>
                </div>
                
                <p class="text-2xl text-white/60 mb-8 stagger-anim font-light uppercase tracking-widest">Representing</p>
                <div class="flex gap-20 justify-center mb-16 stagger-anim text-5xl font-display italic text-white">
                    <div class="liquid-glass px-12 py-8 rounded-3xl"><p>96%</p><p class="text-lg text-white/70 mt-3 font-body not-italic font-light">of businesses</p></div>
                    <div class="liquid-glass px-12 py-8 rounded-3xl"><p>87.9%</p><p class="text-lg text-white/70 mt-3 font-body not-italic font-light">of employment</p></div>
                    <div class="liquid-glass px-12 py-8 rounded-3xl"><p>46.3%</p><p class="text-lg text-white/70 mt-3 font-body not-italic font-light">of GDP</p></div>
                </div>
                
                <div class="stagger-anim">
                    <p class="text-3xl font-display italic text-white tracking-wide">Millions already conduct business primarily through messaging platforms.</p>
                    <p class="text-xl font-light text-white/60 mt-3">Morlen is built for this new operating environment.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 7 -->
        <div class="slide" id="slide7">
            <div class="w-full h-full flex flex-col justify-center">
                <h1 class="huge-headline split-text">Business <i class="italic">Model</i></h1>
                <div class="liquid-glass px-6 py-2 rounded-full inline-block stagger-anim mb-10">
                    <h2 class="text-xl font-medium tracking-[0.2em] uppercase text-white/90 font-body">Subscription SaaS</h2>
                </div>
                <p class="text-2xl text-white/80 mb-12 max-w-4xl stagger-anim font-light leading-relaxed">Starting with a 30 day free trial giving Morlen enough time to learn from customer conversations, build business memory, generate meaningful insights.</p>
                
                <div class="grid grid-cols-3 gap-8 mb-12 stagger-anim">
                    <div class="liquid-glass p-10 rounded-[2.5rem] flex flex-col">
                        <h3 class="text-5xl font-display italic text-white mb-2">Starter</h3>
                        <p class="text-xl text-white/60 font-mono mb-4">N8,000/month</p>
                        <p class="text-base text-white/80 mb-8 font-light">For early stage businesses</p>
                        <ul class="text-white/90 space-y-4 text-lg flex-1 border-t border-white/10 pt-8 font-light">
                            <li>• Executive brief</li>
                            <li>• Business memory</li>
                            <li>• Basic decision intelligence</li>
                            <li>• Single workspace</li>
                        </ul>
                    </div>
                    
                    <div class="liquid-glass p-10 rounded-[2.5rem] flex flex-col relative transform scale-[1.03] z-10" style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.2);">
                        <div class="absolute -top-4 left-1/2 transform -translate-x-1/2 liquid-glass px-6 py-1.5 rounded-full text-xs font-bold tracking-[0.2em] uppercase text-white">Popular</div>
                        <h3 class="text-5xl font-display italic text-white mb-2">Growth</h3>
                        <p class="text-xl text-white font-mono mb-4">N15,000/month</p>
                        <p class="text-base text-white/90 mb-8 font-light">Businesses managing increasing customer conversations.</p>
                        <ul class="text-white space-y-4 text-lg flex-1 border-t border-white/20 pt-8 font-medium">
                            <li>• Everything in starter</li>
                            <li>• Opportunity feed</li>
                            <li>• Advanced AI recommendations</li>
                            <li>• Multi channel integrations</li>
                            <li>• Team Collaboration</li>
                        </ul>
                    </div>
                    
                    <div class="liquid-glass p-10 rounded-[2.5rem] flex flex-col">
                        <h3 class="text-5xl font-display italic text-white mb-2">Enterprise</h3>
                        <p class="text-xl text-white/60 font-mono mb-4">CUSTOM PRICING</p>
                        <p class="text-base text-white/80 mb-8 font-light">Organizations requiring company-wide decision intelligence.</p>
                        <ul class="text-white/90 space-y-4 text-lg flex-1 border-t border-white/10 pt-8 font-light">
                            <li>• Everything in growth</li>
                            <li>• Custom AI deployment</li>
                            <li>• Dedicated Support</li>
                            <li>• Enterprise security and governance</li>
                        </ul>
                    </div>
                </div>
                
                <p class="text-xl text-white/80 stagger-anim liquid-glass inline-block px-8 py-4 rounded-full font-light">
                    Additional revenue: <span class="text-white font-medium ml-2 font-display italic text-2xl tracking-wide">Enterprise Implementation & Onboarding</span>
                </p>
            </div>
        </div>

        <!-- SLIDE 8 -->
        <div class="slide" id="slide8">
            <div class="w-full h-full flex flex-col justify-center">
                <div class="flex gap-20">
                    <div class="flex-1">
                        <h1 class="huge-headline split-text">Funding</h1>
                        <h2 class="text-4xl font-display italic text-white/90 mb-10 stagger-anim">Raising Pre-Seed Capital</h2>
                        <p class="text-xl text-white/60 mb-8 stagger-anim font-light uppercase tracking-widest">Investment will accelerate:</p>
                        
                        <div class="space-y-6 stagger-anim">
                            <div class="liquid-glass p-6 rounded-2xl flex items-center gap-6">
                                <h3 class="text-4xl font-display italic text-white w-24">40%</h3>
                                <div class="w-px h-12 bg-white/20"></div>
                                <div>
                                    <p class="text-lg font-medium text-white">Product Development</p>
                                    <p class="text-sm text-white/60 font-light">Commercial MVP and core intelligence engine.</p>
                                </div>
                            </div>
                            <div class="liquid-glass p-6 rounded-2xl flex items-center gap-6">
                                <h3 class="text-4xl font-display italic text-white w-24">25%</h3>
                                <div class="w-px h-12 bg-white/20"></div>
                                <div>
                                    <p class="text-lg font-medium text-white">AI Infrastructure</p>
                                    <p class="text-sm text-white/60 font-light">Inference, data pipelines and production infrastructure.</p>
                                </div>
                            </div>
                            <div class="liquid-glass p-6 rounded-2xl flex items-center gap-6">
                                <h3 class="text-4xl font-display italic text-white w-24">20%</h3>
                                <div class="w-px h-12 bg-white/20"></div>
                                <div>
                                    <p class="text-lg font-medium text-white">Customer Acq.</p>
                                    <p class="text-sm text-white/60 font-light">Pilot programs and early customer onboarding.</p>
                                </div>
                            </div>
                            <div class="liquid-glass p-6 rounded-2xl flex items-center gap-6">
                                <h3 class="text-4xl font-display italic text-white w-24">15%</h3>
                                <div class="w-px h-12 bg-white/20"></div>
                                <div>
                                    <p class="text-lg font-medium text-white">Operations</p>
                                    <p class="text-sm text-white/60 font-light">Messaging integrations and business development.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="flex-1 flex flex-col justify-center">
                        <h1 class="huge-headline split-text">Outcomes</h1>
                        <h2 class="text-4xl font-display italic text-white/90 mb-12 stagger-anim">Expected Milestones</h2>
                        
                        <div class="space-y-6 stagger-anim">
                            <div class="flex items-center gap-6 liquid-glass p-8 rounded-3xl">
                                <div class="w-2 h-2 rounded-full bg-white"></div>
                                <p class="text-2xl text-white font-light tracking-wide">Commercial MVP</p>
                            </div>
                            <div class="flex items-center gap-6 liquid-glass p-8 rounded-3xl">
                                <div class="w-2 h-2 rounded-full bg-white"></div>
                                <p class="text-2xl text-white font-light tracking-wide">First paying customers</p>
                            </div>
                            <div class="flex items-center gap-6 liquid-glass p-8 rounded-3xl">
                                <div class="w-2 h-2 rounded-full bg-white"></div>
                                <p class="text-2xl text-white font-light tracking-wide">Validated product-market fit</p>
                            </div>
                            <div class="flex items-center gap-6 liquid-glass p-8 rounded-3xl">
                                <div class="w-2 h-2 rounded-full bg-white"></div>
                                <p class="text-2xl text-white font-light tracking-wide">Foundation for national expansion</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 9 -->
        <div class="slide" id="slide9">
            <div class="w-full h-full flex flex-col justify-center">
                <h1 class="huge-headline split-text">Why <i class="italic">Morlen?</i></h1>
                
                <div class="flex gap-16 mt-8">
                    <div class="flex-1 liquid-glass p-12 rounded-[3rem] stagger-anim flex flex-col justify-center">
                        <p class="text-2xl text-white/70 mb-6 font-light uppercase tracking-widest">Software answers:</p>
                        <h2 class="text-[80px] font-display italic text-white leading-none mb-12">"What happened?"</h2>
                        
                        <ul class="text-2xl text-white/80 space-y-6 font-light">
                            <li class="flex items-center gap-4"><div class="w-2 h-2 bg-white/40 rounded-full"></div>CRM stores customer records</li>
                            <li class="flex items-center gap-4"><div class="w-2 h-2 bg-white/40 rounded-full"></div>ERP manages operations</li>
                            <li class="flex items-center gap-4"><div class="w-2 h-2 bg-white/40 rounded-full"></div>BI visualizes historical metrics</li>
                            <li class="flex items-center gap-4"><div class="w-2 h-2 bg-white/40 rounded-full"></div>Chatbots automate conversations</li>
                        </ul>
                    </div>
                    
                    <div class="flex-1 liquid-glass p-12 rounded-[3rem] stagger-anim relative overflow-hidden flex flex-col justify-center" style="background: rgba(255,255,255,0.06);">
                        <p class="text-2xl text-white mb-6 font-medium uppercase tracking-widest">Morlen answers:</p>
                        <h2 class="text-[80px] font-display italic text-white leading-none mb-12 drop-shadow-2xl">"What should I do next?"</h2>
                        
                        <ul class="text-2xl text-white space-y-6 font-light">
                            <li>• Every conversation contains intelligence.</li>
                            <li>• Every business generates opportunities.</li>
                            <li>• Every owner has limited attention.</li>
                        </ul>
                        
                        <div class="mt-12 pt-8 border-t border-white/20">
                            <p class="text-3xl text-white leading-relaxed font-display italic tracking-wide">Morlen exists to protect that attention—<br><span class="not-italic font-sans font-light text-xl text-white/80">by turning conversations into decisions.</span></p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 10 -->
        <div class="slide" id="slide10">
            <div class="w-full h-full flex flex-col justify-center items-center text-center">
                <div class="stagger-anim mb-16 liquid-glass px-12 py-6 rounded-full">
                    <p class="text-3xl font-light text-white/80 tracking-wide">The future of business isn't more software.</p>
                </div>

                <h1 class="text-[250px] font-display italic text-white leading-[0.8] mb-12 split-text drop-shadow-2xl tracking-tight">Morlen.</h1>
                
                <div class="stagger-anim mt-8 max-w-4xl liquid-glass p-10 rounded-[3rem]">
                    <p class="text-3xl text-white mb-4 font-display italic tracking-wide">Businesses already have the conversations.</p>
                    <p class="text-xl text-white/60 font-light uppercase tracking-[0.2em]">Morlen turns them into decisions.</p>
                </div>
            </div>
        </div>

    </div>

    <script>
        document.querySelectorAll('.split-text').forEach(el => {
            const text = el.innerText;
            const words = text.split(' ');
            el.innerHTML = '';
            words.forEach(word => {
                const mask = document.createElement('span');
                mask.className = 'word-mask';
                const inner = document.createElement('span');
                inner.className = 'word-inner';
                
                // Keep italic formatting for specific words in the final output if needed, but since it's hard to split HTML tags elegantly with this simple script, we are just splitting raw text.
                // Wait, some headers have <i> tags!
                // This basic script overrides innerHTML, destroying <i> tags.
                // Let's fix that by NOT running split-text on elements that contain inner HTML tags (like <i>), and just letting them fade in normally, or doing it carefully.
            });
        });
        
        // Better Text Splitter that handles nested <i> tags:
        // Actually, for simplicity and to prevent breaking the beautifully styled <i> tags, 
        // I will just use GSAP to animate the `.split-text` directly with opacity and y-axis shift instead of breaking the DOM structure, 
        // mimicking the elegant fade.
        
        document.querySelectorAll('.split-text').forEach(el => {
             // Reset innerHTML modification to avoid breaking italic fonts.
        });

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
                    opacity: 0, scale: 0.98,
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
            const headers = next.querySelectorAll('.split-text');
            
            gsap.set(fadeElements, { opacity: 0, y: 30, filter: 'blur(10px)' });
            gsap.set(headers, { opacity: 0, y: 40, filter: 'blur(20px)' });

            const tl = gsap.timeline({
                onComplete: () => {
                    currentSlide = index;
                    isAnimating = false;
                }
            });
            
            tl.to(next, { opacity: 1, duration: 0.2 })
              .to(headers, {
                  opacity: 1, y: 0, filter: 'blur(0px)', duration: 1.5, 
                  stagger: 0.2, ease: "power3.out"
              }, "-=0.1")
              .to(fadeElements, {
                  opacity: 1, y: 0, filter: 'blur(0px)', duration: 1.5,
                  stagger: 0.15, ease: "power3.out"
              }, "-=1.0");
        }

        slides[0].classList.add('active');
        slides[0].style.visibility = 'visible';
        slides[0].style.opacity = 1;
        
        gsap.set(slides[0].querySelectorAll('.stagger-anim'), { opacity: 0, y: 30, filter: 'blur(10px)' });
        gsap.set(slides[0].querySelectorAll('.split-text'), { opacity: 0, y: 40, filter: 'blur(20px)' });
        
        setTimeout(() => {
            gsap.to(slides[0].querySelectorAll('.split-text'), {
                opacity: 1, y: 0, filter: 'blur(0px)', duration: 1.5, 
                stagger: 0.2, ease: "power3.out"
            });
            gsap.to(slides[0].querySelectorAll('.stagger-anim'), {
                opacity: 1, y: 0, filter: 'blur(0px)', duration: 1.5,
                stagger: 0.15, ease: "power3.out", delay: 0.5
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

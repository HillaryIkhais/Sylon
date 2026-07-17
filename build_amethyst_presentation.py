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
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        display: ['Outfit', 'sans-serif'],
                        body: ['Plus Jakarta Sans', 'sans-serif'],
                    },
                    colors: {
                        plum: '#0D041A',
                        amethyst: '#1A0B2E',
                        eggplant: '#2D1445',
                        rosegold: '#F4D0B4',
                        copper: '#E0A96D',
                        blush: '#FFF5F5'
                    }
                }
            }
        }
    </script>

    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            background-color: #0D041A;
            color: #FFF5F5;
            font-family: 'Plus Jakarta Sans', sans-serif;
            overflow: hidden;
            width: 100vw;
            height: 100vh;
        }

        #presentation-container {
            width: 1920px;
            height: 1080px;
            position: relative;
            background: radial-gradient(circle at 100% 0%, #1A0B2E 0%, #0D041A 100%);
            overflow: hidden;
        }

        /* Deep atmospheric glowing orbs for rich, nuanced texture */
        .glow-orb {
            position: absolute;
            border-radius: 50%;
            filter: blur(140px);
            opacity: 0.25;
            z-index: 0;
            pointer-events: none;
            animation: float 25s infinite ease-in-out alternate;
        }
        .orb-1 { width: 900px; height: 900px; background: #2D1445; top: -300px; right: -200px; }
        .orb-2 { width: 700px; height: 700px; background: #E0A96D; bottom: -200px; left: -200px; animation-delay: -12s; opacity: 0.1; }

        /* Metallic Rose Gold Typography */
        .text-rosegold-gradient {
            background: linear-gradient(135deg, #F4D0B4 0%, #E0A96D 50%, #C27A7E 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-shadow: 0 4px 20px rgba(224, 169, 109, 0.2);
        }

        /* Diagonal dynamic lines for structure */
        .glass-panel {
            position: absolute;
            background: linear-gradient(135deg, rgba(255,255,255,0.02) 0%, transparent 100%);
            backdrop-filter: blur(30px);
            border-left: 1px solid rgba(244, 208, 180, 0.15);
            border-top: 1px solid rgba(244, 208, 180, 0.15);
            z-index: 1;
            border-radius: 40px;
        }
        
        .panel-bg-1 { width: 85vw; height: 130vh; top: -15vh; right: -10vw; transform: rotate(10deg); }

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
            font-size: 90px;
            font-weight: 700;
            line-height: 1.1;
            color: #F4D0B4;
            margin-bottom: 40px;
            letter-spacing: -0.02em;
        }
        
        .sub-headline {
            font-size: 50px;
            font-weight: 500;
            color: #FFF5F5;
            margin-bottom: 24px;
            line-height: 1.2;
        }

        /* Pricing Card Design */
        .pricing-card {
            background: rgba(26, 11, 46, 0.6);
            border: 1px solid rgba(244, 208, 180, 0.15);
            border-top: 1px solid rgba(244, 208, 180, 0.3);
            border-radius: 24px;
            position: relative;
            backdrop-filter: blur(40px);
            box-shadow: 0 30px 60px rgba(0,0,0,0.4);
        }
        
        .word-mask { display: inline-block; overflow: hidden; vertical-align: top; padding-bottom: 8px; }
        .word-inner { display: inline-block; transform: translateY(100%); }

    </style>
</head>
<body>

    <div id="presentation-container">
        <!-- Background Elements -->
        <div class="glow-orb orb-1"></div>
        <div class="glow-orb orb-2"></div>
        <div class="glass-panel panel-bg-1"></div>

        <!-- SLIDE 1 -->
        <div class="slide" id="slide1">
            <div class="w-full h-full flex flex-col justify-center relative z-10">
                <div class="max-w-4xl">
                    <h1 class="huge-headline text-rosegold-gradient split-text text-[110px]">Morlen</h1>
                    <p class="sub-headline split-text">The Operating System for Business Decisions.</p>
                    <p class="text-3xl text-blush/80 mb-20 stagger-anim font-light">Turning customer conversations into executive decisions.</p>
                    
                    <div class="stagger-anim border-l-4 border-copper pl-6">
                        <p class="text-lg text-rosegold/70 uppercase tracking-widest font-semibold mb-2">Founder Name</p>
                        <p class="text-3xl text-blush font-medium">Hillary Ikhais</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 2 -->
        <div class="slide" id="slide2">
            <div class="w-full h-full flex flex-col justify-center relative z-10">
                <div class="flex gap-20">
                    <div class="flex-1">
                        <h1 class="huge-headline text-rosegold-gradient split-text">The Problem</h1>
                        <h2 class="sub-headline split-text">Businesses have automated transactions.</h2>
                        <p class="text-2xl text-blush/80 leading-relaxed mb-10 stagger-anim font-light">Over the last two decades, businesses have adopted software for almost every operational function:</p>
                        
                        <div class="stagger-anim">
                            <ul class="text-3xl text-blush/90 space-y-5 font-medium grid grid-cols-2">
                                <li class="flex items-center gap-4"><div class="w-2.5 h-2.5 rounded-full bg-copper"></div>Payments.</li>
                                <li class="flex items-center gap-4"><div class="w-2.5 h-2.5 rounded-full bg-copper"></div>CRM.</li>
                                <li class="flex items-center gap-4"><div class="w-2.5 h-2.5 rounded-full bg-copper"></div>Inventory.</li>
                                <li class="flex items-center gap-4"><div class="w-2.5 h-2.5 rounded-full bg-copper"></div>Marketing.</li>
                                <li class="flex items-center gap-4"><div class="w-2.5 h-2.5 rounded-full bg-copper"></div>Accounting.</li>
                                <li class="flex items-center gap-4 text-rosegold col-span-2 mt-6 pt-6 border-t border-rosegold/20 text-4xl"><div class="w-3 h-3 rounded-full bg-rosegold shadow-[0_0_15px_rgba(244,208,180,0.5)]"></div>Conversations</li>
                            </ul>
                        </div>
                    </div>
                    <div class="flex-1 pt-6 border-l border-rosegold/10 pl-16">
                        <p class="text-4xl font-medium text-blush mb-10 split-text leading-tight">Yet business owners still ask the same questions:</p>
                        <ul class="text-3xl text-blush/80 space-y-8 mb-16 stagger-anim font-light">
                            <li>• What deserves attention today?</li>
                            <li>• Which products should I restock?</li>
                            <li>• Which customers need follow-up?</li>
                            <li>• Where am I losing revenue?</li>
                            <li>• Why have sales reduced?</li>
                        </ul>
                        <div class="stagger-anim bg-eggplant/40 p-8 rounded-2xl border border-rosegold/20 shadow-2xl backdrop-blur-md">
                            <p class="text-3xl text-blush mb-2 font-medium">Business software automates operations.</p>
                            <p class="text-3xl text-copper font-medium">It records what happened</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 3 -->
        <div class="slide" id="slide3">
            <div class="w-full h-full flex flex-col justify-center max-w-5xl relative z-10">
                <h1 class="huge-headline text-rosegold-gradient split-text">THE SHIFT</h1>
                <h2 class="sub-headline split-text">Commerce has moved into conversations</h2>
                
                <div class="space-y-10 text-3xl text-blush/80 leading-relaxed stagger-anim font-light">
                    <p>Across Nigeria, businesses now operate inside messaging platforms.<br>
                    <span class="text-2xl mt-4 block text-blush/70">Customers now discover products, negotiate prices, confirm payments and arrange deliveries inside WhatsApp, Instagram and Facebook.</span></p>
                    
                    <div class="bg-eggplant/50 border-l-4 border-copper p-8 rounded-r-2xl shadow-xl">
                        <p class="text-blush font-medium">For Nigerian MSMEs, the entire sales funnel now exists inside conversations.</p>
                    </div>
                    
                    <p class="text-2xl">Yet traditional software was designed for structured forms, not unstructured conversations.</p>
                    
                    <p class="text-2xl">As conversational commerce grows, businesses generate thousands of customer signals every day.</p>
                    
                    <p class="text-rosegold font-medium text-4xl pt-6 border-t border-rosegold/20">Most disappear without ever becoming business intelligence.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 4 -->
        <div class="slide" id="slide4">
            <div class="w-full h-full flex flex-col justify-center max-w-6xl relative z-10">
                <h1 class="huge-headline text-rosegold-gradient split-text">THE PROBLEM</h1>
                <h2 class="sub-headline split-text">Every conversation creates decisions.</h2>
                <p class="text-3xl text-blush/80 mb-12 stagger-anim font-light">A business owner doesn't just receive messages.<br>They constantly decide:</p>
                
                <ul class="text-3xl text-blush space-y-6 mb-16 stagger-anim grid grid-cols-2 gap-8 font-medium">
                    <li class="bg-amethyst/80 p-6 rounded-2xl border border-white/5 shadow-lg">• Should this customer receive follow-up?</li>
                    <li class="bg-amethyst/80 p-6 rounded-2xl border border-white/5 shadow-lg">• Is demand increasing for this product?</li>
                    <li class="bg-amethyst/80 p-6 rounded-2xl border border-white/5 shadow-lg">• Should inventory be reordered?</li>
                    <li class="bg-amethyst/80 p-6 rounded-2xl border border-white/5 shadow-lg">• Are customers becoming more price-sensitive?</li>
                    <li class="bg-amethyst/80 p-6 rounded-2xl border border-white/5 shadow-lg">• Which complaints appear repeatedly?</li>
                    <li class="bg-amethyst/80 p-6 rounded-2xl border border-white/5 shadow-lg">• Which customers are likely to return?</li>
                </ul>
                
                <div class="stagger-anim">
                    <p class="text-3xl text-blush/80 mb-3 font-light">These decisions are still made manually.</p>
                    <p class="text-4xl text-copper font-medium">As conversations increase,<br>Decision complexity grows even faster.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 5 -->
        <div class="slide" id="slide5">
            <div class="w-full h-full flex flex-col justify-center relative z-10">
                <h1 class="huge-headline text-rosegold-gradient split-text">MORLEN</h1>
                <h2 class="sub-headline split-text">Morlen is an Executive Decision Intelligence Platform.</h2>
                <p class="text-2xl text-blush/80 mb-8 max-w-5xl stagger-anim font-light">Morlen continuously analyzes customer conversations, identifies business patterns and delivers prioritized business decisions.</p>
                <p class="text-3xl text-blush font-medium mb-16 max-w-5xl stagger-anim">Instead of presenting plain dashboards,<br><span class="text-copper">Morlen produces a daily executive briefing.</span></p>
                
                <div class="grid grid-cols-4 gap-8 mb-16">
                    <div class="stagger-anim flex flex-col bg-eggplant/30 p-8 rounded-3xl border border-rosegold/10 shadow-xl backdrop-blur-md">
                        <h3 class="text-2xl font-semibold text-rosegold mb-4">Executive Brief</h3>
                        <p class="text-lg text-blush/90 font-light">A daily summary of the highest priority decisions. inventory risks, customer churn, demand spikes, operational issues.</p>
                    </div>
                    <div class="stagger-anim flex flex-col bg-eggplant/30 p-8 rounded-3xl border border-rosegold/10 shadow-xl backdrop-blur-md">
                        <h3 class="text-2xl font-semibold text-rosegold mb-4">Opportunity Feed</h3>
                        <p class="text-lg text-blush/90 font-light">Revenue opportunities detected from conversations including estimated impact, confidence score, supporting evidence.</p>
                    </div>
                    <div class="stagger-anim flex flex-col bg-eggplant/30 p-8 rounded-3xl border border-rosegold/10 shadow-xl backdrop-blur-md">
                        <h3 class="text-2xl font-semibold text-rosegold mb-4">Business Memory</h3>
                        <p class="text-lg text-blush/90 mb-3 font-medium">Long-term behavioural intelligence about customers.</p>
                        <p class="text-sm text-blush/60 font-light">for example customers increasingly ask for same day delivery, demand for product A rises every month end...</p>
                    </div>
                    <div class="stagger-anim flex flex-col bg-eggplant/30 p-8 rounded-3xl border border-rosegold/10 shadow-xl backdrop-blur-md">
                        <h3 class="text-2xl font-semibold text-rosegold mb-4">Evidence-Based Recommendations</h3>
                        <p class="text-lg text-blush/90 mb-3 font-light">Every recommendation explains:</p>
                        <ul class="text-base text-blush space-y-2 font-medium">
                            <li>• Why it exists</li>
                            <li>• Expected impact</li>
                            <li>• Supporting evidence</li>
                        </ul>
                    </div>
                </div>
                
                <div class="stagger-anim">
                    <p class="text-3xl text-blush/80 mb-2 font-light">Business owners stop searching for answers.</p>
                    <p class="text-4xl font-semibold text-copper">Morlen brings the answers to them.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 6 -->
        <div class="slide" id="slide6">
            <div class="w-full h-full flex flex-col justify-center items-center text-center relative z-10">
                <h1 class="huge-headline text-rosegold-gradient split-text text-[80px]">MARKET & BUSINESS MODEL</h1>
                <h2 class="sub-headline split-text mb-16">A Massive Market</h2>
                
                <p class="text-4xl text-blush/80 mb-10 stagger-anim font-light">Nigeria has approximately:</p>
                
                <div class="mb-20 stagger-anim relative">
                    <p class="text-[150px] font-bold text-rosegold leading-none tracking-tighter drop-shadow-[0_0_40px_rgba(244,208,180,0.15)]">39.6 Million MSMEs</p>
                </div>
                
                <p class="text-3xl text-blush/80 mb-10 stagger-anim font-light">Representing:</p>
                <div class="flex gap-24 justify-center mb-20 stagger-anim text-5xl text-blush font-semibold">
                    <div><p>96%</p><p class="text-2xl text-copper mt-4 font-normal">of businesses</p></div>
                    <div class="w-px h-24 bg-copper/20"></div>
                    <div><p>87.9%</p><p class="text-2xl text-copper mt-4 font-normal">of employment</p></div>
                    <div class="w-px h-24 bg-copper/20"></div>
                    <div><p>46.3%</p><p class="text-2xl text-copper mt-4 font-normal">of GDP</p></div>
                </div>
                
                <div class="stagger-anim">
                    <p class="text-3xl text-blush/80 mb-3 font-light">Millions already conduct business primarily through messaging platforms.</p>
                    <p class="text-4xl font-medium text-copper">Morlen is built for this new operating environment.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 7 -->
        <div class="slide" id="slide7">
            <div class="w-full h-full flex flex-col justify-center relative z-10">
                <h1 class="huge-headline text-rosegold-gradient split-text">Business Model</h1>
                <h2 class="sub-headline split-text">Subscription SaaS</h2>
                <p class="text-2xl text-blush/80 mb-12 max-w-5xl stagger-anim font-light">Starting with a 30 day free trial giving Morlen enough time to learn from customer conversations, build business memory, generate meaningful insights</p>
                
                <div class="grid grid-cols-3 gap-10 mb-16 stagger-anim">
                    <div class="pricing-card p-10 flex flex-col">
                        <h3 class="text-4xl font-semibold text-blush mb-2">Starter</h3>
                        <p class="text-2xl text-copper font-medium mb-4">[N8,000/month]</p>
                        <p class="text-lg text-blush/80 mb-8 font-light">For early stage businesses</p>
                        <ul class="text-blush space-y-5 text-xl flex-1 border-t border-rosegold/20 pt-8 font-medium">
                            <li>- Executive brief</li>
                            <li>- Business memory</li>
                            <li>- Basic decision intelligence</li>
                            <li>- Single workspace</li>
                        </ul>
                    </div>
                    
                    <div class="pricing-card p-10 flex flex-col border-rosegold/40 shadow-[0_0_60px_rgba(244,208,180,0.1)] transform scale-105 z-10 bg-eggplant/80">
                        <div class="absolute -top-4 left-1/2 transform -translate-x-1/2 bg-rosegold text-plum px-6 py-1 rounded-full text-sm font-bold tracking-widest uppercase">Popular</div>
                        <h3 class="text-4xl font-semibold text-blush mb-2">Growth</h3>
                        <p class="text-2xl text-copper font-bold mb-4">[N15,000/month]</p>
                        <p class="text-lg text-blush/90 mb-8 font-light">Businesses managing increasing customer conversations.</p>
                        <ul class="text-blush space-y-5 text-xl flex-1 border-t border-rosegold/30 pt-8 font-semibold">
                            <li>- Everything in starter</li>
                            <li>- Opportunity feed</li>
                            <li>- Advanced AI recommendations</li>
                            <li>- Multi channel integrations</li>
                            <li>- Team Collaboration</li>
                        </ul>
                    </div>
                    
                    <div class="pricing-card p-10 flex flex-col">
                        <h3 class="text-4xl font-semibold text-blush mb-2">Enterprise</h3>
                        <p class="text-2xl text-copper font-medium mb-4">[CUSTOM PRICING]</p>
                        <p class="text-lg text-blush/80 mb-8 font-light">Organizations requiring company-wide decision intelligence and integrations.</p>
                        <ul class="text-blush space-y-5 text-xl flex-1 border-t border-rosegold/20 pt-8 font-medium">
                            <li>- Everything in growth</li>
                            <li>- Custom AI deployment</li>
                            <li>- Dedicate Support</li>
                            <li>- Enterprise security and governance</li>
                        </ul>
                    </div>
                </div>
                
                <p class="text-2xl text-blush/80 stagger-anim bg-eggplant/40 inline-block px-8 py-4 rounded-xl border border-rosegold/10 font-light backdrop-blur-md">
                    Additional revenue: <span class="text-copper font-medium ml-2">• Enterprise Implementation & Onboarding</span>
                </p>
            </div>
        </div>

        <!-- SLIDE 8 -->
        <div class="slide" id="slide8">
            <div class="w-full h-full flex flex-col justify-center relative z-10">
                <h1 class="huge-headline text-rosegold-gradient split-text text-[90px]">FUNDING & OUTCOMES</h1>
                
                <div class="flex gap-20">
                    <div class="flex-1">
                        <h2 class="text-5xl font-medium text-copper mb-10 split-text">Raising Pre-Seed Capital</h2>
                        <p class="text-3xl text-blush mb-12 stagger-anim font-light">Investment will accelerate:</p>
                        
                        <div class="space-y-8 stagger-anim">
                            <div class="bg-eggplant/40 p-6 rounded-2xl border-l-4 border-rosegold shadow-lg backdrop-blur-sm">
                                <h3 class="text-3xl font-semibold text-blush mb-2">40% — Product Development</h3>
                                <p class="text-xl text-blush/80 font-light">Complete commercial MVP and core intelligence engine.</p>
                            </div>
                            <div class="bg-eggplant/40 p-6 rounded-2xl border-l-4 border-rosegold/80 shadow-md backdrop-blur-sm">
                                <h3 class="text-3xl font-semibold text-blush mb-2">25% — AI Infrastructure</h3>
                                <p class="text-xl text-blush/80 font-light">Inference, data pipelines and production infrastructure.</p>
                            </div>
                            <div class="bg-eggplant/40 p-6 rounded-2xl border-l-4 border-rosegold/60 shadow-md backdrop-blur-sm">
                                <h3 class="text-3xl font-semibold text-blush mb-2">20% — Customer Acquisition</h3>
                                <p class="text-xl text-blush/80 font-light">Pilot programs and early customer onboarding.</p>
                            </div>
                            <div class="bg-eggplant/40 p-6 rounded-2xl border-l-4 border-rosegold/40 shadow-sm backdrop-blur-sm">
                                <h3 class="text-3xl font-semibold text-blush mb-2">15% — Strategic Partnerships & Operations</h3>
                                <p class="text-xl text-blush/80 font-light">Messaging integrations and business development.</p>
                            </div>
                        </div>
                    </div>
                    
                    <div class="flex-1 pt-4 border-l border-rosegold/10 pl-20">
                        <h2 class="text-5xl font-medium text-copper mb-12 split-text">Expected Outcomes</h2>
                        
                        <div class="space-y-10 stagger-anim mt-16">
                            <div class="flex items-center gap-8 bg-eggplant/30 p-8 rounded-2xl border border-rosegold/10 shadow-lg">
                                <div class="w-8 h-8 rounded-full bg-rosegold shadow-[0_0_20px_rgba(244,208,180,0.5)] flex-shrink-0"></div>
                                <p class="text-4xl text-blush font-medium">Commercial MVP</p>
                            </div>
                            <div class="flex items-center gap-8 bg-eggplant/30 p-8 rounded-2xl border border-rosegold/10 shadow-lg">
                                <div class="w-8 h-8 rounded-full bg-rosegold shadow-[0_0_20px_rgba(244,208,180,0.5)] flex-shrink-0"></div>
                                <p class="text-4xl text-blush font-medium">First paying customers</p>
                            </div>
                            <div class="flex items-center gap-8 bg-eggplant/30 p-8 rounded-2xl border border-rosegold/10 shadow-lg">
                                <div class="w-8 h-8 rounded-full bg-rosegold shadow-[0_0_20px_rgba(244,208,180,0.5)] flex-shrink-0"></div>
                                <p class="text-4xl text-blush font-medium">Validated product-market fit</p>
                            </div>
                            <div class="flex items-center gap-8 bg-eggplant/30 p-8 rounded-2xl border border-rosegold/10 shadow-lg">
                                <div class="w-8 h-8 rounded-full bg-rosegold shadow-[0_0_20px_rgba(244,208,180,0.5)] flex-shrink-0"></div>
                                <p class="text-4xl text-blush font-medium">Foundation for national expansion</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 9 -->
        <div class="slide" id="slide9">
            <div class="w-full h-full flex flex-col justify-center relative z-10">
                <h1 class="huge-headline text-rosegold-gradient split-text">WHY MORLEN?</h1>
                
                <div class="flex gap-24 mt-10">
                    <div class="flex-1 bg-eggplant/40 p-12 rounded-3xl border border-white/5 stagger-anim backdrop-blur-md">
                        <p class="text-3xl text-blush/80 mb-8 font-light">Business software has always answered one question:</p>
                        <h2 class="text-[72px] font-bold text-blush leading-none mb-16">"What happened?"</h2>
                        
                        <ul class="text-3xl text-blush/80 space-y-8 font-medium">
                            <li class="flex items-center gap-4"><div class="w-3 h-3 bg-white/20 rounded-full"></div>CRM stores customer records</li>
                            <li class="flex items-center gap-4"><div class="w-3 h-3 bg-white/20 rounded-full"></div>ERP manages operations</li>
                            <li class="flex items-center gap-4"><div class="w-3 h-3 bg-white/20 rounded-full"></div>BI dashboards visualize historical metrics</li>
                            <li class="flex items-center gap-4"><div class="w-3 h-3 bg-white/20 rounded-full"></div>Chatbots automate conversations</li>
                        </ul>
                    </div>
                    
                    <div class="flex-1 bg-gradient-to-br from-eggplant to-amethyst p-12 rounded-3xl border border-rosegold/30 shadow-[0_0_50px_rgba(244,208,180,0.05)] stagger-anim relative overflow-hidden">
                        <div class="absolute top-0 right-0 w-64 h-64 bg-rosegold opacity-10 rounded-full filter blur-[80px]"></div>
                        <p class="text-3xl text-copper mb-8 font-medium">Morlen answers a different question:</p>
                        <h2 class="text-[72px] font-bold text-rosegold leading-none mb-16 drop-shadow-lg">"What should I do next?"</h2>
                        
                        <ul class="text-3xl text-blush space-y-8 font-medium relative z-10">
                            <li>Every conversation contains intelligence.</li>
                            <li>Every business generates opportunities.</li>
                            <li>Every owner has limited attention.</li>
                        </ul>
                        
                        <div class="mt-16 pt-10 border-t border-rosegold/20 relative z-10">
                            <p class="text-4xl text-blush leading-relaxed font-semibold">Morlen exists to protect that attention—<br><span class="text-copper">by turning conversations into decisions.</span></p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 10 -->
        <div class="slide" id="slide10">
            <div class="w-full h-full flex flex-col justify-center items-center text-center relative z-10">
                <h1 class="text-[250px] font-black tracking-tighter text-rosegold-gradient leading-none mb-16 split-text drop-shadow-[0_0_50px_rgba(244,208,180,0.15)]">MORLEN</h1>
                
                <div class="stagger-anim mb-20">
                    <p class="text-6xl text-blush/90 mb-6 font-medium">The future of business isn't more software.</p>
                    <p class="text-7xl font-bold text-blush">It's better decisions.</p>
                </div>
                
                <div class="stagger-anim pt-12 border-t border-rosegold/30 w-full max-w-5xl">
                    <p class="text-4xl text-blush/80 mb-4 font-medium">Businesses already have the conversations.</p>
                    <p class="text-6xl text-copper font-bold tracking-tight">Morlen turns them into decisions.</p>
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
                inner.innerHTML = word + '&nbsp;';
                mask.appendChild(inner);
                el.appendChild(mask);
            });
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
            const wordInners = next.querySelectorAll('.word-inner');
            
            gsap.set(fadeElements, { opacity: 0, y: 50, scale: 0.95 });
            gsap.set(wordInners, { y: '100%', rotationX: 20 });

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
              }, "-=0.1")
              .to(fadeElements, {
                  opacity: 1, y: 0, scale: 1, duration: 1.2,
                  stagger: 0.15, ease: "expo.out"
              }, "-=0.8");
        }

        slides[0].classList.add('active');
        slides[0].style.visibility = 'visible';
        slides[0].style.opacity = 1;
        
        gsap.set(slides[0].querySelectorAll('.stagger-anim'), { opacity: 0, y: 50, scale: 0.95 });
        gsap.set(slides[0].querySelectorAll('.word-inner'), { y: '100%', rotationX: 20 });
        
        setTimeout(() => {
            gsap.to(slides[0].querySelectorAll('.word-inner'), {
                y: '0%', rotationX: 0, duration: 1.2, 
                stagger: 0.05, ease: "expo.out"
            });
            gsap.to(slides[0].querySelectorAll('.stagger-anim'), {
                opacity: 1, y: 0, scale: 1, duration: 1.2,
                stagger: 0.15, ease: "expo.out", delay: 0.4
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

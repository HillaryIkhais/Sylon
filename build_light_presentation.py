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
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600&display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        display: ['Outfit', 'sans-serif'],
                        body: ['Plus Jakarta Sans', 'sans-serif'],
                    },
                    colors: {
                        ink: '#09090B',
                        slate: '#3F3F46',
                        zinc: '#71717A',
                        cloud: '#F4F4F5',
                        snow: '#FFFFFF'
                    }
                }
            }
        }
    </script>

    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            background-color: #FFFFFF;
            color: #09090B;
            font-family: 'Plus Jakarta Sans', sans-serif;
            overflow: hidden;
            width: 100vw;
            height: 100vh;
        }

        #presentation-container {
            width: 1920px;
            height: 1080px;
            position: relative;
            background: radial-gradient(circle at 50% 50%, #FFFFFF 0%, #F4F4F5 100%);
            overflow: hidden;
        }

        /* Abstract ambient light in pale silver to add motion without color */
        .glow-orb {
            position: absolute;
            border-radius: 50%;
            filter: blur(120px);
            background: #E4E4E7;
            opacity: 0.8;
            z-index: 0;
            pointer-events: none;
            animation: float 25s infinite ease-in-out alternate;
        }
        .orb-1 { width: 1000px; height: 1000px; top: -300px; right: -200px; }
        .orb-2 { width: 800px; height: 800px; bottom: -200px; left: -200px; animation-delay: -12s; background: #D4D4D8; }

        @keyframes float {
            0% { transform: translate(0, 0) scale(1); }
            100% { transform: translate(-100px, 150px) scale(1.1); }
        }

        /* Diagonal frosted glass structure */
        .glass-panel {
            position: absolute;
            background: linear-gradient(135deg, rgba(255,255,255,0.8) 0%, rgba(255,255,255,0.2) 100%);
            backdrop-filter: blur(40px);
            -webkit-backdrop-filter: blur(40px);
            border: 1px solid rgba(255, 255, 255, 1);
            box-shadow: 0 40px 100px rgba(0,0,0,0.03);
            z-index: 1;
            border-radius: 40px;
        }
        
        .panel-bg-1 { width: 90vw; height: 140vh; top: -20vh; right: -15vw; transform: rotate(12deg); }

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
        h1, h2, h3 { font-family: 'Outfit', sans-serif; }
        
        .huge-headline {
            font-size: 100px;
            font-weight: 800;
            line-height: 1.05;
            color: #09090B;
            margin-bottom: 40px;
            letter-spacing: -0.03em;
        }
        
        .sub-headline {
            font-size: 56px;
            font-weight: 600;
            color: #27272A;
            margin-bottom: 24px;
            line-height: 1.15;
            letter-spacing: -0.01em;
        }

        /* Light Pricing Card Design */
        .pricing-card {
            background: rgba(255, 255, 255, 0.7);
            border: 1px solid rgba(255, 255, 255, 1);
            border-radius: 24px;
            position: relative;
            backdrop-filter: blur(40px);
            box-shadow: 0 20px 50px rgba(0,0,0,0.04);
        }

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
            <div class="w-full h-full flex flex-col justify-center">
                <div class="max-w-4xl relative z-10">
                    <h1 class="huge-headline stagger-anim drop-shadow-sm">Morlen</h1>
                    <p class="sub-headline stagger-anim">The Operating System for Business Decisions.</p>
                    <p class="text-3xl text-slate mb-20 stagger-anim font-medium">Turning customer conversations into executive decisions.</p>
                    
                    <div class="stagger-anim border-l-4 border-ink pl-6">
                        <p class="text-lg text-zinc uppercase tracking-widest font-bold mb-2">Founder Name</p>
                        <p class="text-3xl text-ink font-semibold">Hillary Ikhais</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 2 -->
        <div class="slide" id="slide2">
            <div class="w-full h-full flex flex-col justify-center relative z-10">
                <div class="flex gap-20">
                    <div class="flex-1">
                        <h1 class="huge-headline stagger-anim">The Problem</h1>
                        <h2 class="sub-headline stagger-anim">Businesses have automated transactions.</h2>
                        <p class="text-2xl text-slate leading-relaxed mb-10 stagger-anim font-medium">Over the last two decades, businesses have adopted software for almost every operational function:</p>
                        
                        <div class="stagger-anim">
                            <ul class="text-3xl text-ink space-y-5 font-semibold grid grid-cols-2">
                                <li class="flex items-center gap-4"><div class="w-3 h-3 rounded-full bg-ink"></div>Payments.</li>
                                <li class="flex items-center gap-4"><div class="w-3 h-3 rounded-full bg-ink"></div>CRM.</li>
                                <li class="flex items-center gap-4"><div class="w-3 h-3 rounded-full bg-ink"></div>Inventory.</li>
                                <li class="flex items-center gap-4"><div class="w-3 h-3 rounded-full bg-ink"></div>Marketing.</li>
                                <li class="flex items-center gap-4"><div class="w-3 h-3 rounded-full bg-ink"></div>Accounting.</li>
                                <li class="flex items-center gap-4 text-ink col-span-2 mt-6 pt-6 border-t border-zinc/20 text-4xl"><div class="w-4 h-4 rounded-full bg-ink shadow-[0_0_15px_rgba(0,0,0,0.3)]"></div>Conversations</li>
                            </ul>
                        </div>
                    </div>
                    <div class="flex-1 pt-6 border-l border-zinc/20 pl-16">
                        <p class="text-4xl font-bold text-ink mb-10 stagger-anim leading-tight">Yet business owners still ask the same questions:</p>
                        <ul class="text-3xl text-slate space-y-8 mb-16 stagger-anim font-medium">
                            <li>• What deserves attention today?</li>
                            <li>• Which products should I restock?</li>
                            <li>• Which customers need follow-up?</li>
                            <li>• Where am I losing revenue?</li>
                            <li>• Why have sales reduced?</li>
                        </ul>
                        <div class="stagger-anim bg-white/60 backdrop-blur-md p-8 rounded-2xl border border-white shadow-xl">
                            <p class="text-3xl text-ink mb-2 font-bold">Business software automates operations.</p>
                            <p class="text-3xl text-slate font-medium">It records what happened</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 3 -->
        <div class="slide" id="slide3">
            <div class="w-full h-full flex flex-col justify-center max-w-5xl relative z-10">
                <h1 class="huge-headline stagger-anim">THE SHIFT</h1>
                <h2 class="sub-headline stagger-anim">Commerce has moved into conversations</h2>
                
                <div class="space-y-10 text-3xl text-slate leading-relaxed stagger-anim font-medium">
                    <p>Across Nigeria, businesses now operate inside messaging platforms.<br>
                    <span class="text-2xl mt-4 block text-zinc">Customers now discover products, negotiate prices, confirm payments and arrange deliveries inside WhatsApp, Instagram and Facebook.</span></p>
                    
                    <div class="bg-ink text-white p-8 rounded-r-2xl border-l-8 border-slate shadow-2xl">
                        <p class="font-semibold">For Nigerian MSMEs, the entire sales funnel now exists inside conversations.</p>
                    </div>
                    
                    <p class="text-2xl">Yet traditional software was designed for structured forms, not unstructured conversations.</p>
                    
                    <p class="text-2xl">As conversational commerce grows, businesses generate thousands of customer signals every day.</p>
                    
                    <p class="text-ink font-bold text-4xl pt-6 border-t border-zinc/20">Most disappear without ever becoming business intelligence.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 4 -->
        <div class="slide" id="slide4">
            <div class="w-full h-full flex flex-col justify-center max-w-6xl relative z-10">
                <h1 class="huge-headline stagger-anim">THE PROBLEM</h1>
                <h2 class="sub-headline stagger-anim">Every conversation creates decisions.</h2>
                <p class="text-3xl text-slate mb-12 stagger-anim font-medium">A business owner doesn't just receive messages.<br>They constantly decide:</p>
                
                <ul class="text-3xl text-ink space-y-6 mb-16 stagger-anim grid grid-cols-2 gap-12 font-medium">
                    <li class="bg-white/70 backdrop-blur-md p-6 rounded-2xl border border-white shadow-lg">• Should this customer receive follow-up?</li>
                    <li class="bg-white/70 backdrop-blur-md p-6 rounded-2xl border border-white shadow-lg">• Is demand increasing for this product?</li>
                    <li class="bg-white/70 backdrop-blur-md p-6 rounded-2xl border border-white shadow-lg">• Should inventory be reordered?</li>
                    <li class="bg-white/70 backdrop-blur-md p-6 rounded-2xl border border-white shadow-lg">• Are customers becoming more price-sensitive?</li>
                    <li class="bg-white/70 backdrop-blur-md p-6 rounded-2xl border border-white shadow-lg">• Which complaints appear repeatedly?</li>
                    <li class="bg-white/70 backdrop-blur-md p-6 rounded-2xl border border-white shadow-lg">• Which customers are likely to return?</li>
                </ul>
                
                <div class="stagger-anim">
                    <p class="text-3xl text-slate mb-3 font-medium">These decisions are still made manually.</p>
                    <p class="text-5xl text-ink font-bold leading-tight">As conversations increase,<br>Decision complexity grows even faster.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 5 -->
        <div class="slide" id="slide5">
            <div class="w-full h-full flex flex-col justify-center relative z-10">
                <h1 class="huge-headline stagger-anim">MORLEN</h1>
                <h2 class="sub-headline stagger-anim">Morlen is an Executive Decision Intelligence Platform.</h2>
                <p class="text-2xl text-slate mb-8 max-w-5xl stagger-anim font-medium">Morlen continuously analyzes customer conversations, identifies business patterns and delivers prioritized business decisions.</p>
                <p class="text-4xl text-ink font-bold mb-16 max-w-5xl stagger-anim leading-tight">Instead of presenting plain dashboards,<br>Morlen produces a daily executive briefing.</p>
                
                <div class="grid grid-cols-4 gap-8 mb-16">
                    <div class="stagger-anim flex flex-col bg-white/80 p-8 rounded-3xl border border-white shadow-xl backdrop-blur-lg transform hover:-translate-y-2 transition-transform">
                        <h3 class="text-2xl font-bold text-ink mb-4">Executive Brief</h3>
                        <p class="text-lg text-slate font-medium">A daily summary of the highest priority decisions. inventory risks, customer churn, demand spikes, operational issues.</p>
                    </div>
                    <div class="stagger-anim flex flex-col bg-white/80 p-8 rounded-3xl border border-white shadow-xl backdrop-blur-lg transform hover:-translate-y-2 transition-transform">
                        <h3 class="text-2xl font-bold text-ink mb-4">Opportunity Feed</h3>
                        <p class="text-lg text-slate font-medium">Revenue opportunities detected from conversations including estimated impact, confidence score, supporting evidence.</p>
                    </div>
                    <div class="stagger-anim flex flex-col bg-white/80 p-8 rounded-3xl border border-white shadow-xl backdrop-blur-lg transform hover:-translate-y-2 transition-transform">
                        <h3 class="text-2xl font-bold text-ink mb-4">Business Memory</h3>
                        <p class="text-lg text-slate mb-3 font-medium">Long-term behavioural intelligence about customers.</p>
                        <p class="text-sm text-zinc">for example customers increasingly ask for same day delivery, demand for product A rises every month end, customers compare prices...</p>
                    </div>
                    <div class="stagger-anim flex flex-col bg-white/80 p-8 rounded-3xl border border-white shadow-xl backdrop-blur-lg transform hover:-translate-y-2 transition-transform">
                        <h3 class="text-2xl font-bold text-ink mb-4">Evidence-Based Recommendations</h3>
                        <p class="text-lg text-slate mb-3 font-medium">Every recommendation explains:</p>
                        <ul class="text-base text-ink space-y-2 font-bold">
                            <li>• Why it exists</li>
                            <li>• Expected impact</li>
                            <li>• Supporting evidence</li>
                        </ul>
                    </div>
                </div>
                
                <div class="stagger-anim">
                    <p class="text-3xl text-slate mb-2 font-medium">Business owners stop searching for answers.</p>
                    <p class="text-5xl font-bold text-ink">Morlen brings the answers to them.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 6 -->
        <div class="slide" id="slide6">
            <div class="w-full h-full flex flex-col justify-center items-center text-center relative z-10">
                <h1 class="huge-headline stagger-anim text-[80px]">MARKET & BUSINESS MODEL</h1>
                <h2 class="sub-headline stagger-anim mb-16">A Massive Market</h2>
                
                <p class="text-4xl text-slate mb-10 stagger-anim font-medium">Nigeria has approximately:</p>
                
                <div class="mb-20 stagger-anim relative">
                    <p class="text-[150px] font-black text-ink leading-none tracking-tighter drop-shadow-2xl">39.6 Million MSMEs</p>
                </div>
                
                <p class="text-3xl text-slate mb-10 stagger-anim font-medium">Representing:</p>
                <div class="flex gap-24 justify-center mb-20 stagger-anim text-6xl text-ink font-bold">
                    <div><p>96%</p><p class="text-2xl text-slate mt-4 font-medium">of businesses</p></div>
                    <div class="w-px h-24 bg-zinc/30"></div>
                    <div><p>87.9%</p><p class="text-2xl text-slate mt-4 font-medium">of employment</p></div>
                    <div class="w-px h-24 bg-zinc/30"></div>
                    <div><p>46.3%</p><p class="text-2xl text-slate mt-4 font-medium">of GDP</p></div>
                </div>
                
                <div class="stagger-anim">
                    <p class="text-3xl text-slate mb-3 font-medium">Millions already conduct business primarily through messaging platforms.</p>
                    <p class="text-4xl font-bold text-ink">Morlen is built for this new operating environment.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 7 -->
        <div class="slide" id="slide7">
            <div class="w-full h-full flex flex-col justify-center relative z-10">
                <h1 class="huge-headline stagger-anim">Business Model</h1>
                <h2 class="sub-headline stagger-anim">Subscription SaaS</h2>
                <p class="text-2xl text-slate mb-12 max-w-5xl stagger-anim font-medium">Starting with a 30 day free trial giving Morlen enough time to learn from customer conversations, build business memory, generate meaningful insights</p>
                
                <div class="grid grid-cols-3 gap-10 mb-16 stagger-anim">
                    <div class="pricing-card p-10 flex flex-col">
                        <h3 class="text-4xl font-bold text-ink mb-2">Starter</h3>
                        <p class="text-2xl text-slate font-bold mb-4">[N8,000/month]</p>
                        <p class="text-lg text-zinc mb-8 font-medium">For early stage businesses</p>
                        <ul class="text-ink space-y-5 text-xl flex-1 border-t border-zinc/20 pt-8 font-semibold">
                            <li>- Executive brief</li>
                            <li>- Business memory</li>
                            <li>- Basic decision intelligence</li>
                            <li>- Single workspace</li>
                        </ul>
                    </div>
                    
                    <div class="pricing-card p-10 flex flex-col border-ink/20 shadow-2xl transform scale-105 z-10 bg-white">
                        <div class="absolute -top-5 left-1/2 transform -translate-x-1/2 bg-ink text-white px-6 py-2 rounded-full text-sm font-bold tracking-widest uppercase shadow-lg">Popular</div>
                        <h3 class="text-4xl font-bold text-ink mb-2">Growth</h3>
                        <p class="text-2xl text-ink font-black mb-4">[N15,000/month]</p>
                        <p class="text-lg text-slate mb-8 font-medium">Businesses managing increasing customer conversations.</p>
                        <ul class="text-ink space-y-5 text-xl flex-1 border-t border-zinc/30 pt-8 font-bold">
                            <li>- Everything in starter</li>
                            <li>- Opportunity feed</li>
                            <li>- Advanced AI recommendations</li>
                            <li>- Multi channel integrations</li>
                            <li>- Team Collaboration</li>
                        </ul>
                    </div>
                    
                    <div class="pricing-card p-10 flex flex-col">
                        <h3 class="text-4xl font-bold text-ink mb-2">Enterprise</h3>
                        <p class="text-2xl text-slate font-bold mb-4">[CUSTOM PRICING]</p>
                        <p class="text-lg text-zinc mb-8 font-medium">Organizations requiring company-wide decision intelligence and integrations.</p>
                        <ul class="text-ink space-y-5 text-xl flex-1 border-t border-zinc/20 pt-8 font-semibold">
                            <li>- Everything in growth</li>
                            <li>- Custom AI deployment</li>
                            <li>- Dedicate Support</li>
                            <li>- Enterprise security and governance</li>
                        </ul>
                    </div>
                </div>
                
                <p class="text-2xl text-slate stagger-anim bg-white/60 inline-block px-8 py-4 rounded-xl border border-white shadow-sm font-medium">
                    Additional revenue: <span class="text-ink font-bold ml-2">• Enterprise Implementation & Onboarding</span>
                </p>
            </div>
        </div>

        <!-- SLIDE 8 -->
        <div class="slide" id="slide8">
            <div class="w-full h-full flex flex-col justify-center relative z-10">
                <h1 class="huge-headline stagger-anim text-[90px]">FUNDING & OUTCOMES</h1>
                
                <div class="flex gap-20">
                    <div class="flex-1">
                        <h2 class="text-5xl font-bold text-ink mb-10 stagger-anim">Raising Pre-Seed Capital</h2>
                        <p class="text-3xl text-slate mb-12 stagger-anim font-medium">Investment will accelerate:</p>
                        
                        <div class="space-y-8 stagger-anim">
                            <div class="bg-white/80 p-6 rounded-2xl border-l-8 border-ink shadow-lg">
                                <h3 class="text-3xl font-bold text-ink mb-2">40% — Product Development</h3>
                                <p class="text-xl text-slate font-medium">Complete commercial MVP and core intelligence engine.</p>
                            </div>
                            <div class="bg-white/80 p-6 rounded-2xl border-l-8 border-ink/80 shadow-md">
                                <h3 class="text-3xl font-bold text-ink mb-2">25% — AI Infrastructure</h3>
                                <p class="text-xl text-slate font-medium">Inference, data pipelines and production infrastructure.</p>
                            </div>
                            <div class="bg-white/80 p-6 rounded-2xl border-l-8 border-ink/60 shadow-md">
                                <h3 class="text-3xl font-bold text-ink mb-2">20% — Customer Acquisition</h3>
                                <p class="text-xl text-slate font-medium">Pilot programs and early customer onboarding.</p>
                            </div>
                            <div class="bg-white/80 p-6 rounded-2xl border-l-8 border-ink/40 shadow-sm">
                                <h3 class="text-3xl font-bold text-ink mb-2">15% — Strategic Partnerships & Operations</h3>
                                <p class="text-xl text-slate font-medium">Messaging integrations and business development.</p>
                            </div>
                        </div>
                    </div>
                    
                    <div class="flex-1 pt-4 border-l border-zinc/20 pl-20">
                        <h2 class="text-5xl font-bold text-ink mb-12 stagger-anim">Expected Outcomes</h2>
                        
                        <div class="space-y-10 stagger-anim mt-16">
                            <div class="flex items-center gap-8 bg-white/70 p-8 rounded-2xl border border-white shadow-lg">
                                <div class="w-8 h-8 rounded-full bg-ink flex-shrink-0"></div>
                                <p class="text-4xl text-ink font-bold">Commercial MVP</p>
                            </div>
                            <div class="flex items-center gap-8 bg-white/70 p-8 rounded-2xl border border-white shadow-lg">
                                <div class="w-8 h-8 rounded-full bg-ink flex-shrink-0"></div>
                                <p class="text-4xl text-ink font-bold">First paying customers</p>
                            </div>
                            <div class="flex items-center gap-8 bg-white/70 p-8 rounded-2xl border border-white shadow-lg">
                                <div class="w-8 h-8 rounded-full bg-ink flex-shrink-0"></div>
                                <p class="text-4xl text-ink font-bold">Validated product-market fit</p>
                            </div>
                            <div class="flex items-center gap-8 bg-white/70 p-8 rounded-2xl border border-white shadow-lg">
                                <div class="w-8 h-8 rounded-full bg-ink flex-shrink-0"></div>
                                <p class="text-4xl text-ink font-bold">Foundation for national expansion</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 9 -->
        <div class="slide" id="slide9">
            <div class="w-full h-full flex flex-col justify-center relative z-10">
                <h1 class="huge-headline stagger-anim">WHY MORLEN?</h1>
                
                <div class="flex gap-24 mt-10">
                    <div class="flex-1 bg-white/60 backdrop-blur-md p-12 rounded-3xl border border-white shadow-xl stagger-anim">
                        <p class="text-3xl text-slate mb-8 font-medium">Business software has always answered one question:</p>
                        <h2 class="text-[72px] font-black text-ink leading-none mb-16">"What happened?"</h2>
                        
                        <ul class="text-3xl text-slate space-y-8 font-semibold">
                            <li class="flex items-center gap-6"><div class="w-4 h-4 bg-zinc rounded-full"></div>CRM stores customer records</li>
                            <li class="flex items-center gap-6"><div class="w-4 h-4 bg-zinc rounded-full"></div>ERP manages operations</li>
                            <li class="flex items-center gap-6"><div class="w-4 h-4 bg-zinc rounded-full"></div>BI dashboards visualize historical metrics</li>
                            <li class="flex items-center gap-6"><div class="w-4 h-4 bg-zinc rounded-full"></div>Chatbots automate conversations</li>
                        </ul>
                    </div>
                    
                    <div class="flex-1 bg-ink text-white p-12 rounded-3xl border border-ink shadow-2xl stagger-anim relative overflow-hidden transform scale-[1.02]">
                        <p class="text-3xl text-white/80 mb-8 font-medium">Morlen answers a different question:</p>
                        <h2 class="text-[72px] font-black text-white leading-none mb-16">"What should I do next?"</h2>
                        
                        <ul class="text-3xl text-white space-y-8 font-bold relative z-10">
                            <li>Every conversation contains intelligence.</li>
                            <li>Every business generates opportunities.</li>
                            <li>Every owner has limited attention.</li>
                        </ul>
                        
                        <div class="mt-16 pt-10 border-t border-white/20 relative z-10">
                            <p class="text-4xl text-white leading-relaxed font-black">Morlen exists to protect that attention—<br><span class="text-white/80">by turning conversations into decisions.</span></p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 10 -->
        <div class="slide" id="slide10">
            <div class="w-full h-full flex flex-col justify-center items-center text-center relative z-10">
                <h1 class="text-[250px] font-black tracking-tighter text-ink leading-none mb-16 stagger-anim drop-shadow-2xl">MORLEN</h1>
                
                <div class="stagger-anim mb-20">
                    <p class="text-6xl text-slate mb-6 font-semibold">The future of business isn't more software.</p>
                    <p class="text-7xl font-black text-ink">It's better decisions.</p>
                </div>
                
                <div class="stagger-anim pt-12 border-t border-zinc/20 w-full max-w-5xl">
                    <p class="text-4xl text-slate mb-4 font-semibold">Businesses already have the conversations.</p>
                    <p class="text-6xl text-ink font-black tracking-tight">Morlen turns them into decisions.</p>
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
            gsap.set(fadeElements, { opacity: 0, y: 50, scale: 0.98 });

            const tl = gsap.timeline({
                onComplete: () => {
                    currentSlide = index;
                    isAnimating = false;
                }
            });
            
            tl.to(next, { opacity: 1, duration: 0.2 })
              .to(fadeElements, {
                  opacity: 1, y: 0, scale: 1, duration: 1.2,
                  stagger: 0.1, ease: "expo.out"
              }, "-=0.1");
        }

        slides[0].classList.add('active');
        slides[0].style.visibility = 'visible';
        slides[0].style.opacity = 1;
        
        gsap.set(slides[0].querySelectorAll('.stagger-anim'), { opacity: 0, y: 50, scale: 0.98 });
        
        setTimeout(() => {
            gsap.to(slides[0].querySelectorAll('.stagger-anim'), {
                opacity: 1, y: 0, scale: 1, duration: 1.2,
                stagger: 0.1, ease: "expo.out"
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

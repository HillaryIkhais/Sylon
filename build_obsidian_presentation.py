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
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Plus Jakarta Sans', 'sans-serif'],
                    },
                    colors: {
                        obsidian: '#09090B',
                        slate: '#121214',
                        ivory: '#F5F5F0',
                        muted: '#A0A0A5'
                    }
                }
            }
        }
    </script>

    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            background-color: #09090B;
            color: #F5F5F0;
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

        /* Extremely subtle, highly diffused warm structural lighting */
        .ambient-light {
            position: absolute;
            border-radius: 50%;
            filter: blur(200px);
            z-index: 0;
            pointer-events: none;
            opacity: 0.4;
        }
        .light-1 { width: 1200px; height: 1200px; background: #333330; top: -400px; right: -200px; }
        .light-2 { width: 1000px; height: 1000px; background: #1A1A24; bottom: -300px; left: -200px; }

        .slide {
            position: absolute; top: 0; left: 0;
            width: 100%; height: 100%;
            padding: 100px 140px;
            opacity: 0;
            visibility: hidden;
            z-index: 10;
        }

        .slide.active { opacity: 1; visibility: visible; }
        
        /* Ultra Crisp Typography */
        .huge-headline {
            font-size: 100px;
            font-weight: 700;
            line-height: 1.1;
            color: #FFFFFF;
            margin-bottom: 30px;
            letter-spacing: -0.03em;
        }
        
        .sub-headline {
            font-size: 48px;
            font-weight: 500;
            color: #F5F5F0;
            margin-bottom: 24px;
            line-height: 1.2;
            letter-spacing: -0.01em;
        }

        /* Professional, Solid Tactile Cards */
        .pro-card {
            background: #121214;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-top: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
            position: relative;
            z-index: 5;
        }

    </style>
</head>
<body>

    <div id="presentation-container">
        <!-- Ambient Lighting -->
        <div class="ambient-light light-1"></div>
        <div class="ambient-light light-2"></div>

        <!-- SLIDE 1 -->
        <div class="slide" id="slide1">
            <div class="w-full h-full flex flex-col justify-center">
                <div class="max-w-4xl relative z-10">
                    <h1 class="huge-headline stagger-anim">Morlen.</h1>
                    <p class="sub-headline stagger-anim">The Operating System for Business Decisions.</p>
                    <p class="text-3xl text-muted font-light mb-16 stagger-anim">Turning customer conversations into executive decisions.</p>
                    
                    <div class="stagger-anim border-l-2 border-ivory/40 pl-6 mt-12">
                        <p class="text-sm text-muted uppercase tracking-[0.2em] mb-1 font-semibold">Founder</p>
                        <p class="text-3xl text-ivory font-medium">Hillary Ikhais</p>
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
                        <div class="pro-card p-10 stagger-anim mt-10">
                            <p class="text-2xl text-muted leading-relaxed mb-8">Over the last two decades, businesses have adopted software for almost every operational function:</p>
                            <ul class="text-3xl text-ivory space-y-5 font-medium grid grid-cols-2">
                                <li class="flex items-center gap-4"><div class="w-2 h-2 rounded-full bg-ivory/50"></div>Payments.</li>
                                <li class="flex items-center gap-4"><div class="w-2 h-2 rounded-full bg-ivory/50"></div>CRM.</li>
                                <li class="flex items-center gap-4"><div class="w-2 h-2 rounded-full bg-ivory/50"></div>Inventory.</li>
                                <li class="flex items-center gap-4"><div class="w-2 h-2 rounded-full bg-ivory/50"></div>Marketing.</li>
                                <li class="flex items-center gap-4"><div class="w-2 h-2 rounded-full bg-ivory/50"></div>Accounting.</li>
                                <li class="flex items-center gap-4 text-white col-span-2 mt-6 pt-6 border-t border-white/10 text-4xl"><div class="w-3 h-3 rounded-full bg-white shadow-[0_0_15px_rgba(255,255,255,0.8)]"></div>Conversations</li>
                            </ul>
                        </div>
                    </div>
                    <div class="flex-1 flex flex-col justify-center pl-10 pt-8 border-l border-white/5">
                        <p class="text-4xl font-semibold text-white mb-10 stagger-anim leading-tight">Yet business owners still ask the same questions:</p>
                        <ul class="text-3xl text-muted space-y-6 mb-16 stagger-anim">
                            <li>• What deserves attention today?</li>
                            <li>• Which products should I restock?</li>
                            <li>• Which customers need follow-up?</li>
                            <li>• Where am I losing revenue?</li>
                            <li>• Why have sales reduced?</li>
                        </ul>
                        <div class="stagger-anim bg-white/5 p-8 rounded-2xl border border-white/10">
                            <p class="text-3xl text-ivory mb-2 font-semibold">Business software automates operations.</p>
                            <p class="text-3xl text-muted font-medium">It records what happened.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 3 -->
        <div class="slide" id="slide3">
            <div class="w-full h-full flex flex-col justify-center max-w-5xl">
                <h1 class="huge-headline stagger-anim">The Shift</h1>
                <h2 class="sub-headline stagger-anim">Commerce has moved into conversations.</h2>
                
                <div class="space-y-8 text-3xl text-muted leading-relaxed stagger-anim mt-10">
                    <p>Across Nigeria, businesses now operate inside messaging platforms.<br>
                    <span class="text-2xl mt-4 block text-muted/80">Customers now discover products, negotiate prices, confirm payments and arrange deliveries inside WhatsApp, Instagram and Facebook.</span></p>
                    
                    <div class="bg-slate p-8 rounded-2xl border-l-4 border-white shadow-lg">
                        <p class="text-white font-semibold">For Nigerian MSMEs, the entire sales funnel now exists inside conversations.</p>
                    </div>
                    
                    <p>Yet traditional software was designed for structured forms, not unstructured conversations.</p>
                    <p>As conversational commerce grows, businesses generate thousands of customer signals every day.</p>
                    
                    <p class="text-white font-semibold text-4xl pt-8 border-t border-white/10">Most disappear without ever becoming business intelligence.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 4 -->
        <div class="slide" id="slide4">
            <div class="w-full h-full flex flex-col justify-center max-w-6xl">
                <h1 class="huge-headline stagger-anim">The Problem</h1>
                <h2 class="sub-headline stagger-anim">Every conversation creates decisions.</h2>
                <p class="text-3xl text-muted mb-12 stagger-anim">A business owner doesn't just receive messages.<br>They constantly decide:</p>
                
                <ul class="text-3xl text-ivory space-y-6 mb-16 stagger-anim grid grid-cols-2 gap-8 font-medium">
                    <li class="pro-card p-6">• Should this customer receive follow-up?</li>
                    <li class="pro-card p-6">• Is demand increasing for this product?</li>
                    <li class="pro-card p-6">• Should inventory be reordered?</li>
                    <li class="pro-card p-6">• Are customers becoming more price-sensitive?</li>
                    <li class="pro-card p-6">• Which complaints appear repeatedly?</li>
                    <li class="pro-card p-6">• Which customers are likely to return?</li>
                </ul>
                
                <div class="stagger-anim bg-white/5 p-8 rounded-2xl border border-white/10 inline-block">
                    <p class="text-3xl text-muted mb-2 font-medium">These decisions are still made manually.</p>
                    <p class="text-4xl text-white font-semibold">As conversations increase, decision complexity grows even faster.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 5 -->
        <div class="slide" id="slide5">
            <div class="w-full h-full flex flex-col justify-center">
                <h1 class="huge-headline stagger-anim">Morlen</h1>
                <h2 class="sub-headline stagger-anim">An Executive Decision Intelligence Platform.</h2>
                <div class="stagger-anim max-w-5xl mb-12 mt-8">
                    <p class="text-3xl text-muted mb-6">Morlen continuously analyzes customer conversations, identifies business patterns and delivers prioritized business decisions.</p>
                    <p class="text-4xl text-white font-semibold">Instead of presenting plain dashboards, Morlen produces a daily executive briefing.</p>
                </div>
                
                <div class="grid grid-cols-4 gap-8 mb-12">
                    <div class="stagger-anim flex flex-col pro-card p-8">
                        <h3 class="text-2xl font-semibold text-white mb-4">Executive Brief</h3>
                        <p class="text-lg text-muted">A daily summary of the highest priority decisions. inventory risks, customer churn, demand spikes, operational issues.</p>
                    </div>
                    <div class="stagger-anim flex flex-col pro-card p-8">
                        <h3 class="text-2xl font-semibold text-white mb-4">Opportunity Feed</h3>
                        <p class="text-lg text-muted">Revenue opportunities detected from conversations including estimated impact, confidence score, supporting evidence.</p>
                    </div>
                    <div class="stagger-anim flex flex-col pro-card p-8">
                        <h3 class="text-2xl font-semibold text-white mb-4">Business Memory</h3>
                        <p class="text-lg text-muted mb-4">Long-term behavioural intelligence about customers.</p>
                        <p class="text-sm text-muted/60 uppercase tracking-widest font-semibold">Example: demand for product A rises every month end.</p>
                    </div>
                    <div class="stagger-anim flex flex-col pro-card p-8">
                        <h3 class="text-2xl font-semibold text-white mb-4">Evidence-Based Recs.</h3>
                        <p class="text-lg text-muted mb-4">Every recommendation explains:</p>
                        <ul class="text-base text-ivory space-y-2 font-medium">
                            <li>• Why it exists</li>
                            <li>• Expected impact</li>
                            <li>• Supporting evidence</li>
                        </ul>
                    </div>
                </div>
                
                <div class="stagger-anim flex items-center gap-6 mt-6">
                    <p class="text-3xl text-muted font-medium">Business owners stop searching for answers.</p>
                    <div class="w-px h-10 bg-white/20"></div>
                    <p class="text-4xl font-bold text-white">Morlen brings the answers to them.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 6 -->
        <div class="slide" id="slide6">
            <div class="w-full h-full flex flex-col justify-center items-center text-center">
                <div class="stagger-anim mb-12 bg-white/5 border border-white/10 px-6 py-2 rounded-full">
                    <p class="text-sm uppercase tracking-[0.3em] font-semibold text-white/80">Market & Business Model</p>
                </div>
                <h1 class="huge-headline stagger-anim">A Massive Market</h1>
                
                <p class="text-4xl text-muted mb-10 stagger-anim">Nigeria has approximately:</p>
                
                <div class="mb-16 stagger-anim relative">
                    <p class="text-[160px] font-bold text-white leading-none tracking-tight">39.6 Million MSMEs</p>
                </div>
                
                <p class="text-2xl text-muted mb-10 stagger-anim uppercase tracking-widest font-semibold">Representing</p>
                <div class="flex gap-16 justify-center mb-16 stagger-anim text-6xl font-bold text-ivory">
                    <div class="pro-card px-16 py-10"><p>96%</p><p class="text-2xl text-muted mt-4 font-medium tracking-normal">of businesses</p></div>
                    <div class="pro-card px-16 py-10"><p>87.9%</p><p class="text-2xl text-muted mt-4 font-medium tracking-normal">of employment</p></div>
                    <div class="pro-card px-16 py-10"><p>46.3%</p><p class="text-2xl text-muted mt-4 font-medium tracking-normal">of GDP</p></div>
                </div>
                
                <div class="stagger-anim">
                    <p class="text-3xl font-medium text-muted tracking-wide">Millions already conduct business primarily through messaging platforms.</p>
                    <p class="text-4xl font-semibold text-white mt-4">Morlen is built for this new operating environment.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 7 -->
        <div class="slide" id="slide7">
            <div class="w-full h-full flex flex-col justify-center">
                <h1 class="huge-headline stagger-anim">Business Model</h1>
                <div class="stagger-anim mb-10">
                    <h2 class="text-3xl font-semibold text-white">Subscription SaaS</h2>
                </div>
                <p class="text-3xl text-muted mb-12 max-w-5xl stagger-anim leading-relaxed">Starting with a 30 day free trial giving Morlen enough time to learn from customer conversations, build business memory, generate meaningful insights.</p>
                
                <div class="grid grid-cols-3 gap-8 mb-16 stagger-anim">
                    <div class="pro-card p-10 flex flex-col">
                        <h3 class="text-4xl font-bold text-white mb-2">Starter</h3>
                        <p class="text-2xl text-muted font-medium mb-4">N8,000/month</p>
                        <p class="text-lg text-muted mb-8">For early stage businesses</p>
                        <ul class="text-ivory space-y-4 text-xl flex-1 border-t border-white/10 pt-8 font-medium">
                            <li>• Executive brief</li>
                            <li>• Business memory</li>
                            <li>• Basic decision intelligence</li>
                            <li>• Single workspace</li>
                        </ul>
                    </div>
                    
                    <div class="pro-card p-10 flex flex-col relative transform scale-[1.05] z-10 border-white/30" style="box-shadow: 0 30px 60px rgba(0,0,0,0.6);">
                        <div class="absolute -top-4 left-1/2 transform -translate-x-1/2 bg-white text-black px-6 py-1.5 rounded-full text-xs font-bold tracking-[0.2em] uppercase">Popular</div>
                        <h3 class="text-4xl font-bold text-white mb-2">Growth</h3>
                        <p class="text-2xl text-white font-bold mb-4">N15,000/month</p>
                        <p class="text-lg text-ivory mb-8">Businesses managing increasing customer conversations.</p>
                        <ul class="text-white space-y-4 text-xl flex-1 border-t border-white/20 pt-8 font-semibold">
                            <li>• Everything in starter</li>
                            <li>• Opportunity feed</li>
                            <li>• Advanced AI recommendations</li>
                            <li>• Multi channel integrations</li>
                            <li>• Team Collaboration</li>
                        </ul>
                    </div>
                    
                    <div class="pro-card p-10 flex flex-col">
                        <h3 class="text-4xl font-bold text-white mb-2">Enterprise</h3>
                        <p class="text-2xl text-muted font-medium mb-4">CUSTOM PRICING</p>
                        <p class="text-lg text-muted mb-8">Organizations requiring company-wide decision intelligence.</p>
                        <ul class="text-ivory space-y-4 text-xl flex-1 border-t border-white/10 pt-8 font-medium">
                            <li>• Everything in growth</li>
                            <li>• Custom AI deployment</li>
                            <li>• Dedicated Support</li>
                            <li>• Enterprise security and governance</li>
                        </ul>
                    </div>
                </div>
                
                <p class="text-2xl text-muted stagger-anim bg-white/5 inline-block px-8 py-4 rounded-xl border border-white/10">
                    Additional revenue: <span class="text-white font-semibold ml-2">Enterprise Implementation & Onboarding</span>
                </p>
            </div>
        </div>

        <!-- SLIDE 8 -->
        <div class="slide" id="slide8">
            <div class="w-full h-full flex flex-col justify-center">
                <div class="flex gap-20">
                    <div class="flex-1">
                        <h1 class="huge-headline stagger-anim">Funding</h1>
                        <h2 class="text-5xl font-semibold text-white mb-10 stagger-anim">Raising Pre-Seed Capital</h2>
                        <p class="text-2xl text-muted mb-10 stagger-anim">Investment will accelerate:</p>
                        
                        <div class="space-y-6 stagger-anim">
                            <div class="pro-card p-6 flex items-center gap-6 border-l-4 border-l-white">
                                <h3 class="text-4xl font-bold text-white w-24">40%</h3>
                                <div class="w-px h-12 bg-white/10"></div>
                                <div>
                                    <p class="text-xl font-semibold text-ivory mb-1">Product Development</p>
                                    <p class="text-base text-muted">Complete commercial MVP and core intelligence engine.</p>
                                </div>
                            </div>
                            <div class="pro-card p-6 flex items-center gap-6 border-l-4 border-l-white/70">
                                <h3 class="text-4xl font-bold text-white w-24">25%</h3>
                                <div class="w-px h-12 bg-white/10"></div>
                                <div>
                                    <p class="text-xl font-semibold text-ivory mb-1">AI Infrastructure</p>
                                    <p class="text-base text-muted">Inference, data pipelines and production infrastructure.</p>
                                </div>
                            </div>
                            <div class="pro-card p-6 flex items-center gap-6 border-l-4 border-l-white/40">
                                <h3 class="text-4xl font-bold text-white w-24">20%</h3>
                                <div class="w-px h-12 bg-white/10"></div>
                                <div>
                                    <p class="text-xl font-semibold text-ivory mb-1">Customer Acq.</p>
                                    <p class="text-base text-muted">Pilot programs and early customer onboarding.</p>
                                </div>
                            </div>
                            <div class="pro-card p-6 flex items-center gap-6 border-l-4 border-l-white/20">
                                <h3 class="text-4xl font-bold text-white w-24">15%</h3>
                                <div class="w-px h-12 bg-white/10"></div>
                                <div>
                                    <p class="text-xl font-semibold text-ivory mb-1">Operations</p>
                                    <p class="text-base text-muted">Messaging integrations and business development.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="flex-1 flex flex-col justify-center pt-8 border-l border-white/5 pl-20">
                        <h1 class="huge-headline stagger-anim">Outcomes</h1>
                        <h2 class="text-5xl font-semibold text-white mb-12 stagger-anim">Expected Milestones</h2>
                        
                        <div class="space-y-8 stagger-anim mt-10">
                            <div class="flex items-center gap-8 pro-card p-8">
                                <div class="w-4 h-4 rounded-full bg-white shadow-[0_0_15px_rgba(255,255,255,0.8)]"></div>
                                <p class="text-3xl text-ivory font-medium">Commercial MVP</p>
                            </div>
                            <div class="flex items-center gap-8 pro-card p-8">
                                <div class="w-4 h-4 rounded-full bg-white shadow-[0_0_15px_rgba(255,255,255,0.8)]"></div>
                                <p class="text-3xl text-ivory font-medium">First paying customers</p>
                            </div>
                            <div class="flex items-center gap-8 pro-card p-8">
                                <div class="w-4 h-4 rounded-full bg-white shadow-[0_0_15px_rgba(255,255,255,0.8)]"></div>
                                <p class="text-3xl text-ivory font-medium">Validated product-market fit</p>
                            </div>
                            <div class="flex items-center gap-8 pro-card p-8">
                                <div class="w-4 h-4 rounded-full bg-white shadow-[0_0_15px_rgba(255,255,255,0.8)]"></div>
                                <p class="text-3xl text-ivory font-medium">Foundation for national expansion</p>
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
                    <div class="flex-1 pro-card p-12 stagger-anim flex flex-col justify-center border-l-4 border-l-white/20">
                        <p class="text-3xl text-muted mb-6">Business software has always answered one question:</p>
                        <h2 class="text-[72px] font-bold text-white leading-none mb-12">"What happened?"</h2>
                        
                        <ul class="text-3xl text-muted space-y-6 font-medium">
                            <li class="flex items-center gap-4"><div class="w-3 h-3 bg-white/30 rounded-full"></div>CRM stores customer records</li>
                            <li class="flex items-center gap-4"><div class="w-3 h-3 bg-white/30 rounded-full"></div>ERP manages operations</li>
                            <li class="flex items-center gap-4"><div class="w-3 h-3 bg-white/30 rounded-full"></div>BI dashboards visualize historical metrics</li>
                            <li class="flex items-center gap-4"><div class="w-3 h-3 bg-white/30 rounded-full"></div>Chatbots automate conversations</li>
                        </ul>
                    </div>
                    
                    <div class="flex-1 pro-card p-12 stagger-anim flex flex-col justify-center border-white/30 border-l-4 border-l-white">
                        <p class="text-3xl text-ivory mb-6 font-medium">Morlen answers a different question:</p>
                        <h2 class="text-[72px] font-bold text-white leading-none mb-12">"What should I do next?"</h2>
                        
                        <ul class="text-3xl text-white space-y-6 font-medium">
                            <li>• Every conversation contains intelligence.</li>
                            <li>• Every business generates opportunities.</li>
                            <li>• Every owner has limited attention.</li>
                        </ul>
                        
                        <div class="mt-12 pt-10 border-t border-white/20">
                            <p class="text-4xl text-white leading-relaxed font-semibold">Morlen exists to protect that attention—<br><span class="text-muted">by turning conversations into decisions.</span></p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 10 -->
        <div class="slide" id="slide10">
            <div class="w-full h-full flex flex-col justify-center items-center text-center">
                <div class="stagger-anim mb-16 bg-white/5 border border-white/10 px-8 py-4 rounded-full">
                    <p class="text-3xl font-medium text-muted">The future of business isn't more software.</p>
                </div>

                <h1 class="text-[250px] font-bold text-white leading-none tracking-tighter mb-16 stagger-anim">MORLEN</h1>
                
                <div class="stagger-anim mt-10 pro-card p-12">
                    <p class="text-4xl text-ivory mb-6 font-medium">Businesses already have the conversations.</p>
                    <p class="text-5xl text-white font-bold tracking-tight">Morlen turns them into decisions.</p>
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
                    opacity: 0, y: -20,
                    duration: 0.6,
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
                  opacity: 1, y: 0, duration: 1.0,
                  stagger: 0.1, ease: "power3.out"
              }, "-=0.1");
        }

        slides[0].classList.add('active');
        slides[0].style.visibility = 'visible';
        slides[0].style.opacity = 1;
        
        gsap.set(slides[0].querySelectorAll('.stagger-anim'), { opacity: 0, y: 30 });
        
        setTimeout(() => {
            gsap.to(slides[0].querySelectorAll('.stagger-anim'), {
                opacity: 1, y: 0, duration: 1.0,
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

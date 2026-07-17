import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Morlen - Pitch Deck</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        heading: ['Instrument Serif', 'serif'],
                    },
                    colors: {
                        background: '#070505',
                        brand: {
                            light: '#FAF4F0',
                            taupe: '#E3CDBF',
                            mocha: '#7A6458',
                        }
                    }
                }
            }
        }
    </script>

    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            background-color: #070505;
            color: #FAF4F0;
            font-family: 'Inter', sans-serif;
            overflow: hidden;
            width: 1920px;
            height: 1080px;
            -webkit-font-smoothing: antialiased;
            letter-spacing: -0.01em; 
        }

        #presentation-container {
            width: 1920px;
            height: 1080px;
            position: relative;
            background: radial-gradient(circle at top right, #14100E 0%, #070505 80%);
            overflow: hidden;
        }

        #stars-canvas {
            position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; pointer-events: none;
        }

        #video-container {
            position: absolute; bottom: -20vh; left: 0; width: 100%; height: 100vh; z-index: 2; pointer-events: none;
            display: flex; align-items: center; justify-content: center; overflow: hidden;
            mix-blend-mode: luminosity; opacity: 0.12; 
        }
        #video-player { width: 100%; height: 100%; object-fit: cover; }
        .video-gradient { position: absolute; inset: 0; background: radial-gradient(circle at center, transparent 0%, #070505 80%); z-index: 3; }

        .slide {
            position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            visibility: hidden; z-index: 10;
            display: flex; flex-direction: column; padding: 60px 100px;
        }
        .slide.active { visibility: visible; }
        
        .pricing-card {
            background: rgba(20, 16, 14, 0.4);
            border: 1px solid rgba(227, 205, 191, 0.1);
            border-radius: 24px;
            padding: 36px;
        }
        
        .page-header {
            font-family: 'Inter', sans-serif; font-weight: 700; font-size: 64px; letter-spacing: -3px;
            background: linear-gradient(to right, #FAF4F0, #E3CDBF);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            margin-bottom: 1.5rem;
        }
        
        .sub-header {
            font-family: 'Instrument Serif', serif; font-style: italic; font-size: 64px;
            line-height: 1.0; letter-spacing: -1px; font-weight: 400; color: #FAF4F0;
        }
        
        .split-char { display: inline-block; opacity: 0; transform: translateY(20px); }
        .fade-elem { opacity: 0; transform: translateY(15px); }
        
        .premium-line { width: 100%; height: 1px; background: linear-gradient(to right, rgba(227, 205, 191, 0.5), transparent); }
    </style>
</head>
<body>

    <div id="presentation-container">
        <canvas id="stars-canvas"></canvas>
        <div id="video-container">
            <video id="video-player" muted loop playsinline></video>
            <div class="video-gradient"></div>
        </div>
        
        <!-- SLIDE 1 — MORLEN -->
        <div class="slide" id="slide1">
            <div class="flex-1 flex flex-col justify-center items-center text-center">
                <h1 class="page-header text-[200px] leading-[0.8] tracking-[-0.04em] mb-4">Morlen.</h1>
                <p class="split-text font-heading italic text-[80px] text-brand-taupe leading-[1.0] mb-20">The Operating System for Business Decisions.</p>
                
                <div class="fade-elem max-w-4xl mx-auto flex flex-col items-center">
                    <p class="text-[36px] text-brand-light font-normal leading-tight mb-20">Turning customer conversations into executive decisions.</p>
                    <p class="font-heading italic text-5xl text-brand-taupe">Hillary Ikhais</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 2 — THE PROBLEM -->
        <div class="slide" id="slide2">
            <h2 class="page-header fade-elem">The Problem</h2>
            <div class="premium-line mb-10 fade-elem"></div>
            
            <div class="flex-1 flex flex-col">
                <div class="grid grid-cols-2 gap-20 h-full">
                    <div class="flex flex-col pr-8 border-r border-brand-mocha/30 justify-center">
                        <h3 class="split-text text-[56px] font-medium tracking-tight text-brand-light leading-[1.1] mb-10">Businesses have automated transactions.</h3>
                        <p class="fade-elem text-[28px] text-brand-light font-normal leading-relaxed mb-10">Over the last two decades, businesses have adopted software for almost every operational function:</p>
                        
                        <div class="fade-elem grid grid-cols-2 gap-y-6 gap-x-12 text-[28px] font-normal text-brand-taupe">
                            <span>Payments.</span>
                            <span>Inventory.</span>
                            <span>Accounting.</span>
                            <span>CRM.</span>
                            <span>Marketing.</span>
                            <span class="text-brand-light font-medium border-b border-brand-taupe pb-2">Conversations.</span>
                        </div>
                    </div>
                    
                    <div class="flex flex-col justify-center pl-8">
                        <p class="fade-elem font-heading italic text-[64px] text-brand-taupe leading-none mb-10">Yet business owners still ask the same questions:</p>
                        <div class="fade-elem space-y-6 text-[32px] font-normal tracking-tight text-brand-light pl-6 border-l-2 border-brand-taupe/40 mb-12">
                            <p>What deserves attention today?</p>
                            <p>Which products should I restock?</p>
                            <p>Which customers need follow-up?</p>
                            <p>Where am I losing revenue?</p>
                            <p>Why have sales reduced?</p>
                        </div>
                        
                        <div class="fade-elem">
                            <p class="font-heading italic text-[48px] text-brand-light mb-2">Business software automates operations.</p>
                            <p class="text-[28px] font-normal text-brand-taupe tracking-tight">It records what happened.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 3 — THE SHIFT -->
        <div class="slide" id="slide3">
            <h2 class="page-header fade-elem text-center">The Shift</h2>
            <div class="premium-line mb-16 fade-elem w-1/3 mx-auto"></div>
            
            <div class="flex-1 flex flex-col justify-center">
                <h3 class="split-text sub-header text-[110px] mb-20 text-center">Commerce has moved into conversations.</h3>
                
                <div class="grid grid-cols-2 gap-20 px-8">
                    <div class="fade-elem flex flex-col gap-8 pr-12 border-r border-brand-mocha/30">
                        <p class="text-[36px] font-normal text-brand-light leading-snug tracking-tight">Across Nigeria, businesses now operate inside messaging platforms.</p>
                        <p class="text-[28px] font-normal text-brand-taupe leading-relaxed">Customers now discover products, negotiate prices, confirm payments and arrange deliveries inside WhatsApp, Instagram and Facebook.</p>
                        <p class="font-heading italic text-[48px] text-brand-light leading-none mt-6">For Nigerian MSMEs, the entire sales funnel now exists inside conversations.</p>
                    </div>
                    
                    <div class="fade-elem flex flex-col gap-8 pl-12">
                        <p class="text-[36px] font-normal text-brand-light leading-snug tracking-tight">Yet traditional software was designed for structured forms, not unstructured conversations.</p>
                        <p class="text-[28px] font-normal text-brand-taupe leading-relaxed">As conversational commerce grows, businesses generate thousands of customer signals every day.</p>
                        <p class="font-heading italic text-[48px] text-brand-taupe leading-none mt-6">Most disappear without ever becoming business intelligence.</p>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- SLIDE 4 — THE DECISION CRISIS -->
        <div class="slide" id="slide4">
            <h2 class="page-header fade-elem text-center">The Decision Crisis</h2>
            <div class="premium-line mb-12 fade-elem w-1/2 mx-auto"></div>
            
            <div class="flex-1 flex flex-col">
                <h3 class="split-text text-[90px] font-medium tracking-tight text-brand-light text-center mb-16">Every conversation creates decisions.</h3>
                
                <div class="flex flex-col flex-1 px-8">
                    <div class="flex flex-1 gap-20">
                        <!-- Left Column: Intro -->
                        <div class="flex flex-col w-[35%] pr-12 border-r border-brand-mocha/30 pt-4">
                            <p class="text-[40px] font-normal text-brand-light leading-tight mb-8 tracking-tight">A business owner doesn't just receive messages.</p>
                            <p class="fade-elem font-heading italic text-[80px] text-brand-taupe leading-[1.0] text-right">They constantly decide:</p>
                        </div>
                        
                        <!-- Right Column: The Questions (Directly answers the left column) -->
                        <div class="flex flex-col w-[65%] pl-4 pt-4">
                            <div class="fade-elem space-y-10 text-[32px] font-normal tracking-tight text-brand-light">
                                <p>Should this customer receive follow-up?</p>
                                <p>Is demand increasing for this product?</p>
                                <p>Should inventory be reordered?</p>
                                <p>Are customers becoming more price-sensitive?</p>
                                <p>Which complaints appear repeatedly?</p>
                                <p>Which customers are likely to return?</p>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Bottom Bar (Conclusion) -->
                    <div class="mt-12 pt-10 border-t border-brand-mocha/30 fade-elem flex justify-between items-center bg-black/20 p-8 rounded-2xl">
                        <p class="font-heading italic text-[56px] text-brand-light">These decisions are still made manually.</p>
                        <p class="text-[32px] font-normal text-brand-taupe">As conversations increase, <span class="text-brand-light font-bold">Decision complexity grows even faster.</span></p>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 5 — MORLEN -->
        <div class="slide" id="slide5">
            <h2 class="page-header fade-elem text-center">Morlen</h2>
            <div class="premium-line mb-8 fade-elem w-1/4 mx-auto"></div>
            
            <div class="flex-1 flex flex-col justify-center">
                <h3 class="split-text sub-header text-[80px] mb-8 text-center">Morlen is an Executive Decision Intelligence Platform.</h3>
                <div class="mb-16 text-center max-w-6xl mx-auto">
                    <p class="fade-elem text-[32px] font-normal tracking-tight text-brand-light leading-snug mb-6">Morlen continuously analyzes customer conversations, identifies business patterns and delivers prioritized business decisions.</p>
                    <p class="split-text text-[28px] font-medium text-brand-taupe leading-relaxed max-w-4xl mx-auto">Instead of presenting plain dashboards, Morlen produces a daily executive briefing.</p>
                </div>
                
                <div class="grid grid-cols-2 gap-x-20 gap-y-12 max-w-[1500px] mx-auto w-full px-8">
                    <div class="fade-elem flex flex-col">
                        <p class="font-heading italic text-[56px] text-brand-light mb-4 leading-none">Executive Brief</p>
                        <p class="text-[24px] font-normal tracking-tight text-brand-light mb-4">A daily summary of the highest priority decisions.</p>
                        <p class="text-[20px] text-brand-taupe leading-relaxed italic">Inventory risks, customer churn, demand spikes, operational issues.</p>
                    </div>
                    
                    <div class="fade-elem flex flex-col">
                        <p class="font-heading italic text-[56px] text-brand-light mb-4 leading-none">Business Memory</p>
                        <p class="text-[24px] font-normal tracking-tight text-brand-light mb-4">Long-term behavioural intelligence about customers.</p>
                        <p class="text-[20px] font-normal text-brand-taupe leading-relaxed italic">For example: customers increasingly ask for same day delivery, demand for product A rises every month end, customers compare prices before purchasing.</p>
                    </div>
                    
                    <div class="fade-elem flex flex-col">
                        <p class="font-heading italic text-[56px] text-brand-light mb-4 leading-none">Opportunity Feed</p>
                        <p class="text-[24px] font-normal tracking-tight text-brand-light leading-snug">Revenue opportunities detected from conversations including estimated impact, confidence score, supporting evidence.</p>
                    </div>
                    
                    <div class="fade-elem flex flex-col">
                        <p class="font-heading italic text-[56px] text-brand-light mb-4 leading-none">Evidence-Based Recommendations</p>
                        <p class="text-[24px] font-normal tracking-tight text-brand-light mb-4">Every recommendation explains:</p>
                        <div class="flex gap-6 text-[20px] font-medium text-brand-taupe">
                            <span>Why it exists</span>
                            <span class="text-brand-mocha">•</span>
                            <span>Expected impact</span>
                            <span class="text-brand-mocha">•</span>
                            <span>Supporting evidence</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 6 — A MASSIVE MARKET -->
        <div class="slide" id="slide6">
            <h2 class="page-header fade-elem text-center">A Massive Market</h2>
            <div class="premium-line mb-16 fade-elem w-1/3 mx-auto"></div>
            
            <div class="flex-1 flex items-center justify-center">
                <div class="fade-elem flex items-stretch justify-center w-full max-w-[1600px]">
                    <div class="w-1/2 pr-16 border-r border-brand-mocha/50 flex flex-col justify-center text-right">
                        <p class="text-[40px] font-normal text-brand-light mb-4">Nigeria has approximately:</p>
                        <p class="font-heading italic text-[130px] bg-gradient-to-r from-brand-light to-brand-taupe text-transparent bg-clip-text leading-[0.9] pb-4">39.6 Million<br>MSMEs</p>
                    </div>
                    <div class="w-1/2 pl-16 flex flex-col justify-center">
                        <div class="flex flex-col gap-y-6 text-[40px] font-normal text-brand-light mb-12">
                            <p>96% of businesses</p>
                            <p>46.3% of GDP</p>
                            <p>87.9% of employment</p>
                        </div>
                        <div class="pt-8 border-t border-brand-mocha/30">
                            <p class="text-[28px] font-normal text-brand-taupe mb-4">Millions already conduct business primarily through messaging platforms.</p>
                            <p class="font-heading italic text-[48px] text-brand-light leading-none">Morlen is built for this new operating environment.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 7 — BUSINESS MODEL -->
        <div class="slide" id="slide7">
            <h2 class="page-header fade-elem text-center">Business Model</h2>
            <div class="premium-line mb-12 fade-elem w-1/3 mx-auto"></div>
            
            <div class="flex-1 flex flex-col">
                <div class="flex justify-between items-end mb-10 fade-elem px-8">
                    <div class="text-left max-w-4xl">
                        <p class="font-heading italic text-[56px] text-brand-taupe leading-none mb-4">Subscription SaaS.</p>
                        <p class="text-[28px] font-normal text-brand-light">Starting with a 30 day free trial giving Morlen enough time to learn from customer conversations, build business memory, generate meaningful insights.</p>
                    </div>
                </div>
                
                <div class="grid grid-cols-3 gap-6 flex-1 mb-8 px-8">
                    <div class="pricing-card fade-elem flex flex-col">
                        <div class="flex items-end justify-between border-b border-brand-mocha/50 pb-6 mb-6">
                            <p class="font-heading italic text-[54px] text-brand-light leading-none">Starter</p>
                            <p class="font-medium text-xl text-brand-taupe">[N8,000/month]</p>
                        </div>
                        <p class="text-[22px] font-normal text-brand-light mb-6 italic">For early stage businesses</p>
                        <div class="flex flex-col gap-y-3 text-[20px] font-normal text-brand-light">
                            <p>— Executive brief</p>
                            <p>— Business memory</p>
                            <p>— Basic decision intelligence</p>
                            <p>— Single workspace</p>
                        </div>
                    </div>
                    
                    <div class="pricing-card fade-elem flex flex-col bg-brand-mocha/10 border-brand-taupe/40 ring-1 ring-brand-taupe/20">
                        <div class="flex items-end justify-between border-b border-brand-taupe/40 pb-6 mb-6">
                            <p class="font-heading italic text-[54px] text-brand-light leading-none">Growth</p>
                            <p class="font-medium text-xl text-brand-light">[N15,000/month]</p>
                        </div>
                        <p class="text-[22px] font-normal text-brand-light mb-6 italic">Businesses managing increasing customer conversations.</p>
                        <div class="flex flex-col gap-y-3 text-[20px] font-normal text-brand-light">
                            <p>— Everything in starter</p>
                            <p>— Opportunity feed</p>
                            <p>— Advanced AI recommendations</p>
                            <p>— Multi channel integrations</p>
                            <p>— Team Collaboration</p>
                        </div>
                    </div>
                    
                    <div class="pricing-card fade-elem flex flex-col">
                        <div class="flex items-end justify-between border-b border-brand-mocha/50 pb-6 mb-6">
                            <p class="font-heading italic text-[54px] text-brand-light leading-none">Enterprise</p>
                            <p class="font-medium text-xl text-brand-taupe">[CUSTOM PRICING]</p>
                        </div>
                        <p class="text-[22px] font-normal text-brand-light mb-6 italic">Organizations requiring company-wide decision intelligence and integrations.</p>
                        <div class="flex flex-col gap-y-3 text-[20px] font-normal text-brand-light">
                            <p>— Everything in growth</p>
                            <p>— Custom AI deployment</p>
                            <p>— Dedicate Support</p>
                            <p>— Enterprise security and governance</p>
                        </div>
                    </div>
                </div>
                
                <div class="text-right fade-elem pt-2 pr-8">
                    <span class="text-[20px] font-normal text-brand-taupe mr-4">Additional revenue:</span>
                    <span class="text-[24px] font-medium text-brand-light">Enterprise Implementation & Onboarding</span>
                </div>
            </div>
        </div>

        <!-- SLIDE 8 — FUNDING & MILESTONES -->
        <div class="slide" id="slide8">
            <h2 class="page-header fade-elem">Funding & Milestones</h2>
            <div class="premium-line mb-12 fade-elem"></div>
            
            <div class="flex-1 flex flex-col px-8">
                <div class="mb-16">
                    <h3 class="split-text text-[72px] font-normal tracking-tight mb-4">Raising Pre-Seed Capital.</h3>
                    <p class="split-text font-heading italic text-[56px] text-brand-taupe leading-none">Investment will accelerate:</p>
                </div>
                
                <div class="grid grid-cols-12 gap-12 flex-1">
                    <div class="col-span-8 grid grid-cols-2 gap-x-12 gap-y-16 h-full">
                        <div class="fade-elem flex flex-col">
                            <p class="font-heading italic text-[90px] text-brand-taupe leading-none mb-4">40%</p>
                            <p class="text-[28px] font-medium tracking-tight text-brand-light mb-2">Product Development</p>
                            <p class="text-[22px] font-normal text-brand-light">Complete commercial MVP and core intelligence engine.</p>
                        </div>
                        <div class="fade-elem flex flex-col">
                            <p class="font-heading italic text-[90px] text-brand-taupe leading-none mb-4">25%</p>
                            <p class="text-[28px] font-medium tracking-tight text-brand-light mb-2">AI Infrastructure</p>
                            <p class="text-[22px] font-normal text-brand-light">Inference, data pipelines and production infrastructure.</p>
                        </div>
                        <div class="fade-elem flex flex-col">
                            <p class="font-heading italic text-[90px] text-brand-taupe leading-none mb-4">20%</p>
                            <p class="text-[28px] font-medium tracking-tight text-brand-light mb-2">Customer Acquisition</p>
                            <p class="text-[22px] font-normal text-brand-light">Pilot programs and early customer onboarding.</p>
                        </div>
                        <div class="fade-elem flex flex-col">
                            <p class="font-heading italic text-[90px] text-brand-taupe leading-none mb-4">15%</p>
                            <p class="text-[28px] font-medium tracking-tight text-brand-light mb-2 leading-snug">Strategic Partnerships & Operations</p>
                            <p class="text-[22px] font-normal text-brand-light">Messaging integrations and business development.</p>
                        </div>
                    </div>
                    
                    <div class="col-span-4 h-full pl-12 border-l border-brand-mocha/30">
                        <div class="fade-elem flex flex-col pt-4">
                            <h3 class="font-heading italic text-[56px] text-brand-light leading-none mb-10">Expected Outcomes:</h3>
                            
                            <div class="space-y-6 text-[32px] font-normal tracking-tight text-brand-light">
                                <p>Commercial MVP.</p>
                                <p>First paying customers.</p>
                                <p>Validated product-market fit.</p>
                                <p class="text-brand-taupe font-medium pt-6">Foundation for national expansion.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 9 — WHY MORLEN? -->
        <div class="slide" id="slide9">
            <h2 class="page-header fade-elem text-center">Why Morlen?</h2>
            <div class="premium-line mb-16 fade-elem w-1/3 mx-auto"></div>
            
            <div class="flex-1 grid grid-cols-2 gap-20 px-8">
                <div class="fade-elem flex flex-col pr-12 border-r border-brand-mocha/30 justify-center">
                    <p class="text-[40px] font-normal text-brand-light tracking-tight mb-6 leading-snug">Business software has always answered one question:</p>
                    <p class="font-heading italic text-[100px] text-brand-taupe leading-none mb-16">"What happened?"</p>
                    
                    <div class="flex flex-col gap-y-8 text-[32px] font-normal text-brand-light pl-8 border-l-2 border-brand-mocha/40">
                        <span>CRM stores customer records</span>
                        <span>ERP manages operations</span>
                        <span>BI dashboards visualize historical metrics</span>
                        <span>Chatbots automate converstaions</span>
                    </div>
                </div>
                
                <div class="fade-elem flex flex-col pl-12 justify-center">
                    <p class="text-[40px] font-normal text-brand-light tracking-tight mb-6">Morlen answers a different question:</p>
                    <p class="font-heading italic text-[110px] text-transparent bg-gradient-to-r from-brand-light to-brand-taupe bg-clip-text leading-[0.9] mb-16">"What should I do next?"</p>
                    
                    <div class="space-y-6 text-[32px] font-normal tracking-tight text-brand-light mb-16">
                        <p>Every conversation contains intelligence.</p>
                        <p>Every business generates opportunities.</p>
                        <p>Every owner has limited attention.</p>
                    </div>
                    
                    <div class="pt-8 border-t border-brand-taupe/30">
                        <p class="font-heading italic text-[56px] text-brand-light mb-4 leading-none">Morlen exists to protect that attention—</p>
                        <p class="text-[36px] font-medium text-brand-taupe tracking-tight">by turning conversations into decisions.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 10 — FINAL -->
        <div class="slide" id="slide10">
            <div class="flex-1 flex flex-col justify-center items-center text-center">
                <h1 class="page-header text-[220px] mb-12 tracking-[-0.04em]">Morlen.</h1>
                
                <div class="fade-elem max-w-6xl pt-16 border-t border-brand-taupe/30">
                    <h2 class="text-[56px] font-normal tracking-tight text-brand-light leading-tight mb-6">The future of business isn't more software.</h2>
                    <p class="font-heading italic text-[120px] text-brand-taupe mb-20 leading-[0.9]">It's better decisions.</p>
                    
                    <div class="pt-12 border-t border-brand-mocha/30">
                        <p class="text-[36px] font-normal text-brand-light mb-4">Businesses already have the conversations.</p>
                        <p class="font-heading italic text-[64px] text-brand-taupe leading-none">Morlen turns them into decisions.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        const canvas = document.getElementById('stars-canvas');
        const ctx = canvas.getContext('2d');
        canvas.width = 1920;
        canvas.height = 1080;
        
        const stars = [];
        for (let i = 0; i < 200; i++) {
            stars.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                radius: Math.random() * 2.5,
                alpha: Math.random(),
                speedX: (Math.random() - 0.5) * 1.5, 
                speedY: (Math.random() - 0.5) * 1.5,
                pulseSpeed: Math.random() * 0.05 + 0.02
            });
        }
        
        function animateStars() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            stars.forEach(star => {
                star.x += star.speedX;
                star.y += star.speedY;
                star.alpha += Math.sin(Date.now() * star.pulseSpeed) * 0.02;
                
                if (star.x < 0) star.x = canvas.width;
                if (star.x > canvas.width) star.x = 0;
                if (star.y < 0) star.y = canvas.height;
                if (star.y > canvas.height) star.y = 0;
                
                if (star.alpha < 0.1) star.alpha = 0.1;
                if (star.alpha > 0.8) star.alpha = 0.8;
                
                ctx.beginPath();
                ctx.arc(star.x, star.y, star.radius, 0, Math.PI * 2);
                ctx.fillStyle = `rgba(227, 205, 191, ${star.alpha})`;
                ctx.fill();
            });
            requestAnimationFrame(animateStars);
        }
        animateStars();

        const splitTextElements = document.querySelectorAll('.split-text');
        splitTextElements.forEach(el => {
            const text = el.innerText;
            el.innerHTML = '';
            for (let i = 0; i < text.length; i++) {
                const char = text[i];
                if (char === ' ') {
                    el.innerHTML += `&nbsp;`;
                } else {
                    el.innerHTML += `<span class="split-char">${char}</span>`;
                }
            }
        });
        
        const video = document.getElementById('video-player');
        const videoSrc = 'https://stream.mux.com/9JXDljEVWYwWu01PUkAemafDugK89o01BR6zqJ3aS9u00A.m3u8';
        
        if (Hls.isSupported()) {
            const hls = new Hls({ enableWorker: true, lowLatencyMode: true });
            hls.loadSource(videoSrc);
            hls.attachMedia(video);
            hls.on(Hls.Events.MANIFEST_PARSED, () => {
                video.play().catch(e => console.log('Autoplay prevented:', e));
            });
        }

        const slides = document.querySelectorAll('.slide');
        let currentSlide = 0;
        let isAnimating = false;

        function goToSlide(index) {
            if (isAnimating || index < 0 || index >= slides.length) return;
            isAnimating = true;

            const current = slides[currentSlide];
            const next = slides[index];
            
            stars.forEach(star => {
                gsap.to(star, {
                    x: star.x + (Math.random() - 0.5) * 150,
                    y: star.y + (Math.random() - 0.5) * 150,
                    duration: 2.0,
                    ease: "power2.out"
                });
            });
            
            if (current) {
                const currentChars = current.querySelectorAll('.split-char');
                const currentFades = current.querySelectorAll('.fade-elem');
                const currentPageHeader = current.querySelectorAll('.page-header');
                
                const outroTl = gsap.timeline({
                    onComplete: () => {
                        current.classList.remove('active');
                        gsap.set(currentChars, { clearProps: "all" });
                        gsap.set(currentFades, { clearProps: "all" });
                        gsap.set(currentPageHeader, { clearProps: "all" });
                        
                        next.classList.add('active');
                        
                        const chars = next.querySelectorAll('.split-char');
                        const fades = next.querySelectorAll('.fade-elem');
                        const pageHeader = next.querySelectorAll('.page-header');
                        
                        gsap.set(chars, { opacity: 0, y: 30, scale: 0.9, filter: "blur(8px)" });
                        gsap.set(fades, { opacity: 0, y: 20, filter: "blur(8px)" });
                        gsap.set(pageHeader, { opacity: 0, scale: 0.95, filter: "blur(10px)" });

                        const introTl = gsap.timeline({
                            onComplete: () => {
                                currentSlide = index;
                                isAnimating = false;
                            }
                        });
                        
                        introTl.to(pageHeader, {
                            opacity: 1, scale: 1, filter: "blur(0px)", duration: 1.4, ease: "power3.out"
                        })
                        .to(chars, {
                            opacity: 1, y: 0, scale: 1, filter: "blur(0px)", duration: 0.8, stagger: 0.015, ease: "power2.out"
                        }, "-=1.0")
                        .to(fades, {
                            opacity: 1, y: 0, filter: "blur(0px)", duration: 1.2, stagger: 0.15, ease: "power2.out"
                        }, "-=0.6");
                    }
                });

                outroTl.to([currentPageHeader, currentChars, currentFades], {
                    opacity: 0, y: -25, scale: 1.05, filter: "blur(12px)", duration: 0.7, stagger: 0.02, ease: "power2.in"
                });
            } else {
                next.classList.add('active');
                const chars = next.querySelectorAll('.split-char');
                const fades = next.querySelectorAll('.fade-elem');
                const pageHeader = next.querySelectorAll('.page-header');
                
                gsap.set(chars, { opacity: 0, y: 30, scale: 0.9, filter: "blur(8px)" });
                gsap.set(fades, { opacity: 0, y: 20, filter: "blur(8px)" });
                gsap.set(pageHeader, { opacity: 0, scale: 0.95, filter: "blur(10px)" });

                gsap.to(pageHeader, { opacity: 1, scale: 1, filter: "blur(0px)", duration: 1.4, ease: "power3.out", delay: 0.2 });
                gsap.to(chars, { opacity: 1, y: 0, scale: 1, filter: "blur(0px)", duration: 0.8, stagger: 0.015, ease: "power2.out", delay: 0.6 });
                gsap.to(fades, { opacity: 1, y: 0, filter: "blur(0px)", duration: 1.2, stagger: 0.15, ease: "power2.out", delay: 1.0 });
                setTimeout(() => { isAnimating = false; }, 2000);
            }
        }

        goToSlide(0);
        setInterval(() => {
            if (currentSlide < slides.length - 1) {
                goToSlide(currentSlide + 1);
            }
        }, 8000);
        
    </script>
</body>
</html>"""

with open('presentation.html', 'w') as f:
    f.write(html_content)

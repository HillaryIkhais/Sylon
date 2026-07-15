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
    <link href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Geist', 'sans-serif'],
                    },
                    colors: {
                        void: '#000000',
                        slate: '#111111',
                        bone: '#FFFFFF',
                        ash: '#888888'
                    }
                }
            }
        }
    </script>

    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            background-color: #000000;
            color: #FFFFFF;
            font-family: 'Geist', sans-serif;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            width: 100vw;
            height: 100vh;
        }

        #presentation-container {
            width: 1920px;
            height: 1080px;
            position: relative;
            background-color: #000000;
            overflow: hidden;
        }

        .slide {
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            padding: 100px 140px;
            opacity: 0;
            visibility: hidden;
        }

        .slide.active {
            opacity: 1;
            visibility: visible;
        }
        
        .line-wrapper { overflow: hidden; display: inline-block; vertical-align: top; }
        .line-inner { display: inline-block; transform: translateY(100%); }
        
        /* Ultra clean card */
        .clean-card {
            background: #0A0A0A;
            border: 1px solid #222222;
            border-radius: 12px;
        }
    </style>
</head>
<body>

    <div id="presentation-container">

        <!-- SLIDE 1 -->
        <div class="slide" id="slide1">
            <div class="w-full h-full flex flex-col justify-between">
                <div></div>
                <div class="max-w-4xl stagger-element opacity-0">
                    <h1 class="text-[120px] font-bold tracking-tight text-bone leading-none mb-6">Morlen</h1>
                    <p class="text-4xl text-bone font-medium mb-4">The Operating System for Business Decisions.</p>
                    <p class="text-2xl text-ash">Turning customer conversations into executive decisions.</p>
                </div>
                <div class="stagger-element opacity-0 border-t border-[#333] pt-8 flex justify-between items-end">
                    <div>
                        <p class="text-ash uppercase tracking-widest text-sm mb-2">Founder Name</p>
                        <p class="text-xl text-bone">Hillary Ikhais</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 2 -->
        <div class="slide" id="slide2">
            <div class="w-full h-full flex flex-col justify-center">
                <p class="text-ash uppercase tracking-widest text-sm mb-12 stagger-element opacity-0">The Problem</p>
                <div class="flex gap-24">
                    <div class="flex-1">
                        <h2 class="text-5xl font-medium text-bone mb-6 leading-tight stagger-element opacity-0">Businesses have automated transactions.</h2>
                        <p class="text-xl text-ash leading-relaxed mb-10 stagger-element opacity-0">Over the last two decades, businesses have adopted software for almost every operational function</p>
                        <ul class="text-3xl text-bone space-y-4 font-medium stagger-element opacity-0">
                            <li class="text-ash">Payments.</li>
                            <li class="text-ash">Inventory.</li>
                            <li class="text-ash">Accounting.</li>
                            <li class="text-ash">CRM.</li>
                            <li class="text-ash">Marketing.</li>
                            <li class="text-bone">Conversations</li>
                        </ul>
                    </div>
                    <div class="flex-1 border-l border-[#222] pl-24">
                        <p class="text-2xl text-bone mb-8 stagger-element opacity-0">Yet business owners still ask the same questions:</p>
                        <ul class="text-2xl text-ash space-y-6 mb-16 stagger-element opacity-0">
                            <li>What deserves attention today?</li>
                            <li>Which products should I restock?</li>
                            <li>Which customers need follow-up?</li>
                            <li>Where am I losing revenue?</li>
                            <li>Why have sales reduced?</li>
                        </ul>
                        <div class="pt-8 border-t border-[#222] stagger-element opacity-0">
                            <p class="text-2xl text-bone">Business software automates operations.</p>
                            <p class="text-2xl text-ash">It records what happened</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 3 -->
        <div class="slide" id="slide3">
            <div class="w-full h-full flex flex-col justify-center max-w-5xl">
                <p class="text-ash uppercase tracking-widest text-sm mb-8 stagger-element opacity-0">THE SHIFT</p>
                <h2 class="text-[80px] leading-tight font-bold text-bone mb-12 stagger-element opacity-0">Commerce has moved into conversations</h2>
                
                <div class="space-y-8 text-2xl text-ash leading-relaxed stagger-element opacity-0">
                    <p>Across Nigeria, businesses now operate inside messaging platforms.<br>
                    Customers now discover products, negotiate prices, confirm payments and arrange deliveries inside WhatsApp, Instagram and Facebook.</p>
                    
                    <p class="text-bone font-medium">For Nigerian MSMEs, the entire sales funnel now exists inside conversations.</p>
                    
                    <p>Yet traditional software was designed for structured forms, not unstructured conversations.</p>
                    
                    <p>As conversational commerce grows, businesses generate thousands of customer signals every day</p>
                    
                    <p class="text-bone">Most disappear without ever becoming business intelligence.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 4 -->
        <div class="slide" id="slide4">
            <div class="w-full h-full flex flex-col justify-center max-w-6xl">
                <p class="text-ash uppercase tracking-widest text-sm mb-8 stagger-element opacity-0">THE PROBLEM</p>
                <h2 class="text-6xl font-medium text-bone mb-8 stagger-element opacity-0">Every conversation creates decisions.</h2>
                <p class="text-2xl text-ash mb-12 stagger-element opacity-0">A business owner doesn't just receive messages.<br>They constantly decide:</p>
                
                <ul class="text-3xl text-bone space-y-6 mb-16 stagger-element opacity-0">
                    <li>• Should this customer receive follow-up?</li>
                    <li>• Is demand increasing for this product?</li>
                    <li>• Should inventory be reordered?</li>
                    <li>• Are customers becoming more price-sensitive?</li>
                    <li>• Which complaints appear repeatedly?</li>
                    <li>• Which customers are likely to return?</li>
                </ul>
                
                <div class="stagger-element opacity-0">
                    <p class="text-2xl text-ash mb-2">These decisions are still made manually.</p>
                    <p class="text-2xl text-bone">As conversations increase,<br>Decision complexity grows even faster.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 5 -->
        <div class="slide" id="slide5">
            <div class="w-full h-full flex flex-col justify-center">
                <p class="text-ash uppercase tracking-widest text-sm mb-6 stagger-element opacity-0">MORLEN</p>
                <h2 class="text-5xl font-medium text-bone mb-6 stagger-element opacity-0">Morlen is an Executive Decision Intelligence Platform.</h2>
                <p class="text-xl text-ash mb-6 max-w-4xl stagger-element opacity-0">Morlen continuously analyzes customer conversations, identifies business patterns and delivers prioritized business decisions.</p>
                <p class="text-xl text-ash mb-12 max-w-4xl stagger-element opacity-0">Instead of presenting plain dashboards,<br>Morlen produces a daily executive briefing.</p>
                
                <div class="grid grid-cols-2 gap-8 mb-12">
                    <div class="clean-card p-8 stagger-element opacity-0">
                        <h3 class="text-2xl font-medium text-bone mb-3">Executive Brief</h3>
                        <p class="text-ash">A daily summary of the highest priority decisions. inventory risks, customer churn, demand spikes, operational issues.</p>
                    </div>
                    <div class="clean-card p-8 stagger-element opacity-0">
                        <h3 class="text-2xl font-medium text-bone mb-3">Opportunity Feed</h3>
                        <p class="text-ash">Revenue opportunities detected from conversations including estimated impact, confidence score, supporting evidence.</p>
                    </div>
                    <div class="clean-card p-8 stagger-element opacity-0">
                        <h3 class="text-2xl font-medium text-bone mb-3">Business Memory</h3>
                        <p class="text-ash">Long-term behavioural intelligence about customers. for example customers increasingly ask for same day delivery, demand for product A rises every month end, customers compare prices before purchasing, repeat customers typically reorder after 21 days.</p>
                    </div>
                    <div class="clean-card p-8 stagger-element opacity-0">
                        <h3 class="text-2xl font-medium text-bone mb-3">Evidence-Based Recommendations</h3>
                        <p class="text-ash mb-3">Every recommendation explains</p>
                        <ul class="text-ash space-y-1 ml-4">
                            <li>• Why it exists</li>
                            <li>• Expected impact</li>
                            <li>• Supporting evidence</li>
                        </ul>
                    </div>
                </div>
                
                <div class="stagger-element opacity-0 pt-6 border-t border-[#222]">
                    <p class="text-xl text-ash">Business owners stop searching for answers.</p>
                    <p class="text-xl text-bone">Morlen brings the answers to them.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 6 -->
        <div class="slide" id="slide6">
            <div class="w-full h-full flex flex-col justify-center items-center text-center">
                <p class="text-ash uppercase tracking-widest text-sm mb-12 stagger-element opacity-0">MARKET</p>
                <h2 class="text-5xl font-medium text-bone mb-8 stagger-element opacity-0">A Massive Market</h2>
                <p class="text-2xl text-ash mb-4 stagger-element opacity-0">Nigeria has approximately:</p>
                <p class="text-[100px] font-bold text-bone leading-none mb-12 stagger-element opacity-0">39.6 Million MSMEs</p>
                
                <p class="text-2xl text-ash mb-6 stagger-element opacity-0">Representing:</p>
                <ul class="text-3xl text-bone space-y-4 mb-16 stagger-element opacity-0 inline-block text-left">
                    <li>• 96% of businesses</li>
                    <li>• 87.9% of employment</li>
                    <li>• 46.3% of GDP</li>
                </ul>
                
                <div class="stagger-element opacity-0">
                    <p class="text-2xl text-ash mb-2">Millions already conduct business primarily through messaging platforms.</p>
                    <p class="text-2xl text-bone">Morlen is built for this new operating environment.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 7 -->
        <div class="slide" id="slide7">
            <div class="w-full h-full flex flex-col justify-center">
                <p class="text-ash uppercase tracking-widest text-sm mb-6 stagger-element opacity-0">BUSINESS MODEL</p>
                <h2 class="text-5xl font-medium text-bone mb-6 stagger-element opacity-0">Subscription SaaS</h2>
                <p class="text-xl text-ash mb-12 max-w-4xl stagger-element opacity-0">Starting with a 30 day free trial giving Morlen enough time to learn from customer conversations, build business memory, generate meaningful insights</p>
                
                <div class="grid grid-cols-3 gap-6 mb-12">
                    <div class="clean-card p-8 stagger-element opacity-0 flex flex-col">
                        <h3 class="text-3xl font-medium text-bone mb-2">Starter <span class="text-xl text-ash font-normal">[N8,000/month]</span></h3>
                        <p class="text-sm text-ash mb-6 min-h-[40px]">For early stage businesses</p>
                        <ul class="text-bone space-y-3 flex-1 border-t border-[#222] pt-6">
                            <li>- Executive brief</li>
                            <li>- Business memory</li>
                            <li>- Basic decision intelligence</li>
                            <li>- Single workspace</li>
                        </ul>
                    </div>
                    
                    <div class="clean-card p-8 stagger-element opacity-0 flex flex-col border-[#555]">
                        <h3 class="text-3xl font-medium text-bone mb-2">Growth</h3>
                        <p class="text-sm text-ash mb-6 min-h-[40px]">Businesses managing increasing customer conversations.</p>
                        <ul class="text-bone space-y-3 flex-1 border-t border-[#222] pt-6">
                            <li>- Everything in starter</li>
                            <li>- Opportunity feed</li>
                            <li>- Advanced AI recommendations</li>
                            <li>- Multi channel integrations</li>
                            <li>- Team Collaboration</li>
                        </ul>
                    </div>
                    
                    <div class="clean-card p-8 stagger-element opacity-0 flex flex-col">
                        <h3 class="text-3xl font-medium text-bone mb-2">Enterprise</h3>
                        <p class="text-sm text-ash mb-6 min-h-[40px]">Organizations requiring company-wide decision intelligence and integrations.</p>
                        <ul class="text-bone space-y-3 flex-1 border-t border-[#222] pt-6">
                            <li>- Everything in growth</li>
                            <li>- Custom AI deployment</li>
                            <li>- Dedicate Support</li>
                            <li>- Enterprise security and governance</li>
                        </ul>
                    </div>
                </div>
                
                <p class="text-xl text-ash stagger-element opacity-0">Additional revenue:<br><span class="text-bone">• Enterprise Implementation & Onboarding</span></p>
            </div>
        </div>

        <!-- SLIDE 8 -->
        <div class="slide" id="slide8">
            <div class="w-full h-full flex flex-col justify-center max-w-4xl">
                <p class="text-ash uppercase tracking-widest text-sm mb-6 stagger-element opacity-0">FUNDING</p>
                <h2 class="text-6xl font-medium text-bone mb-6 stagger-element opacity-0">Raising Pre-Seed Capital</h2>
                <p class="text-2xl text-ash mb-12 stagger-element opacity-0">Investment will accelerate:</p>
                
                <div class="space-y-10 border-l-2 border-[#222] pl-8">
                    <div class="stagger-element opacity-0">
                        <h3 class="text-3xl font-medium text-bone mb-2">40% — Product Development</h3>
                        <p class="text-xl text-ash">Complete commercial MVP and core intelligence engine.</p>
                    </div>
                    <div class="stagger-element opacity-0">
                        <h3 class="text-3xl font-medium text-bone mb-2">25% — AI Infrastructure</h3>
                        <p class="text-xl text-ash">Inference, data pipelines and production infrastructure.</p>
                    </div>
                    <div class="stagger-element opacity-0">
                        <h3 class="text-3xl font-medium text-bone mb-2">20% — Customer Acquisition</h3>
                        <p class="text-xl text-ash">Pilot programs and early customer onboarding.</p>
                    </div>
                    <div class="stagger-element opacity-0">
                        <h3 class="text-3xl font-medium text-bone mb-2">15% — Strategic Partnerships & Operations</h3>
                        <p class="text-xl text-ash">Messaging integrations and business development.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 9 -->
        <div class="slide" id="slide9">
            <div class="w-full h-full flex flex-col justify-center items-center text-center">
                <p class="text-ash uppercase tracking-widest text-sm mb-12 stagger-element opacity-0">OUTCOMES</p>
                <h2 class="text-[80px] leading-none font-bold text-bone mb-16 stagger-element opacity-0">Expected Outcomes</h2>
                
                <div class="space-y-8 text-4xl font-medium text-bone stagger-element opacity-0">
                    <p>Commercial MVP</p>
                    <p>First paying customers</p>
                    <p>Validated product-market fit</p>
                    <p>Foundation for national expansion</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 10 -->
        <div class="slide" id="slide10">
            <div class="w-full h-full flex flex-col justify-center">
                <p class="text-ash uppercase tracking-widest text-sm mb-12 stagger-element opacity-0">WHY MORLEN?</p>
                
                <div class="flex gap-20">
                    <div class="flex-1 stagger-element opacity-0">
                        <p class="text-2xl text-ash mb-4">Business software has always answered one question:</p>
                        <h2 class="text-5xl font-medium text-bone mb-12">"What happened?"</h2>
                        
                        <ul class="text-2xl text-ash space-y-6">
                            <li>CRM stores customer records</li>
                            <li>ERP manages operations</li>
                            <li>BI dashboards visualize historical metrics</li>
                            <li>Chatbots automate conversations</li>
                        </ul>
                    </div>
                    
                    <div class="flex-1 border-l border-[#222] pl-20 stagger-element opacity-0">
                        <p class="text-2xl text-ash mb-4">Morlen answers a different question:</p>
                        <h2 class="text-5xl font-medium text-bone mb-12">"What should I do next?"</h2>
                        
                        <ul class="text-2xl text-bone space-y-6 font-medium">
                            <li>Every conversation contains intelligence.</li>
                            <li>Every business generates opportunities.</li>
                            <li>Every owner has limited attention.</li>
                        </ul>
                        
                        <div class="mt-12 pt-8 border-t border-[#222]">
                            <p class="text-3xl text-bone">Morlen exists to protect that attention—<br>by turning conversations into decisions.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 11 -->
        <div class="slide" id="slide11">
            <div class="w-full h-full flex flex-col justify-center items-center text-center">
                <h1 class="text-[180px] font-bold tracking-tighter text-bone leading-none mb-12 stagger-element opacity-0">MORLEN</h1>
                
                <p class="text-4xl text-ash mb-4 stagger-element opacity-0">The future of business isn't more software.</p>
                <p class="text-5xl font-medium text-bone mb-20 stagger-element opacity-0">It's better decisions.</p>
                
                <div class="stagger-element opacity-0">
                    <p class="text-2xl text-ash mb-2">Businesses already have the conversations.</p>
                    <p class="text-3xl text-bone font-medium">Morlen turns them into decisions.</p>
                </div>
            </div>
        </div>

    </div>

    <script>
        gsap.registerPlugin(SplitText);

        function animateText(element) {
            const split = new SplitText(element, { type: "lines", linesClass: "line-wrapper" });
            const inners = [];
            
            split.lines.forEach(line => {
                const inner = document.createElement('div');
                inner.className = 'line-inner';
                inner.innerHTML = line.innerHTML;
                line.innerHTML = '';
                line.appendChild(inner);
                inners.push(inner);
            });

            return gsap.to(inners, {
                y: 0,
                duration: 1,
                stagger: 0.1,
                ease: "power4.out"
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
            
            if (current) {
                gsap.to(current, {
                    opacity: 0,
                    duration: 0.5,
                    onComplete: () => {
                        current.classList.remove('active');
                        current.style.visibility = 'hidden';
                    }
                });
            }

            next.classList.add('active');
            next.style.visibility = 'visible';
            
            // Setup next elements
            const elements = next.querySelectorAll('.stagger-element');
            gsap.set(elements, { opacity: 0, y: 30 });
            
            // Handle split text elements if any
            const textElements = next.querySelectorAll('h1, h2');
            let textAnims = [];
            textElements.forEach(el => {
                const innerLines = el.querySelectorAll('.line-inner');
                if (innerLines.length > 0) {
                    gsap.set(innerLines, { y: '100%' });
                    textAnims.push(gsap.to(innerLines, {y: 0, duration: 1, stagger: 0.1, ease: 'power4.out', delay: 0.3}));
                }
            });

            // Animate next elements
            gsap.to(elements, {
                opacity: 1,
                y: 0,
                duration: 0.8,
                stagger: 0.15,
                ease: "power3.out",
                delay: 0.1,
                onComplete: () => {
                    currentSlide = index;
                    isAnimating = false;
                }
            });
        }

        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight' || e.key === 'Space') goToSlide(currentSlide + 1);
            if (e.key === 'ArrowLeft') goToSlide(currentSlide - 1);
        });

        // Start first slide
        slides[0].classList.add('active');
        slides[0].style.visibility = 'visible';
        slides[0].style.opacity = 1;
        gsap.set(slides[0].querySelectorAll('.stagger-element'), { opacity: 0, y: 30 });
        gsap.to(slides[0].querySelectorAll('.stagger-element'), {
            opacity: 1, y: 0, duration: 0.8, stagger: 0.15, ease: "power3.out", delay: 0.1
        });
        
        window.goToSlide = goToSlide;
    </script>
</body>
</html>"""

with open('presentation.html', 'w') as f:
    f.write(html_content)

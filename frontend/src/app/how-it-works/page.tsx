"use client";

import { useRef } from "react";
import gsap from "gsap";
import { useGSAP } from "@gsap/react";
import { MessageSquareText, BrainCircuit, FileText, Zap } from "lucide-react";
import Link from "next/link";
import { useState } from "react";
import WaitlistModal from "@/components/WaitlistModal";

export default function HowItWorksPage() {
  const [isWaitlistOpen, setIsWaitlistOpen] = useState(false);
  const containerRef = useRef<HTMLDivElement>(null);
  const heroRef = useRef<HTMLDivElement>(null);
  const stepRefs = useRef<(HTMLDivElement | null)[]>([]);

  useGSAP(() => {
    // Hero Entrance
    gsap.fromTo(
      heroRef.current,
      { opacity: 0, y: 40, scale: 0.95 },
      { opacity: 1, y: 0, scale: 1, duration: 1.2, ease: "power4.out" }
    );

    // Staggered Steps
    stepRefs.current.forEach((step, index) => {
      if (!step) return;
      gsap.fromTo(
        step,
        { opacity: 0, y: 60 },
        { 
          opacity: 1, 
          y: 0, 
          duration: 1.2, 
          ease: "power3.out",
          scrollTrigger: {
            trigger: step,
            start: "top 85%",
          },
          delay: index < 2 ? index * 0.2 + 0.4 : 0 // Only delay initial visible ones
        }
      );
    });
  }, { scope: containerRef });

  const steps = [
    {
      title: "1. Raw Signal Capture",
      description: "Morlen hooks directly into your primary communication channels—WhatsApp Business, Instagram Direct, and customer support emails. It silently ingests thousands of customer interactions, complaints, and product requests without requiring any manual data entry from your team.",
      icon: <MessageSquareText className="w-8 h-8 text-brand-brown" />,
      metric: "Ingests 10k+ messages per second",
    },
    {
      title: "2. Deep Context Analysis",
      description: "Unlike basic keyword trackers, Morlen uses state-of-the-art Large Language Models (LLMs) to understand the nuance behind every message. It cross-references chat data with your inventory and sales data to identify invisible buying patterns, churn risks, and pricing resistance in real-time.",
      icon: <BrainCircuit className="w-8 h-8 text-brand-brown" />,
      metric: "Identifies sentiment and intent with 99% accuracy",
    },
    {
      title: "3. The Executive Brief",
      description: "You don't log into a dashboard to stare at complex charts. Every morning, Morlen delivers a highly synthesized Executive Brief directly to your inbox or Slack. It tells you exactly what is happening in plain English—for example: 'Demand for Product X surged 40% yesterday, but customers are complaining about shipping costs.'",
      icon: <FileText className="w-8 h-8 text-brand-brown" />,
      metric: "Saves founders 15+ hours of weekly analysis",
    },
    {
      title: "4. Action & Execution",
      description: "Morlen doesn't just inform you; it equips you to act. Alongside every insight is an evidence-based recommendation. With a single click, you can approve an automated response campaign, adjust a price point on your storefront, or trigger a restock order with your supplier.",
      icon: <Zap className="w-8 h-8 text-brand-brown" />,
      metric: "Reduces decision execution time from days to seconds",
    }
  ];

  return (
    <div ref={containerRef} className="min-h-screen pt-24 pb-32 relative overflow-hidden">
      
      {/* Cinematic Ethereal Backgrounds */}
      <div className="absolute top-0 left-0 w-full h-full overflow-hidden pointer-events-none -z-10">
        <div className="absolute top-[-10%] right-[-5%] w-[800px] h-[800px] bg-brand-brown/10 dark:bg-brand-brown/5 rounded-full blur-[150px]" />
        <div className="absolute bottom-[-20%] left-[-10%] w-[1000px] h-[1000px] bg-brand-lightbrown/5 dark:bg-brand-lightbrown/5 rounded-full blur-[150px]" />
      </div>

      <div className="max-w-5xl mx-auto px-4 md:px-8">
        
        {/* Hero Section */}
        <div ref={heroRef} className="text-center mb-24 pt-12">
          <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-brand-brown/10 border border-brand-brown/20 text-brand-brown text-sm font-semibold tracking-wide mb-8">
            <Zap className="w-4 h-4" /> THE MECHANICS
          </div>
          <h1 className="text-5xl md:text-7xl font-bold tracking-tight text-brand-dark dark:text-white mb-6 leading-tight">
            Beyond Insights.<br />
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-brand-brown to-brand-lightbrown">
              Direct Business Impact.
            </span>
          </h1>
          <p className="text-xl text-brand-dark/60 dark:text-white/50 max-w-3xl mx-auto leading-relaxed">
            Morlen transforms your raw customer conversations into a definitive operational playbook. Here is exactly how it turns noise into revenue.
          </p>
        </div>

        {/* The Pipeline / Steps */}
        <div className="space-y-8 md:space-y-12 relative">
          
          {/* Vertical Connecting Line */}
          <div className="absolute left-8 md:left-1/2 top-10 bottom-10 w-px bg-gradient-to-b from-brand-brown/0 via-brand-brown/30 to-brand-brown/0 hidden md:block" />

          {steps.map((step, index) => {
            const isEven = index % 2 === 0;
            return (
              <div 
                key={index}
                ref={el => { stepRefs.current[index] = el; }}
                className={`relative flex flex-col md:flex-row gap-8 md:gap-16 items-center ${isEven ? 'md:flex-row' : 'md:flex-row-reverse'}`}
              >
                {/* Content Box */}
                <div className={`w-full md:w-1/2 flex ${isEven ? 'md:justify-end' : 'md:justify-start'}`}>
                  <div className="bg-white/40 dark:bg-black/40 backdrop-blur-xl border border-brand-dark/10 dark:border-white/10 rounded-3xl p-8 md:p-10 shadow-2xl hover:bg-white/60 dark:hover:bg-black/60 transition-colors w-full max-w-lg">
                    <div className="w-16 h-16 rounded-2xl bg-brand-brown/10 flex items-center justify-center mb-6">
                      {step.icon}
                    </div>
                    <h3 className="text-2xl font-bold text-brand-dark dark:text-white mb-4">
                      {step.title}
                    </h3>
                    <p className="text-brand-dark/70 dark:text-white/60 text-lg leading-relaxed mb-6">
                      {step.description}
                    </p>
                    <div className="inline-block px-4 py-2 bg-black/5 dark:bg-white/5 rounded-lg border border-black/5 dark:border-white/5">
                      <p className="text-sm font-semibold text-brand-brown tracking-wide uppercase">
                        {step.metric}
                      </p>
                    </div>
                  </div>
                </div>

                {/* Center Node (Desktop only) */}
                <div className="hidden md:flex absolute left-1/2 -translate-x-1/2 w-16 h-16 items-center justify-center">
                  <div className="w-4 h-4 rounded-full bg-brand-brown shadow-[0_0_20px_rgba(189,142,94,0.6)] z-10" />
                </div>
                
                {/* Empty Space for layout balancing */}
                <div className="hidden md:block w-1/2" />
              </div>
            );
          })}
        </div>

      </div>

      {/* Final CTA */}
      <div className="w-full text-center mt-32 mb-24 px-4 relative z-10">
        <h2 className="text-3xl md:text-5xl font-bold text-brand-dark dark:text-white mb-6">Ready to see it in action?</h2>
        <p className="text-lg text-brand-dark/70 dark:text-white/60 mb-10 max-w-xl mx-auto">Join the waitlist today and transform how you make decisions.</p>
        <button
          onClick={() => setIsWaitlistOpen(true)}
          className="text-white bg-brand-brown px-10 py-4 rounded-full font-bold inline-flex items-center justify-center space-x-2 hover:opacity-90 transition-all shadow-xl hover:shadow-2xl hover:-translate-y-1"
        >
          <span>Join Waitlist</span>
        </button>
      </div>

      {/* Main Footer */}
      <footer className="w-full pb-8 pt-4 px-8 md:px-16 z-50 relative mt-auto border-t border-brand-dark/10 dark:border-white/10">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between text-xs text-brand-dark dark:text-white/70 font-medium">
          {/* Logo */}
          <div className="mb-4 md:mb-0">
            <span className="text-xl font-bold tracking-wider text-brand-brown">MORLEN</span>
          </div>
          {/* Footer Links */}
          <div className="flex space-x-6 mb-4 md:mb-0">
            <Link href="/pricing" className="hover:text-brand-lightbrown transition-colors">Pricing</Link>
            <Link href="#" className="hover:text-brand-lightbrown transition-colors">Privacy Policy</Link>
            <Link href="#" className="hover:text-brand-lightbrown transition-colors">Terms of Service</Link>
            <Link href="#" className="hover:text-brand-lightbrown transition-colors">Security</Link>
            <Link href="#" className="hover:text-brand-lightbrown transition-colors">Contact</Link>
          </div>
          {/* Copyright */}
          <div>
            © 2026 Morlen Behavioral Intelligence. All rights reserved.
          </div>
        </div>
      </footer>

      <WaitlistModal 
        isOpen={isWaitlistOpen} 
        onClose={() => setIsWaitlistOpen(false)} 
      />
    </div>
  );
}

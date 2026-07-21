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
    gsap.fromTo(
      heroRef.current,
      { opacity: 0, y: 40, scale: 0.95 },
      { opacity: 1, y: 0, scale: 1, duration: 1.2, ease: "power4.out" }
    );

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
          delay: index < 2 ? index * 0.2 + 0.4 : 0
        }
      );
    });
  }, { scope: containerRef });

  const steps = [
    {
      title: "1. Connect Your Apps",
      description: "Morlen safely connects to the apps you already use, like WhatsApp and Instagram. It automatically reads customer questions, complaints, and requests in the background so you never have to type them into a spreadsheet manually.",
      icon: <MessageSquareText className="w-8 h-8 text-brand-brown" />,
      metric: "Works quietly in the background",
    },
    {
      title: "2. Understand the Meaning",
      description: "Instead of just counting words, Morlen's smart AI actually understands what your customers mean. It compares what people are saying with what you are selling to spot hidden trends, like when a price is too high or a product is about to run out.",
      icon: <BrainCircuit className="w-8 h-8 text-brand-brown" />,
      metric: "Catches what you might miss",
    },
    {
      title: "3. Your Morning Summary",
      description: "You don't need to learn complicated software or stare at confusing charts. Every morning, Morlen sends a simple summary straight to your email. It tells you exactly what happened yesterday in plain English.",
      icon: <FileText className="w-8 h-8 text-brand-brown" />,
      metric: "Saves you hours of reading chats",
    },
    {
      title: "4. Take Instant Action",
      description: "Morlen doesn't just give you news; it gives you solutions. Next to every problem, it suggests a fix. With one click, you can send an automatic apology to a frustrated customer, update a price, or order more stock.",
      icon: <Zap className="w-8 h-8 text-brand-brown" />,
      metric: "Fix problems in seconds, not days",
    }
  ];

  return (
    <div className="flex-grow flex flex-col relative w-full z-0 overflow-x-hidden">
      
      {/* Cinematic Ethereal Backgrounds */}
      <div className="fixed inset-0 pointer-events-none z-[-1]">
        <div className="absolute top-[-10%] right-[-5%] w-[800px] h-[800px] bg-brand-brown/10 dark:bg-brand-brown/5 rounded-full blur-[150px]" />
        <div className="absolute bottom-[-20%] left-[-10%] w-[1000px] h-[1000px] bg-brand-lightbrown/5 dark:bg-brand-lightbrown/5 rounded-full blur-[150px]" />
      </div>

      {/* Main Content Wrapper */}
      <div ref={containerRef} className="flex-grow flex flex-col items-center justify-start pt-24 sm:pt-32 pb-24 px-4 z-10 relative w-full">
        <div className="max-w-5xl mx-auto w-full">
          
          {/* Hero Section */}
          <div ref={heroRef} className="text-center mb-24 pt-12">
            <h1 className="text-5xl md:text-7xl font-bold tracking-tight text-brand-dark dark:text-white mb-6 leading-tight">
              Beyond Analytics.<br />
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-brand-brown to-brand-lightbrown">
                Real Business Results.
              </span>
            </h1>
            <p className="text-xl text-brand-dark/70 dark:text-white/60 max-w-3xl mx-auto leading-relaxed font-medium">
              Morlen transforms your everyday customer chats into a clear plan of action. Here is exactly how it turns noise into revenue.
            </p>
          </div>

          {/* The Pipeline / Steps */}
          <div className="space-y-12 md:space-y-24 relative mb-32 w-full">
            
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
                    <div className="bg-white/40 dark:bg-black/40 backdrop-blur-xl border border-brand-dark/10 dark:border-white/10 rounded-3xl p-8 md:p-10 shadow-2xl hover:bg-white/60 dark:hover:bg-black/60 transition-colors w-full max-w-lg relative z-20">
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
                  <div className="hidden md:flex absolute left-1/2 -translate-x-1/2 w-16 h-16 items-center justify-center z-10">
                    <div className="w-4 h-4 rounded-full bg-brand-brown shadow-[0_0_20px_rgba(189,142,94,0.6)]" />
                  </div>
                  
                  {/* Empty Space for layout balancing */}
                  <div className="hidden md:block w-1/2" />
                </div>
              );
            })}
          </div>

          {/* Final CTA */}
          <div className="w-full text-center mb-12">
            <h2 className="text-3xl md:text-5xl font-bold text-brand-dark dark:text-white mb-6">Ready to see it in action?</h2>
            <p className="text-lg text-brand-dark/70 dark:text-white/60 mb-10 max-w-xl mx-auto font-medium">Join the waitlist today and let Morlen handle the hard work for you.</p>
            <button
              onClick={() => setIsWaitlistOpen(true)}
              className="text-white bg-brand-brown px-10 py-4 rounded-full font-bold inline-flex items-center justify-center space-x-2 hover:opacity-90 transition-all shadow-xl hover:shadow-2xl hover:-translate-y-1"
            >
              <span>Join Waitlist</span>
            </button>
          </div>
        </div>
      </div>

      {/* Main Footer */}
      <footer className="w-full pb-8 pt-4 px-8 md:px-16 z-50 relative mt-auto border-t border-brand-dark/10 dark:border-white/10 shrink-0">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between text-xs text-brand-dark dark:text-white/70 font-medium">
          <div className="mb-4 md:mb-0">
            <span className="text-xl font-bold tracking-wider text-brand-brown">MORLEN</span>
          </div>
          <div className="flex space-x-6 mb-4 md:mb-0">
            <Link href="/pricing" className="hover:text-brand-lightbrown transition-colors">Pricing</Link>
            <Link href="#" className="hover:text-brand-lightbrown transition-colors">Privacy Policy</Link>
            <Link href="#" className="hover:text-brand-lightbrown transition-colors">Terms of Service</Link>
            <Link href="#" className="hover:text-brand-lightbrown transition-colors">Security</Link>
            <Link href="#" className="hover:text-brand-lightbrown transition-colors">Contact</Link>
          </div>
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

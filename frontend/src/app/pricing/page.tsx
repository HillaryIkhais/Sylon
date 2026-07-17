"use client";

import Link from "next/link";
import { useRef } from "react";
import { ArrowRight, Check } from "lucide-react";
import gsap from "gsap";
import { useGSAP } from "@gsap/react";

export default function Pricing() {
  const containerRef = useRef<HTMLDivElement>(null);

  useGSAP(() => {
    gsap.fromTo(".fade-up", 
      { y: 40, opacity: 0 },
      { y: 0, opacity: 1, duration: 1, stagger: 0.1, ease: "power3.out" }
    );
  }, { scope: containerRef });

  return (
    <div ref={containerRef} className="w-full max-w-7xl mx-auto p-4 md:p-8 flex flex-col flex-grow animate-in fade-in duration-500 relative">
      {/* Background Glow */}
      <div className="absolute top-[10%] left-[10%] w-[80%] h-[80%] bg-brand-lightbrown/10 blur-[150px] rounded-full pointer-events-none z-[-1]" />

      <div className="text-center mb-16 pt-12 fade-up">
        <h1 className="page-heading text-4xl md:text-5xl lg:text-6xl font-bold tracking-tight mb-4">
          Pricing built for scale.
        </h1>
        <p className="text-brand-dark/60 dark:text-white/60 text-lg max-w-2xl mx-auto">
          Choose the tier that fits your conversation volume and intelligence needs.
        </p>
      </div>

      {/* Pricing Grid */}
      <div className="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto mb-16 w-full fade-up">
        
        {/* Starter */}
        <div className="glass-card rounded-3xl p-8 flex flex-col border border-brand-dark/10 dark:border-white/10 hover:border-brand-brown/40 transition-all hover:-translate-y-1">
          <h3 className="text-xl font-bold text-brand-dark dark:text-white mb-2">Starter</h3>
          <p className="text-sm text-brand-dark/60 dark:text-white/60 mb-6">Perfect for small teams getting started with automation.</p>
          <div className="mb-6 flex items-end gap-1 border-b border-brand-dark/10 dark:border-white/10 pb-6">
            <span className="text-4xl font-bold text-brand-dark dark:text-white">₦8,000</span>
            <span className="text-brand-dark/50 dark:text-white/50 mb-1">/mo</span>
          </div>
          <ul className="space-y-4 mb-8 flex-1">
            <li className="flex items-center gap-3 text-sm text-brand-dark/80 dark:text-white/80">
              <Check className="w-4 h-4 text-brand-brown dark:text-brand-lightbrown flex-shrink-0" /> Up to 1,000 conversations
            </li>
            <li className="flex items-center gap-3 text-sm text-brand-dark/80 dark:text-white/80">
              <Check className="w-4 h-4 text-brand-brown dark:text-brand-lightbrown flex-shrink-0" /> WhatsApp Integration
            </li>
            <li className="flex items-center gap-3 text-sm text-brand-dark/80 dark:text-white/80">
              <Check className="w-4 h-4 text-brand-brown dark:text-brand-lightbrown flex-shrink-0" /> Basic AI Replies
            </li>
          </ul>
          <button className="w-full py-3 rounded-full bg-brand-dark/5 dark:bg-white/10 text-brand-dark dark:text-white font-semibold hover:bg-brand-dark/10 dark:hover:bg-white/20 transition-colors">
            Start Free Trial
          </button>
        </div>

        {/* Growth - Featured */}
        <div className="glass-card rounded-3xl p-8 flex flex-col relative transform md:-translate-y-4 border-2 border-brand-brown/50 dark:border-brand-lightbrown/50 shadow-2xl shadow-brand-lightbrown/10">
          <div className="absolute top-0 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-gradient-to-r from-brand-brown to-brand-lightbrown text-white text-[10px] font-bold px-4 py-1.5 rounded-full uppercase tracking-wider">
            Most Popular
          </div>
          <h3 className="text-xl font-bold text-brand-brown dark:text-brand-lightbrown mb-2">Growth</h3>
          <p className="text-sm text-brand-dark/60 dark:text-white/60 mb-6">Full multi-agent capabilities and business memory.</p>
          <div className="mb-6 flex items-end gap-1 border-b border-brand-dark/10 dark:border-white/10 pb-6">
            <span className="text-4xl font-bold text-brand-dark dark:text-white">₦15,000</span>
            <span className="text-brand-dark/50 dark:text-white/50 mb-1">/mo</span>
          </div>
          <ul className="space-y-4 mb-8 flex-1">
            <li className="flex items-center gap-3 text-sm text-brand-dark/80 dark:text-white/80">
              <Check className="w-4 h-4 text-brand-brown dark:text-brand-lightbrown flex-shrink-0" /> Up to 10,000 conversations
            </li>
            <li className="flex items-center gap-3 text-sm text-brand-dark/80 dark:text-white/80">
              <Check className="w-4 h-4 text-brand-brown dark:text-brand-lightbrown flex-shrink-0" /> WhatsApp, IG, Facebook
            </li>
            <li className="flex items-center gap-3 text-sm text-brand-dark/80 dark:text-white/80">
              <Check className="w-4 h-4 text-brand-brown dark:text-brand-lightbrown flex-shrink-0" /> Executive Brief & Memory
            </li>
            <li className="flex items-center gap-3 text-sm text-brand-dark/80 dark:text-white/80">
              <Check className="w-4 h-4 text-brand-brown dark:text-brand-lightbrown flex-shrink-0" /> CX & CFO Agent Debate
            </li>
          </ul>
          <button className="w-full py-3 rounded-full bg-gradient-to-r from-brand-brown to-brand-lightbrown text-white font-bold hover:opacity-90 transition-opacity">
            Get Started
          </button>
        </div>

        {/* Enterprise */}
        <div className="glass-card rounded-3xl p-8 flex flex-col border border-brand-dark/10 dark:border-white/10 hover:border-brand-brown/40 transition-all hover:-translate-y-1">
          <h3 className="text-xl font-bold text-brand-dark dark:text-white mb-2">Enterprise</h3>
          <p className="text-sm text-brand-dark/60 dark:text-white/60 mb-6">Custom models and unlimited scale for big retail.</p>
          <div className="mb-6 border-b border-brand-dark/10 dark:border-white/10 pb-6">
            <span className="text-4xl font-bold text-brand-dark dark:text-white">Custom</span>
          </div>
          <ul className="space-y-4 mb-8 flex-1">
            <li className="flex items-center gap-3 text-sm text-brand-dark/80 dark:text-white/80">
              <Check className="w-4 h-4 text-brand-brown dark:text-brand-lightbrown flex-shrink-0" /> Unlimited conversations
            </li>
            <li className="flex items-center gap-3 text-sm text-brand-dark/80 dark:text-white/80">
              <Check className="w-4 h-4 text-brand-brown dark:text-brand-lightbrown flex-shrink-0" /> Custom Knowledge Graphs
            </li>
            <li className="flex items-center gap-3 text-sm text-brand-dark/80 dark:text-white/80">
              <Check className="w-4 h-4 text-brand-brown dark:text-brand-lightbrown flex-shrink-0" /> Dedicated Success Manager
            </li>
            <li className="flex items-center gap-3 text-sm text-brand-dark/80 dark:text-white/80">
              <Check className="w-4 h-4 text-brand-brown dark:text-brand-lightbrown flex-shrink-0" /> Custom Integration Webhooks
            </li>
          </ul>
          <button className="w-full py-3 rounded-full bg-brand-dark/5 dark:bg-white/10 text-brand-dark dark:text-white font-semibold hover:bg-brand-dark/10 dark:hover:bg-white/20 transition-colors">
            Contact Sales
          </button>
        </div>

      </div>

      {/* Bottom CTA */}
      <div className="text-center py-16 border-t border-brand-dark/10 dark:border-white/10 max-w-3xl mx-auto fade-up">
        <h2 className="text-3xl md:text-4xl font-bold tracking-tight mb-8 leading-tight text-brand-dark dark:text-white">
          Your business has a memory. Start using it.
        </h2>
        <Link 
          href="/dashboard"
          className="inline-flex items-center gap-2 px-8 py-4 rounded-full bg-gradient-to-r from-brand-brown to-brand-lightbrown text-white font-bold hover:scale-105 transition-transform shadow-xl"
        >
          Return to Executive Briefing
          <ArrowRight className="w-4 h-4" />
        </Link>
      </div>
    </div>
  );
}

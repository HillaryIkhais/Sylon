"use client";

import Link from "next/link";
import { ArrowRight, Check } from "lucide-react";

export default function Pricing() {
  return (
    <div className="min-h-screen bg-[#050505] text-white flex flex-col relative overflow-hidden">
      
      {/* Navbar */}
      <nav className="w-full max-w-7xl mx-auto px-6 py-6 flex items-center justify-between relative z-10 border-b border-white/5">
        <Link href="/" className="flex items-center gap-2">
          <span className="font-semibold text-xl tracking-tight">Morlen</span>
        </Link>
        <Link 
          href="/dashboard" 
          className="px-5 py-2.5 rounded-full bg-white/10 text-white text-sm font-medium hover:bg-white/20 transition-colors"
        >
          Return to Dashboard
        </Link>
      </nav>

      {/* Abstract Backgrounds */}
      <div className="absolute top-[20%] left-[-10%] w-[500px] h-[500px] bg-brand-lightbrown/10 rounded-full blur-[120px] pointer-events-none" />
      <div className="absolute bottom-[20%] right-[-10%] w-[600px] h-[600px] bg-brand-brown/10 rounded-full blur-[150px] pointer-events-none" />

      <main className="flex-1 max-w-7xl mx-auto px-6 py-24 relative z-10 w-full">
        
        <div className="text-center mb-16">
          <h1 className="text-4xl md:text-5xl font-bold tracking-tight mb-4">Pricing built for scale.</h1>
          <p className="text-white/60 text-lg max-w-2xl mx-auto">Choose the tier that fits your conversation volume and intelligence needs.</p>
        </div>

        {/* Pricing Grid */}
        <div className="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto mb-32">
          
          {/* Starter */}
          <div className="p-8 rounded-3xl bg-zinc-900/50 border border-white/10 backdrop-blur-md flex flex-col hover:border-brand-lightbrown/30 transition-colors">
            <h3 className="text-xl font-semibold mb-2">Starter</h3>
            <p className="text-sm text-white/60 mb-6">Perfect for small teams getting started with automation.</p>
            <div className="mb-6 flex items-end gap-1 border-b border-white/10 pb-6">
              <span className="text-4xl font-bold">₦8,000</span>
              <span className="text-white/50 mb-1">/mo</span>
            </div>
            <ul className="space-y-4 mb-8 flex-1">
              <li className="flex items-center gap-3 text-sm text-white/80">
                <Check className="w-4 h-4 text-brand-lightbrown flex-shrink-0" /> Up to 1,000 conversations
              </li>
              <li className="flex items-center gap-3 text-sm text-white/80">
                <Check className="w-4 h-4 text-brand-lightbrown flex-shrink-0" /> WhatsApp Integration
              </li>
              <li className="flex items-center gap-3 text-sm text-white/80">
                <Check className="w-4 h-4 text-brand-lightbrown flex-shrink-0" /> Basic AI Replies
              </li>
            </ul>
            <button className="w-full py-3 rounded-full bg-white/10 text-white font-semibold hover:bg-white/20 transition-colors">
              Start Free Trial
            </button>
          </div>

          {/* Growth */}
          <div className="p-8 rounded-3xl bg-gradient-to-b from-brand-lightbrown/10 to-transparent border border-brand-lightbrown/50 backdrop-blur-xl flex flex-col relative transform md:-translate-y-4 shadow-2xl shadow-brand-lightbrown/10 group">
            <h3 className="text-xl font-bold mb-2 text-brand-lightbrown">Growth</h3>
            <p className="text-sm text-white/60 mb-6">Full multi-agent capabilities and business memory.</p>
            <div className="mb-6 flex items-end gap-1 border-b border-white/10 pb-6">
              <span className="text-4xl font-bold">₦15,000</span>
              <span className="text-white/50 mb-1">/mo</span>
            </div>
            <ul className="space-y-4 mb-8 flex-1">
              <li className="flex items-center gap-3 text-sm text-white/80">
                <Check className="w-4 h-4 text-brand-lightbrown flex-shrink-0" /> Up to 10,000 conversations
              </li>
              <li className="flex items-center gap-3 text-sm text-white/80">
                <Check className="w-4 h-4 text-brand-lightbrown flex-shrink-0" /> WhatsApp, IG, Facebook
              </li>
              <li className="flex items-center gap-3 text-sm text-white/80">
                <Check className="w-4 h-4 text-brand-lightbrown flex-shrink-0" /> Executive Brief & Memory
              </li>
              <li className="flex items-center gap-3 text-sm text-white/80">
                <Check className="w-4 h-4 text-brand-lightbrown flex-shrink-0" /> CX & CFO Agent Debate
              </li>
            </ul>
            <button className="w-full py-3 rounded-full bg-brand-lightbrown text-brand-dark font-bold hover:opacity-90 transition-opacity">
              Get Started
            </button>
          </div>

          {/* Enterprise */}
          <div className="p-8 rounded-3xl bg-zinc-900/50 border border-white/10 backdrop-blur-md flex flex-col hover:border-brand-lightbrown/30 transition-colors">
            <h3 className="text-xl font-semibold mb-2">Enterprise</h3>
            <p className="text-sm text-white/60 mb-6">Custom models and unlimited scale for big retail.</p>
            <div className="mb-6 border-b border-white/10 pb-6">
              <span className="text-4xl font-bold">Custom</span>
            </div>
            <ul className="space-y-4 mb-8 flex-1">
              <li className="flex items-center gap-3 text-sm text-white/80">
                <Check className="w-4 h-4 text-brand-lightbrown flex-shrink-0" /> Unlimited conversations
              </li>
              <li className="flex items-center gap-3 text-sm text-white/80">
                <Check className="w-4 h-4 text-brand-lightbrown flex-shrink-0" /> Custom Knowledge Graphs
              </li>
              <li className="flex items-center gap-3 text-sm text-white/80">
                <Check className="w-4 h-4 text-brand-lightbrown flex-shrink-0" /> Dedicated Success Manager
              </li>
              <li className="flex items-center gap-3 text-sm text-white/80">
                <Check className="w-4 h-4 text-brand-lightbrown flex-shrink-0" /> Custom Integration Webhooks
              </li>
            </ul>
            <button className="w-full py-3 rounded-full bg-white/10 text-white font-semibold hover:bg-white/20 transition-colors">
              Contact Sales
            </button>
          </div>

        </div>

        {/* Closing Sequence */}
        <div className="text-center py-24 border-t border-white/10 max-w-3xl mx-auto">
          <h2 className="text-3xl md:text-5xl font-bold tracking-tight mb-8 leading-tight">
            "Every conversation tells a story. Morlen helps businesses know which ones matter."
          </h2>
          <Link 
            href="/dashboard"
            className="inline-flex items-center gap-2 px-8 py-4 rounded-full bg-white text-black font-semibold hover:scale-105 transition-transform"
          >
            Return to Executive Briefing
            <ArrowRight className="w-4 h-4" />
          </Link>
        </div>

      </main>
    </div>
  );
}

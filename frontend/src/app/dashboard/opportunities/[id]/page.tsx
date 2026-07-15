"use client";

import Link from "next/link";
import { 
  ArrowLeft,
  Sparkles,
  TrendingUp,
  MessageSquare,
  Bot,
  BrainCircuit,
  CheckCircle2,
  AlertCircle
} from "lucide-react";
import { useState } from "react";

export default function OpportunityDetail() {
  const [actionTaken, setActionTaken] = useState(false);

  return (
    <div className="min-h-screen bg-[#050505] text-white flex overflow-hidden">
      
      {/* Sidebar (Collapsed for focus) */}
      <aside className="w-20 border-r border-white/10 bg-[#0a0a0a] flex flex-col items-center py-6 relative z-20">
        <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center font-bold text-sm mb-12">M</div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 overflow-y-auto relative">
        <div className="max-w-4xl mx-auto p-10 relative z-10">
          
          <Link href="/dashboard" className="inline-flex items-center gap-2 text-sm text-zinc-400 hover:text-white mb-8 transition-colors">
            <ArrowLeft className="w-4 h-4" />
            Back to Executive Brief
          </Link>

          <div className="flex items-start justify-between mb-12">
            <div>
              <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/10 text-amber-400 text-xs font-medium border border-amber-500/20 mb-4">
                <Sparkles className="w-3 h-3" />
                Revenue Opportunity
              </div>
              <h1 className="text-3xl font-bold tracking-tight mb-2">Pricing Objection on "Premium Tier"</h1>
              <p className="text-zinc-400">Morlen detected a recurring pattern of churn at the checkout phase.</p>
            </div>
            
            <div className="text-right">
              <div className="text-sm text-zinc-500 mb-1">Estimated Impact</div>
              <div className="text-3xl font-bold text-emerald-400">+$12,500<span className="text-lg text-emerald-500/50">/mo</span></div>
            </div>
          </div>

          {/* Logic Flow / Reasoning Trace */}
          <div className="mb-12">
            <h2 className="text-lg font-semibold mb-6 flex items-center gap-2">
              <BrainCircuit className="w-5 h-5 text-indigo-400" />
              How Morlen found this
            </h2>
            
            <div className="relative pl-6 before:absolute before:left-[11px] before:top-2 before:bottom-2 before:w-0.5 before:bg-white/10 space-y-8">
              
              <div className="relative">
                <div className="absolute -left-[30px] top-1 w-4 h-4 rounded-full bg-zinc-800 border-2 border-indigo-500 z-10" />
                <h3 className="font-medium text-white mb-1">Customer repeatedly requests discount</h3>
                <p className="text-sm text-zinc-400">Individual instances of price pushback on WhatsApp and Instagram.</p>
              </div>

              <div className="relative">
                <div className="absolute -left-[30px] top-1 w-4 h-4 rounded-full bg-zinc-800 border-2 border-purple-500 z-10" />
                <h3 className="font-medium text-white mb-1">Similar requests detected</h3>
                <p className="text-sm text-zinc-400">Vector search found 34 highly similar conversations over the last 72 hours.</p>
              </div>

              <div className="relative">
                <div className="absolute -left-[30px] top-1 w-4 h-4 rounded-full bg-zinc-800 border-2 border-pink-500 z-10" />
                <h3 className="font-medium text-white mb-1">Pattern confirmed by AI Debate</h3>
                <p className="text-sm text-zinc-400">CX Agent flagged high dissatisfaction. CFO Agent calculated the lost LTV (Lifetime Value) vs cost of a discount.</p>
              </div>

            </div>
          </div>

          {/* Action Recommendation */}
          <div className="p-8 rounded-3xl bg-gradient-to-br from-indigo-500/10 to-purple-600/10 border border-indigo-500/20 mb-8 relative overflow-hidden">
            <div className="absolute top-0 right-0 p-6 opacity-20">
              <Bot className="w-32 h-32 text-indigo-500" />
            </div>
            
            <div className="relative z-10">
              <h2 className="text-xl font-bold mb-2">Recommended Action</h2>
              <p className="text-zinc-300 mb-6 max-w-xl">
                Authorize the AI to automatically offer a 15% discount code when it detects high-intent customers hesitating on the Premium Tier price.
              </p>
              
              {!actionTaken ? (
                <div className="flex items-center gap-4">
                  <button 
                    onClick={() => setActionTaken(true)}
                    className="px-6 py-3 rounded-full bg-white text-black font-semibold hover:bg-zinc-200 transition-colors"
                  >
                    Approve Rule Update
                  </button>
                  <button className="px-6 py-3 rounded-full bg-white/5 border border-white/10 font-semibold hover:bg-white/10 transition-colors">
                    Modify Prompt
                  </button>
                </div>
              ) : (
                <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-emerald-500/20 text-emerald-400 font-medium border border-emerald-500/30">
                  <CheckCircle2 className="w-5 h-5" />
                  Rule Successfully Deployed to Production
                </div>
              )}
            </div>
          </div>

          {/* Evidence / Raw Data */}
          <div>
            <h2 className="text-lg font-semibold mb-4 flex items-center gap-2">
              <MessageSquare className="w-5 h-5 text-zinc-400" />
              Evidence (Raw Transcripts)
            </h2>
            
            <div className="grid grid-cols-2 gap-4">
              <div className="p-5 rounded-2xl bg-zinc-900/50 border border-white/5">
                <div className="flex items-center justify-between mb-3">
                  <span className="text-xs font-medium text-zinc-500">WhatsApp • +1 (555) 0192</span>
                  <span className="text-xs text-zinc-500">2h ago</span>
                </div>
                <p className="text-sm text-zinc-300 italic">"I really want the premium features, but $99/mo is just too steep for my team right now. Is there any flexibility?"</p>
              </div>
              
              <div className="p-5 rounded-2xl bg-zinc-900/50 border border-white/5">
                <div className="flex items-center justify-between mb-3">
                  <span className="text-xs font-medium text-zinc-500">Instagram DM • @sarah_designs</span>
                  <span className="text-xs text-zinc-500">5h ago</span>
                </div>
                <p className="text-sm text-zinc-300 italic">"Love the platform but the premium tier is out of my budget. Let me know if you guys ever run a sale!"</p>
              </div>
            </div>
          </div>

        </div>
      </main>
    </div>
  );
}

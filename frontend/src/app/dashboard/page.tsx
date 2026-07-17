"use client";

import Link from "next/link";
import { 
  Briefcase, 
  BrainCircuit, 
  LineChart, 
  TrendingUp, 
  MessageSquare,
  Sparkles,
  Bot,
  Activity
} from "lucide-react";

export default function Dashboard() {
  return (
    <div className="min-h-screen bg-[#050505] text-white flex overflow-hidden">
      
      {/* Sidebar */}
      <aside className="hidden lg:flex w-64 border-r border-white/10 bg-[#0a0a0a] flex-col p-4 relative z-20">
        <div className="flex items-center gap-2 mb-12 px-2 pt-2">
          <span className="font-semibold tracking-tight text-lg">Morlen OS</span>
        </div>

        <nav className="space-y-1">
          <Link href="/dashboard" className="flex items-center gap-3 px-3 py-2.5 rounded-lg bg-white/5 text-brand-lightbrown font-medium text-sm border border-brand-lightbrown/10">
            <Briefcase className="w-4 h-4 text-brand-lightbrown" />
            Executive Brief
          </Link>
          <Link href="/dashboard/memory" className="flex items-center gap-3 px-3 py-2.5 rounded-lg text-zinc-400 hover:bg-white/5 hover:text-white font-medium text-sm transition-colors group">
            <BrainCircuit className="w-4 h-4 group-hover:text-brand-lightbrown transition-colors" />
            Business Memory
          </Link>
          <Link href="/dashboard/opportunities" className="flex items-center gap-3 px-3 py-2.5 rounded-lg text-zinc-400 hover:bg-white/5 hover:text-white font-medium text-sm transition-colors group">
            <TrendingUp className="w-4 h-4 group-hover:text-brand-lightbrown transition-colors" />
            Opportunities
          </Link>
          <Link href="/pricing" className="flex items-center gap-3 px-3 py-2.5 rounded-lg text-zinc-400 hover:bg-white/5 hover:text-white font-medium text-sm transition-colors group mt-8">
            <Sparkles className="w-4 h-4 group-hover:text-brand-lightbrown transition-colors" />
            Upgrade Plan
          </Link>
        </nav>
        
        <div className="mt-auto p-4 rounded-xl bg-gradient-to-br from-brand-lightbrown/10 to-brand-brown/10 border border-brand-lightbrown/20">
          <div className="flex items-center gap-2 mb-2">
            <div className="w-2 h-2 rounded-full bg-brand-lightbrown animate-pulse" />
            <span className="text-xs font-semibold text-brand-lightbrown">Agents Online</span>
          </div>
          <p className="text-xs text-zinc-400 leading-relaxed">
            Morlen is actively monitoring your connected channels.
          </p>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 overflow-y-auto relative w-full">
        {/* Abstract Background */}
        <div className="absolute top-0 right-0 w-[800px] h-[500px] bg-brand-lightbrown/5 rounded-full blur-[150px] pointer-events-none" />

        <div className="max-w-6xl mx-auto p-4 md:p-8 relative z-10">
          
          <header className="mb-10">
            <h1 className="text-2xl md:text-3xl font-bold tracking-tight mb-2">Good morning, Alex.</h1>
            <p className="text-zinc-400">Here is your daily executive briefing.</p>
          </header>

          {/* KPI Cards */}
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
            <div className="p-5 rounded-2xl bg-zinc-900/50 border border-white/5 backdrop-blur-md">
              <div className="text-zinc-400 text-sm mb-2 flex items-center justify-between">
                Conversations
                <MessageSquare className="w-4 h-4 opacity-50" />
              </div>
              <div className="text-2xl font-semibold mb-1">0</div>
              <div className="text-xs text-zinc-500 font-medium">Awaiting data...</div>
            </div>
            
            <div className="p-5 rounded-2xl bg-zinc-900/50 border border-white/5 backdrop-blur-md">
              <div className="text-zinc-400 text-sm mb-2 flex items-center justify-between">
                Auto-Resolved
                <Bot className="w-4 h-4 opacity-50" />
              </div>
              <div className="text-2xl font-semibold mb-1">0%</div>
              <div className="text-xs text-zinc-500 font-medium">Awaiting data...</div>
            </div>

            <div className="p-5 rounded-2xl bg-zinc-900/50 border border-white/5 backdrop-blur-md">
              <div className="text-zinc-400 text-sm mb-2 flex items-center justify-between">
                Lost Sales (Prevented)
                <TrendingUp className="w-4 h-4 opacity-50" />
              </div>
              <div className="text-2xl font-semibold mb-1">$0</div>
              <div className="text-xs text-zinc-500 font-medium">Awaiting data...</div>
            </div>

            <div className="p-5 rounded-2xl bg-zinc-900/50 border border-white/5 backdrop-blur-md">
              <div className="text-zinc-400 text-sm mb-2 flex items-center justify-between">
                Sentiment Score
                <LineChart className="w-4 h-4 opacity-50" />
              </div>
              <div className="text-2xl font-semibold mb-1">0.0 / 10</div>
              <div className="text-xs text-zinc-500 font-medium">Awaiting data...</div>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            
            {/* Left Column: Opportunity Feed & Actions */}
            <div className="col-span-1 md:col-span-2 space-y-8">
              <section>
                <div className="flex items-center justify-between mb-4">
                  <h2 className="text-lg font-semibold flex items-center gap-2">
                    <Sparkles className="w-5 h-5 text-brand-lightbrown" />
                    High-Value Opportunities
                  </h2>
                </div>
                
                <div className="p-12 rounded-3xl bg-zinc-900/30 border border-white/5 flex flex-col items-center text-center justify-center">
                  <Activity className="w-12 h-12 text-zinc-700 mb-4" />
                  <h3 className="font-medium text-lg mb-2">No Opportunities Detected</h3>
                  <p className="text-sm text-zinc-500 max-w-sm">
                    Morlen is analyzing your incoming conversations. High-value revenue opportunities and churn risks will appear here automatically.
                  </p>
                </div>
              </section>
            </div>

            {/* Right Column: Business Memory Highlights */}
            <div className="col-span-1">
              <div className="p-6 rounded-3xl bg-zinc-900/50 border border-white/5 h-full flex flex-col">
                <div className="flex items-center justify-between mb-6">
                  <h2 className="text-lg font-semibold flex items-center gap-2">
                    <BrainCircuit className="w-5 h-5 text-brand-lightbrown" />
                    Memory Digest
                  </h2>
                </div>

                <div className="flex-1 flex flex-col items-center justify-center text-center py-10">
                  <BrainCircuit className="w-10 h-10 text-zinc-700 mb-4" />
                  <p className="text-sm text-zinc-500">
                    Your business memory is currently empty. Connect your channels to begin extracting insights.
                  </p>
                </div>
              </div>
            </div>

          </div>
        </div>
      </main>
    </div>
  );
}

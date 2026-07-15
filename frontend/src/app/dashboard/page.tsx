"use client";

import Link from "next/link";
import { 
  Briefcase, 
  BrainCircuit, 
  LineChart, 
  TrendingUp, 
  AlertCircle, 
  MessageSquare,
  ArrowRight,
  Sparkles,
  Bot
} from "lucide-react";

export default function Dashboard() {
  return (
    <div className="min-h-screen bg-[#050505] text-white flex overflow-hidden">
      
      {/* Sidebar */}
      <aside className="w-64 border-r border-white/10 bg-[#0a0a0a] flex flex-col p-4 relative z-20">
        <div className="flex items-center gap-2 mb-12 px-2 pt-2">
          <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center font-bold text-sm">M</div>
          <span className="font-semibold tracking-tight text-lg">Morlen OS</span>
        </div>

        <nav className="space-y-1">
          <Link href="/dashboard" className="flex items-center gap-3 px-3 py-2.5 rounded-lg bg-white/5 text-white font-medium text-sm border border-white/5">
            <Briefcase className="w-4 h-4 text-indigo-400" />
            Executive Brief
          </Link>
          <Link href="/dashboard/memory" className="flex items-center gap-3 px-3 py-2.5 rounded-lg text-zinc-400 hover:bg-white/5 hover:text-white font-medium text-sm transition-colors group">
            <BrainCircuit className="w-4 h-4 group-hover:text-purple-400 transition-colors" />
            Business Memory
          </Link>
          <Link href="/dashboard/opportunities" className="flex items-center gap-3 px-3 py-2.5 rounded-lg text-zinc-400 hover:bg-white/5 hover:text-white font-medium text-sm transition-colors group">
            <TrendingUp className="w-4 h-4 group-hover:text-emerald-400 transition-colors" />
            Opportunities
          </Link>
          <Link href="/pricing" className="flex items-center gap-3 px-3 py-2.5 rounded-lg text-zinc-400 hover:bg-white/5 hover:text-white font-medium text-sm transition-colors group mt-8">
            <Sparkles className="w-4 h-4 group-hover:text-amber-400 transition-colors" />
            Upgrade Plan
          </Link>
        </nav>
        
        <div className="mt-auto p-4 rounded-xl bg-gradient-to-br from-indigo-500/10 to-purple-500/10 border border-indigo-500/20">
          <div className="flex items-center gap-2 mb-2">
            <div className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
            <span className="text-xs font-semibold text-indigo-300">Agents Online</span>
          </div>
          <p className="text-xs text-zinc-400 leading-relaxed">
            Morlen is actively monitoring 3 channels and negotiating with 12 customers.
          </p>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 overflow-y-auto relative">
        {/* Abstract Background */}
        <div className="absolute top-0 right-0 w-[800px] h-[500px] bg-indigo-600/5 rounded-full blur-[150px] pointer-events-none" />

        <div className="max-w-6xl mx-auto p-8 relative z-10">
          
          <header className="mb-10">
            <h1 className="text-3xl font-bold tracking-tight mb-2">Good morning, Alex.</h1>
            <p className="text-zinc-400">Here is your daily executive briefing.</p>
          </header>

          {/* KPI Cards */}
          <div className="grid grid-cols-4 gap-4 mb-8">
            <div className="p-5 rounded-2xl bg-zinc-900/50 border border-white/5 backdrop-blur-md">
              <div className="text-zinc-400 text-sm mb-2 flex items-center justify-between">
                Conversations
                <MessageSquare className="w-4 h-4" />
              </div>
              <div className="text-2xl font-semibold mb-1">1,284</div>
              <div className="text-xs text-emerald-400 font-medium">+12% vs last week</div>
            </div>
            
            <div className="p-5 rounded-2xl bg-zinc-900/50 border border-white/5 backdrop-blur-md">
              <div className="text-zinc-400 text-sm mb-2 flex items-center justify-between">
                Auto-Resolved
                <Bot className="w-4 h-4" />
              </div>
              <div className="text-2xl font-semibold mb-1">94%</div>
              <div className="text-xs text-emerald-400 font-medium">Saved 42 human hours</div>
            </div>

            <div className="p-5 rounded-2xl bg-zinc-900/50 border border-white/5 backdrop-blur-md">
              <div className="text-zinc-400 text-sm mb-2 flex items-center justify-between">
                Lost Sales (Prevented)
                <TrendingUp className="w-4 h-4" />
              </div>
              <div className="text-2xl font-semibold mb-1">$4,250</div>
              <div className="text-xs text-emerald-400 font-medium">18 carts recovered</div>
            </div>

            <div className="p-5 rounded-2xl bg-zinc-900/50 border border-white/5 backdrop-blur-md">
              <div className="text-zinc-400 text-sm mb-2 flex items-center justify-between">
                Sentiment Score
                <LineChart className="w-4 h-4" />
              </div>
              <div className="text-2xl font-semibold mb-1">9.2 / 10</div>
              <div className="text-xs text-emerald-400 font-medium">+0.4 vs last week</div>
            </div>
          </div>

          <div className="grid grid-cols-3 gap-8">
            
            {/* Left Column: Opportunity Feed & Actions */}
            <div className="col-span-2 space-y-8">
              
              <section>
                <div className="flex items-center justify-between mb-4">
                  <h2 className="text-lg font-semibold flex items-center gap-2">
                    <Sparkles className="w-5 h-5 text-amber-400" />
                    High-Value Opportunities
                  </h2>
                  <Link href="/dashboard/opportunities" className="text-sm text-zinc-400 hover:text-white transition-colors">View all</Link>
                </div>
                
                <div className="space-y-4">
                  {/* Opportunity Item 1 */}
                  <Link href="/dashboard/opportunities/1" className="block p-5 rounded-2xl bg-gradient-to-r from-amber-500/10 to-transparent border border-amber-500/20 hover:border-amber-500/40 transition-colors group">
                    <div className="flex justify-between items-start mb-2">
                      <div className="flex items-center gap-2">
                        <span className="px-2 py-0.5 rounded text-xs font-medium bg-amber-500/20 text-amber-300">Revenue Pattern</span>
                        <span className="text-sm text-zinc-400">Detected 2 hours ago</span>
                      </div>
                      <div className="text-emerald-400 font-semibold text-sm">+$12,500/mo Est.</div>
                    </div>
                    <h3 className="font-medium text-lg mb-1">Pricing Objection on "Premium Tier"</h3>
                    <p className="text-sm text-zinc-400 mb-4 line-clamp-1">34 customers dropped off at checkout after asking for a discount on the premium tier.</p>
                    <div className="flex items-center gap-2 text-amber-400 text-sm font-medium">
                      Review Recommendation <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
                    </div>
                  </Link>

                  {/* Opportunity Item 2 */}
                  <Link href="/dashboard/opportunities/2" className="block p-5 rounded-2xl bg-zinc-900/50 border border-white/5 hover:border-white/20 transition-colors group">
                    <div className="flex justify-between items-start mb-2">
                      <div className="flex items-center gap-2">
                        <span className="px-2 py-0.5 rounded text-xs font-medium bg-indigo-500/20 text-indigo-300">Product Request</span>
                        <span className="text-sm text-zinc-400">Detected yesterday</span>
                      </div>
                      <div className="text-emerald-400 font-semibold text-sm">High Demand</div>
                    </div>
                    <h3 className="font-medium text-lg mb-1">Surge in requests for "Same-Day Delivery"</h3>
                    <p className="text-sm text-zinc-400 mb-4 line-clamp-1">Customer mentions of "fast shipping" or "same day" increased by 45% this week.</p>
                    <div className="flex items-center gap-2 text-indigo-400 text-sm font-medium">
                      Review Recommendation <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
                    </div>
                  </Link>
                </div>
              </section>

            </div>

            {/* Right Column: Business Memory Highlights */}
            <div className="col-span-1">
              <div className="p-6 rounded-3xl bg-zinc-900/50 border border-white/5 h-full">
                <div className="flex items-center justify-between mb-6">
                  <h2 className="text-lg font-semibold flex items-center gap-2">
                    <BrainCircuit className="w-5 h-5 text-purple-400" />
                    Memory Digest
                  </h2>
                  <Link href="/dashboard/memory" className="text-xs text-zinc-400 hover:text-white">Expand</Link>
                </div>

                <div className="space-y-6 relative before:absolute before:inset-0 before:ml-2.5 before:-translate-x-px md:before:mx-auto md:before:translate-x-0 before:h-full before:w-0.5 before:bg-gradient-to-b before:from-purple-500/50 before:to-transparent">
                  
                  <div className="relative flex items-start gap-4">
                    <div className="w-5 h-5 rounded-full bg-[#0a0a0a] border-2 border-purple-500 flex-shrink-0 z-10" />
                    <div>
                      <h4 className="text-sm font-medium mb-1">Brand Voice Aligned</h4>
                      <p className="text-xs text-zinc-400 leading-relaxed">CX Agent successfully adapted to using more emojis in responses after analyzing top 100 positive interactions.</p>
                    </div>
                  </div>

                  <div className="relative flex items-start gap-4">
                    <div className="w-5 h-5 rounded-full bg-[#0a0a0a] border-2 border-indigo-500 flex-shrink-0 z-10" />
                    <div>
                      <h4 className="text-sm font-medium mb-1">Refund Policy Updated</h4>
                      <p className="text-xs text-zinc-400 leading-relaxed">System now automatically offers store credit instead of full refunds based on CFO Agent's new mandate.</p>
                    </div>
                  </div>

                  <div className="relative flex items-start gap-4">
                    <div className="w-5 h-5 rounded-full bg-[#0a0a0a] border-2 border-emerald-500 flex-shrink-0 z-10" />
                    <div>
                      <h4 className="text-sm font-medium mb-1">Competitor Mention</h4>
                      <p className="text-xs text-zinc-400 leading-relaxed">5 customers mentioned "Acme Co" pricing this week. Monitored for churn risk.</p>
                    </div>
                  </div>

                </div>

                <Link href="/dashboard/memory" className="mt-8 block w-full py-2.5 rounded-lg bg-white/5 text-center text-sm font-medium hover:bg-white/10 transition-colors">
                  View Full Memory
                </Link>
              </div>
            </div>

          </div>
        </div>
      </main>
    </div>
  );
}

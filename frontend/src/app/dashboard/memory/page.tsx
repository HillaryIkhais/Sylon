"use client";

import Link from "next/link";
import { 
  Briefcase, 
  BrainCircuit, 
  TrendingUp, 
  Sparkles,
  Search,
  Filter,
  ArrowUpRight,
  Package,
  Users,
  MessageSquare
} from "lucide-react";

export default function BusinessMemory() {
  return (
    <div className="min-h-screen bg-[#050505] text-white flex overflow-hidden">
      
      {/* Sidebar */}
      <aside className="w-64 border-r border-white/10 bg-[#0a0a0a] flex flex-col p-4 relative z-20">
        <div className="flex items-center gap-2 mb-12 px-2 pt-2">
          <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center font-bold text-sm">M</div>
          <span className="font-semibold tracking-tight text-lg">Morlen OS</span>
        </div>

        <nav className="space-y-1">
          <Link href="/dashboard" className="flex items-center gap-3 px-3 py-2.5 rounded-lg text-zinc-400 hover:bg-white/5 hover:text-white font-medium text-sm transition-colors group">
            <Briefcase className="w-4 h-4 group-hover:text-indigo-400 transition-colors" />
            Executive Brief
          </Link>
          <Link href="/dashboard/memory" className="flex items-center gap-3 px-3 py-2.5 rounded-lg bg-white/5 text-white font-medium text-sm border border-white/5">
            <BrainCircuit className="w-4 h-4 text-purple-400" />
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
      </aside>

      {/* Main Content */}
      <main className="flex-1 overflow-y-auto relative">
        {/* Abstract Background */}
        <div className="absolute top-[-10%] left-[20%] w-[600px] h-[600px] bg-purple-600/5 rounded-full blur-[150px] pointer-events-none" />

        <div className="max-w-6xl mx-auto p-8 relative z-10">
          
          <header className="mb-10 flex items-end justify-between">
            <div>
              <h1 className="text-3xl font-bold tracking-tight mb-2">Business Memory</h1>
              <p className="text-zinc-400">The collective intelligence of your business, extracted from raw conversations.</p>
            </div>
            
            <div className="flex items-center gap-3">
              <div className="relative">
                <Search className="w-4 h-4 text-zinc-400 absolute left-3 top-1/2 -translate-y-1/2" />
                <input 
                  type="text" 
                  placeholder="Search memory..." 
                  className="pl-9 pr-4 py-2 rounded-full bg-zinc-900 border border-white/10 text-sm text-white focus:outline-none focus:border-purple-500 w-64"
                />
              </div>
              <button className="p-2 rounded-full border border-white/10 bg-zinc-900 hover:bg-zinc-800 transition-colors text-zinc-400">
                <Filter className="w-4 h-4" />
              </button>
            </div>
          </header>

          {/* Masonry / Grid Layout for Insights */}
          <div className="grid grid-cols-3 gap-6">
            
            {/* Memory 1 */}
            <div className="p-6 rounded-3xl bg-zinc-900/50 border border-white/5 hover:border-purple-500/30 transition-colors group flex flex-col justify-between">
              <div>
                <div className="flex items-center justify-between mb-4">
                  <div className="w-10 h-10 rounded-full bg-indigo-500/20 flex items-center justify-center text-indigo-400">
                    <Package className="w-5 h-5" />
                  </div>
                  <span className="text-xs font-medium px-2 py-1 rounded bg-white/5 text-zinc-400">Product Trend</span>
                </div>
                <h3 className="text-lg font-semibold mb-2">Customers increasingly request same-day delivery.</h3>
                <p className="text-sm text-zinc-400 leading-relaxed mb-4">
                  32% of incoming sales inquiries over the last week asked about delivery timelines, with a strong preference for same-day options.
                </p>
              </div>
              <div className="text-sm font-medium text-indigo-400 flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity cursor-pointer">
                View related conversations <ArrowUpRight className="w-4 h-4" />
              </div>
            </div>

            {/* Memory 2 */}
            <div className="p-6 rounded-3xl bg-zinc-900/50 border border-white/5 hover:border-emerald-500/30 transition-colors group flex flex-col justify-between">
              <div>
                <div className="flex items-center justify-between mb-4">
                  <div className="w-10 h-10 rounded-full bg-emerald-500/20 flex items-center justify-center text-emerald-400">
                    <Users className="w-5 h-5" />
                  </div>
                  <span className="text-xs font-medium px-2 py-1 rounded bg-white/5 text-zinc-400">Customer Behavior</span>
                </div>
                <h3 className="text-lg font-semibold mb-2">Repeat buyers return every 24 days.</h3>
                <p className="text-sm text-zinc-400 leading-relaxed mb-4">
                  Morlen has identified a natural buying cycle. Re-engagement broadcasts sent around day 21 have a 4x higher conversion rate.
                </p>
              </div>
              <div className="text-sm font-medium text-emerald-400 flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity cursor-pointer">
                View related conversations <ArrowUpRight className="w-4 h-4" />
              </div>
            </div>

            {/* Memory 3 */}
            <div className="p-6 rounded-3xl bg-zinc-900/50 border border-white/5 hover:border-amber-500/30 transition-colors group flex flex-col justify-between">
              <div>
                <div className="flex items-center justify-between mb-4">
                  <div className="w-10 h-10 rounded-full bg-amber-500/20 flex items-center justify-center text-amber-400">
                    <TrendingUp className="w-5 h-5" />
                  </div>
                  <span className="text-xs font-medium px-2 py-1 rounded bg-white/5 text-zinc-400">Pricing Insight</span>
                </div>
                <h3 className="text-lg font-semibold mb-2">Price objections increased 18%.</h3>
                <p className="text-sm text-zinc-400 leading-relaxed mb-4">
                  Since the new pricing update on Tuesday, pushback regarding the mid-tier plan has notably increased.
                </p>
              </div>
              <div className="text-sm font-medium text-amber-400 flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity cursor-pointer">
                View related conversations <ArrowUpRight className="w-4 h-4" />
              </div>
            </div>

            {/* Memory 4 */}
            <div className="p-6 rounded-3xl bg-zinc-900/50 border border-white/5 hover:border-pink-500/30 transition-colors group flex flex-col justify-between">
              <div>
                <div className="flex items-center justify-between mb-4">
                  <div className="w-10 h-10 rounded-full bg-pink-500/20 flex items-center justify-center text-pink-400">
                    <MessageSquare className="w-5 h-5" />
                  </div>
                  <span className="text-xs font-medium px-2 py-1 rounded bg-white/5 text-zinc-400">Inventory Demand</span>
                </div>
                <h3 className="text-lg font-semibold mb-2">Demand for Arabian Oud is rising.</h3>
                <p className="text-sm text-zinc-400 leading-relaxed mb-4">
                  Mention of "Arabian Oud" and "Oud variants" have spiked across WhatsApp and Instagram DMs over the weekend.
                </p>
              </div>
              <div className="text-sm font-medium text-pink-400 flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity cursor-pointer">
                View related conversations <ArrowUpRight className="w-4 h-4" />
              </div>
            </div>

          </div>

        </div>
      </main>
    </div>
  );
}

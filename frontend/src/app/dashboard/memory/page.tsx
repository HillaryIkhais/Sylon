"use client";

import Link from "next/link";
import { 
  Briefcase, 
  BrainCircuit, 
  TrendingUp, 
  Zap,
  Search,
  Filter
} from "lucide-react";

export default function BusinessMemory() {
  return (
    <div className="min-h-screen bg-zinc-50 dark:bg-[#050505] text-zinc-900 dark:text-white flex overflow-hidden">
      
      {/* Sidebar */}
      <aside className="hidden lg:flex w-64 border-r border-zinc-200 dark:border-white/10 bg-white dark:bg-[#0a0a0a] flex-col p-4 relative z-20">
        <div className="flex items-center gap-2 mb-12 px-2 pt-2">
          <span className="font-semibold tracking-tight text-lg pl-2">Morlen OS</span>
        </div>

        <nav className="space-y-1">
          <Link href="/dashboard" className="flex items-center gap-3 px-3 py-2.5 rounded-lg text-zinc-500 dark:text-zinc-400 dark:text-zinc-400 hover:bg-zinc-100 dark:bg-white/5 hover:text-zinc-900 dark:hover:text-white font-medium text-sm transition-colors group">
            <Briefcase className="w-4 h-4 group-hover:text-brand-lightbrown transition-colors" />
            Executive Brief
          </Link>
          <Link href="/dashboard/memory" className="flex items-center gap-3 px-3 py-2.5 rounded-lg bg-zinc-100 dark:bg-white/5 text-brand-lightbrown font-medium text-sm border border-brand-lightbrown/10">
            <BrainCircuit className="w-4 h-4 text-brand-lightbrown" />
            Business Memory
          </Link>
          <Link href="/dashboard/opportunities" className="flex items-center gap-3 px-3 py-2.5 rounded-lg text-zinc-500 dark:text-zinc-400 dark:text-zinc-400 hover:bg-zinc-100 dark:bg-white/5 hover:text-zinc-900 dark:hover:text-white font-medium text-sm transition-colors group">
            <TrendingUp className="w-4 h-4 group-hover:text-brand-lightbrown transition-colors" />
            Opportunities
          </Link>
          <Link href="/pricing" className="flex items-center gap-3 px-3 py-2.5 rounded-lg text-zinc-500 dark:text-zinc-400 dark:text-zinc-400 hover:bg-zinc-100 dark:bg-white/5 hover:text-zinc-900 dark:hover:text-white font-medium text-sm transition-colors group mt-8">
            <Zap className="w-4 h-4 group-hover:text-brand-lightbrown transition-colors" />
            Upgrade Plan
          </Link>
        </nav>
      </aside>

      {/* Main Content */}
      <main className="flex-1 overflow-y-auto relative w-full">
        {/* Abstract Background */}
        <div className="absolute top-[-10%] left-[20%] w-[600px] h-[600px] bg-brand-brown/5 rounded-full blur-[150px] pointer-events-none" />

        <div className="max-w-6xl mx-auto p-4 md:p-8 relative z-10">
          
          <header className="mb-10 flex flex-col md:flex-row md:items-end justify-between gap-4">
            <div>
              <h1 className="text-2xl md:text-3xl font-bold tracking-tight mb-2">Business Memory</h1>
              <p className="text-zinc-500 dark:text-zinc-400 dark:text-zinc-400">The collective intelligence of your business, extracted from raw conversations.</p>
            </div>
            
            <div className="flex items-center gap-3">
              <div className="relative">
                <Search className="w-4 h-4 text-zinc-500 dark:text-zinc-400 dark:text-zinc-400 absolute left-3 top-1/2 -translate-y-1/2" />
                <input 
                  type="text" 
                  placeholder="Search memory..." 
                  className="pl-9 pr-4 py-2 rounded-full bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-white/10 text-sm text-white focus:outline-none focus:border-brand-lightbrown w-full md:w-64"
                />
              </div>
              <button className="p-2 rounded-full border border-zinc-200 dark:border-white/10 bg-white dark:bg-zinc-900 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors text-zinc-500 dark:text-zinc-400 dark:text-zinc-400">
                <Filter className="w-4 h-4" />
              </button>
            </div>
          </header>

          {/* Empty State Layout */}
          <div className="p-16 rounded-3xl bg-zinc-100 dark:bg-white dark:bg-zinc-900/30 border border-zinc-200 dark:border-white/5 flex flex-col items-center justify-center text-center mt-12">
            <div className="w-20 h-20 bg-zinc-200 dark:bg-zinc-800/50 rounded-full flex items-center justify-center mb-6">
              <BrainCircuit className="w-10 h-10 text-zinc-500 dark:text-zinc-600" />
            </div>
            <h3 className="text-xl font-semibold mb-3">No insights generated yet</h3>
            <p className="text-zinc-500 dark:text-zinc-400 dark:text-zinc-400 max-w-md mx-auto mb-8 leading-relaxed">
              Morlen is continuously analyzing your conversations. Once enough data is collected, high-level business insights and behavior patterns will appear here.
            </p>
          </div>

        </div>
      </main>
    </div>
  );
}

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
    <div className="min-h-screen text-brand-dark dark:text-white flex overflow-hidden">
      
      {/* Sidebar */}
      <aside className="hidden lg:flex w-64 border-r border-brand-dark/10 dark:border-white/10 bg-white/50 dark:bg-brand-dark/50 backdrop-blur-xl flex-col p-4 relative z-20">
        <div className="flex items-center gap-2 mb-12 px-2 pt-2">
          <span className="font-semibold tracking-tight text-lg pl-2 text-brand-brown dark:text-brand-lightbrown">Morlen OS</span>
        </div>

        <nav className="space-y-1">
          <Link href="/dashboard" className="flex items-center gap-3 px-3 py-2.5 rounded-lg text-brand-dark/60 dark:text-white/60 hover:bg-brand-lightbrown/5 hover:text-brand-dark dark:hover:text-white font-medium text-sm transition-colors group">
            <Briefcase className="w-4 h-4 group-hover:text-brand-lightbrown transition-colors" />
            Executive Brief
          </Link>
          <Link href="/dashboard/memory" className="flex items-center gap-3 px-3 py-2.5 rounded-lg bg-brand-lightbrown/10 text-brand-brown dark:text-brand-lightbrown font-medium text-sm border border-brand-lightbrown/20">
            <BrainCircuit className="w-4 h-4 text-brand-brown dark:text-brand-lightbrown" />
            Business Memory
          </Link>
          <Link href="/dashboard/opportunities" className="flex items-center gap-3 px-3 py-2.5 rounded-lg text-brand-dark/60 dark:text-white/60 hover:bg-brand-lightbrown/5 hover:text-brand-dark dark:hover:text-white font-medium text-sm transition-colors group">
            <TrendingUp className="w-4 h-4 group-hover:text-brand-lightbrown transition-colors" />
            Opportunities
          </Link>
          <Link href="/pricing" className="flex items-center gap-3 px-3 py-2.5 rounded-lg text-brand-dark/60 dark:text-white/60 hover:bg-brand-lightbrown/5 hover:text-brand-dark dark:hover:text-white font-medium text-sm transition-colors group mt-8">
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
              <h1 className="text-2xl md:text-3xl font-bold tracking-tight mb-2 text-brand-dark dark:text-white">Business Memory</h1>
              <p className="text-brand-dark/60 dark:text-white/60">The collective intelligence of your business, extracted from raw conversations.</p>
            </div>
            
            <div className="flex items-center gap-3">
              <div className="relative">
                <Search className="w-4 h-4 text-brand-dark/40 dark:text-white/40 absolute left-3 top-1/2 -translate-y-1/2" />
                <input 
                  type="text" 
                  placeholder="Search memory..." 
                  className="pl-9 pr-4 py-2 rounded-full bg-white/60 dark:bg-white/5 border border-brand-dark/10 dark:border-white/10 text-sm text-brand-dark dark:text-white focus:outline-none focus:border-brand-lightbrown w-full md:w-64 backdrop-blur-md"
                />
              </div>
              <button className="p-2 rounded-full border border-brand-dark/10 dark:border-white/10 bg-white/60 dark:bg-white/5 hover:bg-brand-lightbrown/10 transition-colors text-brand-dark/60 dark:text-white/60 backdrop-blur-md">
                <Filter className="w-4 h-4" />
              </button>
            </div>
          </header>

          {/* Empty State Layout */}
          <div className="glass-card p-16 rounded-3xl flex flex-col items-center justify-center text-center mt-12">
            <div className="w-20 h-20 bg-brand-lightbrown/10 rounded-full flex items-center justify-center mb-6">
              <BrainCircuit className="w-10 h-10 text-brand-brown/50 dark:text-brand-lightbrown/50" />
            </div>
            <h3 className="text-xl font-semibold mb-3 text-brand-dark dark:text-white">No insights generated yet</h3>
            <p className="text-brand-dark/60 dark:text-white/60 max-w-md mx-auto mb-8 leading-relaxed">
              Morlen is continuously analyzing your conversations. Once enough data is collected, high-level business insights and behavior patterns will appear here.
            </p>
          </div>

        </div>
      </main>
    </div>
  );
}

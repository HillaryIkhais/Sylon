"use client";

import Link from "next/link";
import { 
  Briefcase, 
  BrainCircuit, 
  TrendingUp, 
  Zap,
  Activity,
  Filter,
  Search
} from "lucide-react";
import DashboardMobileNav from "@/components/DashboardMobileNav";

export default function Opportunities() {
  return (
    <div className="min-h-screen text-brand-dark dark:text-white flex overflow-hidden">
      
      {/* Sidebar */}
      <aside className="hidden lg:flex w-64 border-r border-brand-dark/10 dark:border-white/10 bg-white/50 dark:bg-black/20 backdrop-blur-xl flex-col p-4 relative z-20">
        <div className="flex items-center gap-2 mb-12 px-2 pt-2">
          <span className="font-semibold tracking-tight text-lg pl-2 text-brand-brown dark:text-brand-lightbrown">Morlen OS</span>
        </div>

        <nav className="space-y-1">
          <Link href="/dashboard" className="flex items-center gap-3 px-3 py-2.5 rounded-lg text-brand-dark/60 dark:text-brand-dark/70 hover:bg-brand-lightbrown/5 hover:text-brand-dark dark:hover:text-white font-medium text-sm transition-colors group">
            <Briefcase className="w-4 h-4 group-hover:text-brand-lightbrown transition-colors" />
            Executive Brief
          </Link>
          <Link href="/dashboard/memory" className="flex items-center gap-3 px-3 py-2.5 rounded-lg text-brand-dark/60 dark:text-brand-dark/70 hover:bg-brand-lightbrown/5 hover:text-brand-dark dark:hover:text-white font-medium text-sm transition-colors group">
            <BrainCircuit className="w-4 h-4 group-hover:text-brand-lightbrown transition-colors" />
            Business Memory
          </Link>
          <Link href="/dashboard/opportunities" className="flex items-center gap-3 px-3 py-2.5 rounded-lg bg-brand-lightbrown/10 text-brand-brown dark:text-brand-lightbrown font-medium text-sm border border-brand-lightbrown/20">
            <TrendingUp className="w-4 h-4 text-brand-brown dark:text-brand-lightbrown" />
            Opportunities
          </Link>
          <Link href="/pricing" className="flex items-center gap-3 px-3 py-2.5 rounded-lg text-brand-dark/60 dark:text-brand-dark/70 hover:bg-brand-lightbrown/5 hover:text-brand-dark dark:hover:text-white font-medium text-sm transition-colors group mt-8">
            <Zap className="w-4 h-4 group-hover:text-brand-lightbrown transition-colors" />
            Upgrade Plan
          </Link>
        </nav>
      </aside>

      {/* Main Content */}
      <main className="flex-1 overflow-y-auto relative w-full pb-24 lg:pb-0">
        {/* Abstract Background */}
        <div className="absolute top-[-10%] left-[20%] w-[600px] h-[600px] bg-brand-lightbrown/5 rounded-full blur-[150px] pointer-events-none" />

        <div className="max-w-6xl mx-auto p-4 md:p-8 relative z-10">
          <DashboardMobileNav activePath="/dashboard/opportunities" />
          
          <header className="mb-10 flex flex-col md:flex-row md:items-end justify-between gap-4">
            <div>
              <h1 className="text-2xl md:text-3xl font-bold tracking-tight mb-2 text-brand-dark dark:text-white">High-Value Opportunities</h1>
              <p className="text-brand-dark/60 dark:text-brand-dark/70">Revenue patterns and churn risks identified by Morlen.</p>
            </div>
            
            <div className="flex items-center gap-3">
              <div className="relative">
                <Search className="w-4 h-4 text-brand-dark/40 dark:text-white/40 absolute left-3 top-1/2 -translate-y-1/2" />
                <input 
                  type="text" 
                  placeholder="Search opportunities..." 
                  className="pl-9 pr-4 py-2 rounded-full bg-white/60 dark:bg-white/5 border border-brand-dark/10 dark:border-white/10 text-sm text-brand-dark dark:text-white focus:outline-none focus:border-brand-lightbrown w-full md:w-64 backdrop-blur-md"
                />
              </div>
              <button className="p-2 rounded-full border border-brand-dark/10 dark:border-white/10 bg-white/60 dark:bg-white/5 hover:bg-brand-lightbrown/10 transition-colors text-brand-dark/60 dark:text-brand-dark/70 backdrop-blur-md">
                <Filter className="w-4 h-4" />
              </button>
            </div>
          </header>

          {/* Empty State Layout */}
          <div className="glass-card p-16 rounded-3xl flex flex-col items-center justify-center text-center mt-12">
            <div className="w-20 h-20 bg-brand-lightbrown/10 rounded-full flex items-center justify-center mb-6">
              <Activity className="w-10 h-10 text-brand-brown dark:text-brand-lightbrown" />
            </div>
            <h3 className="text-xl font-semibold mb-3 text-brand-dark dark:text-white">No Opportunities Detected</h3>
            <p className="text-brand-dark/60 dark:text-brand-dark/70 max-w-md mx-auto mb-8 leading-relaxed">
              Morlen is continuously analyzing your conversations. High-value revenue opportunities and churn risks will appear here once detected.
            </p>
          </div>

        </div>
      </main>
    </div>
  );
}

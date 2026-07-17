"use client";

import Link from "next/link";
import { 
  ArrowLeft,
  Zap,
  Activity
} from "lucide-react";
import { useState } from "react";

export default function OpportunityDetail() {
  const [actionTaken, setActionTaken] = useState(false);

  return (
    <div className="min-h-screen bg-zinc-50 dark:bg-[#050505] text-zinc-900 dark:text-white flex overflow-hidden">
      
      {/* Sidebar (Collapsed for focus) */}
      <aside className="hidden md:flex w-20 border-r border-zinc-200 dark:border-white/10 bg-white dark:bg-[#0a0a0a] flex-col items-center py-6 relative z-20">
        {/* Placeholder for future icon, removed M logo */}
      </aside>

      {/* Main Content */}
      <main className="flex-1 overflow-y-auto relative w-full">
        <div className="max-w-4xl mx-auto p-4 md:p-10 relative z-10">
          
          <Link href="/dashboard" className="inline-flex items-center gap-2 text-sm text-zinc-500 dark:text-zinc-400 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-white mb-8 transition-colors">
            <ArrowLeft className="w-4 h-4" />
            Back to Executive Brief
          </Link>

          <div className="flex flex-col md:flex-row md:items-start justify-between mb-12 gap-6">
            <div>
              <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-brand-lightbrown/10 text-brand-lightbrown text-xs font-medium border border-brand-lightbrown/20 mb-4">
                <Zap className="w-3 h-3" />
                Revenue Opportunity
              </div>
              <h1 className="text-2xl md:text-3xl font-bold tracking-tight mb-2">Analyzing Data...</h1>
              <p className="text-zinc-500 dark:text-zinc-400 dark:text-zinc-400">Morlen is actively building patterns from your conversations.</p>
            </div>
          </div>

          {/* Empty State */}
          <div className="p-12 md:p-24 rounded-3xl bg-zinc-100 dark:bg-white dark:bg-zinc-900/30 border border-zinc-200 dark:border-white/5 flex flex-col items-center text-center justify-center">
            <Activity className="w-16 h-16 text-zinc-400 dark:text-zinc-700 mb-6" />
            <h3 className="font-medium text-xl mb-3">No Opportunity Selected</h3>
            <p className="text-zinc-500 dark:text-zinc-400 max-w-md">
              When Morlen detects a specific revenue pattern or churn risk, detailed analysis and recommended actions will appear here.
            </p>
          </div>

        </div>
      </main>
    </div>
  );
}

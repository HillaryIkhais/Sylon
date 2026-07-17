import Link from "next/link";
import { Briefcase, BrainCircuit, TrendingUp, Zap } from "lucide-react";

export default function DashboardMobileNav({ activePath }: { activePath: string }) {
  return (
    <div className="lg:hidden flex overflow-x-auto gap-3 pb-4 mb-6 scrollbar-hide w-full px-2">
      <Link href="/dashboard" className={`flex-shrink-0 flex items-center gap-2 px-4 py-2.5 rounded-full text-sm font-semibold transition-all ${activePath === '/dashboard' ? 'bg-brand-brown text-white shadow-md' : 'glass-card text-brand-dark dark:text-white border border-brand-dark/5 dark:border-white/5'}`}>
        <Briefcase className="w-4 h-4" />
        Executive Brief
      </Link>
      <Link href="/dashboard/memory" className={`flex-shrink-0 flex items-center gap-2 px-4 py-2.5 rounded-full text-sm font-semibold transition-all ${activePath === '/dashboard/memory' ? 'bg-brand-brown text-white shadow-md' : 'glass-card text-brand-dark dark:text-white border border-brand-dark/5 dark:border-white/5'}`}>
        <BrainCircuit className="w-4 h-4" />
        Business Memory
      </Link>
      <Link href="/dashboard/opportunities" className={`flex-shrink-0 flex items-center gap-2 px-4 py-2.5 rounded-full text-sm font-semibold transition-all ${activePath === '/dashboard/opportunities' ? 'bg-brand-brown text-white shadow-md' : 'glass-card text-brand-dark dark:text-white border border-brand-dark/5 dark:border-white/5'}`}>
        <TrendingUp className="w-4 h-4" />
        Opportunities
      </Link>
      <Link href="/pricing" className={`flex-shrink-0 flex items-center gap-2 px-4 py-2.5 rounded-full text-sm font-semibold transition-all ${activePath === '/pricing' ? 'bg-brand-brown text-white shadow-md' : 'glass-card text-brand-dark dark:text-white border border-brand-dark/5 dark:border-white/5'}`}>
        <Zap className="w-4 h-4" />
        Upgrade Plan
      </Link>
    </div>
  );
}

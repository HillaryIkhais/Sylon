import Link from "next/link";
import { Briefcase, BrainCircuit, TrendingUp, Zap } from "lucide-react";

export default function DashboardMobileNav({ activePath }: { activePath: string }) {
  return (
    <div className="lg:hidden fixed bottom-0 left-0 right-0 z-[100] bg-white/95 dark:bg-[#1a1a1a]/95 backdrop-blur-xl border-t border-brand-dark/10 dark:border-white/10 px-2 py-3 flex justify-around items-center pb-safe">
      <Link href="/dashboard" className={`flex flex-col items-center gap-1.5 p-2 rounded-xl transition-all ${activePath === '/dashboard' ? 'text-brand-brown dark:text-brand-lightbrown scale-105' : 'text-brand-dark/50 dark:text-white/50 hover:text-brand-dark dark:hover:text-white'}`}>
        <Briefcase className="w-6 h-6" />
        <span className="text-[11px] font-bold">Brief</span>
      </Link>
      <Link href="/dashboard/memory" className={`flex flex-col items-center gap-1.5 p-2 rounded-xl transition-all ${activePath === '/dashboard/memory' ? 'text-brand-brown dark:text-brand-lightbrown scale-105' : 'text-brand-dark/50 dark:text-white/50 hover:text-brand-dark dark:hover:text-white'}`}>
        <BrainCircuit className="w-6 h-6" />
        <span className="text-[11px] font-bold">Memory</span>
      </Link>
      <Link href="/dashboard/opportunities" className={`flex flex-col items-center gap-1.5 p-2 rounded-xl transition-all ${activePath === '/dashboard/opportunities' ? 'text-brand-brown dark:text-brand-lightbrown scale-105' : 'text-brand-dark/50 dark:text-white/50 hover:text-brand-dark dark:hover:text-white'}`}>
        <TrendingUp className="w-6 h-6" />
        <span className="text-[11px] font-bold">Signals</span>
      </Link>
      <Link href="/pricing" className={`flex flex-col items-center gap-1.5 p-2 rounded-xl transition-all ${activePath === '/pricing' ? 'text-brand-brown dark:text-brand-lightbrown scale-105' : 'text-brand-dark/50 dark:text-white/50 hover:text-brand-dark dark:hover:text-white'}`}>
        <Zap className="w-6 h-6" />
        <span className="text-[11px] font-bold">Upgrade</span>
      </Link>
    </div>
  );
}

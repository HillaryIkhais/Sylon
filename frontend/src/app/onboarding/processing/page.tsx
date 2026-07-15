"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { BrainCircuit, Database, Network, Sparkles, CheckCircle2 } from "lucide-react";
import { ConversationProvider } from "@elevenlabs/react";
import EtherealOrb from "@/components/EtherealOrb";

export default function Processing() {
  const router = useRouter();
  const [phase, setPhase] = useState(0);

  const phases = [
    { text: "Creating business profile...", icon: MessageSquare, color: "text-brand-brown", bg: "bg-brand-brown/10" },
    { text: "Structuring intelligence layer...", icon: BrainCircuit, color: "text-brand-lightbrown", bg: "bg-brand-brown/10" },
    { text: "Calibrating algorithms...", icon: Database, color: "text-brand-dark", bg: "bg-brand-dark/10" },
    { text: "Finalizing workspace setup...", icon: Sparkles, color: "text-brand-brown", bg: "bg-brand-brown/10" }
  ];

  // Needed for first icon
  function MessageSquare(props: any) {
    return (
      <svg
        {...props}
        xmlns="http://www.w3.org/2000/svg"
        width="24"
        height="24"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
      >
        <path d="m3 21 1.9-5.7a8.5 8.5 0 1 1 3.8 3.8z" />
      </svg>
    )
  }

  useEffect(() => {
    // Cycle through phases every 2 seconds
    const interval = setInterval(() => {
      setPhase((prev) => {
        if (prev < phases.length - 1) {
          return prev + 1;
        }
        clearInterval(interval);
        // Once done, redirect to ingestion page
        setTimeout(() => {
          router.push("/upload");
        }, 1500);
        return prev;
      });
    }, 2000);

    return () => clearInterval(interval);
  }, [router, phases.length]);

  return (
    <div className="min-h-screen bg-glow-bg text-brand-dark flex flex-col md:flex-row relative overflow-hidden">
      
      {/* Left Side: Creative Brand Identity */}
      <div className="hidden md:flex md:w-1/2 relative bg-white/40 backdrop-blur-2xl border-r border-brand-dark/5 flex-col items-center justify-center p-12">
        <div className="absolute top-[-10%] left-[-10%] w-[120%] h-[120%] bg-brand-glow/20 rounded-full blur-[120px] pointer-events-none mix-blend-multiply" />
        
        <div className="relative z-10 w-full max-w-md text-left flex flex-col h-full justify-between">
          <div>
            <div className="w-16 h-16 rounded-2xl bg-gradient-to-br from-brand-lightbrown to-brand-brown mb-8 flex items-center justify-center font-bold text-4xl text-white shadow-2xl shadow-brand-brown/30">M</div>
            <h1 className="text-5xl font-bold tracking-tight mb-6 leading-tight">
              Creating your <br />
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-brand-lightbrown to-brand-brown">Workspace</span>
            </h1>
            <p className="text-xl text-brand-dark/60 font-medium">
              We're setting up your Morlen environment and calibrating the intelligence layer for your industry.
            </p>
          </div>
          
          <div className="w-full flex justify-center items-center transform scale-[0.8] opacity-80 pointer-events-none mt-12 h-[300px]">
             <ConversationProvider>
               <EtherealOrb />
             </ConversationProvider>
          </div>
        </div>
      </div>

      {/* Right Side: Interactive Form */}
      <div className="w-full md:w-1/2 flex flex-col items-center justify-center p-8 md:p-16 relative z-10 overflow-y-auto">
        <div className="w-full max-w-md relative z-10 flex flex-col items-center">
          
          {/* Central Animation Ring */}
          <div className="relative w-48 h-48 mb-16 flex items-center justify-center">
            {/* Outer rotating dashed ring */}
            <div className="absolute inset-0 rounded-full border-2 border-dashed border-brand-dark/20 animate-[spin_10s_linear_infinite]" />
            
            {/* Inner pulse */}
            <div className={`absolute inset-4 rounded-full transition-colors duration-1000 animate-pulse ${phases[phase].bg}`} />
            
            {/* Central Icon */}
            <div className={`relative z-10 transition-all duration-500 scale-125`}>
              {(() => {
                const Icon = phases[phase].icon;
                return <Icon className={`w-12 h-12 ${phases[phase].color}`} />;
              })()}
            </div>
          </div>

          {/* Text */}
          <div className="h-16 flex flex-col items-center justify-center">
            <h2 className="text-3xl font-bold tracking-tight text-center animate-in fade-in slide-in-from-bottom-4 duration-500 text-brand-dark" key={phase}>
              {phases[phase].text}
            </h2>
          </div>

          {/* Progress Checklist */}
          <div className="mt-16 w-full space-y-4">
            {phases.map((p, i) => {
              const isCompleted = i < phase;
              const isCurrent = i === phase;
              
              return (
                <div 
                  key={i} 
                  className={`flex items-center gap-4 transition-all duration-500 ${
                    isCompleted ? "opacity-100" : isCurrent ? "opacity-100 translate-x-2" : "opacity-30"
                  }`}
                >
                  {isCompleted ? (
                    <CheckCircle2 className="w-6 h-6 text-emerald-500 flex-shrink-0" />
                  ) : isCurrent ? (
                    <div className="w-6 h-6 rounded-full border-[3px] border-brand-dark/10 border-t-brand-brown animate-spin flex-shrink-0" />
                  ) : (
                    <div className="w-6 h-6 rounded-full border-2 border-brand-dark/20 flex-shrink-0" />
                  )}
                  <span className={`text-base font-bold tracking-wide ${isCompleted ? 'text-brand-dark/40' : isCurrent ? 'text-brand-dark' : 'text-brand-dark/40'}`}>
                    {p.text}
                  </span>
                </div>
              )
            })}
          </div>

        </div>
      </div>
    </div>
  );
}

'use client';

import { useState, useEffect } from 'react';
import { ChevronRight, ChevronLeft, TrendingDown, Users, Zap, Briefcase, Activity, ShieldAlert, CheckCircle, Network, TrendingUp } from 'lucide-react';

const slides = [
  {
    id: 1,
    title: "Sylon",
    subtitle: "The Autonomous Board of Directors for SMBs",
    content: (
      <div className="flex flex-col items-center justify-center space-y-8 text-center h-full">
        <h1 className="text-6xl md:text-8xl font-bold tracking-tighter bg-clip-text text-transparent bg-gradient-to-br from-indigo-400 to-cyan-300">
          Sylon.
        </h1>
        <p className="text-2xl md:text-4xl text-gray-400 font-light max-w-3xl">
          The Autonomous Board of Directors for Local Businesses.
        </p>
        <div className="mt-12 flex items-center gap-4 text-sm text-gray-500 uppercase tracking-widest">
          <span className="w-12 h-[1px] bg-gray-700"></span>
          Press Space or Arrows to Navigate
          <span className="w-12 h-[1px] bg-gray-700"></span>
        </div>
      </div>
    )
  },
  {
    id: 2,
    title: "The Problem",
    subtitle: "Guessing in a Volatile Market",
    content: (
      <div className="grid grid-cols-1 md:grid-cols-2 gap-12 h-full items-center">
        <div className="space-y-6">
          <h2 className="text-4xl font-semibold leading-tight text-white">
            A wrong guess today means <span className="text-rose-400">shutting down tomorrow.</span>
          </h2>
          <p className="text-xl text-gray-400 leading-relaxed">
            Enterprise companies hire McKinsey to simulate decisions. Small businesses just guess. When diesel costs spike or exchange rates fluctuate, trial and error is no longer a viable strategy.
          </p>
        </div>
        <div className="flex flex-col gap-6">
          <div className="p-6 rounded-2xl bg-white/5 border border-white/10 backdrop-blur-sm flex items-start gap-4">
            <div className="p-3 rounded-lg bg-rose-500/20 text-rose-400"><TrendingDown size={24} /></div>
            <div>
              <h3 className="text-lg font-medium text-white">Rising Operational Costs</h3>
              <p className="text-gray-400 text-sm mt-1">Fuel, inflation, and unpredictable overheads.</p>
            </div>
          </div>
          <div className="p-6 rounded-2xl bg-white/5 border border-white/10 backdrop-blur-sm flex items-start gap-4">
            <div className="p-3 rounded-lg bg-amber-500/20 text-amber-400"><ShieldAlert size={24} /></div>
            <div>
              <h3 className="text-lg font-medium text-white">Unpredictable Customer Reactions</h3>
              <p className="text-gray-400 text-sm mt-1">Fear of triggering online backlash ("wahala") over price or service changes.</p>
            </div>
          </div>
        </div>
      </div>
    )
  },
  {
    id: 3,
    title: "The Solution",
    subtitle: "The Agent Society",
    content: (
      <div className="flex flex-col h-full justify-center space-y-12">
        <div className="text-center space-y-4">
          <h2 className="text-3xl md:text-5xl font-semibold text-white">Data-Backed Strategy in 10 Seconds</h2>
          <p className="text-xl text-gray-400">Sylon spawns a multi-agent debate based on your actual customer reviews.</p>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-8">
          <div className="p-8 rounded-2xl bg-gradient-to-b from-indigo-900/40 to-transparent border border-indigo-500/20 text-center relative overflow-hidden">
            <div className="absolute top-0 left-0 w-full h-1 bg-indigo-500/50"></div>
            <div className="mx-auto w-16 h-16 rounded-full bg-indigo-500/20 flex items-center justify-center text-indigo-400 mb-6"><Briefcase size={32} /></div>
            <h3 className="text-xl font-bold text-white mb-3">CFO Agent</h3>
            <p className="text-gray-400 text-sm">Calculates margin impact, cost savings, and survival metrics.</p>
          </div>
          <div className="p-8 rounded-2xl bg-gradient-to-b from-cyan-900/40 to-transparent border border-cyan-500/20 text-center relative overflow-hidden">
            <div className="absolute top-0 left-0 w-full h-1 bg-cyan-500/50"></div>
            <div className="mx-auto w-16 h-16 rounded-full bg-cyan-500/20 flex items-center justify-center text-cyan-400 mb-6"><Users size={32} /></div>
            <h3 className="text-xl font-bold text-white mb-3">VP of CX Agent</h3>
            <p className="text-gray-400 text-sm">Simulates backlash against distinct local customer personas.</p>
          </div>
          <div className="p-8 rounded-2xl bg-gradient-to-b from-emerald-900/40 to-transparent border border-emerald-500/20 text-center relative overflow-hidden">
            <div className="absolute top-0 left-0 w-full h-1 bg-emerald-500/50"></div>
            <div className="mx-auto w-16 h-16 rounded-full bg-emerald-500/20 flex items-center justify-center text-emerald-400 mb-6"><Activity size={32} /></div>
            <h3 className="text-xl font-bold text-white mb-3">COO Agent</h3>
            <p className="text-gray-400 text-sm">Evaluates friction on kitchen staff, logistics, and supply chain.</p>
          </div>
        </div>
        
        <div className="flex justify-center items-center gap-4 mt-4">
          <span className="w-1/4 h-[1px] bg-gradient-to-r from-transparent to-white/20"></span>
          <div className="px-6 py-3 rounded-full bg-white/10 border border-white/20 text-white font-medium flex items-center gap-2">
            <Zap size={18} className="text-yellow-400" /> Synthesized by the CEO Agent
          </div>
          <span className="w-1/4 h-[1px] bg-gradient-to-l from-transparent to-white/20"></span>
        </div>
      </div>
    )
  },
  {
    id: 4,
    title: "Execution",
    subtitle: "Beyond Advice: Autopilot",
    content: (
      <div className="grid grid-cols-1 md:grid-cols-2 gap-12 h-full items-center">
        <div className="space-y-6">
          <h2 className="text-4xl font-semibold text-white">We don't just advise.<br/><span className="text-indigo-400">We execute.</span></h2>
          <p className="text-xl text-gray-400 leading-relaxed">
            When the Board reaches a consensus, Sylon's Autopilot queues up the operational changes for you. 
          </p>
          <ul className="space-y-4 mt-8">
            <li className="flex items-center gap-3 text-gray-300"><CheckCircle className="text-emerald-400" size={20}/> Drafts culturally relevant social media posts.</li>
            <li className="flex items-center gap-3 text-gray-300"><CheckCircle className="text-emerald-400" size={20}/> Stages API calls to update Google Business hours.</li>
            <li className="flex items-center gap-3 text-gray-300"><CheckCircle className="text-emerald-400" size={20}/> Waits for your 1-click 'Human-in-the-Loop' approval.</li>
          </ul>
        </div>
        
        <div className="bg-[#111116] rounded-xl border border-white/10 p-6 shadow-2xl relative overflow-hidden group">
          <div className="absolute top-0 right-0 w-32 h-32 bg-indigo-500/10 rounded-full blur-3xl -mr-10 -mt-10"></div>
          <div className="flex items-center justify-between border-b border-white/10 pb-4 mb-4">
            <h4 className="text-sm font-semibold text-gray-300 uppercase tracking-wider">Autopilot Actions</h4>
            <span className="px-2 py-1 text-xs rounded-md bg-yellow-500/20 text-yellow-400 font-medium">2 Pending</span>
          </div>
          
          <div className="space-y-4">
            <div className="bg-white/5 rounded-lg p-4 border border-white/5">
              <div className="flex justify-between items-start mb-2">
                <span className="text-sm font-medium text-white">Draft Social Post</span>
                <span className="text-xs text-gray-500">Instagram</span>
              </div>
              <p className="text-sm text-gray-400 mb-3">"To ensure we maintain top-tier quality despite rising costs, we are adjusting our closing time..."</p>
              <button className="w-full py-2 bg-white/10 hover:bg-white/20 text-white rounded-md text-sm transition-colors border border-white/10 pointer-events-none">Approve & Publish</button>
            </div>
            
            <div className="bg-white/5 rounded-lg p-4 border border-white/5">
              <div className="flex justify-between items-start mb-2">
                <span className="text-sm font-medium text-white">Update Google Profile</span>
                <span className="text-xs text-gray-500">API</span>
              </div>
              <p className="text-sm text-gray-400 mb-3">Update operating hours: Close at 10:00 PM (formerly 12:00 AM)</p>
              <button className="w-full py-2 bg-indigo-600 hover:bg-indigo-500 text-white rounded-md text-sm transition-colors shadow-lg shadow-indigo-900/20 pointer-events-none">Approve & Execute</button>
            </div>
          </div>
        </div>
      </div>
    )
  },
  {
    id: 5,
    title: "Under The Hood",
    subtitle: "Architecture",
    content: (
      <div className="flex flex-col items-center justify-center h-full text-center space-y-12">
        <Network size={64} className="text-indigo-400 mb-4" />
        <h2 className="text-4xl font-semibold text-white">Not a chatbot. A Simulation Engine.</h2>
        <p className="text-xl text-gray-400 max-w-2xl mx-auto">
          Instead of relying on a single, generic AI prompt that hallucinates, we use an advanced Multi-Agent architecture. Specialized models challenge each other, creating a highly accurate simulation of real-world business dynamics before you make a move.
        </p>
      </div>
    )
  },
  {
    id: 6,
    title: "The Vision",
    subtitle: "Democratizing Strategy",
    content: (
      <div className="flex flex-col items-center justify-center h-full text-center space-y-8">
        <TrendingUp size={48} className="text-cyan-400 mb-6" />
        <h2 className="text-5xl md:text-7xl font-bold text-white leading-tight">
          Give <span className="bg-clip-text text-transparent bg-gradient-to-r from-indigo-400 to-cyan-300">every business</span><br/>the Board it deserves.
        </h2>
        <p className="text-2xl text-gray-400 max-w-3xl mt-8 font-light mx-auto">
          We want to give the local bakery in Surulere and the fashion brand in Ikeja the exact same strategic firepower as a Fortune 500 company.
        </p>
        <div className="mt-16 text-3xl font-bold tracking-widest text-white/80">
          SYLON.
        </div>
      </div>
    )
  }
];

export default function PitchDeck() {
  const [currentSlide, setCurrentSlide] = useState(0);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'ArrowRight' || e.key === ' ') {
        setCurrentSlide((prev) => Math.min(prev + 1, slides.length - 1));
      } else if (e.key === 'ArrowLeft') {
        setCurrentSlide((prev) => Math.max(prev - 1, 0));
      }
    };
    
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  return (
    <div className="fixed inset-0 bg-[#0a0a0c] text-white overflow-hidden font-sans select-none flex flex-col">
      {/* Background Glows */}
      <div className="absolute top-0 left-1/4 w-[500px] h-[500px] bg-indigo-900/20 rounded-full blur-[120px] pointer-events-none"></div>
      <div className="absolute bottom-0 right-1/4 w-[600px] h-[600px] bg-cyan-900/10 rounded-full blur-[150px] pointer-events-none"></div>
      
      {/* Header / Nav Progress */}
      <header className="absolute top-0 left-0 w-full p-8 z-20 flex justify-between items-center opacity-50">
        <div className="font-bold tracking-widest text-xl">SYLON</div>
        <div className="flex gap-2">
          {slides.map((_, i) => (
            <div 
              key={i} 
              className={`h-1.5 rounded-full transition-all duration-500 ${i === currentSlide ? 'w-8 bg-white' : 'w-2 bg-white/20'}`}
            />
          ))}
        </div>
      </header>

      {/* Main Slide Content */}
      <main className="flex-1 relative z-10 w-full max-w-7xl mx-auto px-12 pt-24 pb-20 flex items-center justify-center">
        {slides.map((slide, i) => (
          <div 
            key={slide.id}
            className={`absolute inset-0 px-12 pt-24 pb-20 transition-all duration-700 ease-[cubic-bezier(0.23,1,0.32,1)] flex flex-col items-center justify-center ${
              i === currentSlide 
                ? 'opacity-100 translate-y-0 scale-100 pointer-events-auto z-10' 
                : i < currentSlide 
                  ? 'opacity-0 -translate-y-8 scale-95 pointer-events-none z-0'
                  : 'opacity-0 translate-y-8 scale-105 pointer-events-none z-0'
            }`}
          >
            {/* Slide Header (Except title slide) */}
            {i !== 0 && i !== slides.length - 1 && (
              <div className="absolute top-24 left-12">
                <h3 className="text-indigo-400 font-medium tracking-wider uppercase text-sm mb-2">{slide.subtitle}</h3>
              </div>
            )}
            
            {/* Slide Body */}
            <div className="w-full h-full flex flex-col justify-center">
              {slide.content}
            </div>
          </div>
        ))}
      </main>

      {/* Controls */}
      <div className="absolute bottom-8 right-8 z-20 flex gap-4">
        <button 
          onClick={() => setCurrentSlide(prev => Math.max(prev - 1, 0))}
          className={`p-3 rounded-full border border-white/10 backdrop-blur-md transition-all ${currentSlide === 0 ? 'opacity-30 cursor-not-allowed' : 'hover:bg-white/10 text-white'}`}
          disabled={currentSlide === 0}
        >
          <ChevronLeft size={24} />
        </button>
        <button 
          onClick={() => setCurrentSlide(prev => Math.min(prev + 1, slides.length - 1))}
          className={`p-3 rounded-full border border-white/10 backdrop-blur-md transition-all ${currentSlide === slides.length - 1 ? 'opacity-30 cursor-not-allowed' : 'hover:bg-white/10 text-white'}`}
          disabled={currentSlide === slides.length - 1}
        >
          <ChevronRight size={24} />
        </button>
      </div>
    </div>
  );
}

import React from 'react';

export const Navbar: React.FC = () => {
  return (
    <nav className="fixed top-0 left-0 w-full z-50 glass-nav py-4 px-8 md:px-16 flex items-center justify-between">
      <div className="flex items-center">
        <span className="text-white font-medium tracking-tight text-xl">Synapse</span>
      </div>
      
      <div className="hidden md:flex items-center space-x-8">
        <a href="#features" className="text-sm font-medium text-white px-3 py-1 border border-white/20 rounded-full bg-gradient-to-r from-white/10 to-transparent">Features</a>
        <a href="#insights" className="text-sm font-light text-white/70 hover:text-white transition-colors">Insights</a>
        <a href="#about" className="text-sm font-light text-white/70 hover:text-white transition-colors">About</a>
        <a href="#casestudies" className="text-sm font-light text-white/40 line-through decoration-white/40">Case Studies</a>
        <a href="#contact" className="text-sm font-light text-white/70 hover:text-white transition-colors">Contact</a>
      </div>
      
      <div>
        <button className="bg-gradient-to-r from-white to-gray-300 text-black px-5 py-2.5 rounded-full text-sm font-medium hover:opacity-90 transition-opacity">
          Get Started for Free
        </button>
      </div>
    </nav>
  );
};

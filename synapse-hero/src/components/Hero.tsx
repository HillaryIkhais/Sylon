import React from 'react';
import { motion } from 'framer-motion';
import { Zap, Shield, Globe } from 'lucide-react';

export const Hero: React.FC = () => {
  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.2,
        delayChildren: 0.3,
      },
    },
  };

  const itemVariants = {
    hidden: { opacity: 0, y: 20 },
    visible: { 
      opacity: 1, 
      y: 0,
      transition: { duration: 0.8, ease: [0.16, 1, 0.3, 1] }
    },
  };

  return (
    <div className="relative z-10 w-full h-full flex flex-col items-center justify-center pt-20 pointer-events-none">
      <motion.div 
        className="flex flex-col items-center text-center max-w-5xl px-6 pointer-events-auto"
        variants={containerVariants}
        initial="hidden"
        animate="visible"
      >
        {/* Badges */}
        <motion.div variants={itemVariants} className="flex items-center space-x-4 mb-8">
          <div className="glass-badge px-4 py-1.5 rounded-full flex items-center space-x-2 text-xs text-white/80">
            <span className="font-light">Integrated with</span>
            <Zap size={14} className="text-white" />
          </div>
          <div className="glass-badge px-4 py-1.5 rounded-full flex items-center space-x-2 text-xs text-white/80">
            <span className="font-light">Integrated with</span>
            <Shield size={14} className="text-white" />
          </div>
          <div className="glass-badge px-4 py-1.5 rounded-full flex items-center space-x-2 text-xs text-white/80">
            <span className="font-light">Integrated with</span>
            <Globe size={14} className="text-white" />
          </div>
        </motion.div>

        {/* Headline */}
        <motion.h1 
          variants={itemVariants}
          className="text-6xl md:text-[80px] font-medium leading-[0.95] tracking-tight text-white mb-8"
        >
          Where Innovation <br />
          <span className="gradient-text">Meets Execution</span>
        </motion.h1>

        {/* Subtext */}
        <motion.p 
          variants={itemVariants}
          className="text-lg md:text-xl text-white/60 font-light max-w-2xl leading-relaxed mb-10"
        >
          Streamline your testing and deployment pipelines instantly. <br />
          Built for teams that demand precision without sacrificing speed.
        </motion.p>

        {/* Buttons */}
        <motion.div variants={itemVariants} className="flex items-center space-x-6">
          <button className="bg-black border border-white/30 text-white px-8 py-3.5 rounded-full text-sm font-medium hover:bg-white hover:text-black transition-colors">
            Get Started for Free
          </button>
          <button className="glass-badge text-white px-8 py-3.5 rounded-full text-sm font-medium hover:bg-white/10 transition-colors">
            Let's Get Connected
          </button>
        </motion.div>
      </motion.div>
    </div>
  );
};

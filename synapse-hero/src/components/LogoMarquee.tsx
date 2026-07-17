import React from 'react';

const Logo = () => (
  <svg width="120" height="40" viewBox="0 0 120 40" fill="none" xmlns="http://www.w3.org/2000/svg" className="opacity-40 grayscale hover:grayscale-0 hover:opacity-100 transition-all duration-300">
    <rect width="120" height="40" fill="url(#pattern0)" fillOpacity="0.5"/>
    <defs>
      <pattern id="pattern0" patternContentUnits="objectBoundingBox" width="1" height="1">
        <use href="#image0" transform="scale(0.00833333 0.025)"/>
      </pattern>
      <image id="image0" width="120" height="40" href="data:image/svg+xml,%3Csvg width='120' height='40' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M20 20L40 20' stroke='white' stroke-width='4' stroke-linecap='round'/%3E%3Cpath d='M30 10L30 30' stroke='white' stroke-width='4' stroke-linecap='round'/%3E%3Crect x='60' y='10' width='20' height='20' rx='4' stroke='white' stroke-width='2' fill='none'/%3E%3Ccircle cx='100' cy='20' r='10' fill='white'/%3E%3C/svg%3E"/>
    </defs>
  </svg>
);

export const LogoMarquee: React.FC = () => {
  return (
    <div className="absolute bottom-0 left-0 w-full py-8 border-t border-white/5 bg-black/50 backdrop-blur-sm z-20 overflow-hidden">
      <div className="flex w-full items-center justify-around px-8">
        <Logo />
        <Logo />
        <Logo />
        <Logo />
        <Logo />
      </div>
    </div>
  );
};

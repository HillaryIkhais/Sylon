import React from 'react';
import { Navbar } from './components/Navbar';
import { Hero } from './components/Hero';
import { LogoMarquee } from './components/LogoMarquee';
import { VideoPlayer } from './components/VideoPlayer';

function App() {
  return (
    <div className="relative w-full h-screen bg-black overflow-hidden flex flex-col">
      <Navbar />
      
      {/* Background Video Component */}
      <VideoPlayer src="https://stream.mux.com/9JXDljEVWYwWu01PUkAemafDugK89o01BR6zqJ3aS9u00A.m3u8" />
      
      {/* Hero Content positioned over the video */}
      <Hero />
      
      {/* Static Marquee at the bottom */}
      <LogoMarquee />
    </div>
  );
}

export default App;

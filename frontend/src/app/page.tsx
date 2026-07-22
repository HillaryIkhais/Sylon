"use client";

import Link from "next/link";
import { useRef } from "react";
import gsap from "gsap";
import { useGSAP } from "@gsap/react";
import { ConversationProvider } from "@elevenlabs/react";
import EtherealOrb from "@/components/EtherealOrb";
import { usePrivy } from "@privy-io/react-auth";
import { useRouter } from "next/navigation";
import { useEffect } from "react";
import ThemeToggle from "@/components/ThemeToggle";

export default function Home() {
  const { login, authenticated, ready } = usePrivy();
  const router = useRouter();

  useEffect(() => {
    if (ready && authenticated && typeof window !== 'undefined') {
      if (!localStorage.getItem('morlen_onboarded')) {
        router.push('/onboarding');
      }
    }
  }, [authenticated, ready, router]);

  const containerRef = useRef<HTMLDivElement>(null);

  // Background animation refs
  const bgRing1Ref = useRef<HTMLDivElement>(null);
  const bgRing2Ref = useRef<HTMLDivElement>(null);
  const nebulaGlowRef = useRef<HTMLDivElement>(null);

  const heroTextRef = useRef<HTMLHeadingElement>(null);
  const subTextRef = useRef<HTMLParagraphElement>(null);

  useGSAP(() => {
    // Hero Text Entrance
    gsap.fromTo(
      heroTextRef.current,
      { y: 30, opacity: 0, scale: 0.95 },
      { y: 0, opacity: 1, scale: 1, duration: 1.5, ease: "power4.out", delay: 0.2 }
    );

    gsap.fromTo(
      subTextRef.current,
      { y: 20, opacity: 0 },
      { y: 0, opacity: 1, duration: 1, ease: "power3.out", delay: 1 }
    );

    // Continuous Background Animations
    gsap.to(bgRing1Ref.current, {
      rotation: 360,
      scale: 1.05,
      duration: 30,
      repeat: -1,
      yoyo: true,
      ease: "sine.inOut"
    });

    gsap.to(bgRing2Ref.current, {
      rotation: -360,
      scale: 1.1,
      duration: 40,
      repeat: -1,
      yoyo: true,
      ease: "sine.inOut"
    });

    gsap.to(nebulaGlowRef.current, {
      scale: 1.2,
      opacity: 0.8,
      duration: 8,
      repeat: -1,
      yoyo: true,
      ease: "sine.inOut"
    });

  }, { scope: containerRef });

  return (
    <div ref={containerRef} className="font-sans text-brand-dark flex-grow flex flex-col relative overflow-x-hidden z-0">
      {/* Complex Background Layers */}
      <div className="fixed inset-0 z-[-1] pointer-events-none overflow-hidden">
        {/* Soft, billowy clouds at the bottom */}
        <div className="absolute bottom-[-20%] left-[-10%] right-[-10%] h-[80vh] bg-gradient-to-t from-[#fff5f0] via-brand-lightbrown/40 to-transparent blur-[100px] mix-blend-screen opacity-90" />

        {/* Sweeping glowing trails of light in background */}
        <div
          ref={bgRing1Ref}
          className="absolute top-[10%] left-[-30%] w-[160%] h-[80%] border-t-[8px] border-white/60 rounded-[100%] rotate-[-15deg] blur-[16px] mix-blend-overlay opacity-80"
        />
        <div
          ref={bgRing2Ref}
          className="absolute top-[5%] left-[-15%] w-[130%] h-[90%] border-b-[12px] border-brand-lightbrown/40 rounded-[100%] rotate-[10deg] blur-[24px] mix-blend-screen opacity-70"
        />

        {/* Additional radial glow for Warm Cosmic Nebula effect */}
        <div
          ref={nebulaGlowRef}
          className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[90vw] h-[90vw] md:w-[70vw] md:h-[70vw] bg-gradient-to-r from-brand-glow/40 to-brand-lightbrown/30 rounded-full blur-[140px] mix-blend-screen opacity-70"
        />
      </div>



      {/* Main Content */}
      <main className="flex-grow flex flex-col justify-start pt-8 md:pt-24 pb-24 px-6 md:px-12 z-10 relative w-full max-w-7xl mx-auto">
        <div className="grid grid-cols-1 md:grid-cols-2 items-center w-full gap-y-6 md:gap-y-0 md:gap-x-12 perspective-1000">
          
          {/* Headline (Order 1 on mobile, Col 1 Row 1 on desktop) */}
          <h1
            ref={heroTextRef}
            className="text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-bold tracking-tight text-center md:text-left text-brand-dark leading-tight drop-shadow-sm order-1 md:col-start-1 md:row-start-1 mb-0 md:mb-6 relative z-10"
          >
            Turn customer conversations into <span className="text-transparent bg-clip-text bg-gradient-to-r from-brand-lightbrown to-brand-brown block md:inline">executive decisions.</span>
          </h1>

          {/* Right Column: Ethereal Orb (Order 2 on mobile, Col 2 Row 1-3 on desktop) */}
          <div className="w-full flex justify-center items-center transform scale-[0.9] md:scale-100 relative h-[350px] sm:h-[400px] md:h-[500px] order-2 md:col-start-2 md:row-start-1 md:row-span-3">
             <ConversationProvider>
               <EtherealOrb />
             </ConversationProvider>
          </div>
            
          {/* Subheadline (Order 3 on mobile, Col 1 Row 2 on desktop) */}
          <p
            ref={subTextRef}
            className="text-base sm:text-lg md:text-xl text-brand-dark/70 max-w-lg mx-auto md:mx-0 text-center md:text-left font-medium order-3 md:col-start-1 md:row-start-2 mb-2 md:mb-8 relative z-10"
          >
            The intelligence layer for conversational commerce. Morlen gathers clues from every customer interaction to tell you exactly where your next opportunity is.
          </p>
            
          {/* CTA (Order 4 on mobile, Col 1 Row 3 on desktop) */}
          <div className="flex flex-col sm:flex-row items-center justify-center md:justify-start gap-4 order-4 md:col-start-1 md:row-start-3">
            <button
              onClick={() => router.push('/onboarding')}
              className="text-white bg-brand-brown px-8 py-4 rounded-full font-bold inline-flex items-center justify-center w-full sm:w-auto space-x-2 shadow-xl hover:scale-105 transition-all"
            >
              <span>Get Started</span>
            </button>
          </div>

        </div>
      </main>



      {/* Bottom CTA */}
      <section className="w-full py-32 px-4 bg-gradient-to-b from-brand-lightbrown/10 to-transparent relative z-10 text-center">
        <div className="max-w-3xl mx-auto">
          <h2 className="text-4xl md:text-5xl font-bold text-brand-dark mb-6">Your business has a memory. Start using it.</h2>
          <p className="text-xl text-brand-dark/70 mb-10 max-w-xl mx-auto">Connect Morlen today and transform thousands of raw customer chats into your most powerful competitive advantage.</p>
          <button onClick={() => router.push('/onboarding')} className="text-white bg-brand-brown px-12 py-5 rounded-full font-bold text-lg inline-flex items-center space-x-2 shadow-xl hover:scale-105 transition-all">
            <span>Get Started with Morlen</span>
          </button>
        </div>
      </section>

      {/* Main Footer */}
      <footer className="w-full pb-8 pt-4 px-8 md:px-16 z-50 relative mt-auto border-t border-brand-dark/10">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between text-xs text-brand-dark font-medium">
          {/* Logo */}
          <div className="mb-4 md:mb-0">
            <span className="text-xl font-bold tracking-wider text-brand-brown">MORLEN</span>
          </div>
          {/* Footer Links */}
          <div className="flex space-x-6 mb-4 md:mb-0">
            <Link href="/pricing" className="hover:text-brand-lightbrown transition-colors">Pricing</Link>
            <Link href="#" className="hover:text-brand-lightbrown transition-colors">Privacy Policy</Link>
            <Link href="#" className="hover:text-brand-lightbrown transition-colors">Terms of Service</Link>
            <Link href="#" className="hover:text-brand-lightbrown transition-colors">Security</Link>
            <Link href="#" className="hover:text-brand-lightbrown transition-colors">Contact</Link>
          </div>
          {/* Copyright */}
          <div>
            © 2026 Morlen Behavioral Intelligence. All rights reserved.
          </div>
        </div>
      </footer>
    </div>
  );
}

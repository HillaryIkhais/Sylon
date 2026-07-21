"use client";

import { useRef } from "react";
import gsap from "gsap";
import { useGSAP } from "@gsap/react";
import { ChevronDown } from "lucide-react";
import { useState } from "react";
import Link from "next/link";
import WaitlistModal from "@/components/WaitlistModal";

const faqs = [
  {
    question: "How fast is setup and integration?",
    answer: "Morlen integrates instantly. There is no manual configuration. You simply connect your WhatsApp, Instagram, or e-commerce platform via OAuth, and Morlen immediately begins syncing historical chat logs and transaction data to build your baseline.",
  },
  {
    question: "Is my customer data secure?",
    answer: "Absolutely. We employ bank-grade encryption (AES-256) for all data at rest and in transit. Your customer conversations are anonymized before passing through our language models, meaning personal identifiers (PII) are stripped out, ensuring total privacy.",
  },
  {
    question: "How does Morlen actually drive revenue?",
    answer: "Morlen isn't just an analytics dashboard. It actively reads customer signals (e.g., people asking for a specific product out of stock). It then generates a daily Executive Brief directly to your inbox, quantifying exactly how much money you are leaving on the table and providing a 1-click execution button to fix the operational bottleneck.",
  },
  {
    question: "What platforms does Morlen support?",
    answer: "Currently, Morlen seamlessly integrates natively with WhatsApp Business API, Instagram Direct, Shopify, and Stripe. We are actively rolling out integrations for WooCommerce, Intercom, and Zendesk.",
  },
  {
    question: "Do I need technical knowledge to use it?",
    answer: "Zero. If you can read a morning newsletter, you can use Morlen. The platform is designed specifically for founders and operators who don't have time to write SQL queries or stare at complex graphs.",
  },
];

export default function FAQPage() {
  const [openIndex, setOpenIndex] = useState<number | null>(0);
  const [isWaitlistOpen, setIsWaitlistOpen] = useState(false);
  const containerRef = useRef<HTMLDivElement>(null);
  const titleRef = useRef<HTMLHeadingElement>(null);
  const faqRefs = useRef<(HTMLDivElement | null)[]>([]);

  useGSAP(() => {
    gsap.fromTo(
      titleRef.current,
      { opacity: 0, y: 40, scale: 0.95 },
      { opacity: 1, y: 0, scale: 1, duration: 1.2, ease: "power4.out" }
    );

    gsap.fromTo(
      faqRefs.current,
      { opacity: 0, x: -30 },
      { opacity: 1, x: 0, duration: 0.8, stagger: 0.1, ease: "power3.out", delay: 0.3 }
    );
  }, { scope: containerRef });

  return (
    <>
    <div ref={containerRef} className="min-h-screen pt-32 pb-24 px-4 md:px-8 max-w-4xl mx-auto w-full relative">
      
      {/* Background glow elements */}
      <div className="absolute top-[10%] left-1/2 -translate-x-1/2 w-[600px] h-[600px] bg-brand-brown/10 dark:bg-brand-brown/5 rounded-full blur-[120px] -z-10 pointer-events-none" />

      <div className="text-center mb-16">
        <h1 ref={titleRef} className="text-4xl md:text-6xl font-bold tracking-tight text-brand-dark dark:text-white mb-6">
          Common <span className="text-transparent bg-clip-text bg-gradient-to-r from-brand-brown to-brand-lightbrown">Questions</span>
        </h1>
        <p className="text-lg text-brand-dark/60 dark:text-white/50 max-w-2xl mx-auto">
          Everything you need to know about setting up and scaling your business with Morlen.
        </p>
      </div>

      <div className="space-y-4">
        {faqs.map((faq, index) => {
          const isOpen = openIndex === index;
          return (
            <div
              key={index}
              ref={el => { faqRefs.current[index] = el; }}
              className={`border border-brand-dark/10 dark:border-white/10 rounded-2xl overflow-hidden transition-all duration-300 ${
                isOpen ? "bg-white/40 dark:bg-black/40 backdrop-blur-md shadow-xl" : "bg-white/10 dark:bg-white/5 backdrop-blur-sm hover:bg-white/20 dark:hover:bg-white/10"
              }`}
            >
              <button
                onClick={() => setOpenIndex(isOpen ? null : index)}
                className="w-full px-6 py-6 flex items-center justify-between text-left focus:outline-none"
              >
                <h3 className={`text-lg md:text-xl font-medium transition-colors ${isOpen ? "text-brand-brown dark:text-brand-lightbrown" : "text-brand-dark dark:text-white/90"}`}>
                  {faq.question}
                </h3>
                <ChevronDown className={`w-6 h-6 text-brand-dark/50 dark:text-white/50 transition-transform duration-300 ${isOpen ? "rotate-180 text-brand-brown" : ""}`} />
              </button>
              
              <div 
                className={`px-6 overflow-hidden transition-all duration-500 ease-in-out ${isOpen ? "max-h-96 pb-6 opacity-100" : "max-h-0 opacity-0"}`}
              >
                <p className="text-brand-dark/70 dark:text-white/60 leading-relaxed text-base md:text-lg">
                  {faq.answer}
                </p>
              </div>
            </div>
          );
        })}
      </div>
      
      {/* Final CTA */}
      <div className="w-full text-center mt-32 mb-8 px-4 relative z-10">
        <h2 className="text-3xl md:text-5xl font-bold text-brand-dark dark:text-white mb-6">Still have questions?</h2>
        <p className="text-lg text-brand-dark/70 dark:text-white/60 mb-10 max-w-xl mx-auto">Get early access and see exactly how Morlen fits into your stack.</p>
        <button
          onClick={() => setIsWaitlistOpen(true)}
          className="text-white bg-brand-brown px-10 py-4 rounded-full font-bold inline-flex items-center justify-center space-x-2 hover:opacity-90 transition-all shadow-xl hover:shadow-2xl hover:-translate-y-1"
        >
          <span>Join Waitlist</span>
        </button>
      </div>

    </div>
    
    {/* Main Footer (Placed outside max-w-4xl container to span full width) */}
    <footer className="w-full pb-8 pt-4 px-8 md:px-16 z-50 relative mt-auto border-t border-brand-dark/10 dark:border-white/10">
      <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between text-xs text-brand-dark dark:text-white/70 font-medium">
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

    <WaitlistModal 
      isOpen={isWaitlistOpen} 
      onClose={() => setIsWaitlistOpen(false)} 
    />
    </>
  );
}

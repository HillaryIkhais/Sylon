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
    question: "How fast is setup?",
    answer: "Morlen sets up instantly. There is nothing complicated to install. You just log in, connect your WhatsApp or Instagram, and Morlen immediately starts analyzing your past chats to learn about your business.",
  },
  {
    question: "Is my customer data safe?",
    answer: "Yes, completely safe. We use the same high-level security as major banks. Before Morlen's AI reads anything, it hides personal details like names and phone numbers, so your customers' privacy is always protected.",
  },
  {
    question: "How does Morlen actually help my business?",
    answer: "Morlen acts like a brilliant assistant who reads every single message from your customers. It notices things you don't have time to see—like a sudden drop in interest for a product—and sends you an email telling you exactly how to fix it before you lose money.",
  },
  {
    question: "What apps does Morlen work with?",
    answer: "Right now, Morlen works perfectly with WhatsApp, Instagram, and Shopify. We are adding more apps very soon so you can connect everything in one place.",
  },
  {
    question: "Do I need technical skills to use it?",
    answer: "None at all. If you can read an email, you can use Morlen. We built it specifically for busy business owners who don't have time to learn complicated new software.",
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
    <div className="flex-grow flex flex-col relative w-full z-0 overflow-x-hidden">
      
      {/* Background glow elements */}
      <div className="fixed inset-0 pointer-events-none z-[-1]">
        <div className="absolute top-[10%] left-1/2 -translate-x-1/2 w-[600px] h-[600px] bg-brand-brown/10 dark:bg-brand-brown/5 rounded-full blur-[120px]" />
      </div>

      {/* Main Content Wrapper */}
      <div ref={containerRef} className="flex-grow flex flex-col items-center justify-start pt-24 sm:pt-32 pb-24 px-4 z-10 relative w-full">
        <div className="max-w-4xl mx-auto w-full">
          
          <div className="text-center mb-16">
            <h1 ref={titleRef} className="text-4xl md:text-6xl font-bold tracking-tight text-brand-dark dark:text-white mb-6">
              Common <span className="text-transparent bg-clip-text bg-gradient-to-r from-brand-brown to-brand-lightbrown">Questions</span>
            </h1>
            <p className="text-lg text-brand-dark/70 dark:text-white/60 max-w-2xl mx-auto font-medium">
              Everything you need to know about setting up and scaling your business with Morlen.
            </p>
          </div>

          <div className="space-y-4 w-full relative z-20">
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
                    <h3 className={`text-lg md:text-xl font-bold transition-colors ${isOpen ? "text-brand-brown dark:text-brand-lightbrown" : "text-brand-dark dark:text-white/90"}`}>
                      {faq.question}
                    </h3>
                    <ChevronDown className={`w-6 h-6 shrink-0 text-brand-dark/50 dark:text-white/50 transition-transform duration-300 ${isOpen ? "rotate-180 text-brand-brown" : ""}`} />
                  </button>
                  
                  <div 
                    className={`px-6 overflow-hidden transition-all duration-500 ease-in-out ${isOpen ? "max-h-96 pb-6 opacity-100" : "max-h-0 opacity-0"}`}
                  >
                    <p className="text-brand-dark/70 dark:text-white/60 leading-relaxed text-base md:text-lg font-medium">
                      {faq.answer}
                    </p>
                  </div>
                </div>
              );
            })}
          </div>

          {/* Final CTA */}
          <div className="w-full text-center mt-32 mb-12">
            <h2 className="text-3xl md:text-5xl font-bold text-brand-dark dark:text-white mb-6">Still have questions?</h2>
            <p className="text-lg text-brand-dark/70 dark:text-white/60 mb-10 max-w-xl mx-auto font-medium">Get early access and see exactly how Morlen fits into your business.</p>
            <button
              onClick={() => setIsWaitlistOpen(true)}
              className="text-white bg-brand-brown px-10 py-4 rounded-full font-bold inline-flex items-center justify-center space-x-2 hover:opacity-90 transition-all shadow-xl hover:shadow-2xl hover:-translate-y-1"
            >
              <span>Join Waitlist</span>
            </button>
          </div>
        </div>
      </div>
      
      {/* Main Footer */}
      <footer className="w-full pb-8 pt-4 px-8 md:px-16 z-50 relative mt-auto border-t border-brand-dark/10 dark:border-white/10 shrink-0">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between text-xs text-brand-dark dark:text-white/70 font-medium">
          <div className="mb-4 md:mb-0">
            <span className="text-xl font-bold tracking-wider text-brand-brown">MORLEN</span>
          </div>
          <div className="flex space-x-6 mb-4 md:mb-0">
            <Link href="/pricing" className="hover:text-brand-lightbrown transition-colors">Pricing</Link>
            <Link href="#" className="hover:text-brand-lightbrown transition-colors">Privacy Policy</Link>
            <Link href="#" className="hover:text-brand-lightbrown transition-colors">Terms of Service</Link>
            <Link href="#" className="hover:text-brand-lightbrown transition-colors">Security</Link>
            <Link href="#" className="hover:text-brand-lightbrown transition-colors">Contact</Link>
          </div>
          <div>
            © 2026 Morlen Behavioral Intelligence. All rights reserved.
          </div>
        </div>
      </footer>

      <WaitlistModal 
        isOpen={isWaitlistOpen} 
        onClose={() => setIsWaitlistOpen(false)} 
      />
    </div>
  );
}

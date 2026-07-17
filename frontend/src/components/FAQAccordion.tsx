"use client";

import { useState } from "react";
import { ChevronDown } from "lucide-react";

type FAQ = {
  question: string;
  answer: string;
};

const faqs: FAQ[] = [
  {
    question: "What exactly does Morlen do?",
    answer: "Morlen is an intelligence layer that connects to your sales channels and surfaces hidden patterns in customer conversations, so you know exactly what your customers want without having to guess."
  },
  {
    question: "Do you work with businesses of my size?",
    answer: "Yes, Morlen is designed to scale. Whether you're an independent retailer handling a few hundred messages a week or a large enterprise processing millions, our infrastructure handles it effortlessly."
  },
  {
    question: "Does this replace my customer service team?",
    answer: "No. Morlen empowers your team by giving them insights and automating data entry, so they can focus on closing sales and building relationships instead of manually tagging messages."
  },
  {
    question: "How does this connect to my current tools?",
    answer: "Morlen seamlessly integrates with WhatsApp Business API, Instagram DMs, Facebook Messenger, and your website chat in just a few clicks. No coding or complex setup required."
  },
  {
    question: "How do I know the data is accurate?",
    answer: "Every insight Morlen generates is backed by empirical evidence. You can click on any data point in your dashboard to see the exact customer quotes and original conversations that support it."
  }
];

export default function FAQAccordion() {
  const [openIndex, setOpenIndex] = useState<number | null>(0);

  const toggle = (index: number) => {
    setOpenIndex(openIndex === index ? null : index);
  };

  return (
    <div className="w-full max-w-3xl mx-auto space-y-4">
      {faqs.map((faq, index) => {
        const isOpen = openIndex === index;
        return (
          <div 
            key={index} 
            className="border border-brand-dark/10 bg-white/50 dark:bg-black/20 backdrop-blur-md rounded-2xl overflow-hidden transition-all duration-300"
          >
            <button
              onClick={() => toggle(index)}
              className="w-full flex items-center justify-between p-6 text-left focus:outline-none"
            >
              <span className="font-bold text-brand-dark text-lg pr-8">{faq.question}</span>
              <ChevronDown 
                className={`w-5 h-5 text-brand-dark/70 flex-shrink-0 transition-transform duration-300 ${isOpen ? "rotate-180" : ""}`} 
              />
            </button>
            <div 
              className={`overflow-hidden transition-all duration-300 ease-in-out ${isOpen ? "max-h-96 opacity-100" : "max-h-0 opacity-0"}`}
            >
              <div className="p-6 pt-0 text-brand-dark/70 text-base leading-relaxed">
                {faq.answer}
              </div>
            </div>
          </div>
        );
      })}
    </div>
  );
}

"use client";

import { useState } from "react";
import Link from "next/link";
import { ArrowRight, ArrowLeft, Check, Building2, Users, Target, Smartphone } from "lucide-react";
import { useRouter } from "next/navigation";
import { ConversationProvider } from "@elevenlabs/react";
import EtherealOrb from "@/components/EtherealOrb";

export default function Onboarding() {
  const router = useRouter();
  const [step, setStep] = useState(1);
  const [formData, setFormData] = useState({
    businessName: "",
    businessType: "",
    industry: "",
    otherIndustry: "",
    teamSize: "",
    goals: [] as string[],
    channels: [] as string[]
  });

  const businessTypes = ["Boutique / Fashion", "Supermarket / Retail", "Restaurant / Food Service", "Service Provider (Salon, Artisan)", "Wholesale / Distribution", "Other"];
  const industries = ["E-Commerce & Retail", "Food & Beverage", "Finance & Banking", "Health & Wellness", "Fashion & Apparel", "Other"];
  const goals = ["Increase Sales", "Keep Customers Coming Back", "Better Inventory Tracking", "Automate Follow-ups"];
  const channels = ["WhatsApp", "Instagram", "Facebook", "Website", "Physical Store"];

  const handleNext = () => {
    if (!isStepValid()) return;
    if (step < 3) {
      setStep(step + 1);
    } else {
      localStorage.setItem("morlen_industry", formData.industry);
      localStorage.setItem("morlen_business_name", formData.businessName);
      router.push("/onboarding/processing");
    }
  };

  const isStepValid = () => {
    if (step === 1) {
      if (!formData.businessName.trim() || !formData.businessType || !formData.industry || !formData.teamSize) return false;
      if (formData.industry === "Other" && !formData.otherIndustry.trim()) return false;
      return true;
    }
    if (step === 2) return formData.channels.length > 0;
    if (step === 3) return formData.goals.length > 0;
    return false;
  };

  const toggleSelection = (field: "goals" | "channels", value: string) => {
    setFormData(prev => ({
      ...prev,
      [field]: prev[field].includes(value) 
        ? prev[field].filter(v => v !== value)
        : [...prev[field], value]
    }));
  };

  return (
    <div className="min-h-screen bg-glow-bg text-brand-dark flex flex-col md:flex-row relative overflow-hidden">
      
      {/* Left Side: Creative Brand Identity */}
      <div className="hidden md:flex md:w-1/2 relative bg-white/40 backdrop-blur-2xl border-r border-brand-dark/5 flex-col items-center justify-center p-12">
        <div className="absolute top-[-10%] left-[-10%] w-[120%] h-[120%] bg-brand-glow/20 rounded-full blur-[120px] pointer-events-none mix-blend-multiply" />
        
        <div className="relative z-10 w-full max-w-md text-left flex flex-col h-full justify-between">
          <div>
            <h1 className="text-5xl font-bold tracking-tight mb-6 leading-tight">
              Build your <br />
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-brand-lightbrown to-brand-brown">Business Memory</span>
            </h1>
            <p className="text-xl text-brand-dark/60 font-medium">
              We need a few details to perfectly calibrate Morlen's intelligence layer for your specific workflow.
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
        <div className="w-full max-w-lg">
          
          {/* Progress Bar */}
          <div className="flex items-center gap-2 mb-16">
            {[1, 2, 3].map((i) => (
              <div key={i} className={`h-1.5 rounded-full transition-all duration-700 ease-out ${step >= i ? 'bg-brand-brown w-16' : 'bg-brand-dark/10 w-8'}`} />
            ))}
          </div>

          <div className="relative w-full">
            
            {/* Step 1: Basics */}
            {step === 1 && (
              <div className="animate-in fade-in slide-in-from-right-8 duration-700 ease-out fill-mode-both">
                <div className="flex items-center gap-3 mb-12 text-brand-brown">
                  <Building2 className="w-6 h-6" />
                  <h2 className="text-2xl font-bold text-brand-dark">Business Details</h2>
                </div>
                
                <div className="space-y-10">
                  <div>
                    <label className="block text-base font-bold text-brand-dark/60 mb-2 uppercase tracking-wider">Business Name</label>
                    <input 
                      type="text" 
                      className="w-full bg-transparent border-b-2 border-brand-dark/10 px-0 py-4 text-3xl md:text-4xl font-bold text-brand-dark focus:outline-none focus:border-brand-brown transition-all placeholder:text-brand-dark/20"
                      value={formData.businessName}
                      onChange={(e) => setFormData({...formData, businessName: e.target.value})}
                    />
                  </div>
                  
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div>
                      <label className="block text-sm font-bold text-brand-dark/60 mb-2 uppercase tracking-wider">Business Type</label>
                      <select 
                        className="w-full bg-white/50 border border-brand-dark/10 rounded-2xl px-4 py-4 text-brand-dark font-medium focus:outline-none focus:border-brand-brown focus:ring-1 focus:ring-brand-brown transition-all appearance-none shadow-sm"
                        value={formData.businessType}
                        onChange={(e) => setFormData({...formData, businessType: e.target.value})}
                      >
                        <option value="" disabled>Select business type</option>
                        {businessTypes.map(type => <option key={type} value={type}>{type}</option>)}
                      </select>
                    </div>
                    
                    <div>
                      <label className="block text-sm font-bold text-brand-dark/60 mb-2 uppercase tracking-wider">Industry</label>
                      <select 
                        className="w-full bg-white/50 border border-brand-dark/10 rounded-2xl px-4 py-4 text-brand-dark font-medium focus:outline-none focus:border-brand-brown focus:ring-1 focus:ring-brand-brown transition-all appearance-none shadow-sm"
                        value={formData.industry}
                        onChange={(e) => setFormData({...formData, industry: e.target.value})}
                      >
                        <option value="" disabled>Select your industry</option>
                        {industries.map(ind => <option key={ind} value={ind}>{ind}</option>)}
                      </select>
                    </div>
                  </div>

                  {formData.industry === "Other" && (
                    <div className="animate-in fade-in slide-in-from-top-2 duration-500">
                      <label className="block text-sm font-bold text-brand-dark/60 mb-2 uppercase tracking-wider">Please specify your industry</label>
                      <input 
                        type="text" 
                        className="w-full bg-transparent border-b-2 border-brand-dark/10 px-0 py-3 text-xl font-bold text-brand-dark focus:outline-none focus:border-brand-brown transition-all placeholder:text-brand-dark/20"
                        placeholder="Type your industry..."
                        value={formData.otherIndustry}
                        onChange={(e) => setFormData({...formData, otherIndustry: e.target.value})}
                      />
                    </div>
                  )}

                  <div>
                    <label className="block text-sm font-bold text-brand-dark/60 mb-4 uppercase tracking-wider">Team Size</label>
                    <div className="grid grid-cols-4 gap-3">
                      {["1", "2-10", "11-50", "50+"].map(size => (
                        <button
                          key={size}
                          onClick={() => setFormData({...formData, teamSize: size})}
                          className={`py-4 rounded-2xl border-2 transition-all text-base font-bold shadow-sm ${formData.teamSize === size ? 'bg-brand-brown/10 border-brand-brown text-brand-brown scale-[1.02]' : 'bg-white/50 border-brand-dark/5 text-brand-dark/70 hover:border-brand-dark/20 hover:bg-white'}`}
                        >
                          {size}
                        </button>
                      ))}
                    </div>
                  </div>
                </div>
              </div>
            )}

            {/* Step 2: Channels */}
            {step === 2 && (
              <div className="animate-in fade-in slide-in-from-right-8 duration-700 ease-out fill-mode-both">
                <div className="flex items-center gap-3 mb-6 text-brand-brown">
                  <Smartphone className="w-6 h-6" />
                  <h2 className="text-2xl font-bold text-brand-dark">Sales Channels</h2>
                </div>
                <p className="text-lg text-brand-dark/60 mb-10 font-medium">Where do your customers talk to you? Select all that apply.</p>
                
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  {channels.map(channel => {
                    const isSelected = formData.channels.includes(channel);
                    return (
                      <button
                        key={channel}
                        onClick={() => toggleSelection("channels", channel)}
                        className={`p-6 rounded-2xl border-2 flex items-center justify-between transition-all shadow-sm ${isSelected ? 'bg-brand-brown/10 border-brand-brown text-brand-brown scale-[1.02]' : 'bg-white/50 border-brand-dark/5 text-brand-dark/70 hover:border-brand-dark/20 hover:bg-white'}`}
                      >
                        <span className="font-bold text-lg">{channel}</span>
                        {isSelected && <Check className="w-5 h-5" />}
                      </button>
                    )
                  })}
                </div>
              </div>
            )}

            {/* Step 3: Goals */}
            {step === 3 && (
              <div className="animate-in fade-in slide-in-from-right-8 duration-700 ease-out fill-mode-both">
                <div className="flex items-center gap-3 mb-6 text-brand-brown">
                  <Target className="w-6 h-6" />
                  <h2 className="text-2xl font-bold text-brand-dark">Business Goals</h2>
                </div>
                <p className="text-lg text-brand-dark/60 mb-10 font-medium">What are you hoping to achieve with Morlen?</p>
                
                <div className="grid gap-4">
                  {goals.map(goal => {
                    const isSelected = formData.goals.includes(goal);
                    return (
                      <button
                        key={goal}
                        onClick={() => toggleSelection("goals", goal)}
                        className={`p-6 rounded-2xl border-2 flex items-center justify-between transition-all shadow-sm ${isSelected ? 'bg-brand-brown/10 border-brand-brown text-brand-brown scale-[1.02]' : 'bg-white/50 border-brand-dark/5 text-brand-dark/70 hover:border-brand-dark/20 hover:bg-white'}`}
                      >
                        <span className="font-bold text-lg">{goal}</span>
                        {isSelected && <Check className="w-5 h-5" />}
                      </button>
                    )
                  })}
                </div>
              </div>
            )}

            {/* Navigation Buttons */}
            <div className="mt-16 flex items-center justify-between pt-8 border-t border-brand-dark/10">
              <button 
                onClick={() => step > 1 ? setStep(step - 1) : router.push("/")}
                className="px-4 py-2 text-brand-dark/50 hover:text-brand-dark transition-colors flex items-center gap-2 text-sm font-bold uppercase tracking-wider"
              >
                <ArrowLeft className="w-4 h-4" />
                Back
              </button>
              <button 
                onClick={handleNext}
                disabled={!isStepValid()}
                className={`px-10 py-4 rounded-full font-bold flex items-center gap-2 transition-all text-lg shadow-xl ${isStepValid() ? 'bg-brand-brown text-white hover:scale-105 shadow-brand-brown/20' : 'bg-brand-dark/5 text-brand-dark/30 cursor-not-allowed shadow-none'}`}
              >
                {step === 3 ? "Create Profile" : "Continue"}
                <ArrowRight className="w-5 h-5" />
              </button>
            </div>

          </div>
        </div>
      </div>
    </div>
  );
}

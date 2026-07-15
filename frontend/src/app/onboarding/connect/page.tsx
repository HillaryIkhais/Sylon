"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { MessageCircle, FileUp, Database, ArrowRight, Loader2, CheckCircle2 } from "lucide-react";
import { ConversationProvider } from "@elevenlabs/react";
import EtherealOrb from "@/components/EtherealOrb";

const ActualInstagramIcon = ({ className }: { className?: string }) => (
  <svg viewBox="0 0 24 24" fill="currentColor" className={className} xmlns="http://www.w3.org/2000/svg">
    <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/>
  </svg>
);

const WhatsAppIcon = ({ className }: { className?: string }) => (
  <svg viewBox="0 0 24 24" fill="currentColor" className={className} xmlns="http://www.w3.org/2000/svg">
    <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.888-.788-1.489-1.761-1.663-2.06-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 0 0-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/>
  </svg>
);

export default function ConnectData() {
  const router = useRouter();
  const [connecting, setConnecting] = useState<string | null>(null);
  const [connected, setConnected] = useState<string[]>([]);
  const [showUpload, setShowUpload] = useState(false);

  const handleConnect = (platform: string) => {
    setConnecting(platform);
    
    // Simulate OAuth/Connection delay
    setTimeout(() => {
      setConnecting(null);
      setConnected(prev => [...prev, platform]);
    }, 2000);
  };

  const handleFinish = () => {
    router.push("/onboarding/processing");
  };

  return (
    <div className="min-h-screen bg-glow-bg text-brand-dark flex flex-col md:flex-row relative overflow-hidden">
      
      {/* Left Side: Creative Brand Identity */}
      <div className="hidden md:flex md:w-1/2 relative bg-white/40 backdrop-blur-2xl border-r border-brand-dark/5 flex-col items-center justify-center p-12">
        <div className="absolute top-[-10%] left-[-10%] w-[120%] h-[120%] bg-brand-glow/20 rounded-full blur-[120px] pointer-events-none mix-blend-multiply" />
        
        <div className="relative z-10 w-full max-w-md text-left flex flex-col h-full justify-between">
          <div>
            <div className="w-16 h-16 rounded-2xl bg-gradient-to-br from-brand-lightbrown to-brand-brown mb-8 flex items-center justify-center font-bold text-4xl text-white shadow-2xl shadow-brand-brown/30">M</div>
            <h1 className="text-5xl font-bold tracking-tight mb-6 leading-tight">
              Connect your <br />
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-brand-lightbrown to-brand-brown">Data Sources</span>
            </h1>
            <p className="text-xl text-brand-dark/60 font-medium">
              Morlen needs raw conversation data to build your Business Memory and find hidden revenue opportunities.
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
          
          <div className="mb-12">
            <h2 className="text-2xl font-bold text-brand-dark mb-2">Sync your channels</h2>
            <p className="text-lg text-brand-dark/60 font-medium">Connect at least one source to continue.</p>
          </div>

          <div className="grid gap-6 mb-12">
            
            {/* WhatsApp Integration */}
            <div className={`p-6 rounded-2xl border-2 transition-all shadow-sm ${connected.includes('whatsapp') ? 'bg-emerald-500/5 border-emerald-500/30' : 'bg-white/50 border-brand-dark/5 hover:border-brand-dark/20 hover:bg-white'}`}>
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-4">
                  <div className="w-12 h-12 rounded-xl bg-green-50 flex items-center justify-center text-[#25D366] shadow-sm">
                    <WhatsAppIcon className="w-7 h-7" />
                  </div>
                  <div>
                    <h3 className="font-bold text-lg text-brand-dark">WhatsApp Business</h3>
                    <p className="text-sm text-brand-dark/60 font-medium">Sync your customer chats and sales.</p>
                  </div>
                </div>
                
                {connected.includes('whatsapp') ? (
                  <div className="flex items-center gap-2 text-emerald-600 font-bold px-4 py-2 bg-emerald-500/10 rounded-full">
                    <CheckCircle2 className="w-4 h-4" /> Connected
                  </div>
                ) : (
                  <button 
                    onClick={() => handleConnect('whatsapp')}
                    disabled={connecting !== null}
                    className="px-6 py-2.5 rounded-full bg-brand-dark text-white font-bold text-sm hover:scale-105 transition-all w-32 flex justify-center shadow-lg"
                  >
                    {connecting === 'whatsapp' ? <Loader2 className="w-5 h-5 animate-spin" /> : "Connect"}
                  </button>
                )}
              </div>
            </div>

            {/* Instagram Integration */}
            <div className={`p-6 rounded-2xl border-2 transition-all shadow-sm ${connected.includes('instagram') ? 'bg-emerald-500/5 border-emerald-500/30' : 'bg-white/50 border-brand-dark/5 hover:border-brand-dark/20 hover:bg-white'}`}>
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-4">
                  <div className="w-12 h-12 rounded-xl bg-gradient-to-tr from-[#f09433] via-[#e6683c] to-[#bc1888] flex items-center justify-center text-white shadow-md">
                    <ActualInstagramIcon className="w-7 h-7" />
                  </div>
                  <div>
                    <h3 className="font-bold text-lg text-brand-dark">Instagram</h3>
                    <p className="text-sm text-brand-dark/60 font-medium">Sync your DMs and comments.</p>
                  </div>
                </div>
                
                {connected.includes('instagram') ? (
                  <div className="flex items-center gap-2 text-emerald-600 font-bold px-4 py-2 bg-emerald-500/10 rounded-full">
                    <CheckCircle2 className="w-4 h-4" /> Connected
                  </div>
                ) : (
                  <button 
                    onClick={() => handleConnect('instagram')}
                    disabled={connecting !== null}
                    className="px-6 py-2.5 rounded-full bg-brand-dark text-white font-bold text-sm hover:scale-105 transition-all w-32 flex justify-center shadow-lg"
                  >
                    {connecting === 'instagram' ? <Loader2 className="w-5 h-5 animate-spin" /> : "Connect"}
                  </button>
                )}
              </div>
            </div>

            {/* Upload CSV */}
            <div className="p-6 rounded-2xl border-2 border-dashed border-brand-dark/20 bg-white/30 hover:bg-white transition-colors cursor-pointer group shadow-sm">
              <div className="flex items-center gap-4">
                <div className="w-12 h-12 rounded-xl bg-brand-dark/5 flex items-center justify-center text-brand-dark/50 group-hover:text-brand-brown transition-colors">
                  <FileUp className="w-6 h-6" />
                </div>
                <div>
                  <h3 className="font-bold text-lg text-brand-dark">Upload Chat History (CSV)</h3>
                  <p className="text-sm text-brand-dark/60 font-medium">Already have exports from Zendesk or Intercom? Upload them here.</p>
                </div>
              </div>
            </div>

          </div>

          <div className="flex justify-between items-center mt-8 pt-8 border-t border-brand-dark/10">
            <p className="text-sm text-brand-dark/50 font-bold uppercase tracking-wider">
              {connected.length > 0 ? `${connected.length} sources connected.` : "Pending..."}
            </p>
            <button 
              onClick={handleFinish}
              disabled={connected.length === 0}
              className={`px-10 py-4 rounded-full font-bold flex items-center gap-2 transition-all text-lg shadow-xl ${connected.length > 0 ? 'bg-brand-brown text-white hover:scale-105 shadow-brand-brown/20' : 'bg-brand-dark/5 text-brand-dark/30 cursor-not-allowed shadow-none'}`}
            >
              Sync Data
              <ArrowRight className="w-5 h-5" />
            </button>
          </div>

        </div>
      </div>
    </div>
  );
}

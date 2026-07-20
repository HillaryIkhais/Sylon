'use client';
import { useState, useEffect, useRef } from 'react';
import { Send, Store, User, Sparkles, RefreshCw, MessageCircle } from 'lucide-react';
import Link from 'next/link';

type Message = {
  role: 'system' | 'user' | 'assistant';
  content: string;
  board_debate?: any;
  decision?: string;
  timestamp?: string;
};

export default function DemoChat() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [mode, setMode] = useState<'onboarding' | 'customer'>('onboarding');
  const [sessionId, setSessionId] = useState<string>('');
  const [isInitializing, setIsInitializing] = useState(true);
  
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    // Always start fresh on page load for the best demo experience
    const newSession = 'demo_' + Math.random().toString(36).substring(2, 9);
    sessionStorage.setItem('morlen_demo_session', newSession);
    setSessionId(newSession);
    
    // Trigger initial onboarding message
    triggerOnboarding(newSession);
  }, []);

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const triggerOnboarding = async (sid: string) => {
    try {
      setLoading(true);
      setIsInitializing(true);
      const res = await fetch('/api/demo/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ session_id: sid, text: 'start', mode: 'onboarding' })
      });
      const data = await res.json();
      if (data.response) {
        setMessages([{ role: 'assistant', content: data.response }]);
      }
    } catch (e) {
      console.error(e);
      setMessages([{ role: 'assistant', content: 'Connection error. Please check your network and try again.' }]);
    } finally {
      setLoading(false);
      setIsInitializing(false);
    }
  };

  const handleReset = () => {
    const newSession = 'demo_' + Math.random().toString(36).substring(2, 9);
    sessionStorage.setItem('morlen_demo_session', newSession);
    setSessionId(newSession);
    setMessages([]);
    setMode('onboarding');
    triggerOnboarding(newSession);
  };

  const sendMessage = async (e?: React.FormEvent) => {
    if (e) e.preventDefault();
    if (!input.trim() || !sessionId || loading || isInitializing) return;

    const userText = input;
    setMessages(prev => [...prev, { role: 'user', content: userText, timestamp: new Date().toISOString() }]);
    setInput('');
    setLoading(true);

    try {
      const res = await fetch('/api/demo/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ session_id: sessionId, text: userText, mode })
      });
      
      const data = await res.json();
      
      setMessages(prev => [...prev, { 
        role: 'assistant', 
        content: data.response || 'Sorry, I encountered an error.', 
        board_debate: data.board_debate,
        decision: data.decision,
        timestamp: new Date().toISOString()
      }]);

      if (data.status === 'ready') {
        setMode('customer');
      }
      
    } catch (err) {
      console.error(err);
      setMessages(prev => [...prev, { role: 'assistant', content: 'Sorry, there was an error processing your request.' }]);
    } finally {
      setLoading(false);
    }
  };

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  return (
    <div className="flex flex-col flex-1 w-full min-h-0 h-full overflow-hidden text-brand-dark dark:text-gray-100 relative font-sans">
      
      {/* Decorative Background Elements */}
      <div className="absolute top-0 left-0 w-full h-full overflow-hidden pointer-events-none z-0">
        <div className="absolute top-[-10%] left-[-10%] w-[40%] h-[40%] rounded-full bg-brand-lightbrown/10 dark:bg-brand-brown/10 blur-[100px] opacity-70"></div>
        <div className="absolute bottom-[-10%] right-[-10%] w-[40%] h-[40%] rounded-full bg-brand-brown/5 dark:bg-brand-lightbrown/5 blur-[100px] opacity-70"></div>
      </div>
      
      {/* Premium Header */}
      <header className="flex-shrink-0 bg-white/40 dark:bg-black/30 backdrop-blur-xl border-b border-brand-dark/5 dark:border-white/5 px-4 md:px-8 py-4 flex items-center justify-between z-10 shadow-sm transition-colors duration-300">
        <div className="flex items-center gap-4">
          <Link href="/dashboard" className="hidden md:flex p-2 -ml-2 rounded-full hover:bg-black/5 dark:hover:bg-white/5 text-gray-500 dark:text-gray-400 transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="m15 18-6-6 6-6"/></svg>
          </Link>
          
          <div className="w-12 h-12 rounded-2xl bg-gradient-to-br from-brand-brown to-brand-dark dark:from-brand-lightbrown dark:to-brand-brown flex items-center justify-center text-white font-bold shadow-lg transform rotate-3">
            <Sparkles className="w-6 h-6 text-white/90 transform -rotate-3" />
          </div>
          <div>
            <h1 className="font-extrabold text-xl leading-tight flex items-center gap-2 text-transparent bg-clip-text bg-gradient-to-r from-brand-dark to-brand-brown dark:from-white dark:to-gray-400">
              Morlen {mode === 'onboarding' ? 'Setup' : 'Live Agent'}
              {mode === 'customer' && <span className="flex h-2.5 w-2.5 relative ml-1"><span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span><span className="relative inline-flex rounded-full h-2.5 w-2.5 bg-emerald-500"></span></span>}
            </h1>
            <p className="text-sm font-medium text-gray-500 dark:text-gray-400 flex items-center gap-1.5 mt-0.5">
              {mode === 'onboarding' ? (
                <><Store className="w-3.5 h-3.5" /> Building your workspace</>
              ) : (
                <><User className="w-3.5 h-3.5" /> Simulating customer interaction</>
              )}
            </p>
          </div>
        </div>
        
        <button 
          onClick={handleReset}
          className="text-sm font-bold flex items-center gap-2 text-gray-600 dark:text-gray-300 hover:text-brand-brown dark:hover:text-brand-lightbrown transition-all px-4 py-2 bg-gray-100 dark:bg-[#222] rounded-full border border-transparent hover:border-brand-brown/20 dark:hover:border-brand-lightbrown/20 shadow-sm"
        >
          <RefreshCw className="w-3.5 h-3.5" />
          <span className="hidden sm:inline">Reset Demo</span>
        </button>
      </header>

      {/* Main Chat Area */}
      <div className="flex-1 overflow-y-auto p-4 md:p-8 relative z-10 scroll-smooth">
        <div className="max-w-3xl mx-auto flex flex-col gap-6">
          
          {isInitializing && (
            <div className="flex flex-col items-center justify-center h-full opacity-60 mt-32 animate-pulse">
              <div className="w-16 h-16 rounded-full bg-brand-lightbrown/20 dark:bg-brand-brown/20 flex items-center justify-center mb-6">
                <Sparkles className="w-8 h-8 text-brand-brown dark:text-brand-lightbrown" />
              </div>
              <p className="font-semibold text-lg">Initializing Morlen Intelligence...</p>
              <p className="text-sm text-gray-500 dark:text-gray-400 mt-2">Connecting to AI Decision Engine</p>
            </div>
          )}

          {!isInitializing && messages.map((m, i) => (
            <div key={i} className={`flex flex-col ${m.role === 'user' ? 'items-end' : 'items-start'} group animate-in slide-in-from-bottom-2 fade-in duration-300`}>
              
              {m.role === 'assistant' && (
                <div className="flex items-center gap-2 mb-2 ml-1 opacity-80">
                  <div className="w-6 h-6 rounded-full bg-gradient-to-br from-brand-brown to-brand-dark flex items-center justify-center shadow-sm">
                    {mode === 'onboarding' ? <Store className="w-3 h-3 text-white" /> : <Sparkles className="w-3 h-3 text-white" />}
                  </div>
                  <span className="text-xs font-bold uppercase tracking-wider text-gray-500 dark:text-gray-400">
                    {mode === 'onboarding' ? 'Morlen Onboarding' : 'Morlen Agent'}
                  </span>
                </div>
              )}

              <div className={`max-w-[85%] md:max-w-[75%] rounded-3xl p-5 shadow-sm transition-all ${
                m.role === 'user' 
                  ? 'bg-gradient-to-r from-brand-lightbrown to-brand-brown text-white rounded-br-sm shadow-md' 
                  : 'bg-white/80 dark:bg-[#1f1411]/80 backdrop-blur-md border border-gray-100 dark:border-white/5 rounded-bl-sm text-brand-dark dark:text-gray-200 shadow-xl shadow-brand-dark/5'
              }`}>
                
                <div className="text-base leading-relaxed whitespace-pre-wrap font-medium">{m.content}</div>

                {/* Debate Trace (Only visible in Customer mode for transparency) */}
                {m.board_debate && (
                  <div className="mt-5 pt-4 border-t border-gray-100 dark:border-white/10">
                    <div className="flex items-center gap-2 mb-3">
                      <div className="px-2 py-1 bg-brand-lightbrown/10 text-brand-brown dark:text-brand-lightbrown text-[10px] font-bold uppercase rounded-md tracking-wider">
                        Internal Reasoning
                      </div>
                      <div className="text-xs font-semibold text-gray-500 dark:text-gray-400 truncate">
                        Route: {m.decision}
                      </div>
                    </div>
                    
                    <div className="bg-gray-50 dark:bg-[#111] rounded-xl p-4 text-sm space-y-3 border border-gray-100 dark:border-white/5 shadow-inner">
                      {m.board_debate.cx && (
                        <div className="flex gap-3">
                          <span className="font-extrabold text-brand-brown dark:text-brand-lightbrown w-8">CX:</span> 
                          <span className="text-gray-600 dark:text-gray-400 flex-1">{m.board_debate.cx}</span>
                        </div>
                      )}
                      {m.board_debate.cfo && (
                        <div className="flex gap-3">
                          <span className="font-extrabold text-blue-600 dark:text-blue-400 w-8">CFO:</span> 
                          <span className="text-gray-600 dark:text-gray-400 flex-1">{m.board_debate.cfo}</span>
                        </div>
                      )}
                      {m.board_debate.ops && (
                        <div className="flex gap-3">
                          <span className="font-extrabold text-emerald-600 dark:text-emerald-400 w-8">OPS:</span> 
                          <span className="text-gray-600 dark:text-gray-400 flex-1">{m.board_debate.ops}</span>
                        </div>
                      )}
                    </div>
                  </div>
                )}
              </div>
            </div>
          ))}

          {loading && !isInitializing && (
            <div className="flex items-start">
              <div className="bg-white dark:bg-[#1a1a1a] border border-gray-100 dark:border-white/5 rounded-3xl rounded-bl-sm px-6 py-5 shadow-xl shadow-brand-dark/5">
                <div className="flex gap-1.5 items-center h-4">
                  <div className="w-2.5 h-2.5 rounded-full bg-brand-lightbrown animate-bounce" style={{ animationDelay: '0ms' }}></div>
                  <div className="w-2.5 h-2.5 rounded-full bg-brand-lightbrown animate-bounce" style={{ animationDelay: '150ms' }}></div>
                  <div className="w-2.5 h-2.5 rounded-full bg-brand-lightbrown animate-bounce" style={{ animationDelay: '300ms' }}></div>
                </div>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} className="h-4" />
        </div>
      </div>

      {/* Input Area */}
      <div className="flex-shrink-0 bg-white/40 dark:bg-black/30 backdrop-blur-xl border-t border-brand-dark/5 dark:border-white/5 p-4 md:p-6 pb-8 md:pb-10 z-20 relative shadow-[0_-10px_40px_rgba(0,0,0,0.03)] dark:shadow-[0_-10px_40px_rgba(0,0,0,0.2)]">
        <div className="max-w-3xl mx-auto flex flex-col gap-3">
          
          {mode === 'customer' && (
            <div className="flex flex-wrap justify-center gap-2 mb-1 animate-in slide-in-from-bottom-2 fade-in duration-500">
              <button type="button" onClick={() => { setInput("How much is the red shoe?"); document.getElementById('chat-input')?.focus(); }} className="text-xs font-medium px-4 py-1.5 bg-gray-50 dark:bg-[#222] text-gray-600 dark:text-gray-300 rounded-full hover:bg-brand-brown hover:text-white dark:hover:bg-white dark:hover:text-black transition-all border border-gray-200 dark:border-white/10 shadow-sm">Test Pricing</button>
              <button type="button" onClick={() => { setInput("Can you remove 5k from the price?"); document.getElementById('chat-input')?.focus(); }} className="text-xs font-medium px-4 py-1.5 bg-gray-50 dark:bg-[#222] text-gray-600 dark:text-gray-300 rounded-full hover:bg-brand-brown hover:text-white dark:hover:bg-white dark:hover:text-black transition-all border border-gray-200 dark:border-white/10 shadow-sm">Test Negotiation</button>
              <button type="button" onClick={() => { setInput("Your delivery guy stole my money!"); document.getElementById('chat-input')?.focus(); }} className="text-xs font-medium px-4 py-1.5 bg-gray-50 dark:bg-[#222] text-gray-600 dark:text-gray-300 rounded-full hover:bg-brand-brown hover:text-white dark:hover:bg-white dark:hover:text-black transition-all border border-gray-200 dark:border-white/10 shadow-sm">Test Escalation</button>
            </div>
          )}

          <form onSubmit={sendMessage} className="relative flex items-center group">
            <input
              id="chat-input"
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              disabled={loading || isInitializing}
              placeholder={mode === 'onboarding' ? "Reply to Morlen..." : "Message your business as a customer..."}
              className="w-full bg-gray-100 dark:bg-[#222] border border-transparent focus:border-brand-brown/30 dark:focus:border-brand-lightbrown/30 focus:bg-white dark:focus:bg-[#111] rounded-full py-4 pl-6 pr-16 outline-none text-base transition-all shadow-inner placeholder-gray-400 dark:placeholder-gray-500 font-medium text-brand-dark dark:text-white disabled:opacity-50"
            />
            <button 
              type="submit"
              disabled={loading || isInitializing || !input.trim()}
              className="absolute right-2 top-1/2 -translate-y-1/2 w-11 h-11 bg-brand-brown text-white rounded-full flex items-center justify-center hover:bg-brand-dark hover:scale-105 active:scale-95 transition-all disabled:opacity-40 disabled:hover:scale-100 shadow-md"
            >
              <Send className="w-5 h-5 ml-0.5" />
            </button>
          </form>
          
        </div>
      </div>
    </div>
  );
}

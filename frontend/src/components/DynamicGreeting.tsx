"use client";
import { useState, useEffect } from "react";

export default function DynamicGreeting() {
  const [currentTime, setCurrentTime] = useState<Date | null>(null);
  const [businessName, setBusinessName] = useState<string>("");

  useEffect(() => {
    setCurrentTime(new Date());
    const name = localStorage.getItem("morlen_business_name");
    if (name) setBusinessName(name);

    const timer = setInterval(() => setCurrentTime(new Date()), 60000);
    return () => clearInterval(timer);
  }, []);

  const getGreeting = () => {
    if (!currentTime) return "Good morning";
    const hour = currentTime.getHours();
    if (hour < 12) return "Good morning";
    if (hour < 18) return "Good afternoon";
    return "Good evening";
  };

  const dateStr = currentTime 
    ? currentTime.toLocaleDateString(undefined, { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }) + " · " + currentTime.toLocaleTimeString(undefined, { hour: '2-digit', minute: '2-digit' })
    : "Loading date...";

  return (
    <header className="mb-8">
      <h1 className="text-2xl md:text-3xl font-bold tracking-tight mb-2 text-brand-dark dark:text-white">
        {getGreeting()}{businessName ? `, ${businessName}` : '.'}
      </h1>
      <p className="text-brand-dark/60 dark:text-brand-dark/70 font-medium">
        {dateStr}
      </p>
    </header>
  );
}

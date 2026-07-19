"use client";

import { useRouter } from "next/navigation";

// HACKATHON BUILD: Always shows "Dashboard" button, no sign-in/sign-out.
export default function AuthButton() {
  const router = useRouter();
  return (
    <button
      onClick={() => router.push('/dashboard')}
      className="text-xs sm:text-sm font-bold text-white bg-brand-brown px-4 sm:px-5 py-1.5 sm:py-2 rounded-full hover:opacity-90 shadow-md transition-colors whitespace-nowrap"
    >
      Dashboard
    </button>
  );
}

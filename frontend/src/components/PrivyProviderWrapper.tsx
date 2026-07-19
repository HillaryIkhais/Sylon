"use client";

// HACKATHON BUILD: Privy replaced with a pass-through wrapper.
// Judges can access all features without signing in.
export default function PrivyProviderWrapper({
  children,
}: {
  children: React.ReactNode;
}) {
  return <>{children}</>;
}

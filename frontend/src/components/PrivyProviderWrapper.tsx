"use client";

import { PrivyProvider } from "@privy-io/react-auth";

export default function PrivyProviderWrapper({
  children,
}: {
  children: React.ReactNode;
}) {
  const appId = process.env.NEXT_PUBLIC_PRIVY_APP_ID || "cmph0wa1300110cjr9eyypdv6";

  if (appId === "cmph0wa1300110cjr9eyypdv6" && !process.env.NEXT_PUBLIC_PRIVY_APP_ID) {
    console.warn("NEXT_PUBLIC_PRIVY_APP_ID is not set in Vercel. Using fallback keys to prevent crashes.");
  }

  return (
    <PrivyProvider
      appId={appId}
      clientId={process.env.NEXT_PUBLIC_PRIVY_CLIENT_ID || process.env.PRIVY_CLIENT_ID || "client-WY6ZYaTXB11CBFjDZwFSWg9Xxh6TwgTh8kgqqfn8dVhMA"}
      config={{
        appearance: {
          theme: "light",
          accentColor: "#A57365",
          logo: undefined,
        },
        loginMethods: ["email", "google"],
      }}
    >
      {children}
    </PrivyProvider>
  );
}

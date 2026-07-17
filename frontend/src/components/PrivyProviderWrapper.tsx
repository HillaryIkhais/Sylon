"use client";

import { PrivyProvider } from "@privy-io/react-auth";
import { useEffect, useState } from "react";

export default function PrivyProviderWrapper({
  children,
}: {
  children: React.ReactNode;
}) {
  const appId = process.env.NEXT_PUBLIC_PRIVY_APP_ID;
  const [theme, setTheme] = useState<"light" | "dark">("dark");

  useEffect(() => {
    // Match the app's own dark/light mode logic (checks the <html> class)
    const isDark = document.documentElement.classList.contains("dark");
    setTheme(isDark ? "dark" : "light");

    // Watch for theme changes in real time
    const observer = new MutationObserver(() => {
      const nowDark = document.documentElement.classList.contains("dark");
      setTheme(nowDark ? "dark" : "light");
    });
    observer.observe(document.documentElement, { attributes: true, attributeFilter: ["class"] });
    return () => observer.disconnect();
  }, []);

  if (!appId) {
    console.warn("NEXT_PUBLIC_PRIVY_APP_ID is not set. Auth disabled.");
    return <>{children}</>;
  }

  return (
    <PrivyProvider
      appId={appId}
      clientId={process.env.NEXT_PUBLIC_PRIVY_CLIENT_ID || process.env.PRIVY_CLIENT_ID}
      config={{
        appearance: {
          theme: theme,
          accentColor: "#A57365",
        },
        loginMethods: ["email", "google"],
      }}
    >
      {children}
    </PrivyProvider>
  );
}

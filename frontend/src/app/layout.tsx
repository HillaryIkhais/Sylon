import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import Navbar from "@/components/Navbar";
import { ThemeProvider } from "@/components/ThemeProvider";
import PrivyProviderWrapper from "@/components/PrivyProviderWrapper";

const inter = Inter({
  variable: "--font-inter",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Sylon Strategist",
  description: "Premium Business Intelligence Orchestrator",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={inter.variable} suppressHydrationWarning>
      <body>
        <ThemeProvider attribute="class" defaultTheme="light" enableSystem disableTransitionOnChange>
          <PrivyProviderWrapper>
            <Navbar />
            <main className="bg-glow-bg min-h-screen">
              {children}
            </main>
          </PrivyProviderWrapper>
        </ThemeProvider>
      </body>
    </html>
  );
}


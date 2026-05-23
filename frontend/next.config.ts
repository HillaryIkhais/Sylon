import type { NextConfig } from "next";

const apiUrl = process.env.SYLON_API_URL || "https://sylon-demo-2026.loca.lt";

const nextConfig: NextConfig = {
  output: 'standalone',
  async rewrites() {
    return [
      {
        source: "/api/:path*",
        destination: `${apiUrl}/:path*`,
      },
    ];
  },
};

export default nextConfig;

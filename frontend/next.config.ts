import type { NextConfig } from "next";

const apiUrl = process.env.SYLON_API_URL || "https://wqhwe-197-211-52-66.run.pinggy-free.link";

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

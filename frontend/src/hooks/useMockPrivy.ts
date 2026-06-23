"use client";

export function usePrivy() {
  return {
    ready: true,
    authenticated: true,
    login: () => {},
    logout: () => {},
    user: { id: "mock_user", email: { address: "demo@sylon.ai" } },
    getAccessToken: async () => "mock_token"
  };
}

export function PrivyProvider({children}: any) {
  return children;
}

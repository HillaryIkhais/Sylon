/**
 * Hackathon Auth Stub
 * Replaces Privy in the hackathon branch so judges can test
 * without needing to sign in. All hooks return a simulated
 * "always authenticated" state.
 */

export const HACKATHON_USER = {
  id: "judge-demo-user",
  email: { address: "judge@morlen.demo" },
  google: { name: "Demo Judge" },
};

export function useHackathonAuth() {
  return {
    ready: true,
    authenticated: true,
    user: HACKATHON_USER,
    login: () => {},
    logout: () => {},
    getAccessToken: async () => "hackathon-demo-token",
  };
}

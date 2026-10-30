import type { NextConfig } from "next";

// Netlify serves the preview at the domain root.
// GitHub Pages (if re-enabled later) requires the repository prefix.
const isGitHubPages = process.env.DEPLOY_TARGET === "github-pages";

const nextConfig: NextConfig = {
  output: "export",
  trailingSlash: true,
  ...(isGitHubPages ? { basePath: "/WHMCS_Mosalam" } : {}),
  images: { unoptimized: true },
};

export default nextConfig;
